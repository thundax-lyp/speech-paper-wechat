---
title: "Agent/LLM论文速递｜2026-05-28｜全量版4/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版4/13：本期收录 20 篇，重点看 RAG与知识检索、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版4/13：本期收录 20 篇，重点看 RAG与知识检索、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "RAG与知识检索 / LLM推理与规划"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版4/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**20** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 4/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer? | ⭐ 8/10 | retrieval |
| LLM推理与规划 | 1 | Reasoning and Planning with Dynamically Changing Norms | ⭐ 8/10 | reasoning, planning |
| RAG与知识检索 | 2 | Trinity: Unifying Class-Agnostic Terrain and Semantic Segmentation for Unstructured Outdoor Environments by Leveraging Synthetic Data | ⭐ 8/10 | RAG |
| RAG与知识检索 | 3 | Hierarchical Prompt-Domain Control and Learning for Resource-Constrained Agentic Language Models | ⭐ 8/10 | agent |
| LLM推理与规划 | 2 | Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking | ⭐ 8/10 | reasoning |
| RAG与知识检索 | 4 | UserHarness: Harnessing User Minds for Stronger Agent Theory-of-Mind | ⭐ 8/10 | agent |
| RAG与知识检索 | 5 | PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft | ⭐ 8/10 | agent |
| LLM推理与规划 | 3 | Can Segmentation Models Understand the World? Towards Proactive Affordance Reasoning via Visual Chain-of-Thought | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 4 | A Query Engine for the Agents | ⭐ 8/10 | agent |
| RAG与知识检索 | 6 | Fine-Tuned LLM as a Complementary Predictor Improving Ads System | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 7 | C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning | ⭐ 8/10 | retrieval, reasoning |
| RAG与知识检索 | 8 | FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research | ⭐ 8/10 | agent, search |
| RAG与知识检索 | 9 | DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation | ⭐ 8/10 | RAG |
| RAG与知识检索 | 10 | Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents | ⭐ 8/10 | agent |
| RAG与知识检索 | 11 | Boundary Suppression Asymmetry in Post-trained Assistants: Over-expansion as a Controllability Cost | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 12 | Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 13 | Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG | ⭐ 8/10 | RAG |
| RAG与知识检索 | 14 | MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 15 | Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 16 | SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning | ⭐ 8/10 | retrieval |

</span>

## 🧠 LLM 推理 / 规划 / RAG


### [1] Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer?

- **评分**：8/10
- **作者/机构**：Syed Huma Shah
- **论文链接**：https://arxiv.org/abs/2605.27494
- **PDF**：https://arxiv.org/pdf/2605.27494
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer?”展开，属于「RAG与知识检索」方向。作者核心问题是：Modern retrieval-augmented generation (RAG) deployments increasingly rely on caching to reduce token cost and time-to-first-token (TTFT). Prefix-level KV reuse is now standard in serving stacks such as vLLM, and chunk-level and position-independent reuse have…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer?”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Reasoning and Planning with Dynamically Changing Norms

- **评分**：8/10
- **作者/机构**：Taylor Olson, Roberto Salas-Damian, Kenneth D. Forbus
- **论文链接**：https://arxiv.org/abs/2605.27622
- **PDF**：https://arxiv.org/pdf/2605.27622
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reasoning and Planning with Dynamically Changing Norms”展开，属于「LLM推理与规划」方向。作者核心问题是：This paper is organized as follows. We start by provid- arXiv:2605.27622v1 [cs.AI] 26 May 2026 ing background on the formal representations we draw upon. To safely interact with humans, AI agents must Next, we introduce our approach to reasoning about dynam-…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Reasoning and Planning with Dynamically Changing Norms”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] Trinity: Unifying Class-Agnostic Terrain and Semantic Segmentation for Unstructured Outdoor Environments by Leveraging Synthetic Data

- **评分**：8/10
- **作者/机构**：Marcus G Müller, Wout Boerdijk, Maximilian Durner, Riccardo Giubilato, Abel Gawel, Wolfgang Stürzl, Roland Siegwart, Rudolph Triebel
- **论文链接**：https://arxiv.org/abs/2605.27644
- **PDF**：https://arxiv.org/pdf/2605.27644
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Trinity: Unifying Class-Agnostic Terrain and Semantic Segmentation for Unstructured Outdoor Environments by Leveraging Synthetic Data”展开，属于「RAG与知识检索」方向。作者核心问题是：Terrain understanding is fundamental for mobile robots operating in unstructured outdoor environments. Ex- isting vision-based traversability estimation methods rely on robot-specific annotations or semantic class mappings, limit- arXiv:2605.27644v1 [cs.RO] 2…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Trinity: Unifying Class-Agnostic Terrain and Semantic Segmentation for Unstructured Outdoor Environments by Leveraging Synthetic Data”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] Hierarchical Prompt-Domain Control and Learning for Resource-Constrained Agentic Language Models

- **评分**：8/10
- **作者/机构**：Joan Vendrell Gallart, Russell Bent, Michael Grosskopf
- **论文链接**：https://arxiv.org/abs/2605.27703
- **PDF**：https://arxiv.org/pdf/2605.27703
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Hierarchical Prompt-Domain Control and Learning for Resource-Constrained Agentic Language Models”展开，属于「RAG与知识检索」方向。作者核心问题是：Large Language Models are increasingly deployed inside agentic systems, where they must follow structured protocols, adapt to evolving states, and operate under memory, latency, and cost constraints. In such regimes, prompt extension is unreliable: growing co…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Hierarchical Prompt-Domain Control and Learning for Resource-Constrained Agentic Language Models”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking

- **评分**：8/10
- **作者/机构**：Zhenghan Song, Yunyi Li, Yulong Liu
- **论文链接**：https://arxiv.org/abs/2605.27712
- **PDF**：https://arxiv.org/pdf/2605.27712
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking”展开，属于「LLM推理与规划」方向。作者核心问题是：that can be computed during generation, not after Long reasoning traces need reliability esti- final correctness is available. This connects to se- arXiv:2605.27712v1 [cs.AI] 26 May 2026 mates before final answers are known. We lective prediction and confiden…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] UserHarness: Harnessing User Minds for Stronger Agent Theory-of-Mind

- **评分**：8/10
- **作者/机构**：Cheng Qian, Jiayu Liu, Heng Ji
- **论文链接**：https://arxiv.org/abs/2605.27721
- **PDF**：https://arxiv.org/pdf/2605.27721
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“UserHarness: Harnessing User Minds for Stronger Agent Theory-of-Mind”展开，属于「RAG与知识检索」方向。作者核心问题是：The core difficulty of ToM does not come merely from long context or complex language, but often Understanding what a user believes and intends arXiv:2605.27721v1 [cs.CL] 26 May 2026 is central to building effective agent assistants. lie in perspective: the u…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“UserHarness: Harnessing User Minds for Stronger Agent Theory-of-Mind”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft

- **评分**：8/10
- **作者/机构**：Yuchen Guo, Junli Gong, Hongmin Cai, Yiu-ming Cheung, Weifeng Su
- **论文链接**：https://arxiv.org/abs/2605.27762
- **PDF**：https://arxiv.org/pdf/2605.27762
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft”展开，属于「RAG与知识检索」方向。作者核心问题是：idation, PEAM introduces a parameterization- We present PEAM, a Parametric Embodied worthiness score for deciding which experience Agent Memory framework in Minecraft that should be internalized, and a scale-free self- transforms agent memory from inference-t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Can Segmentation Models Understand the World? Towards Proactive Affordance Reasoning via Visual Chain-of-Thought

- **评分**：8/10
- **作者/机构**：Yuchen Guo, Junli Gong, Hongmin Cai, Yiu-ming Cheung, Weifeng Su
- **论文链接**：https://arxiv.org/abs/2605.27764
- **PDF**：https://arxiv.org/pdf/2605.27764
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Can Segmentation Models Understand the World? Towards Proactive Affordance Reasoning via Visual Chain-of-Thought”展开，属于「LLM推理与规划」方向。作者核心问题是：instructions are commonly studied as explicit re- ferring expressions (Kazemzadeh et al., 2014; Yu arXiv:2605.27764v1 [cs.CV] 26 May 2026 Recent segmentation models couple large lan- et al., 2016; Liu et al., 2023) or implicit reasoning guage models (LLMs) wi…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Can Segmentation Models Understand the World? Towards Proactive Affordance Reasoning via Visual Chain-of-Thought”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] A Query Engine for the Agents

- **评分**：8/10
- **作者/机构**：Kenny Daniel
- **论文链接**：https://arxiv.org/abs/2605.27785
- **PDF**：https://arxiv.org/pdf/2605.27785
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Query Engine for the Agents”展开，属于「LLM推理与规划」方向。作者核心问题是：stay where it already lives [5]. The conventional read path puts The fastest-growing data in production today is unstructured text: heavy infrastructure (Spark, Trino, a managed warehouse, a query agent traces, chat logs, reasoning chains, model outputs. Peop…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“A Query Engine for the Agents”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] Fine-Tuned LLM as a Complementary Predictor Improving Ads System

- **评分**：8/10
- **作者/机构**：Hui Yang, Daiwei He, Kevin Jiang, Taejin Park, Kungang Li, Jiajun Luo, Yuying Chen, Xinyi Zhang, Sihan Wang, Haoyu He, Yu Liu, Lakshmi Manoharan 等
- **论文链接**：https://arxiv.org/abs/2605.27856
- **PDF**：https://arxiv.org/pdf/2605.27856
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Fine-Tuned LLM as a Complementary Predictor Improving Ads System”展开，属于「RAG与知识检索」方向。作者核心问题是：predictive capacity can be efficiently harnessed. Beyond validating Recommendation systems power engagement and monetization LLMs for ads applications, our results show that targeted ancil- across feeds, ads, and short-video platforms, but translating the lar…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Fine-Tuned LLM as a Complementary Predictor Improving Ads System”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning

- **评分**：8/10
- **作者/机构**：Yuwei Miao, Gen Li, Yunsheng Zeng, Xiandong Li, Yujin Wang, Siyu Chen, Luning Wang, Yunhao Qiao, Junfeng Wang, Jianwei Lv, Bo Yuan
- **论文链接**：https://arxiv.org/abs/2605.27860
- **PDF**：https://arxiv.org/pdf/2605.27860
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning”展开，属于「RAG与知识检索」方向。作者核心问题是：Allergic Sinusitis Ground Truth Clinical History arXiv:2605.27860v1 [cs.AI] 27 May 2026 Retrieval-augmented generation combined Think Retrieve Refine Allergic Rhinitis with reinforcement learning has shown promise Clinical Query Multi-Turn RAG Diagnosis Proce…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research

- **评分**：8/10
- **作者/机构**：Di Zhu, Zheng, Zihan Chen
- **论文链接**：https://arxiv.org/abs/2605.27864
- **PDF**：https://arxiv.org/pdf/2605.27864
- **代码链接**：https://github.com/dgtql/FundaPod

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research”展开，属于「RAG与知识检索」方向。作者核心问题是：Large language models (LLMs) are increasingly applied in finance, yet most existing work em- phasizes trading signals or financial NLP tasks centered on prediction. Institutional fundamental research, by contrast, requires human analysts or AI agents to gathe…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation

- **评分**：8/10
- **作者/机构**：Xinjiang Yu, Junyi Han, Zhuofan Chen, Chi Zhang, Xiangyu Fu, Jingyuan Tan, Zirui You, Yixiang Jian, Yu-Ping Wang, Chengliang Chai
- **论文链接**：https://arxiv.org/abs/2605.27931
- **PDF**：https://arxiv.org/pdf/2605.27931
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation”展开，属于「RAG与知识检索」方向。作者核心问题是：Scientific diagrams are essential for communicating complex methodologies in academic papers. A natural way for researchers to specify such diagrams is through rough sketches, where text labels, connectors, and spatial arrangements express early semantic and…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents

- **评分**：8/10
- **作者/机构**：Xinze Li, Yuhang Zang, Yixin Cao, Aixin Sun
- **论文链接**：https://arxiv.org/abs/2605.27955
- **PDF**：https://arxiv.org/pdf/2605.27955
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：used as our experimental substrate, and server-side MCP descriptions (Anthropic, 2024) all ship as arXiv:2605.27955v1 [cs.PL] 27 May 2026 Markdown skill libraries for LLM agents ship free-form prose for human and LLM readers. as free-form prose, forcing the a…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Boundary Suppression Asymmetry in Post-trained Assistants: Over-expansion as a Controllability Cost

- **评分**：8/10
- **作者/机构**：Jiarui Han
- **论文链接**：https://arxiv.org/abs/2605.27969
- **PDF**：https://arxiv.org/pdf/2605.27969
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Boundary Suppression Asymmetry in Post-trained Assistants: Over-expansion as a Controllability Cost”展开，属于「RAG与知识检索」方向。作者核心问题是：to be helpful, complete, cautious, and unlikely to leave important information unsaid. Instruc- Post-trained language-model assistants are of- tion tuning and preference-based post-training re- ten optimized to avoid under-answering, en- inforce this broad di…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Boundary Suppression Asymmetry in Post-trained Assistants: Over-expansion as a Controllability Cost”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses

- **评分**：8/10
- **作者/机构**：Kerui Peng, Feifei Li, Xingyu Fan, Wenhui Que
- **论文链接**：https://arxiv.org/abs/2605.27971
- **PDF**：https://arxiv.org/pdf/2605.27971
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses”展开，属于「RAG与知识检索」方向。作者核心问题是：ferent style conditions or across multiple valid so- lutions under the same condition, CE under finite- When large language models are fine-tuned capacity shared representations tends to encourage arXiv:2605.27971v1 [cs.CL] 27 May 2026 to generate persona- or…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG

- **评分**：8/10
- **作者/机构**：Jiaming Zhang, Yibo Zhao, Jing Yu, Jianxiang Yu, Xiang Li
- **论文链接**：https://arxiv.org/abs/2605.28004
- **PDF**：https://arxiv.org/pdf/2605.28004
- **代码链接**：https://github.com/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG”展开，属于「RAG与知识检索」方向。作者核心问题是：2024). This direction has shown particular promise for long texts and complex QA, where flat vector arXiv:2605.28004v1 [cs.CL] 27 May 2026 GraphRAG extends retrieval-augmented gener- retrieval frequently surfaces superficially relevant ation by organizing cor…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models

- **评分**：8/10
- **作者/机构**：Hyeonjeong Ha, Jeonghwan Kim, Cheng Qian, Jiayu Liu, William M. Campbell, Yue Wu, Yuji Zhang, Kathleen McKeown, Dilek Hakkani-Tur, Heng Ji
- **论文链接**：https://arxiv.org/abs/2605.28009
- **PDF**：https://arxiv.org/pdf/2605.28009
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models”展开，属于「RAG与知识检索」方向。作者核心问题是：2025), but it also creates a new reliability risk: once noisy, unsupported, or misstructured knowledge is arXiv:2605.28009v1 [cs.CL] 27 May 2026 Memory-augmented large language models ex- written to memory, it can be repeatedly retrieved tend reasoning beyond…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts

- **评分**：8/10
- **作者/机构**：Liu O. Martin, Lucas Bandarkar, Nanyun Peng
- **论文链接**：https://arxiv.org/abs/2605.28042
- **PDF**：https://arxiv.org/pdf/2605.28042
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts”展开，属于「RAG与知识检索」方向。作者核心问题是：22 Kept 21 Pruned 20 arXiv:2605.28042v1 [cs.CL] 27 May 2026 19 Modern large language models (LLMs) achieve 18 17 state-of-the-art machine translation perfor- 16 15 mance, but they do so as broad generalists 14 13 largely trained for many tasks and capabilitie…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning

- **评分**：8/10
- **作者/机构**：Jiachen Qian
- **论文链接**：https://arxiv.org/abs/2605.28074
- **PDF**：https://arxiv.org/pdf/2605.28074
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning”展开，属于「RAG与知识检索」方向。作者核心问题是：Keywords Retrieval-Augmented Generation (RAG) mitigates LLM hallucina- Retrieval-Augmented Generation, Data Poisoning, Adversarial At- tions but introduces a critical vulnerability: corpus integrity. We tacks, Dense Retrieval, Large Language Models arXiv:2605…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
