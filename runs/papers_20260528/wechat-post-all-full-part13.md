---
title: "Agent/LLM论文速递｜2026-05-28｜全量版13/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版13/13：本期收录 18 篇，重点看 应用与基准；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版13/13：本期收录 18 篇，重点看 应用与基准；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "应用与基准"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版13/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **18** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 13/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| 应用与基准 | 1 | Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models | ⭐ 6/10 | LLM, application |
| 应用与基准 | 2 | Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation | ⭐ 6/10 | LLM, application |
| 应用与基准 | 3 | Learning the Error Patterns of Language Models | ⭐ 6/10 | LLM, application |
| 应用与基准 | 4 | Diffusion Large Language Models for Visual Speech Recognition | ⭐ 6/10 | LLM, application |
| 应用与基准 | 5 | Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets | ⭐ 6/10 | LLM, application |
| 应用与基准 | 6 | The Ethics of LLM Sandbox and Persona Dynamics | ⭐ 6/10 | LLM, application |
| 应用与基准 | 7 | Human-AI Collaboration for Estimating Scientific Replicability | ⭐ 5/10 | LLM, application |
| 应用与基准 | 8 | Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 9 | Soro: A Lightweight Foundation Model and Chatbot for Tajik | ⭐ 4/10 | LLM, application |
| 应用与基准 | 10 | Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions | ⭐ 4/10 | LLM, application |
| 应用与基准 | 11 | Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts | ⭐ 4/10 | LLM, application |
| 应用与基准 | 12 | CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 13 | FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales | ⭐ 4/10 | LLM, application |
| 应用与基准 | 14 | When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 15 | Pruning and Distilling Mixture-of-Experts into Dense Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 16 | PrunePath: Towards Highly Structured Sparse Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 17 | Entropy-aware Masking for Masked Language Modeling | ⭐ 4/10 | LLM, application |
| 应用与基准 | 18 | Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests | ⭐ 4/10 | LLM, application |

</span>

## 🧪 应用 / Benchmark


### [1] Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models

- **评分**：6/10
- **作者/机构**：Himanshu Beniwal, Mayank Singh
- **论文链接**：https://arxiv.org/abs/2605.27997
- **PDF**：https://arxiv.org/pdf/2605.27997
- **代码链接**：https://github.com/himanshubeniwal/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models”展开，属于「应用与基准」方向。作者核心问题是：Toxic Layers! arXiv:2605.27997v1 [cs.CL] 27 May 2026 Large language models frequently generate Toxic Text Toxic Generation (I hate you and want to hurt…) (and stab you so...) toxic, hateful, or harmful content, yet exist- ing mitigation methods rely on costly…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [2] Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation

- **评分**：6/10
- **作者/机构**：Annabella Sánchez-Guzmán, Lukas Eberhard, Denis Helic, Lisette Espín-Noboa
- **论文链接**：https://arxiv.org/abs/2605.28187
- **PDF**：https://arxiv.org/pdf/2605.28187
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [3] Learning the Error Patterns of Language Models

- **评分**：6/10
- **作者/机构**：Jinwoo Kim, Taylor Berg-KirkPatrick, Loris D'Antoni
- **论文链接**：https://arxiv.org/abs/2605.28328
- **PDF**：https://arxiv.org/pdf/2605.28328
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learning the Error Patterns of Language Models”展开，属于「应用与基准」方向。作者核心问题是：When generating outputs for domains with specific validity constraints (e.g., a program should compile), LLMs often fail in a small number of focused ways: for example, by using Python function names when generating TypeScript. We observe that these error pat…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Learning the Error Patterns of Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [4] Diffusion Large Language Models for Visual Speech Recognition

- **评分**：6/10
- **作者/机构**：Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro
- **论文链接**：https://arxiv.org/abs/2605.28456
- **PDF**：https://arxiv.org/pdf/2605.28456
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Diffusion Large Language Models for Visual Speech Recognition”展开，属于「应用与基准」方向。作者核心问题是：Left-to-right decoding: early errors cannot be revised Step 1 I arXiv:2605.28456v1 [cs.AI] 27 May 2026 Existing Visual Speech Recognition (VSR) sys- Step 2 I BACK tems commonly rely on left-to-right autoregres- BACK 0.42 ✓ selected sive decoding, which can fo…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Diffusion Large Language Models for Visual Speech Recognition”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [5] Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets

- **评分**：6/10
- **作者/机构**：Andrea Gurioli, Davide D'Ascenzo, Federico Pennino, Maurizio Gabbrielli, Stefano Zacchiroli
- **论文链接**：https://arxiv.org/abs/2605.28510
- **PDF**：https://arxiv.org/pdf/2605.28510
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets”展开，属于「应用与基准」方向。作者核心问题是：Large language models (LLMs) for code completion generation process of Large Language Models (LLMs) raises and generation are increasingly used in software development, significant concerns. Generating code without acknowledging yet they may reproduce trainin…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [6] The Ethics of LLM Sandbox and Persona Dynamics

- **评分**：6/10
- **作者/机构**：Tim Gebbie, Stewart Gebbie
- **论文链接**：https://arxiv.org/abs/2605.28647
- **PDF**：https://arxiv.org/pdf/2605.28647
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“The Ethics of LLM Sandbox and Persona Dynamics”展开，属于「应用与基准」方向。作者核心问题是：arXiv:2605.28647v1 [cs.AI] 27 May 2026 It is well known that LLM guardrails and trained persona dynamics can produce a reality gap: the distance between the world a LLM is permitted or shaped to describe, and the world in which users must act. Here we argue t…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“The Ethics of LLM Sandbox and Persona Dynamics”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [7] Human-AI Collaboration for Estimating Scientific Replicability

- **评分**：5/10
- **作者/机构**：Tatiana Chakravorti, Robert Fraleigh, Timothy Fritton, Christopher Griffin, Vaibhav Singh, Sai Koneru, C. Lee Giles, David Pennock, Anthony Kwasnica, Sarah Rajtmajer
- **论文链接**：https://arxiv.org/abs/2605.27394
- **PDF**：https://arxiv.org/pdf/2605.27394
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Human-AI Collaboration for Estimating Scientific Replicability”展开，属于「应用与基准」方向。作者核心问题是：. Determining whether published scientific findings can successfully be replicated is a long-standing challenge in the empirical sciences. Existing ap- proaches for replicability assessment typically rely either on human judgment, i.e., creative assembly of h…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Human-AI Collaboration for Estimating Scientific Replicability”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [8] Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models

- **评分**：4/10
- **作者/机构**：Jaehoon Kang, Yejin Lee, Yoonji Park, Kyuhong Shim
- **论文链接**：https://arxiv.org/abs/2605.27376
- **PDF**：https://arxiv.org/pdf/2605.27376
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models”展开，属于「应用与基准」方向。作者核心问题是：A. Inter-utterance Style Interpolation While prompt-based text-to-speech (TTS) mod- arXiv:2605.27376v1 [cs.CL] 9 Apr 2026 els enable natural language-driven speaking style control, they often provide limited fine- Source Style: Male voice Target Style: Female…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [9] Soro: A Lightweight Foundation Model and Chatbot for Tajik

- **评分**：4/10
- **作者/机构**：Stanislav Liashkov, Haitz Sáez de Ocáriz Borde, Azizjon Azimi, Khushbakht Shaymardonov, Shuhratjon Khalitbekov, Bonu Boboeva
- **论文链接**：https://arxiv.org/abs/2605.27379
- **PDF**：https://arxiv.org/pdf/2605.27379
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Soro: A Lightweight Foundation Model and Chatbot for Tajik”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Soro: A Lightweight Foundation Model and Chatbot for Tajik”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [10] Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions

- **评分**：4/10
- **作者/机构**：Antonia Karamolegkou, Nicolas Angleraud, Benoît Sagot, Thibault Clérice
- **论文链接**：https://arxiv.org/abs/2605.27750
- **PDF**：https://arxiv.org/pdf/2605.27750
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions”展开，属于「应用与基准」方向。作者核心问题是：often producing semantically plausible but visually unsupported output (Shu et al., 2025; Liang et al., arXiv:2605.27750v1 [cs.CL] 26 May 2026 Recent work has shown that Vision-Language 2026; He et al., 2025; Gong et al., 2026). While Models (VLMs) used for o…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [11] Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts

- **评分**：4/10
- **作者/机构**：Yuyue Wang, Xihua Wang, Xin Cheng, Yijing Chen, Ruihua Song
- **论文链接**：https://arxiv.org/abs/2605.28063
- **PDF**：https://arxiv.org/pdf/2605.28063
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts”展开，属于「应用与基准」方向。作者核心问题是：Audio generation has made significant progress, yet synthesizing unified audio where speech and sounds are naturally composited remains a challenge. Current methods either rely on disjoint pipelines, which fail to capture fine-grained inter- actions, or requi…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [12] CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models

- **评分**：4/10
- **作者/机构**：Fengze Yang, Bo Yu, Xuewen Luo, Cathy Liu, Chenxi Liu
- **论文链接**：https://arxiv.org/abs/2605.28115
- **PDF**：https://arxiv.org/pdf/2605.28115
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [13] FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales

- **评分**：4/10
- **作者/机构**：Jorge L. Rodriguez, Victor Angulo Morales, Areej Alwahas, Mariana Elias Lara, Fida Mohammad Thoker, Kasper Johansen, Bernard Ghanem, Fernando T. Maestre, Matthew F. McCabe
- **论文链接**：https://arxiv.org/abs/2605.28174
- **PDF**：https://arxiv.org/pdf/2605.28174
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [14] When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models

- **评分**：4/10
- **作者/机构**：Jungwon Park, Jimyeong Kim, Jungmin Ko, Nojun Kwak, Wonjong Rhee
- **论文链接**：https://arxiv.org/abs/2605.28181
- **PDF**：https://arxiv.org/pdf/2605.28181
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models”展开，属于「应用与基准」方向。作者核心问题是：Most training-free DLM decoding strategies use Diffusion language models decode text by it- model confidence as the position-selection sig- arXiv:2605.28181v1 [cs.CL] 27 May 2026 eratively denoising masked token sequences, nal. For example, top-probability de…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [15] Pruning and Distilling Mixture-of-Experts into Dense Language Models

- **评分**：4/10
- **作者/机构**：Junhyuck Kim, Jihun Yun, Haechan Kim, Gyeongman Kim, Joonghyun Bae, Jaewoong Cho
- **论文链接**：https://arxiv.org/abs/2605.28207
- **PDF**：https://arxiv.org/pdf/2605.28207
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Pruning and Distilling Mixture-of-Experts into Dense Language Models”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Pruning and Distilling Mixture-of-Experts into Dense Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [16] PrunePath: Towards Highly Structured Sparse Language Models

- **评分**：4/10
- **作者/机构**：Zhexuan Gu, Zixun Fu, Yancheng Yuan
- **论文链接**：https://arxiv.org/abs/2605.28283
- **PDF**：https://arxiv.org/pdf/2605.28283
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PrunePath: Towards Highly Structured Sparse Language Models”展开，属于「应用与基准」方向。作者核心问题是：… Transformer Backbone (N Layers) MoE Layer arXiv:2605.28283v1 [cs.CL] 27 May 2026 Feed-forward networks (FFNs) dominate the Input sequence (Token) Input sequence (Token) Input Token Embedding parameter count and computation of modern language models, yet exi…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“PrunePath: Towards Highly Structured Sparse Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [17] Entropy-aware Masking for Masked Language Modeling

- **评分**：4/10
- **作者/机构**：Gokul Srinivasagan, Kai Hartung, Munir Georges
- **论文链接**：https://arxiv.org/abs/2605.28526
- **PDF**：https://arxiv.org/pdf/2605.28526
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Entropy-aware Masking for Masked Language Modeling”展开，属于「应用与基准」方向。作者核心问题是：training the model to predict these masked tokens using the surrounding context. This enables the Masked language modeling has become a stan- arXiv:2605.28526v1 [cs.AI] 27 May 2026 model to learn both syntactic structure and seman- dard pretraining objective…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Entropy-aware Masking for Masked Language Modeling”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [18] Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests

- **评分**：4/10
- **作者/机构**：Richard J. Young, Gregory D. Moody
- **论文链接**：https://arxiv.org/abs/2605.28734
- **PDF**：https://arxiv.org/pdf/2605.28734
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
