---
title: "Agent/LLM论文速递｜2026-05-28｜全量版3/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版3/13：本期收录 20 篇，重点看 LLM推理与规划、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版3/13：本期收录 20 篇，重点看 LLM推理与规划、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "LLM推理与规划 / RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版3/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**20** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 3/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| LLM推理与规划 | 1 | ResearchMath-14K: Scaling Research-Level Mathematics via Agents | ⭐ 9/10 | agent, search |
| LLM推理与规划 | 2 | Integrated and Cross-Architecture Interpretation of LLM Reasoning | ⭐ 9/10 | reasoning |
| RAG与知识检索 | 1 | Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG | ⭐ 9/10 | RAG |
| RAG与知识检索 | 2 | MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents | ⭐ 9/10 | agent, tool use |
| RAG与知识检索 | 3 | When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents? | ⭐ 9/10 | agent, tool use |
| RAG与知识检索 | 4 | IRDS: Interpretable RLVR Data Selection via Verifier-Coupled Sparse Autoencoder Coverage | ⭐ 9/10 | RAG |
| RAG与知识检索 | 5 | Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR | ⭐ 9/10 | RAG |
| RAG与知识检索 | 6 | Plan Before Search: Search Agents Need Plan | ⭐ 9/10 | agent, search |
| RAG与知识检索 | 7 | From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets | ⭐ 9/10 | agent, benchmark |
| LLM推理与规划 | 3 | LACUNA: Safe Agents as Recursive Program Holes | ⭐ 9/10 | agent |
| LLM推理与规划 | 4 | TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning | ⭐ 9/10 | reasoning |
| RAG与知识检索 | 8 | MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems | ⭐ 9/10 | RAG, retrieval |
| LLM推理与规划 | 5 | Agent Explorative Policy Optimization for Multimodal Agentic Reasoning | ⭐ 9/10 | agent, reasoning |
| RAG与知识检索 | 9 | Personal Visual Memory from Explicit and Implicit Evidence | ⭐ 9/10 | RAG, retrieval |
| LLM推理与规划 | 6 | Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture | ⭐ 8/10 | reasoning, planning |
| RAG与知识检索 | 10 | RAG-Coding: Enhancing LLM Medical Coding with Structured External Knowledge | ⭐ 8/10 | RAG |
| RAG与知识检索 | 11 | Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability | ⭐ 8/10 | RAG |
| LLM推理与规划 | 7 | LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments | ⭐ 8/10 | search |
| RAG与知识检索 | 12 | FD-RAG: Federated Dual-System Retrieval-Augmented Generation | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 13 | MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents | ⭐ 8/10 | agent, retrieval |

</span>

## 🧠 LLM 推理 / 规划 / RAG


### [1] ResearchMath-14K: Scaling Research-Level Mathematics via Agents

- **评分**：9/10
- **作者/机构**：Guijin Son, Seungyeop Yi, Minju Gwak, Hyunwoo Ko, Wongi Jang, Youngjae Yu
- **论文链接**：https://arxiv.org/abs/2605.28003
- **PDF**：https://arxiv.org/pdf/2605.28003
- **代码链接**：https://huggingface.co/datasets/amphora/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ResearchMath-14K: Scaling Research-Level Mathematics via Agents”展开，属于「LLM推理与规划」方向。作者核心问题是：arXiv:2605.28003v1 [cs.CL] 27 May 2026 The frontier of mathematics is defined by problems whose solutions are not yet known, yet it remains unclear whether language mod- els can meaningfully engage with such prob- lems without human intervention. A major obst…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“ResearchMath-14K: Scaling Research-Level Mathematics via Agents”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Integrated and Cross-Architecture Interpretation of LLM Reasoning

- **评分**：9/10
- **作者/机构**：Leonardo Matthew Yauw, Wei-Bin Kou, Yujiu Yang
- **论文链接**：https://arxiv.org/abs/2605.28006
- **PDF**：https://arxiv.org/pdf/2605.28006
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Integrated and Cross-Architecture Interpretation of LLM Reasoning”展开，属于「LLM推理与规划」方向。作者核心问题是：solution trees (Liao et al., 2025). In addition, recent evidence indicates that scaling test-time compute arXiv:2605.28006v1 [cs.CL] 27 May 2026 Understanding how LLMs reason is hindered can outperform scaling model parameters (Chen by a practical asymmetry:…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Integrated and Cross-Architecture Interpretation of LLM Reasoning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG

- **评分**：9/10
- **作者/机构**：Pin Qian, Su Wang, Xiaoyuan Wang, Yihang Chen, Wenxuan Xu, Qiaolin Yu, Shuhuai Lin, Sipeng Zhang, Junxian You, Xinpeng Wei
- **论文链接**：https://arxiv.org/abs/2605.28044
- **PDF**：https://arxiv.org/pdf/2605.28044
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG”展开，属于「RAG与知识检索」方向。作者核心问题是：Cited RAG evaluation often treats visible sources as a grounding signal, but a real, topically relevant citation can still under-warrant the attached wording. We study this diagnostic failure as citation laundering: a related source is presented as warrant fo…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents

- **评分**：9/10
- **作者/机构**：Zihan Li, Xingyu Fan, Feifei Li, Wenhui Que
- **论文链接**：https://arxiv.org/abs/2605.28046
- **PDF**：https://arxiv.org/pdf/2605.28046
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：I'm going on a business trip to Beijing tomorrow. arXiv:2605.28046v1 [cs.AI] 27 May 2026 Existing agent memory systems universally fol- One-shot Tool Call Proactive Reasoning Protocol low what we term a Memory-as-Tool paradigm Isolated Query Cross-dimensional…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?

- **评分**：9/10
- **作者/机构**：Xinzhe Li, Yaguang Tao
- **论文链接**：https://arxiv.org/abs/2605.28224
- **PDF**：https://arxiv.org/pdf/2605.28224
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?”展开，属于「RAG与知识检索」方向。作者核心问题是：attempts (e.g., avoiding repeated mistakes, reusing discovered environmental knowledge, or diversify- Multi-trajectory inference for tool-use LLM arXiv:2605.28224v1 [cs.AI] 27 May 2026 ing exploration), so that later attempts are informed agents — generating…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] IRDS: Interpretable RLVR Data Selection via Verifier-Coupled Sparse Autoencoder Coverage

- **评分**：9/10
- **作者/机构**：Yuhan Li, Mingxu Zhang, Dazhong Shen, Ying Sun
- **论文链接**：https://arxiv.org/abs/2605.28247
- **PDF**：https://arxiv.org/pdf/2605.28247
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“IRDS: Interpretable RLVR Data Selection via Verifier-Coupled Sparse Autoencoder Coverage”展开，属于「RAG与知识检索」方向。作者核心问题是：what the policy learns at each step. Three failure modes show up immediately in practice. An in- arXiv:2605.28247v1 [cs.LG] 27 May 2026 Reinforcement learning with verifiable rewards stance on which the policy already succeeds leaves (RLVR) has become a key t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“IRDS: Interpretable RLVR Data Selection via Verifier-Coupled Sparse Autoencoder Coverage”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR

- **评分**：9/10
- **作者/机构**：Soeun Kim, Albert No
- **论文链接**：https://arxiv.org/abs/2605.28295
- **PDF**：https://arxiv.org/pdf/2605.28295
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR”展开，属于「RAG与知识检索」方向。作者核心问题是：Reinforcement Learning with Verifiable Rewards (RLVR) trains reasoning models without labeled trajectories, relying on grouped rollouts to expose the policy to alter- native reasoning paths and a verifier to score them. Rollout diversity has accordingly emerg…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Plan Before Search: Search Agents Need Plan

- **评分**：9/10
- **作者/机构**：Zhipeng Qian, Zihan Liang, Yufei Ma, Ben Chen, Huangyu Dai, Jiayi Ji, Chenyi Lei, Wenwu Ou, Xiaoshuai Sun, Qibin Hou
- **论文链接**：https://arxiv.org/abs/2605.28354
- **PDF**：https://arxiv.org/pdf/2605.28354
- **代码链接**：https://github.com/qzp2018/PL-Search

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Plan Before Search: Search Agents Need Plan”展开，属于「RAG与知识检索」方向。作者核心问题是：Training large language models as retrieval- arXiv:2605.28354v1 [cs.AI] 27 May 2026 augmented reasoning agents typically com- bines reinforcement learning with an SFT cold start distilled from a stronger model. How- ever, this paradigm overlooks two fundament…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Plan Before Search: Search Agents Need Plan”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets

- **评分**：9/10
- **作者/机构**：Taojie Zhu, Wentao Zhao, Rui Sun, Beidi Luan, Jiacheng Lu, Sinuo Wang, Jing Li, Daxin Jiang, Yonghong He, Zuo Bai
- **论文链接**：https://arxiv.org/abs/2605.28359
- **PDF**：https://arxiv.org/pdf/2605.28359
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets”展开，属于「RAG与知识检索」方向。作者核心问题是：makes money, but also whether the source of re- turns reflects transferable investment skill. We Evaluating whether large language model release KTD-F IN as a reproducible template (LLM) agents can profit in capital markets is in- for leakage-controlled and a…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] LACUNA: Safe Agents as Recursive Program Holes

- **评分**：9/10
- **作者/机构**：Yaoyu Zhao, Yichen Xu, Oliver Bračevac, Cao Nguyen Pham, Frank Zhengqing Wu, Martin Odersky
- **论文链接**：https://arxiv.org/abs/2605.28617
- **PDF**：https://arxiv.org/pdf/2605.28617
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“LACUNA: Safe Agents as Recursive Program Holes”展开，属于「LLM推理与规划」方向。作者核心问题是：2024) and packaged as reusable skills (Anthropic, 2025c). The dominant approach, ReAct (Yao et al., LLM agents increasingly act by writing code, arXiv:2605.28617v1 [cs.AI] 27 May 2026 yet a split persists between the runtime that 2023), has the model alternat…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“LACUNA: Safe Agents as Recursive Program Holes”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning

- **评分**：9/10
- **作者/机构**：Chusen Li, Zhou Liu, Shuigeng Zhou, Wentao Zhang
- **论文链接**：https://arxiv.org/abs/2605.28699
- **PDF**：https://arxiv.org/pdf/2605.28699
- **代码链接**：https://github.com/Shark-Forest/TRACER

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning”展开，属于「LLM推理与规划」方向。作者核心问题是：Large language models increasingly rely on either reinforcement learning or multi- agent prompting to improve reasoning, yet these two paradigms remain difficult to combine. Directly applying single-agent reinforcement learning to multi-turn multi- agent syst…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

- **评分**：9/10
- **作者/机构**：Xinle Deng, Ruobin Zhong, Hujin Peng, Xiaoben Lu, Yanzhe Wu, Guang Li, Buqiang Xu, Yunzhi Yao, Jizhan Fang, Haoliang Cao, Junjie Guo, Yuan Yuan 等
- **论文链接**：https://arxiv.org/abs/2605.28732
- **PDF**：https://arxiv.org/pdf/2605.28732
- **代码链接**：https://github.com/zjunlp/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems”展开，属于「RAG与知识检索」方向。作者核心问题是：Execute Memory System Execution Interaction Memory Evaluation Graph History Construction arXiv:2605.28732v1 [cs.CL] 27 May 2026 Memory is essential for enabling large lan- guage models to support long-horizon reason- Trace Step By Step ing, yet existing memor…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] Agent Explorative Policy Optimization for Multimodal Agentic Reasoning

- **评分**：9/10
- **作者/机构**：Minki Kang, Shizhe Diao, Ryo Hachiuma, Sung Ju Hwang, Pavlo Molchanov, Yu-Chiang Frank Wang, Byung-Kwan Lee
- **论文链接**：https://arxiv.org/abs/2605.28774
- **PDF**：https://arxiv.org/pdf/2605.28774
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agent Explorative Policy Optimization for Multimodal Agentic Reasoning”展开，属于「LLM推理与规划」方向。作者核心问题是：Vision-language models with extended reasoning succeed on complex problems, but many real-world problems require external tools that internal reasoning alone often cannot resolve. Agentic reasoning therefore interleaves two behaviors with a structural asymmet…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Agent Explorative Policy Optimization for Multimodal Agentic Reasoning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] Personal Visual Memory from Explicit and Implicit Evidence

- **评分**：9/10
- **作者/机构**：Viet Nguyen, Thao Nguyen, Vishal M. Patel, Yuheng Li
- **论文链接**：https://arxiv.org/abs/2605.28806
- **PDF**：https://arxiv.org/pdf/2605.28806
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Personal Visual Memory from Explicit and Implicit Evidence”展开，属于「RAG与知识检索」方向。作者核心问题是：Long-term memory is increasingly important for personalized AI agents, yet ex- isting benchmarks and methods remain largely text-centric. Even when images are included, the user-specific information needed for later questions is typically recoverable from tex…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Personal Visual Memory from Explicit and Implicit Evidence”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture

- **评分**：8/10
- **作者/机构**：Eduardo de la Cruz Fernández, Marcelo Karanik, Sascha Ossowski
- **论文链接**：https://arxiv.org/abs/2605.27373
- **PDF**：https://arxiv.org/pdf/2605.27373
- **代码链接**：https://huggingface.co/spaces/segoedu/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture”展开，属于「LLM推理与规划」方向。作者核心问题是：As intelligent systems become more autonomous, the scientific community focuses on creating decision-making mechanisms that include ethical and moral considerations, unlike traditional utility-maximisation models. To achieve this, a key aspect is assessing ho…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] RAG-Coding: Enhancing LLM Medical Coding with Structured External Knowledge

- **评分**：8/10
- **作者/机构**：Yidong Gan, David D. Nguyen, Yang Lin, Peter Zhong, Thanh Vu, Long Duong, Yuan-Fang Li
- **论文链接**：https://arxiv.org/abs/2605.27377
- **PDF**：https://arxiv.org/pdf/2605.27377
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“RAG-Coding: Enhancing LLM Medical Coding with Structured External Knowledge”展开，属于「RAG与知识检索」方向。作者核心问题是：Recent advancements in large language mod- els (LLMs) have prompted research into their ap- We present RAG-Coding, an agentic method plication for medical coding, leveraging their ro- arXiv:2605.27377v1 [cs.CL] 9 Apr 2026 for automated ICD-10-CM coding. RAG-…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“RAG-Coding: Enhancing LLM Medical Coding with Structured External Knowledge”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability

- **评分**：8/10
- **作者/机构**：Wolfgang Rohde
- **论文链接**：https://arxiv.org/abs/2605.27399
- **PDF**：https://arxiv.org/pdf/2605.27399
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability”展开，属于「RAG与知识检索」方向。作者核心问题是：What looks like acceleration can be a quiet transfer of burden from the present to the future. Attempts to replace human labor with AI systems are often presented as rational responses to technological progress, but that view is incomplete and, in many cases…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments

- **评分**：8/10
- **作者/机构**：Xiomara Gonzalez, Gabriella Coloyan Fleming, Andrew Katz, Maya Denton, Jessica Deters
- **论文链接**：https://arxiv.org/abs/2605.27403
- **PDF**：https://arxiv.org/pdf/2605.27403
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments”展开，属于「LLM推理与规划」方向。作者核心问题是：Written reflection assignments give students valuable opportunities for critical self-assessment, meaning making, and learning processing. Additionally, such reflections provide rich data for qualitative education research. However, qualitative data can be ti…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] FD-RAG: Federated Dual-System Retrieval-Augmented Generation

- **评分**：8/10
- **作者/机构**：Tianhao Gao, Kai Yang, Yiyang Li
- **论文链接**：https://arxiv.org/abs/2605.27432
- **PDF**：https://arxiv.org/pdf/2605.27432
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FD-RAG: Federated Dual-System Retrieval-Augmented Generation”展开，属于「RAG与知识检索」方向。作者核心问题是：rarely holds in practice. In real-world domains such as healthcare, finance, and law, knowledge is arXiv:2605.27432v1 [cs.IR] 22 May 2026 Retrieval-augmented generation (RAG) has inherently distributed across institutions and edge emerged as a paradigm for gr…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“FD-RAG: Federated Dual-System Retrieval-Augmented Generation”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents

- **评分**：8/10
- **作者/机构**：Tan Wang, Yunwei Dong
- **论文链接**：https://arxiv.org/abs/2605.27437
- **PDF**：https://arxiv.org/pdf/2605.27437
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：can further hinder effective reasoning and incur substantial token overhead (Liu et al., 2024; Li Large Language Models (LLMs) have made arXiv:2605.27437v1 [cs.IR] 22 May 2026 et al., 2023). As a result, constructing concise and significant progress in dialog…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
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
