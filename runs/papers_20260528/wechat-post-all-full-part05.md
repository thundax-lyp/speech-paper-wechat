---
title: "Agent/LLM论文速递｜2026-05-28｜全量版5/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版5/13：本期收录 20 篇，重点看 RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版5/13：本期收录 20 篇，重点看 RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版5/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**20** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 5/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | ConRAG: Consensus-Driven Multi-View Retrieval for Multi-Hop Question Answering | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 2 | A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG | ⭐ 8/10 | RAG |
| RAG与知识检索 | 3 | MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content | ⭐ 8/10 | agent, RAG |
| LLM推理与规划 | 1 | Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning | ⭐ 8/10 | reasoning |
| RAG与知识检索 | 4 | Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation | ⭐ 8/10 | RAG |
| RAG与知识检索 | 5 | Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 2 | Revisiting Anthropomorphic Reflection Markers in Large Language Model Reasoning | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 3 | Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach | ⭐ 8/10 | reasoning, planning |
| RAG与知识检索 | 6 | FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models | ⭐ 8/10 | RAG, retrieval |
| LLM推理与规划 | 4 | Prompt Codebooks: Discrete Compositional Optimization for Language Model Instruction Refinement | ⭐ 8/10 | reasoning, planning |
| LLM推理与规划 | 5 | FABSVer: Faster Training and Better Self-Verification for LLM Mathematical Reasoning | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 6 | VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 7 | SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 8 | The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search | ⭐ 8/10 | agent, search |
| RAG与知识检索 | 7 | Token Optimization Strategies for LLM-Based Oracle-to-PostgreSQL Migration | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 8 | Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution | ⭐ 8/10 | agent |
| RAG与知识检索 | 9 | GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction | ⭐ 8/10 | RAG |
| LLM推理与规划 | 9 | An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning | ⭐ 8/10 | planning |
| RAG与知识检索 | 10 | Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL | ⭐ 8/10 | RAG |
| RAG与知识检索 | 11 | Rethinking Memory as Continuously Evolving Connectivity | ⭐ 8/10 | RAG, retrieval |

</span>

## 🧠 LLM 推理 / 规划 / RAG


### [1] ConRAG: Consensus-Driven Multi-View Retrieval for Multi-Hop Question Answering

- **评分**：8/10
- **作者/机构**：Yikai Zhu, Kunfeng Chen, Qihuang Zhong, Juhua Liu, Bo Du
- **论文链接**：https://arxiv.org/abs/2605.28093
- **PDF**：https://arxiv.org/pdf/2605.28093
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ConRAG: Consensus-Driven Multi-View Retrieval for Multi-Hop Question Answering”展开，属于「RAG与知识检索」方向。作者核心问题是：Decomposition Execution Retrieval Generation arXiv:2605.28093v1 [cs.CL] 27 May 2026 Retrieval-augmented generation (RAG) has Question Dependency-aware Plan Sub Question Passage Answer emerged as a promising paradigm for enhanc- Passage-level Retrieval ing lar…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“ConRAG: Consensus-Driven Multi-View Retrieval for Multi-Hop Question Answering”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG

- **评分**：8/10
- **作者/机构**：Junjie Mu, Qiongxiu Li
- **论文链接**：https://arxiv.org/abs/2605.28112
- **PDF**：https://arxiv.org/pdf/2605.28112
- **代码链接**：https://github.com/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG”展开，属于「RAG与知识检索」方向。作者核心问题是：2020). In privacy-sensitive domains such as health- care (Kim et al., 2025), however, these knowl- arXiv:2605.28112v1 [cs.CR] 27 May 2026 Federated Retrieval-Augmented Generation edge sources are often inherently decentralized (FedRAG) is attractive for priva…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content

- **评分**：8/10
- **作者/机构**：Ruoqi Guo, Yi Liu, Gelei Deng, Yiheng Xiong, Yuekang Li, Ying Zhang, Leo Yu Zhang, Lida Zhao, Ji Jie, Yuxiao Lu
- **论文链接**：https://arxiv.org/abs/2605.28116
- **PDF**：https://arxiv.org/pdf/2605.28116
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content”展开，属于「RAG与知识检索」方向。作者核心问题是：Task Setup: The GUI agent visits a battery product page to check battery-life reviews. arXiv:2605.28116v1 [cs.CR] 27 May 2026 Mobile graphical user interface (GUI) agents Expected action: driven by vision–language models (VLMs) per- Tap the battery-life revie…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning

- **评分**：8/10
- **作者/机构**：Yi Wang, Haojie Lu, Zhaofan Zhang, Li Chen, Sihong Xie
- **论文链接**：https://arxiv.org/abs/2605.28144
- **PDF**：https://arxiv.org/pdf/2605.28144
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning”展开，属于「LLM推理与规划」方向。作者核心问题是：LLMs have shown remarkable proficiency in arXiv:2605.28144v1 [cs.AI] 27 May 2026 general language understanding and reason- ing. However, they consistently underperform in spatial reasoning that severely limits their application, particularly in embodied inte…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation

- **评分**：8/10
- **作者/机构**：Evgenii Palnikov, Elizaveta Gavrilova
- **论文链接**：https://arxiv.org/abs/2605.28222
- **PDF**：https://arxiv.org/pdf/2605.28222
- **代码链接**：https://github.com/EugPal/rag-lora-tradeoffs

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation”展开，属于「RAG与知识检索」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning

- **评分**：8/10
- **作者/机构**：Zhikai Pan, Chih-Ting Liao, Chunrui Liu, Xi Xiao, Yitong Qiao, Chunlei Meng, Zhangquan Chen, Xin Cao
- **论文链接**：https://arxiv.org/abs/2605.28277
- **PDF**：https://arxiv.org/pdf/2605.28277
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning”展开，属于「RAG与知识检索」方向。作者核心问题是：level and disrupting strict JSON output for most open-weight models at L5. (iv) At generative arXiv:2605.28277v1 [cs.AI] 27 May 2026 Whether large language models (LLMs) con- world-graph output, node identification (object struct internal spatial world models…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] Revisiting Anthropomorphic Reflection Markers in Large Language Model Reasoning

- **评分**：8/10
- **作者/机构**：Yahan Yu, Noa Nakanishi, Fei Cheng
- **论文链接**：https://arxiv.org/abs/2605.28305
- **PDF**：https://arxiv.org/pdf/2605.28305
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Revisiting Anthropomorphic Reflection Markers in Large Language Model Reasoning”展开，属于「LLM推理与规划」方向。作者核心问题是：Let A be the set of all ordered pairs of integers (m, n) such that 7m + 12n = 22. What is the greatest Ground Truth: -4 negative number in the set B = {m + n : (m, n) \in A}? Large Language Models (LLMs) often produce arXiv:2605.28305v1 [cs.CL] 27 May 2026 ex…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Revisiting Anthropomorphic Reflection Markers in Large Language Model Reasoning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach

- **评分**：8/10
- **作者/机构**：Nicolás Benjamín Ocampo, Agnes Paullate Nyiranziza, Davide Ceolin
- **论文链接**：https://arxiv.org/abs/2605.28313
- **PDF**：https://arxiv.org/pdf/2605.28313
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach”展开，属于「LLM推理与规划」方向。作者核心问题是：texts such as essays (Wachsmuth et al., 2016) un- til more research shifted toward assessing argu- arXiv:2605.28313v1 [cs.CL] 27 May 2026 Large Language Models (LLMs) have demon- ment quality (Wachsmuth et al., 2017b). A par- strated remarkable capabilities i…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models

- **评分**：8/10
- **作者/机构**：Xucong Wang, Pengkun Wang, Zhe Zhao, Liheng Yu, Shuang Wang, Yang Wang
- **论文链接**：https://arxiv.org/abs/2605.28347
- **PDF**：https://arxiv.org/pdf/2605.28347
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models”展开，属于「RAG与知识检索」方向。作者核心问题是：(a) Fed-DualCoOp Method Pred. 1 Pred. 2 Pred. 3 Ground Truth Cat Chair Dining Table Training Fed- Chair Dining Table Cat Multi-Label Recognition (MLR) based on Vision-Language DualCoOp 0.94 0.79 0.72 FedMVP FedMPT Models (VLMs) aims to leverage their pre-trai…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] Prompt Codebooks: Discrete Compositional Optimization for Language Model Instruction Refinement

- **评分**：8/10
- **作者/机构**：Jyotirmoy Nath, Neeraj Kumar, Brejesh Lall
- **论文链接**：https://arxiv.org/abs/2605.28360
- **PDF**：https://arxiv.org/pdf/2605.28360
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Prompt Codebooks: Discrete Compositional Optimization for Language Model Instruction Refinement”展开，属于「LLM推理与规划」方向。作者核心问题是：and discrete planning steps preclude analytic gra- dients. Within this landscape, automatic prompt Automatic prompt optimization (APO) has arXiv:2605.28360v1 [cs.AI] 27 May 2026 optimization (APO) is a core sub-problem: ev- driven significant gains in LLM-bas…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Prompt Codebooks: Discrete Compositional Optimization for Language Model Instruction Refinement”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] FABSVer: Faster Training and Better Self-Verification for LLM Mathematical Reasoning

- **评分**：8/10
- **作者/机构**：Haihui Pan, Junwei Bao, Hongfei Jiang, Yang Song
- **论文链接**：https://arxiv.org/abs/2605.28389
- **PDF**：https://arxiv.org/pdf/2605.28389
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FABSVer: Faster Training and Better Self-Verification for LLM Mathematical Reasoning”展开，属于「LLM推理与规划」方向。作者核心问题是：While large language models have made significant progress in mathematical reasoning, they remain unreliable at judging the correctness of their own solutions. Existing approaches that equip models with self-verification typically treat solution generation an…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“FABSVer: Faster Training and Better Self-Verification for LLM Mathematical Reasoning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs

- **评分**：8/10
- **作者/机构**：Qiaoru Li, Shaotian Liang, Jintao Chen, Haoran Sun, Yuxiang Cai, Jianwei Yin, Yankai Jiang
- **论文链接**：https://arxiv.org/abs/2605.28422
- **PDF**：https://arxiv.org/pdf/2605.28422
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs”展开，属于「LLM推理与规划」方向。作者核心问题是：2025; Wang et al., 2025b; Fan et al., 2026) with Latent reasoning enables reasoning over con- expert-annotated visual evidence at each step (Le- arXiv:2605.28422v1 [cs.CV] 27 May 2026 tinuous hidden states rather than explicit to- Duc et al., 2025). However…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs

- **评分**：8/10
- **作者/机构**：Jiawei Li, Ziyi Liu, Weijie Shi, Long Chen, Jiajie Xu, Xiaofang Zhou
- **论文链接**：https://arxiv.org/abs/2605.28490
- **PDF**：https://arxiv.org/pdf/2605.28490
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs”展开，属于「LLM推理与规划」方向。作者核心问题是：3D object grounding localizes referred objects in a 3D scene from natural language. Unified instance-centric 3D-LLMs aim to solve grounding together with dialog, QA, and captioning, yet many rely on a single pointer-style grounding decision that compresses a…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search

- **评分**：8/10
- **作者/机构**：Mert Yazan, Frederik Bungaran Ishak Situmeang, Suzan Verberne
- **论文链接**：https://arxiv.org/abs/2605.28498
- **PDF**：https://arxiv.org/pdf/2605.28498
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search”展开，属于「LLM推理与规划」方向。作者核心问题是：The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search Mert Yazan, Frederik Bungaran Ishak Situmeang, Suzan Verberne The Decision to Verify: How Warmth and User Characteristics Shape Reliance…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Token Optimization Strategies for LLM-Based Oracle-to-PostgreSQL Migration

- **评分**：8/10
- **作者/机构**：Oleg Grynets, Dmytro Babarytskyi, Vasyl Lyashkevych
- **论文链接**：https://arxiv.org/abs/2605.28557
- **PDF**：https://arxiv.org/pdf/2605.28557
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Token Optimization Strategies for LLM-Based Oracle-to-PostgreSQL Migration”展开，属于「RAG与知识检索」方向。作者核心问题是：Large Language Models (LLMs) are increasingly dialects but also preservation of procedural logic, schema used for software modernization, code translation, automated constraints, triggers, stored procedures, packages, cursors, refactoring, and database migrat…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Token Optimization Strategies for LLM-Based Oracle-to-PostgreSQL Migration”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution

- **评分**：8/10
- **作者/机构**：Susanna Cifani, Mario Luca Bernardi, Marta Cimitile
- **论文链接**：https://arxiv.org/abs/2605.28607
- **PDF**：https://arxiv.org/pdf/2605.28607
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution”展开，属于「RAG与知识检索」方向。作者核心问题是：Modern information systems require autonomous perception allows it to leverage the underlying transition arXiv:2605.28607v1 [cs.AI] 27 May 2026 agents capable of navigating complex workflows, yet current topology to anticipate the consequences of alternative…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction

- **评分**：8/10
- **作者/机构**：Jinze Gu, Qinghua Mao, Xi Lin, Jun Wu
- **论文链接**：https://arxiv.org/abs/2605.28645
- **PDF**：https://arxiv.org/pdf/2605.28645
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction”展开，属于「RAG与知识检索」方向。作者核心问题是：arXiv:2605.28645v1 [cs.CR] 27 May 2026 Retrieval-Augmented Generation (RAG) en- hances LLMs by grounding generation in query-relevant external evidence. Beyond un- structured text corpora, Graph RAG integrates knowledge graphs into the retrieval pipeline, ena…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning

- **评分**：8/10
- **作者/机构**：Luis Miguel Vieira da Silva, Nicolas König, Felix Gehlhoff
- **论文链接**：https://arxiv.org/abs/2605.28666
- **PDF**：https://arxiv.org/pdf/2605.28666
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning”展开，属于「LLM推理与规划」方向。作者核心问题是：In modern industry, dynamic environments and the into a desired goal state while respecting the functions and complexity of modular and reconfigurable resources require auto- constraints of the available resources [3]. mated planning of process sequences. Cap…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

- **评分**：8/10
- **作者/机构**：Kunhao Zheng, Pierre Chambon, Juliette Decugis, Jonas Gehring, Taco Cohen, Benjamin Negrevergne, Gabriel Synnaeve
- **论文链接**：https://arxiv.org/abs/2605.28751
- **PDF**：https://arxiv.org/pdf/2605.28751
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL”展开，属于「RAG与知识检索」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] Rethinking Memory as Continuously Evolving Connectivity

- **评分**：8/10
- **作者/机构**：Jizhan Fang, Buqiang Xu, Zhixian Wang, Haoliang Cao, Xinle Deng, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu, Ying Wei, Guozhou Zheng, Feiyu Xiong 等
- **论文链接**：https://arxiv.org/abs/2605.28773
- **PDF**：https://arxiv.org/pdf/2605.28773
- **代码链接**：https://github.com/zjunlp/LightMem

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Rethinking Memory as Continuously Evolving Connectivity”展开，属于「RAG与知识检索」方向。作者核心问题是：Existing memory-augmented LLM agents of- arXiv:2605.28773v1 [cs.CL] 27 May 2026 ten treat memory as a static repository with pre-defined representations and fixed retrieval pipelines, which is brittle in dynamic agen- tic environments where feedback, task var…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Rethinking Memory as Continuously Evolving Connectivity”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
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
