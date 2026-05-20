import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Jimp, JimpMime } from "jimp";
import decodeWebp, { init as initWebpDecode } from "@jsquash/webp/decode.js";

export interface WechatUploadAsset {
  buffer: Buffer;
  filename: string;
  contentType: string;
  fileExt: string;
  fileSize: number;
}

export interface PreparedWechatUploadAsset {
  buffer: Buffer;
  filename: string;
  contentType: string;
  wasProcessed: boolean;
  processingNotes: string[];
}

export const WECHAT_BODY_IMAGE_MAX_SIZE = 1024 * 1024;
export const WECHAT_BODY_IMAGE_UNSUPPORTED_FORMATS = new Set([
  ".gif", ".webp", ".bmp", ".tiff", ".tif", ".svg", ".ico",
]);

const BODY_UPLOAD_ALLOWED_MIME_TYPES = new Set([JimpMime.jpeg, JimpMime.png]);

const MIME_TO_EXT: Record<string, string> = {
  "image/jpeg": ".jpg", "image/png": ".png", "image/gif": ".gif",
  "image/webp": ".webp", "image/bmp": ".bmp", "image/x-ms-bmp": ".bmp",
  "image/tiff": ".tiff", "image/svg+xml": ".svg", "image/x-icon": ".ico",
  "image/vnd.microsoft.icon": ".ico",
};

const JPEG_QUALITY_STEPS = [82, 74, 66, 58, 50, 42, 34];
const MAX_WIDTH_STEPS = [2560, 2048, 1600, 1280, 1024, 800, 640, 480];

export function detectImageFormatFromBuffer(buffer: Buffer): { contentType: string; fileExt: string } | null {
  if (buffer.length < 12) return null;
  if (buffer[0]===0x52&&buffer[1]===0x49&&buffer[2]===0x46&&buffer[3]===0x46&&buffer[8]===0x57&&buffer[9]===0x45&&buffer[10]===0x42&&buffer[11]===0x50) return { contentType: "image/webp", fileExt: ".webp" };
  if (buffer[0]===0x89&&buffer[1]===0x50&&buffer[2]===0x4e&&buffer[3]===0x47) return { contentType: "image/png", fileExt: ".png" };
  if (buffer[0]===0xff&&buffer[1]===0xd8&&buffer[2]===0xff) return { contentType: "image/jpeg", fileExt: ".jpg" };
  if (buffer[0]===0x47&&buffer[1]===0x49&&buffer[2]===0x46&&buffer[3]===0x38) return { contentType: "image/gif", fileExt: ".gif" };
  if (buffer[0]===0x42&&buffer[1]===0x4d) return { contentType: "image/bmp", fileExt: ".bmp" };
  return null;
}

let webpDecoderReady: Promise<void> | undefined;
type JimpImage = Awaited<ReturnType<typeof Jimp.read>>;

function normalizeMimeType(ct: string): string { return ct.split(";")[0]!.trim().toLowerCase(); }
function extFromMimeType(ct: string): string { return MIME_TO_EXT[normalizeMimeType(ct)] || ""; }
function ensureFileExt(a: WechatUploadAsset): string { return a.fileExt || extFromMimeType(a.contentType); }
function basenameWithoutExt(f: string): string { return path.basename(f, path.extname(f)) || "image"; }
function renameWithExt(f: string, e: string): string { return `${basenameWithoutExt(f)}${e}`; }

export function needsWechatBodyImageProcessing(asset: WechatUploadAsset): boolean {
  if (asset.fileSize > WECHAT_BODY_IMAGE_MAX_SIZE) return true;
  const n = normalizeMimeType(asset.contentType);
  if (BODY_UPLOAD_ALLOWED_MIME_TYPES.has(n)) return false;
  const fe = ensureFileExt(asset);
  return WECHAT_BODY_IMAGE_UNSUPPORTED_FORMATS.has(fe) || !fe;
}

async function ensureWebpDecoder(): Promise<void> {
  if (!webpDecoderReady) {
    webpDecoderReady = (async () => {
      const __filename = fileURLToPath(import.meta.url);
      const __dirname = path.dirname(__filename);
      const wasmPath = path.resolve(__dirname, "node_modules/@jsquash/webp/codec/dec/webp_dec.wasm");
      const wasmModule = await WebAssembly.compile(await fs.readFile(wasmPath));
      await initWebpDecode(wasmModule, {});
    })();
  }
  await webpDecoderReady;
}

async function loadImageForProcessing(asset: WechatUploadAsset): Promise<JimpImage> {
  const fe = ensureFileExt(asset);
  const n = normalizeMimeType(asset.contentType);
  if (fe === ".webp" || n === "image/webp") {
    await ensureWebpDecoder();
    const decoded = await decodeWebp(asset.buffer);
    return new Jimp({ data: Buffer.from(decoded.data.buffer, decoded.data.byteOffset, decoded.data.byteLength), width: decoded.width, height: decoded.height });
  }
  if (fe === ".svg" || fe === ".ico") throw new Error(`Cannot convert ${fe} for WeChat body upload`);
  return Jimp.read(asset.buffer);
}

function imageHasTransparency(image: JimpImage): boolean {
  const { data } = image.bitmap;
  for (let i = 3; i < data.length; i += 4) { if (data[i] !== 255) return true; }
  return false;
}

function buildCandidateWidths(w: number): number[] {
  const c = new Set<number>([w]);
  for (const mw of MAX_WIDTH_STEPS) { if (w > mw) c.add(mw); }
  return [...c].sort((a, b) => b - a);
}

function resizeToWidth(image: JimpImage, w: number): JimpImage {
  const cl = image.clone();
  if (w < image.bitmap.width) cl.resize({ w });
  return cl;
}

function flattenOnWhite(image: JimpImage): JimpImage {
  const f = new Jimp({ width: image.bitmap.width, height: image.bitmap.height, color: 0xffffffff });
  f.composite(image, 0, 0);
  return f;
}

async function encodePng(image: JimpImage): Promise<Buffer> { return image.getBuffer(JimpMime.png); }
async function encodeJpeg(image: JimpImage, quality: number): Promise<Buffer> {
  const src = imageHasTransparency(image) ? flattenOnWhite(image) : image;
  return src.getBuffer(JimpMime.jpeg, { quality });
}

function buildProcessingNotes(asset: WechatUploadAsset): string[] {
  const notes: string[] = [];
  const fe = ensureFileExt(asset);
  if (fe && WECHAT_BODY_IMAGE_UNSUPPORTED_FORMATS.has(fe)) notes.push(`converted unsupported ${fe} source`);
  if (asset.fileSize > WECHAT_BODY_IMAGE_MAX_SIZE) notes.push(`compressed ${(asset.fileSize/1024/1024).toFixed(2)}MB source below 1MB`);
  if (notes.length === 0) notes.push("re-encoded for WeChat body upload");
  return notes;
}

export async function prepareWechatBodyImageUpload(asset: WechatUploadAsset): Promise<PreparedWechatUploadAsset> {
  if (!needsWechatBodyImageProcessing(asset)) return { buffer: asset.buffer, filename: asset.filename, contentType: asset.contentType, wasProcessed: false, processingNotes: [] };
  const image = await loadImageForProcessing(asset);
  const widths = buildCandidateWidths(image.bitmap.width);
  const ext = ensureFileExt(asset);
  const preferPng = imageHasTransparency(image) || ext === ".png" || ext === ".webp";
  const pn = buildProcessingNotes(asset);
  for (const w of widths) {
    const resized = resizeToWidth(image, w);
    if (preferPng) { const buf = await encodePng(resized); if (buf.length <= WECHAT_BODY_IMAGE_MAX_SIZE) return { buffer: buf, filename: renameWithExt(asset.filename, ".png"), contentType: JimpMime.png, wasProcessed: true, processingNotes: w < image.bitmap.width ? [...pn, `resized to ${w}px wide`] : pn }; }
    for (const q of JPEG_QUALITY_STEPS) { const buf = await encodeJpeg(resized, q); if (buf.length <= WECHAT_BODY_IMAGE_MAX_SIZE) { const n2 = [...pn, `encoded as JPEG (${q} quality)`]; if (w < image.bitmap.width) n2.push(`resized to ${w}px wide`); return { buffer: buf, filename: renameWithExt(asset.filename, ".jpg"), contentType: JimpMime.jpeg, wasProcessed: true, processingNotes: n2 }; } }
  }
  throw new Error(`Unable to reduce ${asset.filename} below 1MB for WeChat body upload.`);
}
