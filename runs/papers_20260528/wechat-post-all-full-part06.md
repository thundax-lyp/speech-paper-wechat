---
title: "Agent/LLM论文速递｜2026-05-28｜全量版6/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版6/13：本期收录 20 篇，重点看 RAG与知识检索、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版6/13：本期收录 20 篇，重点看 RAG与知识检索、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "RAG与知识检索 / LLM推理与规划"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版6/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**20** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 6/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | BioELX: Cross-lingual Biomedical Entity Linking via Alias-based Retrieval and LLM Ranking | ⭐ 7/10 | retrieval |
| RAG与知识检索 | 2 | A Systematic Evaluation of Retrieval-Augmented Generation and Language Models for Space Operations | ⭐ 7/10 | retrieval, evaluation |
| LLM推理与规划 | 1 | When prompt perturbations break your A/B test: A valid statistical test for generative surveying | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 3 | CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text | ⭐ 7/10 | retrieval |
| RAG与知识检索 | 4 | High-Fidelity Industrial Crash Dynamics Prediction via Geometry-Aware Operator Learning with Memory-Efficient Low-Rank Attention | ⭐ 7/10 | RAG, retrieval |
| LLM推理与规划 | 2 | Playing with Words, Improving with Rewards: Training Language Models for Creative Association | ⭐ 7/10 | reasoning, planning |
| LLM推理与规划 | 3 | Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 5 | Periodic RoPE for Infinite Context LLMs | ⭐ 7/10 | RAG, retrieval |
| LLM推理与规划 | 4 | Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 6 | How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving | ⭐ 7/10 | RAG, retrieval |
| LLM推理与规划 | 5 | Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 7 | Memory-Based vs. Context-Only Conditioning Produces Distinct Behavioral Patterns in Stateful Personalization | ⭐ 6/10 | RAG, retrieval |
| LLM推理与规划 | 6 | Mathematical Modelling of Ethical AI Use in Higher Education: A Coordination Game Framework for Future-Facing Learning | ⭐ 6/10 | reasoning, planning |
| RAG与知识检索 | 8 | Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit | ⭐ 5/10 | retrieval |
| RAG与知识检索 | 9 | Paraphrase Brittleness in Production Retrieval-Augmented Commercial Recommendation: Reproducibility Below the Rerun-Stability Baseline | ⭐ 5/10 | retrieval |
| RAG与知识检索 | 10 | Tensor Memory: Fixed-Size Recurrent State for Long-Horizon Transformers | ⭐ 5/10 | RAG, retrieval |
| LLM推理与规划 | 7 | Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning | ⭐ 5/10 | planning |
| LLM推理与规划 | 8 | HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning | ⭐ 5/10 | planning |
| LLM推理与规划 | 9 | Do Models Know Why They Changed Their Mind? Interpretability and Faithfulness of Chain-of-Thought Under Knowledge Conflict | ⭐ 5/10 | reasoning, planning |
| RAG与知识检索 | 11 | ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor | ⭐ 5/10 | search |

</span>

## 🧠 LLM 推理 / 规划 / RAG


### [1] BioELX: Cross-lingual Biomedical Entity Linking via Alias-based Retrieval and LLM Ranking

- **评分**：7/10
- **作者/机构**：Yi Wang, Corina Dima, Liangyu Zhong, Steffen Staab
- **论文链接**：https://arxiv.org/abs/2605.27380
- **PDF**：https://arxiv.org/pdf/2605.27380
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“BioELX: Cross-lingual Biomedical Entity Linking via Alias-based Retrieval and LLM Ranking”展开，属于「RAG与知识检索」方向。作者核心问题是：gual, where mentions may appear in any language but must arXiv:2605.27380v1 [cs.CL] 9 Apr 2026 be linked to the same KB entities. In the example sentence Cross-lingual biomedical entity linking (BEL) “Une réduction du nombre de globules rouges peut entraı̂ne…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「RAG与知识检索」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“BioELX: Cross-lingual Biomedical Entity Linking via Alias-based Retrieval and LLM Ranking”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] A Systematic Evaluation of Retrieval-Augmented Generation and Language Models for Space Operations

- **评分**：7/10
- **作者/机构**：Ruben Belo, Marta Guimarães, Cláudia Soares
- **论文链接**：https://arxiv.org/abs/2605.27444
- **PDF**：https://arxiv.org/pdf/2605.27444
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Systematic Evaluation of Retrieval-Augmented Generation and Language Models for Space Operations”展开，属于「RAG与知识检索」方向。作者核心问题是：are inefficient, difficult to scale, and costly [21]. As a conse- quence, information handling in mission operations remains The rapid expansion of space activities has led to an un- time-intensive, error-prone, and cognitively demanding for precedented accum…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「RAG与知识检索」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“A Systematic Evaluation of Retrieval-Augmented Generation and Language Models for Space Operations”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] When prompt perturbations break your A/B test: A valid statistical test for generative surveying

- **评分**：7/10
- **作者/机构**：Hayden Helm, Carey Priebe
- **论文链接**：https://arxiv.org/abs/2605.27463
- **PDF**：https://arxiv.org/pdf/2605.27463
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When prompt perturbations break your A/B test: A valid statistical test for generative surveying”展开，属于「LLM推理与规划」方向。作者核心问题是：generative surveying has been explored for pref- arXiv:2605.27463v1 [stat.ME] 26 May 2026 erence elicitation (Brand et al., 2023; Hämäläinen Generative surveying – where collections of et al., 2023), policy design simulation and predic- LLM-based personas pro…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM推理与规划」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“When prompt perturbations break your A/B test: A valid statistical test for generative surveying”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text

- **评分**：7/10
- **作者/机构**：Khashayar Khajavi, Shaghayegh Sadeghi, Rise Adhikari, Alexander Tessier
- **论文链接**：https://arxiv.org/abs/2605.27700
- **PDF**：https://arxiv.org/pdf/2605.27700
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text”展开，属于「RAG与知识检索」方向。作者核心问题是：quirements of generated scientific text. In scholarly writing, factuality is not only a matter of producing fluent and plau- Large language models (LLMs) are increasingly sible claims: each claim must be connected to a traceable arXiv:2605.27700v1 [cs.DL] 26…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「RAG与知识检索」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] High-Fidelity Industrial Crash Dynamics Prediction via Geometry-Aware Operator Learning with Memory-Efficient Low-Rank Attention

- **评分**：7/10
- **作者/机构**：Deepak Akhare, Mohammad Amin Nabian, Corey Adams, Sudeep Chavare, Sanjay Choudhry
- **论文链接**：https://arxiv.org/abs/2605.27758
- **PDF**：https://arxiv.org/pdf/2605.27758
- **代码链接**：https://github.com/NVIDIA/physicsnemo/blob/main/examples/str

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“High-Fidelity Industrial Crash Dynamics Prediction via Geometry-Aware Operator Learning with Memory-Efficient Low-Rank Attention”展开，属于「RAG与知识检索」方向。作者核心问题是：Automotive crashworthiness optimization remains a safety-critical challenge, requiring the manage- ment of large-scale nonlinear structural deformations and energy dissipation through iterative, high- fidelity simulations. While traditional finite element sol…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「RAG与知识检索」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“High-Fidelity Industrial Crash Dynamics Prediction via Geometry-Aware Operator Learning with Memory-Efficient Low-Rank Attention”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] Playing with Words, Improving with Rewards: Training Language Models for Creative Association

- **评分**：7/10
- **作者/机构**：Vijeta Deshpande, Namrata Shivagunde, Sherin Muckatira, Hadrien Glaude, Mikhail Gronas, Claire Stevenson, Roger Beaty, Anna Rumshisky
- **论文链接**：https://arxiv.org/abs/2605.27832
- **PDF**：https://arxiv.org/pdf/2605.27832
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Playing with Words, Improving with Rewards: Training Language Models for Creative Association”展开，属于「LLM推理与规划」方向。作者核心问题是：AI research: how can we explicitly train LLMs to be genuinely creative, rather than merely hoping arXiv:2605.27832v1 [cs.CL] 27 May 2026 Large Language Models (LLMs) are being ap- creativity emerges as a byproduct of scale? plied to increasingly difficult pro…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM推理与规划」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Playing with Words, Improving with Rewards: Training Language Models for Creative Association”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China

- **评分**：7/10
- **作者/机构**：Hiroto Fukada, Takayuki Mizuno
- **论文链接**：https://arxiv.org/abs/2605.27845
- **PDF**：https://arxiv.org/pdf/2605.27845
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China”展开，属于「LLM推理与规划」方向。作者核心问题是：Financial and economic research often relies on urgent international priority, motivating calls for interdisci- arXiv:2605.27845v1 [cs.SI] 27 May 2026 structured supply-chain disclosures and commercial databases. plinary alliances [7]. China occupies a centra…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM推理与规划」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Periodic RoPE for Infinite Context LLMs

- **评分**：7/10
- **作者/机构**：Simin Huo
- **论文链接**：https://arxiv.org/abs/2605.27980
- **PDF**：https://arxiv.org/pdf/2605.27980
- **代码链接**：https://github.com/Cominder/miniwin

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Periodic RoPE for Infinite Context LLMs”展开，属于「RAG与知识检索」方向。作者核心问题是：arXiv:2605.27980v1 [cs.CL] 27 May 2026 The ability to process ultra-long contexts is 0 1 2 3 4 5 6 7 crucial for large language models (LLMs) to (a) 𝜃0 𝜃1 𝜃2 𝜃3 𝜃4 𝜃5 𝜃6 𝜃7 perform long-horizon tasks. While recent ef- forts have extended context windows to 1M…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「RAG与知识检索」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Periodic RoPE for Infinite Context LLMs”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback

- **评分**：7/10
- **作者/机构**：Bowen Wei, Nan Wang, Yuqing Zhou, Jinhao Pan, Ziwei Zhu
- **论文链接**：https://arxiv.org/abs/2605.28010
- **PDF**：https://arxiv.org/pdf/2605.28010
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback”展开，属于「LLM推理与规划」方向。作者核心问题是：self-evolution seeks to obtain such feedback auto- matically. arXiv:2605.28010v1 [cs.AI] 27 May 2026 Self-evolving large language models (LLMs) The central bottleneck is noisy self-generated learn by generating their own training tasks feedback. In domains su…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM推理与规划」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving

- **评分**：7/10
- **作者/机构**：Hanjiang Wu, Abhimanyu Rajeshkumar Bambhaniya, Sarbartha Banerjee, Tuhin Khare, Sudarshan Srinivasan, Suvinay Subramanian, Souvik Kundu, Madhu Kumar, Midhilesh Elavazhagan, William Won, Amir Yazdanbakhsh, Tushar Krishna
- **论文链接**：https://arxiv.org/abs/2605.28302
- **PDF**：https://arxiv.org/pdf/2605.28302
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving”展开，属于「RAG与知识检索」方向。作者核心问题是：Modern large language model (LLM) inference has progressively disaggregated to keep pace with growing model sizes and tight TTFT and TPOT service-level objec- tives: from chunked-prefill aggregation, to prefill–decode (P/D) disaggregation, and most recently t…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「RAG与知识检索」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay

- **评分**：7/10
- **作者/机构**：Mariah Al Giptiah Binte Yusoff, Jakin Tan, Bocheng Chen, Guangliang Liu, Xi Chen
- **论文链接**：https://arxiv.org/abs/2605.28782
- **PDF**：https://arxiv.org/pdf/2605.28782
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay”展开，属于「LLM推理与规划」方向。作者核心问题是：have emerged as an increasingly important research topic (Sheffield et al., 2025; Sadlier-Brown et al., arXiv:2605.28782v1 [cs.CL] 27 May 2026 Discourse particles, such as well and kind of, 2024; Wang et al., 2025; Rocha et al., 2025; Ein- are crucial compone…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM推理与规划」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] Memory-Based vs. Context-Only Conditioning Produces Distinct Behavioral Patterns in Stateful Personalization

- **评分**：6/10
- **作者/机构**：Junsoo Park, Youssef Medhat, Htet Phyo Wai, Ploy Thajchayapong, Ashok K. Goel
- **论文链接**：https://arxiv.org/abs/2605.27389
- **PDF**：https://arxiv.org/pdf/2605.27389
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Memory-Based vs. Context-Only Conditioning Produces Distinct Behavioral Patterns in Stateful Personalization”展开，属于「RAG与知识检索」方向。作者核心问题是：. We study how conditioning context shapes personalization behavior in a teacher-facing educational recommender system. We compare contextual conditioning based on the current student question with memory-based conditioning using persistent learner informatio…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Memory-Based vs. Context-Only Conditioning Produces Distinct Behavioral Patterns in Stateful Personalization”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [13] Mathematical Modelling of Ethical AI Use in Higher Education: A Coordination Game Framework for Future-Facing Learning

- **评分**：6/10
- **作者/机构**：Ndidi Bianca Ogbo, Zhao Song, Shatha Ghareeb, Anh Han
- **论文链接**：https://arxiv.org/abs/2605.27400
- **PDF**：https://arxiv.org/pdf/2605.27400
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Mathematical Modelling of Ethical AI Use in Higher Education: A Coordination Game Framework for Future-Facing Learning”展开，属于「LLM推理与规划」方向。作者核心问题是：The rapid uptake of generative artificial intelligence (AI) in higher education is reshaping assess- ment practices and intensifying concerns around academic integrity, fairness, and learning quality. While institutional responses increasingly emphasise polic…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Mathematical Modelling of Ethical AI Use in Higher Education: A Coordination Game Framework for Future-Facing Learning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM推理与规划」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [14] Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit

- **评分**：5/10
- **作者/机构**：Will Jack, Noah Lehman, Keller Maloney, Sarah Xu
- **论文链接**：https://arxiv.org/abs/2605.27439
- **PDF**：https://arxiv.org/pdf/2605.27439
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit”展开，属于「RAG与知识检索」方向。作者核心问题是：AI assistants like ChatGPT and Claude are recommendation engines, not search engines: they answer commercial queries by directly nominating brands rather than returning a list of links. Marketing to AI is therefore a broader problem than “show up in search” —…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [15] Paraphrase Brittleness in Production Retrieval-Augmented Commercial Recommendation: Reproducibility Below the Rerun-Stability Baseline

- **评分**：5/10
- **作者/机构**：Will Jack, Noah Lehman, Keller Maloney, Sarah Xu
- **论文链接**：https://arxiv.org/abs/2605.27440
- **PDF**：https://arxiv.org/pdf/2605.27440
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Paraphrase Brittleness in Production Retrieval-Augmented Commercial Recommendation: Reproducibility Below the Rerun-Stability Baseline”展开，属于「RAG与知识检索」方向。作者核心问题是：Small changes to how a buyer phrases a question — “best CRM” vs “top CRM” vs “best CRM for a SaaS startup” — produce substantially different brand recom- mendations from AI assistants. Across ∼6,000 paraphrase runs and ∼6,000 same- prompt rerun controls on Op…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Paraphrase Brittleness in Production Retrieval-Augmented Commercial Recommendation: Reproducibility Below the Rerun-Stability Baseline”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [16] Tensor Memory: Fixed-Size Recurrent State for Long-Horizon Transformers

- **评分**：5/10
- **作者/机构**：Kabir Swain, Sijie Han, Daniel Karl I. Weidele, Mauro Martino, Antonio Torralba
- **论文链接**：https://arxiv.org/abs/2605.27686
- **PDF**：https://arxiv.org/pdf/2605.27686
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Tensor Memory: Fixed-Size Recurrent State for Long-Horizon Transformers”展开，属于「RAG与知识检索」方向。作者核心问题是：rently with lightweight dynamics, and the retrieved memory Transformers process images and videos by flat- signal is fused back into the token stream through a gated tening space and time into long token sequences. residual path. At the same time, most modern…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Tensor Memory: Fixed-Size Recurrent State for Long-Horizon Transformers”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [17] Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning

- **评分**：5/10
- **作者/机构**：Jinhao Liang, Sven Koenig, Ferdinando Fioretto
- **论文链接**：https://arxiv.org/abs/2605.27697
- **PDF**：https://arxiv.org/pdf/2605.27697
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning”展开，属于「LLM推理与规划」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM推理与规划」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [18] HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning

- **评分**：5/10
- **作者/机构**：Kevin Lin, Ajay Mandlekar, Caelan Reed Garrett, Nikita Chernyadev, Yu Fang, Runyu Ding, Yuqi Xie, Justin Tran, Linxi Fan, Yuke Zhu
- **论文链接**：https://arxiv.org/abs/2605.27724
- **PDF**：https://arxiv.org/pdf/2605.27724
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning”展开，属于「LLM推理与规划」方向。作者核心问题是：Imitation learning is a promising approach for training humanoid robots to both walk and manipulate, but it requires a large number of demonstrations, which are time-intensive and difficult to collect via teleoperation. Existing data-generation algorithms can…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM推理与规划」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [19] Do Models Know Why They Changed Their Mind? Interpretability and Faithfulness of Chain-of-Thought Under Knowledge Conflict

- **评分**：5/10
- **作者/机构**：Pruthvinath Jeripity Venkata
- **论文链接**：https://arxiv.org/abs/2605.27773
- **PDF**：https://arxiv.org/pdf/2605.27773
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Models Know Why They Changed Their Mind? Interpretability and Faithfulness of Chain-of-Thought Under Knowledge Conflict”展开，属于「LLM推理与规划」方向。作者核心问题是：When a language model is shown a document that contradicts what it learned during training, it must choose: follow the document or trust its own knowledge. Prior work [Jeripity Venkata, 2026] proved that this choice depends on how well-known the fact is: famo…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Do Models Know Why They Changed Their Mind? Interpretability and Faithfulness of Chain-of-Thought Under Knowledge Conflict”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM推理与规划」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [20] ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor

- **评分**：5/10
- **作者/机构**：Taiheng Pan
- **论文链接**：https://arxiv.org/abs/2605.28062
- **PDF**：https://arxiv.org/pdf/2605.28062
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor”展开，属于「RAG与知识检索」方向。作者核心问题是：We describe ConvMemory, a small (∼3.6M-parameter) learned reranker for conversa- tional long-term memory retrieval, trained with cross-encoder teacher supervision over fused dense and lexical features. On the LongMemEval memory family, ConvMemory operates abo…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
