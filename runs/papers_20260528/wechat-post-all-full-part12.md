---
title: "Agent/LLM论文速递｜2026-05-28｜全量版12/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版12/13：本期收录 20 篇，重点看 评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版12/13：本期收录 20 篇，重点看 评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "评测与安全"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版12/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**8** 篇

这是今天全量版第 12/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| 评测与安全 | 1 | Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 2 | Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 3 | A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 4 | Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 5 | Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 6 | Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models | ⭐ 6/10 | evaluation, reliability |
| 评测与安全 | 7 | When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs | ⭐ 5/10 | evaluation, reliability |
| 评测与安全 | 8 | Measuring Form and Function in Language Models | ⭐ 5/10 | evaluation, reliability |
| 应用与基准 | 1 | SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter | ⭐ 8/10 | LLM, application |
| 应用与基准 | 2 | From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons | ⭐ 7/10 | LLM, application |
| 应用与基准 | 3 | Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking | ⭐ 7/10 | LLM, application |
| 应用与基准 | 4 | BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving | ⭐ 7/10 | LLM, application |
| 应用与基准 | 5 | Locality-Aware Redundancy Pruning for LLM Depth Compression | ⭐ 7/10 | LLM, application |
| 应用与基准 | 6 | Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis | ⭐ 7/10 | LLM, application |
| 应用与基准 | 7 | Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification | ⭐ 7/10 | LLM, application |
| 应用与基准 | 8 | Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection | ⭐ 7/10 | LLM, application |
| 应用与基准 | 9 | Efficient Pre-Training of LLMs through Truncated SVD Layers | ⭐ 7/10 | LLM, application |
| 应用与基准 | 10 | Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence? | ⭐ 7/10 | LLM, application |
| 应用与基准 | 11 | Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting | ⭐ 6/10 | LLM, application |
| 应用与基准 | 12 | Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations | ⭐ 6/10 | LLM, application |

</span>

## 🛡️ 评测 / 安全 / 可靠性


### [1] Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation

- **评分**：7/10
- **作者/机构**：Jingwen Wu, Xijun Zhang, Ge Song
- **论文链接**：https://arxiv.org/abs/2605.27993
- **PDF**：https://arxiv.org/pdf/2605.27993
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation”展开，属于「评测与安全」方向。作者核心问题是：(a) VFV axis ( ): Visual vs. Parametric Knowledge (external-vs-internal) 20 vanilla LLaVA-1.5 Qwen-VL 18 arXiv:2605.27993v1 [cs.CL] 27 May 2026 Object hallucination remains a primary obsta- cle to the reliable deployment of Multimodal 16 Large Language Models…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations

- **评分**：7/10
- **作者/机构**：Matteo Gioele Collu, Riccardo Conte, Alberto Giaretta, Denis Kleyko, Mauro Conti, Matteo Zavatteri, Roberto Confalonieri
- **论文链接**：https://arxiv.org/abs/2605.28553
- **PDF**：https://arxiv.org/pdf/2605.28553
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations”展开，属于「评测与安全」方向。作者核心问题是：man Feedback (Christiano et al., 2017; Bai et al., 2022) and Supervised Fine-Tuning (Ouyang et al., In this paper, we investigate whether refusal arXiv:2605.28553v1 [cs.AI] 27 May 2026 behavior can be predicted from LLM interme- 2022). While effective in many…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models

- **评分**：7/10
- **作者/机构**：Aditya Kommineni, Emily Zhou, Kleanthis Avramidis, Tiantian Feng, Shrikanth Narayanan
- **论文链接**：https://arxiv.org/abs/2605.28563
- **PDF**：https://arxiv.org/pdf/2605.28563
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models”展开，属于「评测与安全」方向。作者核心问题是：et al., 2004; Goldberger et al., 2000), BCI Competi- Evaluating foundation models under appropri- tion IV-2A (Brunner et al., 2008), Kaggle ERN (Mat- ate adaptation settings is essential for under- tout et al., 2014), TUEV (Obeid and Picone, 2016), standing t…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking

- **评分**：7/10
- **作者/机构**：Ziyang You, Huilong He, Xiaoke Yang, Xuxing Lu
- **论文链接**：https://arxiv.org/abs/2605.28632
- **PDF**：https://arxiv.org/pdf/2605.28632
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking”展开，属于「评测与安全」方向。作者核心问题是：Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs). Existing schemes, including KGW, Unigram, and DipMark, derive their security guarantees from the assumption that the underlying pseudo-random numbe…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text

- **评分**：7/10
- **作者/机构**：Bushi Xiao, Sarvesh Soni, Daisy Zhe Wang
- **论文链接**：https://arxiv.org/abs/2605.28740
- **PDF**：https://arxiv.org/pdf/2605.28740
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text”展开，属于「评测与安全」方向。作者核心问题是：predictions. This is a form of self-assessment that reflects model reliability independent of ground arXiv:2605.28740v1 [cs.CL] 27 May 2026 As large language models are increasingly de- truth. Yona et al. (2026) formalize this distinction, ployed for clinical…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models

- **评分**：6/10
- **作者/机构**：Yuang Huang, Yafeng Zhang, Yu Zilan
- **论文链接**：https://arxiv.org/abs/2605.28123
- **PDF**：https://arxiv.org/pdf/2605.28123
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models”展开，属于「评测与安全」方向。作者核心问题是：In current practice, such verification prompts are often applied indiscriminately to all inputs (always- arXiv:2605.28123v1 [cs.CL] 27 May 2026 Prompt-based verification is widely used to mit- on prompting). However, this raises a question that igate hallucin…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「评测与安全」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [7] When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs

- **评分**：5/10
- **作者/机构**：Marcell Fekete, Johannes Bjerva, Tamás Káldi
- **论文链接**：https://arxiv.org/abs/2605.28346
- **PDF**：https://arxiv.org/pdf/2605.28346
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs”展开，属于「评测与安全」方向。作者核心问题是：arXiv:2605.28346v1 [cs.CL] 27 May 2026 Vision-language models (VLMs) are increas- ingly evaluated for whether they identify the right visual content, but little is known about whether they express such content in a discourse-appropriate form. We address this…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「评测与安全」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [8] Measuring Form and Function in Language Models

- **评分**：5/10
- **作者/机构**：Héctor Javier Vázquez Martínez, Charles Yang
- **论文链接**：https://arxiv.org/abs/2605.28616
- **PDF**：https://arxiv.org/pdf/2605.28616
- **代码链接**：https://github.com/hjvm/llm-form-and-function

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Measuring Form and Function in Language Models”展开，属于「评测与安全」方向。作者核心问题是：arXiv:2605.28616v1 [cs.CL] 27 May 2026 We introduce quantitative metrics from child language research to evaluate language mod- els. Our focus is on the formal syntactic and functional discourse properties of determiners in English, which young children acqui…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Measuring Form and Function in Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「评测与安全」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 🧪 应用 / Benchmark


### [9] SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter

- **评分**：8/10
- **作者/机构**：Lee Jung-Mok, Kim Sung-Bin, Joohyun Chang, Lee Hyun, Tae-Hyun Oh
- **论文链接**：https://arxiv.org/abs/2605.28084
- **PDF**：https://arxiv.org/pdf/2605.28084
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter”展开，属于「应用与基准」方向。作者核心问题是：Following recent advancements in artificial so- cial intelligence (Bainbridge et al., 1994; Dauten- Laughter is a complex social signal that con- arXiv:2605.28084v1 [cs.CL] 27 May 2026 veys communicative intent beyond amusement. hahn, 2007; Williams et al., 2…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「应用与基准」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons

- **评分**：7/10
- **作者/机构**：Xiangyu Ma, Teng Xiao, Zuchao Li, Lefei Zhang
- **论文链接**：https://arxiv.org/abs/2605.27387
- **PDF**：https://arxiv.org/pdf/2605.27387
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons”展开，属于「应用与基准」方向。作者核心问题是：arXiv:2605.27387v1 [cs.CL] 11 Apr 2026 Diffusion models promise efficient parallel text generation but rely on bidirectional atten- tion, creating a structural mismatch with pre- trained Autoregressive (AR) models. This in- compatibility precludes reusing rob…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking

- **评分**：7/10
- **作者/机构**：Wonkyun Kim, Sehyun Bae, Kwanki Ahn, Mungyu Bae, Saeun Choi, Soyeon You, Chandra Prabhakar, Sehyun Kim
- **论文链接**：https://arxiv.org/abs/2605.27429
- **PDF**：https://arxiv.org/pdf/2605.27429
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking”展开，属于「应用与基准」方向。作者核心问题是：1 Introduction Industrial video-on-demand (VOD) recommenders need richer Production recommenders are served through multi-stage pipelines: content understanding, but LLM-as-reranker designs repeat candidate generation, ranking or reranking, filtering, and fin…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving

- **评分**：7/10
- **作者/机构**：Tianyao Shi, Yi Ding
- **论文链接**：https://arxiv.org/abs/2605.27480
- **PDF**：https://arxiv.org/pdf/2605.27480
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving”展开，属于「应用与基准」方向。作者核心问题是：paper focuses on biodiversity impact (BI) charac- arXiv:2605.27480v1 [q-bio.OT] 26 May 2026 terization. BI measures ecosystem damage induced Large language model (LLM) serving cre- ates environmental impacts beyond carbon and by human activities through multi…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] Locality-Aware Redundancy Pruning for LLM Depth Compression

- **评分**：7/10
- **作者/机构**：Vincent-Daniel Yun, Youngrae Kim, Woosang Lim, YoungJin Heo, Minkyu Kim, Sunwoo Lee
- **论文链接**：https://arxiv.org/abs/2605.27786
- **PDF**：https://arxiv.org/pdf/2605.27786
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Locality-Aware Redundancy Pruning for LLM Depth Compression”展开，属于「应用与基准」方向。作者核心问题是：Large language models are known to contain representational redundancy across network depth, making depth pruning an effective approach for improving inference efficiency. Existing one-shot pruning methods rely on local layer importance or fixed redundancy as…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Locality-Aware Redundancy Pruning for LLM Depth Compression”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis

- **评分**：7/10
- **作者/机构**：Nils Constantin Hellwig, Niklas Donhauser, Jakob Fehle, Udo Kruschwitz, Christian Wolff
- **论文链接**：https://arxiv.org/abs/2605.28058
- **PDF**：https://arxiv.org/pdf/2605.28058
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis”展开，属于「应用与基准」方向。作者核心问题是：While recent few-shot prompting approaches have narrowed the gap to fine-tuned models (Hell- Recent work explored the capabilities of Large wig et al., 2025), a performance gap remains, par- arXiv:2605.28058v1 [cs.CL] 27 May 2026 Language Models (LLMs) in Asp…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification

- **评分**：7/10
- **作者/机构**：Dylan Bouchard, Mohit Singh Chauhan, Zeya Ahmad, Ho-Kyeong Ra
- **论文链接**：https://arxiv.org/abs/2605.28500
- **PDF**：https://arxiv.org/pdf/2605.28500
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification”展开，属于「应用与基准」方向。作者核心问题是：2024) and LiveSQLBench (Team, 2024) show that even state-of-the-art models produce incorrect so- arXiv:2605.28500v1 [cs.CL] 27 May 2026 Large language models have shown impres- lutions for a substantial fraction of problems (Gao sive capabilities in code gene…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection

- **评分**：7/10
- **作者/机构**：Zhixing Zuo, Huilin He, Jiasheng Wu, Dawei Cheng
- **论文链接**：https://arxiv.org/abs/2605.28524
- **PDF**：https://arxiv.org/pdf/2605.28524
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection”展开，属于「应用与基准」方向。作者核心问题是：<Text attributes> : This y1 y2 y3 … transaction occurred at… 0.15 0.76 -1.2 … arXiv:2605.28524v1 [cs.AI] 27 May 2026 In recent years, Large Language Models (LLMs) have shown great capability in pro- Privacy cessing graph tasks such as fraud detection. Constra…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] Efficient Pre-Training of LLMs through Truncated SVD Layers

- **评分**：7/10
- **作者/机构**：Kaivan Kamali, Kajetan Schweighofer, Hormoz Shahrzad, Olivier Francon, Babak Hodjat, Risto Miikkulainen
- **论文链接**：https://arxiv.org/abs/2605.28573
- **PDF**：https://arxiv.org/pdf/2605.28573
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Efficient Pre-Training of LLMs through Truncated SVD Layers”展开，属于「应用与基准」方向。作者核心问题是：The massive scaling of Large Language Models (LLMs) has made pretraining in- creasingly cost-prohibitive. While low-rank representation and orthonormal weight matrices could in principle reduce parameter counts and computational overhead, most existing method…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Efficient Pre-Training of LLMs through Truncated SVD Layers”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?

- **评分**：7/10
- **作者/机构**：Gabrielle Kaili-May Liu, Arman Cohan
- **论文链接**：https://arxiv.org/abs/2605.28778
- **PDF**：https://arxiv.org/pdf/2605.28778
- **代码链接**：https://github.com/yale-nlp/marker_internal_confidence

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?”展开，属于「应用与基准」方向。作者核心问题是：LLMs’ linguistically expressed confidence should faithfully reflect their intrinsic uncertainty. While recent work shows LLMs struggle to use epistemic markers (e.g., “it is likely...”) in a human-aligned fashion, it remains unclear whether models can apply t…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting

- **评分**：6/10
- **作者/机构**：Hui Dai, Ryan Teehan, Parsa Torabian, Mengye Ren
- **论文链接**：https://arxiv.org/abs/2605.27668
- **PDF**：https://arxiv.org/pdf/2605.27668
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting”展开，属于「应用与基准」方向。作者核心问题是：Probabilistic forecasting estimates the likelihood of uncertain future events. To improve LLM forecast- ing, existing methods typically learn from binary outcomes to output verbalized forecasts. However, while aggregated human forecasts contain rich informati…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [20] Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations

- **评分**：6/10
- **作者/机构**：Simardeep Singh, Paras Chopra
- **论文链接**：https://arxiv.org/abs/2605.27970
- **PDF**：https://arxiv.org/pdf/2605.27970
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations”展开，属于「应用与基准」方向。作者核心问题是：data. Recent work has shown that LLM representations While large language models (LLMs) are trained exhibit structured geometry across a range of concepts. For instance, cyclical domains such as days of the week, months, arXiv:2605.27970v1 [cs.AI] 27 May 2026…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
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
