# Changelog

## 1.8.0 - 2026-05-21

- 仓库化每日语音论文公众号 pipeline，包含 arXiv 日期块抓取、稿件生成、封面生成和微信草稿推送脚本
- 将封面生成入口统一为 `nanobanana`，主脚本为 `scripts/image/generate_nanobanana.py`
- 敏感配置只保留 `.env.example` / `nanobanana.env.example` 模板，不提交真实凭据
- 重写英文 README，新增中文 README，并将项目主许可证设为 Apache-2.0
- 将 README 使用方式调整为 Codex / Claude Code agent-first，手动命令降级为调试路径
- 新增 README hero 插图、badge 组和更清晰的功能/自动化概览
- 新增每日推送公众号二维码入口，并为 README 标题/核心章节添加轻量 emoji

## 1.7.1 - 2026-04-08

- 固化默认双文章输出：精选版 + 全量版
- 精选版启用固定 rubric（新意 / 影响力 / 证据强度 / 受众匹配度），默认取 3–6 篇
- 微信发布链路支持 `--multi-manifest`，一次性生成同一个多图文草稿
- 总览表改为「方向 / 序号 / 论文 / 评分 / 关键词」结构
- 正文小标题统一改为 emoji 风格：📌 / ☠️ / 🔧 / 📊 / 💡
- 补充封面格式经验：微信会校验真实文件类型，不能只改扩展名
