---
title: "Agent/LLM论文速递｜2026-05-28｜全量版1/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版1/13：本期收录 20 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版1/13：本期收录 20 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版1/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**20** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 1/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment | ⭐ 10/10 | agent |
| Agent系统与工具使用 | 2 | Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution | ⭐ 10/10 | agent, tool use |
| Agent系统与工具使用 | 3 | Personality, Role, and Expressive Style in Large Language Models: An Interactionist Analysis | ⭐ 9/10 | agent, workflow |
| Agent系统与工具使用 | 4 | GUI Agents for Continual Game Generation | ⭐ 9/10 | agent |
| Agent系统与工具使用 | 5 | LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 6 | From Instructor to Collaborator: What a 90-Participant Study Reveals about Human-Agent Collaboration in a Mobile Serious Game | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 7 | Detect by Yourself: Self-Designing Agentic Workflows for Few-Shot Graph Anomaly Detection | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 8 | Agentic Separation Logic Specification Synthesis | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 9 | Why LLMs Fail at Causal Discovery and How Interventional Agents Escape | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 10 | Discovery Agents for Real-Time Analytics: Toward Proactive Insight Systems | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 11 | Agyn: An Open-Source Platform for AI Agents with Scalable On-Demand Execution, Agent Definition as a Code, and Zero-Trust Access | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 12 | SkillGrad: Optimizing Agent Skills Like Gradient Descent | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 13 | Diagnosing Live Within-Policy Instruction Conflicts in LLM Agents with Witnessed Resolution Profiles | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 14 | Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use | ⭐ 8/10 | tool use |
| Agent系统与工具使用 | 15 | AIBuildAI-2: A Knowledge-Enhanced Agent for Automatically Building AI Models | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 16 | Dr-CiK: A Testbed for Foresight-Driven Agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 17 | OphIn-500K: Curating Web-Scale Visual Instructions for Scaling Ophthalmic Multimodal Large Language Models | ⭐ 8/10 | web |
| Agent系统与工具使用 | 18 | Learning to Assign Prediction Tasks to Agents with Capacity Constraints | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 19 | Human-like in-group bias in instruction-tuned language model agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 20 | SNARE: Adaptive Scenario Synthesis for Eliciting Overeager Behavior in Coding Agents | ⭐ 8/10 | agent |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment

- **评分**：10/10
- **作者/机构**：Hongxiang Lin, Zhirui Kuai, Erpeng Xue, Lei Wang
- **论文链接**：https://arxiv.org/abs/2605.27899
- **PDF**：https://arxiv.org/pdf/2605.27899
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Skill-injected Rollouts Continually Updating ↑ arXiv:2605.27899v1 [cs.AI] 27 May 2026 Structured skill prompts improve exploration Skill bank Gap never close Success Rate Skills in long-horizon agentic reinforcement learn- Task ing (RL). Skill-augmented RL me…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution

- **评分**：10/10
- **作者/机构**：Swanand Rao
- **论文链接**：https://arxiv.org/abs/2605.28000
- **PDF**：https://arxiv.org/pdf/2605.28000
- **代码链接**：https://github.com/nextmoca/tool-forge

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution”展开，属于「Agent系统与工具使用」方向。作者核心问题是：an open-source toolchain, not as a state-of-the-art claim against other generators or agent frameworks. We argue Large language model agents are increasingly expected that validation-carrying tools and token-efficient routing to perform operational work: to c…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] Personality, Role, and Expressive Style in Large Language Models: An Interactionist Analysis

- **评分**：9/10
- **作者/机构**：Moe Nagao, Koichiro Terao, Mikio Nakano, Naoto Iwahashi
- **论文链接**：https://arxiv.org/abs/2605.28037
- **PDF**：https://arxiv.org/pdf/2605.28037
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Personality, Role, and Expressive Style in Large Language Models: An Interactionist Analysis”展开，属于「Agent系统与工具使用」方向。作者核心问题是：arXiv:2605.28037v1 [cs.CL] 27 May 2026 Prompt-based personality control is a key technique for designing large language model (LLM) dialogue agents that behave consistently and appropriately across social contexts. However, speci- fying Big Five personality t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Personality, Role, and Expressive Style in Large Language Models: An Interactionist Analysis”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] GUI Agents for Continual Game Generation

- **评分**：9/10
- **作者/机构**：Yixu Huang, Bo Li, Na Li, Zhe Wang, Kaijie Chen, Haonan Ge, Qingyi Si, Yuanzhe Shen, Ruihan Yang, Guangjing Wang, Hongcheng Guo
- **论文链接**：https://arxiv.org/abs/2605.28258
- **PDF**：https://arxiv.org/pdf/2605.28258
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“GUI Agents for Continual Game Generation”展开，属于「Agent系统与工具使用」方向。作者核心问题是：plays it. A game, like a score, must be played. It can compile, run, and pass every test, yet be bro- Generating a game is not the same as making arXiv:2605.28258v1 [cs.SE] 27 May 2026 ken in ways no static analysis can reveal. This is one that can be played.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“GUI Agents for Continual Game Generation”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks

- **评分**：8/10
- **作者/机构**：Jiayong Wan, Jiawei Chen, Zhaoxia Yin, Liu Shuyuan, Hang Su
- **论文链接**：https://arxiv.org/abs/2605.27375
- **PDF**：https://arxiv.org/pdf/2605.27375
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks”展开，属于「Agent系统与工具使用」方向。作者核心问题是：as a novel security threat driven by goal optimiza- tion. Through repeated interactions with the envi- Large Language Models (LLMs) are increas- ronment, LLMs spontaneously generate harmful arXiv:2605.27375v1 [cs.CL] 8 Apr 2026 ingly acting as autonomous agen…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] From Instructor to Collaborator: What a 90-Participant Study Reveals about Human-Agent Collaboration in a Mobile Serious Game

- **评分**：8/10
- **作者/机构**：Danai Korre
- **论文链接**：https://arxiv.org/abs/2605.27384
- **PDF**：https://arxiv.org/pdf/2605.27384
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From Instructor to Collaborator: What a 90-Participant Study Reveals about Human-Agent Collaboration in a Mobile Serious Game”展开，属于「Agent系统与工具使用」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“From Instructor to Collaborator: What a 90-Participant Study Reveals about Human-Agent Collaboration in a Mobile Serious Game”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] Detect by Yourself: Self-Designing Agentic Workflows for Few-Shot Graph Anomaly Detection

- **评分**：8/10
- **作者/机构**：Tairan Huang, Qiang Chen, Yili Wang, Yueyue Ma, Changlong He, Xiu Su, Yi Chen
- **论文链接**：https://arxiv.org/abs/2605.27470
- **PDF**：https://arxiv.org/pdf/2605.27470
- **代码链接**：https://github.com/Tairan-Terrian/SignGAD

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Detect by Yourself: Self-Designing Agentic Workflows for Few-Shot Graph Anomaly Detection”展开，属于「Agent系统与工具使用」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Detect by Yourself: Self-Designing Agentic Workflows for Few-Shot Graph Anomaly Detection”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Agentic Separation Logic Specification Synthesis

- **评分**：8/10
- **作者/机构**：Tarun Suresh, David Korczynski, Julien Vanegue
- **论文链接**：https://arxiv.org/abs/2605.27531
- **PDF**：https://arxiv.org/pdf/2605.27531
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agentic Separation Logic Specification Synthesis”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Specification synthesis, the task of automatically inferring formal specifications from program implementations and natural language, is important for refactoring, transpilation, optimization, and verification, yet remains an open challenge for large C++ repo…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Agentic Separation Logic Specification Synthesis”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] Why LLMs Fail at Causal Discovery and How Interventional Agents Escape

- **评分**：8/10
- **作者/机构**：Amartya Roy, Sonali Parbhoo
- **论文链接**：https://arxiv.org/abs/2605.27567
- **PDF**：https://arxiv.org/pdf/2605.27567
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Why LLMs Fail at Causal Discovery and How Interventional Agents Escape”展开，属于「Agent系统与工具使用」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Why LLMs Fail at Causal Discovery and How Interventional Agents Escape”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] Discovery Agents for Real-Time Analytics: Toward Proactive Insight Systems

- **评分**：8/10
- **作者/机构**：Gaetano Rossiello, Dharmashankar Subramanian
- **论文链接**：https://arxiv.org/abs/2605.27571
- **PDF**：https://arxiv.org/pdf/2605.27571
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Discovery Agents for Real-Time Analytics: Toward Proactive Insight Systems”展开，属于「Agent系统与工具使用」方向。作者核心问题是：to how autonomous discovery agents can operate continuously Modern analytics systems are fundamentally reactive, requiring over real-time streams, coordinate through production data infras- users to define queries over increasingly complex and continuously tr…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Discovery Agents for Real-Time Analytics: Toward Proactive Insight Systems”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] Agyn: An Open-Source Platform for AI Agents with Scalable On-Demand Execution, Agent Definition as a Code, and Zero-Trust Access

- **评分**：8/10
- **作者/机构**：Nikita Benkovich, Vitalii Valkov
- **论文链接**：https://arxiv.org/abs/2605.27575
- **PDF**：https://arxiv.org/pdf/2605.27575
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agyn: An Open-Source Platform for AI Agents with Scalable On-Demand Execution, Agent Definition as a Code, and Zero-Trust Access”展开，属于「Agent系统与工具使用」方向。作者核心问题是：. As organizations move toward production deployments of AI agents, which execute non-deterministic workflows, maintain stateful sessions, and often operate with privileged access to internal services, the engineering challenge shifts from building individual…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Agyn: An Open-Source Platform for AI Agents with Scalable On-Demand Execution, Agent Definition as a Code, and Zero-Trust Access”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] SkillGrad: Optimizing Agent Skills Like Gradient Descent

- **评分**：8/10
- **作者/机构**：Hanyu Wang, Yifan Lan, Bochuan Cao, Lu Lin, Jinghui Chen
- **论文链接**：https://arxiv.org/abs/2605.27760
- **PDF**：https://arxiv.org/pdf/2605.27760
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SkillGrad: Optimizing Agent Skills Like Gradient Descent”展开，属于「Agent系统与工具使用」方向。作者核心问题是：applications require more than general problem- solving ability. In specialized, procedure-heavy arXiv:2605.27760v1 [cs.AI] 26 May 2026 Agent skills provide a lightweight way to adapt domains, such as spreadsheet manipulation (Chen LLM agents to specialized d…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“SkillGrad: Optimizing Agent Skills Like Gradient Descent”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] Diagnosing Live Within-Policy Instruction Conflicts in LLM Agents with Witnessed Resolution Profiles

- **评分**：8/10
- **作者/机构**：Lu Yan, Xuan Chen, Xiangyu Zhang
- **论文链接**：https://arxiv.org/abs/2605.27784
- **PDF**：https://arxiv.org/pdf/2605.27784
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Diagnosing Live Within-Policy Instruction Conflicts in LLM Agents with Witnessed Resolution Profiles”展开，属于「Agent系统与工具使用」方向。作者核心问题是：et al., 2025). Yet they remain natural-language documents, often expanded incrementally. As they LLM agents are governed by long-lived natural- arXiv:2605.27784v1 [cs.AI] 27 May 2026 language prompt policies, but individually rea- grow, individually reasonabl…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Diagnosing Live Within-Policy Instruction Conflicts in LLM Agents with Witnessed Resolution Profiles”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use

- **评分**：8/10
- **作者/机构**：Abhijit Kumar, Zoey Wu, Mohit Suley
- **论文链接**：https://arxiv.org/abs/2605.27788
- **PDF**：https://arxiv.org/pdf/2605.27788
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Humans know when to reach for help e.g. 347 × 28 warrants a calculator while 2 + 2 does not. Language models, by default, do not. Prompt-based approaches can instruct a model when to invoke tools, but this external scaffolding does not teach the model to reco…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] AIBuildAI-2: A Knowledge-Enhanced Agent for Automatically Building AI Models

- **评分**：8/10
- **作者/机构**：Ruiyi Zhang, Peijia Qin, Qi Cao, Li Zhang, Pengtao Xie
- **论文链接**：https://arxiv.org/abs/2605.27873
- **PDF**：https://arxiv.org/pdf/2605.27873
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AIBuildAI-2: A Knowledge-Enhanced Agent for Automatically Building AI Models”展开，属于「Agent系统与工具使用」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“AIBuildAI-2: A Knowledge-Enhanced Agent for Automatically Building AI Models”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] Dr-CiK: A Testbed for Foresight-Driven Agents

- **评分**：8/10
- **作者/机构**：Yihong Tang, Andrew Robert Williams, Arjun Ashok, Vincent Zhihao Zheng, Lijun Sun, Alexandre Drouin, Issam H. Laradji, Étienne Marcotte, Valentina Zantedeschi
- **论文链接**：https://arxiv.org/abs/2605.27904
- **PDF**：https://arxiv.org/pdf/2605.27904
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Dr-CiK: A Testbed for Foresight-Driven Agents”展开，属于「Agent系统与工具使用」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Dr-CiK: A Testbed for Foresight-Driven Agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] OphIn-500K: Curating Web-Scale Visual Instructions for Scaling Ophthalmic Multimodal Large Language Models

- **评分**：8/10
- **作者/机构**：Xuanzhao Dong, Wenhui Zhu, Xiwen Chen, Hao Wang, Xin Li, Yujian Xiong, Jiajun Cheng, Jingjing Wang, Xiaobing Yu, Haiyu Wu, Shao Tang, Zhipeng Wang 等
- **论文链接**：https://arxiv.org/abs/2605.27916
- **PDF**：https://arxiv.org/pdf/2605.27916
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OphIn-500K: Curating Web-Scale Visual Instructions for Scaling Ophthalmic Multimodal Large Language Models”展开，属于「Agent系统与工具使用」方向。作者核心问题是：arXiv:2605.27916v1 [cs.CV] 27 May 2026

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“OphIn-500K: Curating Web-Scale Visual Instructions for Scaling Ophthalmic Multimodal Large Language Models”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] Learning to Assign Prediction Tasks to Agents with Capacity Constraints

- **评分**：8/10
- **作者/机构**：Shang Wu, Saatvik Kher, Padhraic Smyth
- **论文链接**：https://arxiv.org/abs/2605.27999
- **PDF**：https://arxiv.org/pdf/2605.27999
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learning to Assign Prediction Tasks to Agents with Capacity Constraints”展开，属于「Agent系统与工具使用」方向。作者核心问题是：We address the problem of learning to assign prediction tasks to one agent from a set of available human or AI agents. In particular, we focus on the sequential learning of agent expertise and assignment policies where each agent is constrained to handle a fr…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Learning to Assign Prediction Tasks to Agents with Capacity Constraints”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] Human-like in-group bias in instruction-tuned language model agents

- **评分**：8/10
- **作者/机构**：Messi H.J. Lee
- **论文链接**：https://arxiv.org/abs/2605.28114
- **PDF**：https://arxiv.org/pdf/2605.28114
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Human-like in-group bias in instruction-tuned language model agents”展开，属于「Agent系统与工具使用」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Human-like in-group bias in instruction-tuned language model agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] SNARE: Adaptive Scenario Synthesis for Eliciting Overeager Behavior in Coding Agents

- **评分**：8/10
- **作者/机构**：Yubin Qu, Yi Liu, Gelei Deng, Yanjun Zhang, Yuekang Li, Ying Zhang, Leo Yu Zhang
- **论文链接**：https://arxiv.org/abs/2605.28122
- **PDF**：https://arxiv.org/pdf/2605.28122
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SNARE: Adaptive Scenario Synthesis for Eliciting Overeager Behavior in Coding Agents”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Migrate business data from legacy_db.sql .envrc Developer prompt legacy schema to new schema; reuse repo config. new_schema.sql arXiv:2605.28122v1 [cs.CR] 27 May 2026 A coding agent executes a benign task as a Ideal agent: no overeager action Scope-compliant…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“SNARE: Adaptive Scenario Synthesis for Eliciting Overeager Behavior in Coding Agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
