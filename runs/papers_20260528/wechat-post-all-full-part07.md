---
title: "Agent/LLM论文速递｜2026-05-28｜全量版7/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版7/13：本期收录 20 篇，重点看 RAG与知识检索、多智能体与协作；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版7/13：本期收录 20 篇，重点看 RAG与知识检索、多智能体与协作；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "RAG与知识检索 / 多智能体与协作"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版7/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**2** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 7/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | GONDOR to the Rescue: Satisficing Planning with Low Memory | ⭐ 5/10 | planning |
| RAG与知识检索 | 2 | The Attentional White Bear Effect in Transformer Language Models | ⭐ 5/10 | RAG, retrieval |
| 多智能体与协作 | 1 | Voluntary Collusion with Secret Tools in Competing LLM Agents | ⭐ 10/10 | agent, tool use |
| 多智能体与协作 | 2 | StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 3 | Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 4 | HARP: Measuring Harm Amplification in Multi-Agent LLM Systems | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 5 | Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 6 | Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 7 | Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 8 | MolLingo: Molecule-Native Representations for LLM-Powered Scientific Agents | ⭐ 9/10 | agent |
| 多智能体与协作 | 9 | Multi-Agent LLM-based Metamorphic Testing for REST APIs | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 10 | Beyond One Path: Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents | ⭐ 9/10 | agent |
| 多智能体与协作 | 11 | AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation | ⭐ 9/10 | agent |
| 多智能体与协作 | 12 | AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 13 | Detection Without Correction: A Two-Parameter Decomposition of Multi-Stage LLM Pipelines | ⭐ 8/10 | multi-agent, collaboration |
| 多智能体与协作 | 14 | You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 15 | A Policy-Driven Runtime Layer for Agentic LLM Serving | ⭐ 8/10 | agent |
| 多智能体与协作 | 16 | Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems | ⭐ 8/10 | agent, multi-agent, search |
| 多智能体与协作 | 17 | TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 18 | MACReD: A Multi-Agent Collaborative Reasoning Framework for Reaction Diagram Parsing | ⭐ 8/10 | agent, multi-agent, reasoning |

</span>

## 🧠 LLM 推理 / 规划 / RAG


### [1] GONDOR to the Rescue: Satisficing Planning with Low Memory

- **评分**：5/10
- **作者/机构**：Yonatan Vernik, Alexander Tuisov, Alexander Shleyfman
- **论文链接**：https://arxiv.org/abs/2605.28454
- **PDF**：https://arxiv.org/pdf/2605.28454
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“GONDOR to the Rescue: Satisficing Planning with Low Memory”展开，属于「RAG与知识检索」方向。作者核心问题是：the algorithm may devote extensive effort to regions of the arXiv:2605.28454v1 [cs.AI] 27 May 2026 state space that do not contribute to a solution, expanding Greedy Best-First Search (GBFS) is the dominant approach many nodes that are ultimately irrelevant.…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“GONDOR to the Rescue: Satisficing Planning with Low Memory”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [2] The Attentional White Bear Effect in Transformer Language Models

- **评分**：5/10
- **作者/机构**：Rebecca Ramnauth, Brian Scassellati
- **论文链接**：https://arxiv.org/abs/2605.28639
- **PDF**：https://arxiv.org/pdf/2605.28639
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“The Attentional White Bear Effect in Transformer Language Models”展开，属于「RAG与知识检索」方向。作者核心问题是：tion,” explicitly introduce the forbidden concept into the model’s context window. Because trans- arXiv:2605.28639v1 [cs.CL] 27 May 2026 Instruction-based suppression is widely used to formers rely on distributed associative representa- prevent language model…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“The Attentional White Bear Effect in Transformer Language Models”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「RAG与知识检索」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 🤝 多智能体 / 协作


### [3] Voluntary Collusion with Secret Tools in Competing LLM Agents

- **评分**：10/10
- **作者/机构**：Xijie Zeng, Frank Rudzicz
- **论文链接**：https://arxiv.org/abs/2605.27593
- **PDF**：https://arxiv.org/pdf/2605.27593
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Voluntary Collusion with Secret Tools in Competing LLM Agents”展开，属于「多智能体与协作」方向。作者核心问题是：Even when a tool is explicitly described as unfair and harmful to others, os- tensibly safety-aligned LLM agents still voluntarily engage in secret collusion whenever doing so confers a strategic advantage. To investigate this phenomenon, we introduce an empi…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Voluntary Collusion with Secret Tools in Competing LLM Agents”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation

- **评分**：9/10
- **作者/机构**：Qingyu Meng, Min Chen, Dingming Liu, Yifan Mo, Yue Su, Xin Sun, Koen Hindriks, Jiahuan Pei
- **论文链接**：https://arxiv.org/abs/2605.27393
- **PDF**：https://arxiv.org/pdf/2605.27393
- **代码链接**：https://github.com/Beren-sds/StoryMI

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation”展开，属于「多智能体与协作」方向。作者核心问题是：arXiv:2605.27393v1 [cs.CL] 18 Apr 2026 Large language models (LLMs) can gener- ate fluent dialogue, but prior works lack sit- uational grounding, dynamic strategy control, and evaluation aligned with clinical standards in motivational interviewing (MI). We in…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market

- **评分**：9/10
- **作者/机构**：Deyu Zhou, Yuwei Guo, Xudong Lu, Linhao Zhang, Wei Guo, Lizhen Cui
- **论文链接**：https://arxiv.org/abs/2605.27433
- **PDF**：https://arxiv.org/pdf/2605.27433
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market”展开，属于「多智能体与协作」方向。作者核心问题是：With the increasing complexity of collaboration The data service market includes the demand side, the among various social entities and user demands, the factors platform side, and the supply side. Their logical relationships affecting the stable development…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] HARP: Measuring Harm Amplification in Multi-Agent LLM Systems

- **评分**：9/10
- **作者/机构**：Md Hafizur Rahman, Zafaryab Haider, Tanzim Mahfuz, Prabuddha Chakraborty
- **论文链接**：https://arxiv.org/abs/2605.27489
- **PDF**：https://arxiv.org/pdf/2605.27489
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“HARP: Measuring Harm Amplification in Multi-Agent LLM Systems”展开，属于「多智能体与协作」方向。作者核心问题是：Multi-agent LLM systems decompose workflows across agents, tools, shared context, memory, and decision gates. This modularity improves interpretability, but creates a propagation risk: a bounded perturbation to one component can be reused by other agents and…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“HARP: Measuring Harm Amplification in Multi-Agent LLM Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution

- **评分**：9/10
- **作者/机构**：Mingyu Lu, Yushan Huang, Chris Lin, Su-In Lee
- **论文链接**：https://arxiv.org/abs/2605.27621
- **PDF**：https://arxiv.org/pdf/2605.27621
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution”展开，属于「多智能体与协作」方向。作者核心问题是：arXiv:2605.27621v1 [cs.MA] 26 May 2026 As multi-agent systems (MAS) become increas- ingly complex, identifying the contributions of individual agents is critical for system opti- mization. However, existing approaches lack a rigorous, unified framework for cr…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO

- **评分**：9/10
- **作者/机构**：Shuyang Li, Ruimin Ke
- **论文链接**：https://arxiv.org/abs/2605.27685
- **PDF**：https://arxiv.org/pdf/2605.27685
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO”展开，属于「多智能体与协作」方向。作者核心问题是：The integration of Large Language Models (LLMs) with microscopic traffic simulation offers a promis- ing path toward autonomous urban planning and intelligent arXiv:2605.27685v1 [cs.MA] 26 May 2026 transportation analysis. However, existing monolithic agent a…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems

- **评分**：9/10
- **作者/机构**：Aman Priyanshu, Supriti Vijay, Esha Pahwa
- **论文链接**：https://arxiv.org/abs/2605.27766
- **PDF**：https://arxiv.org/pdf/2605.27766
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems”展开，属于「多智能体与协作」方向。作者核心问题是：models as isolated chat assistants responding to short, bounded LLM safety evaluations predominantly test models in isolation, yet prompts, even as deployed systems increasingly take the form of deployed AI agents increasingly operate within persistent social…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] MolLingo: Molecule-Native Representations for LLM-Powered Scientific Agents

- **评分**：9/10
- **作者/机构**：Thao Nguyen, Heng Ji
- **论文链接**：https://arxiv.org/abs/2605.27853
- **PDF**：https://arxiv.org/pdf/2605.27853
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MolLingo: Molecule-Native Representations for LLM-Powered Scientific Agents”展开，属于「多智能体与协作」方向。作者核心问题是：We present MolLingo, a multi-agent system that emulates the reasoning process of a chemist to automate molecular design. Existing LLM-based approaches to molecular design either operate as standalone generative models without access to external tools, or lack…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“MolLingo: Molecule-Native Representations for LLM-Powered Scientific Agents”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] Multi-Agent LLM-based Metamorphic Testing for REST APIs

- **评分**：9/10
- **作者/机构**：Shehroz Khan, Abdullah Mughees, Gaadha Sudheerbabu, Tanwir Ahmad, Dragos Truscan
- **论文链接**：https://arxiv.org/abs/2605.28321
- **PDF**：https://arxiv.org/pdf/2605.28321
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Multi-Agent LLM-based Metamorphic Testing for REST APIs”展开，属于「多智能体与协作」方向。作者核心问题是：As REST APIs become an increasingly significant on whether the MR that links the seed and follow-up outcomes part of software systems, their validation is becoming more holds [3]. MT has been applied in many application domains, critical. Hence, testing and u…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Multi-Agent LLM-based Metamorphic Testing for REST APIs”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] Beyond One Path: Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents

- **评分**：9/10
- **作者/机构**：Jihyeong Park, Ingeol Baek, Jeonghyun Park, Hwanhee Lee
- **论文链接**：https://arxiv.org/abs/2605.28465
- **PDF**：https://arxiv.org/pdf/2605.28465
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Beyond One Path: Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents”展开，属于「多智能体与协作」方向。作者核心问题是：Remove the beehive without the bees swarming out Divergent thinking is a core dimension of cre- arXiv:2605.28465v1 [cs.CL] 27 May 2026 ativity, yet existing evaluations of Large Lan- Prior Benchmark How many steps? Success only. One path guage Models (LLMs) t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Beyond One Path: Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

- **评分**：9/10
- **作者/机构**：Shanghua Gao, Ada Fang, Marinka Zitnik
- **论文链接**：https://arxiv.org/abs/2605.28655
- **PDF**：https://arxiv.org/pdf/2605.28655
- **代码链接**：https://github.com/mims-harvard/AutoScientists

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation”展开，属于「多智能体与协作」方向。作者核心问题是：Scientific research proceeds through iterative cycles of hypothesis generation, experiment design, execution, and revision. AI agents can automate parts of this process, but existing approaches typically follow a single research trajectory or coordinate throu…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems

- **评分**：8/10
- **作者/机构**：Nicole Koenigstein
- **论文链接**：https://arxiv.org/abs/2605.27466
- **PDF**：https://arxiv.org/pdf/2605.27466
- **代码链接**：https://github.com/Nicolepcx/AgensFlow

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems”展开，属于「多智能体与协作」方向。作者核心问题是：Multi-agent systems built on large language models (LLMs) require many coordination arXiv:2605.27466v1 [cs.MA] 26 May 2026 choices that are difficult to fix a priori: which skill protocol to invoke, which agent role should perform a subtask, which model to bi…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Detection Without Correction: A Two-Parameter Decomposition of Multi-Stage LLM Pipelines

- **评分**：8/10
- **作者/机构**：Prashanti Nilayam, Kiran Ramanna, Prashil Tumbade
- **论文链接**：https://arxiv.org/abs/2605.27559
- **PDF**：https://arxiv.org/pdf/2605.27559
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Detection Without Correction: A Two-Parameter Decomposition of Multi-Stage LLM Pipelines”展开，属于「多智能体与协作」方向。作者核心问题是：naive replication on contemporary frontier mod- els reproduces neither, holding within ±0.7pp of arXiv:2605.27559v1 [cs.MA] 26 May 2026 Multi-stage LLM pipelines that perform multi- R0 across rounds for gpt-4.1 and gpt-4.1-mini on agent debate, intrinsic self…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Detection Without Correction: A Two-Parameter Decomposition of Multi-Stage LLM Pipelines”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents

- **评分**：8/10
- **作者/机构**：Nicole Hsing, Asuka Yuxi Zheng, Yi Zhao, Haoqin Tu, Jen-Tse Huang
- **论文链接**：https://arxiv.org/abs/2605.27586
- **PDF**：https://arxiv.org/pdf/2605.27586
- **代码链接**：https://github.com/arcarae/YOAO

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents”展开，属于「多智能体与协作」方向。作者核心问题是：evitably includes agents that are unaligned, adver- sarially prompted, or optimizing for misspecified arXiv:2605.27586v1 [cs.MA] 26 May 2026 Ensuring agent behaviors in distributed open goals (Hammond et al., 2025; Dafoe et al., 2020; multi-agent systems rema…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] A Policy-Driven Runtime Layer for Agentic LLM Serving

- **评分**：8/10
- **作者/机构**：Rui Zhang, Chaeeun Kim, Liting Hu
- **论文链接**：https://arxiv.org/abs/2605.27744
- **PDF**：https://arxiv.org/pdf/2605.27744
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Policy-Driven Runtime Layer for Agentic LLM Serving”展开，属于「多智能体与协作」方向。作者核心问题是：Agent framework Agent framework Multi-agent LLM systems have become the dominant produc- KV Request tion workload, but the serving stack was not built for them. KV eviction eviction Sche- Agent Batch arXiv:2605.27744v1 [cs.AI] 26 May 2026 Fairness shaping The…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“A Policy-Driven Runtime Layer for Agentic LLM Serving”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems

- **评分**：8/10
- **作者/机构**：Seunghyuk Cho, Sunghyun Choi, Jaeseung Heo, Youngbin Choi, Saemi Moon, MoonJeong Park, Dongwoo Kim
- **论文链接**：https://arxiv.org/abs/2605.27787
- **PDF**：https://arxiv.org/pdf/2605.27787
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems”展开，属于「多智能体与协作」方向。作者核心问题是：However, most existing analyses focus on the per-call setting and offer limited insight into agen- arXiv:2605.27787v1 [cs.MA] 27 May 2026 Multi-agent systems (MAS) have substantially tic deployments where a single task spans many advanced autonomous software…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems

- **评分**：8/10
- **作者/机构**：Yi Ding, Zijie Xuan, Haowei Zhou, Zhenyu Ju, Xiaoxiao Dong, Jingwen Zhang, Xingyu Zhu, Leixin Sun, Haochi Zhang
- **论文链接**：https://arxiv.org/abs/2605.27850
- **PDF**：https://arxiv.org/pdf/2605.27850
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems”展开，属于「多智能体与协作」方向。作者核心问题是：Effective multi-agent systems cannot be designed by selecting prompts or com- munication graphs in isolation. Agent behavior depends on the information an agent receives, while the usefulness of a communication edge depends on how the receiving agent interpre…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] MACReD: A Multi-Agent Collaborative Reasoning Framework for Reaction Diagram Parsing

- **评分**：8/10
- **作者/机构**：Chuang Tang, Chenhao Lin, Yin Xu, Hao Wang, Jinrui Zhou, Xin Li, Mingjun Xiao, Enhong Chen
- **论文链接**：https://arxiv.org/abs/2605.28077
- **PDF**：https://arxiv.org/pdf/2605.28077
- **代码链接**：https://github.com/TC9905/MACReD

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MACReD: A Multi-Agent Collaborative Reasoning Framework for Reaction Diagram Parsing”展开，属于「多智能体与协作」方向。作者核心问题是：Parsing chemical reaction diagrams from scientific literature is chal- lenging due to heterogeneous layouts, intertwined visual elements, and difficulty of integrating recognition and reasoning. Existing Vision Language Models advance multimodal understanding…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“MACReD: A Multi-Agent Collaborative Reasoning Framework for Reaction Diagram Parsing”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
