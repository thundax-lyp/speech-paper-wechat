---
title: "Agent/LLM论文速递｜2026-06-18｜12篇精选"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-06-18｜12篇精选：本期收录 12 篇，重点看 RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-06-18｜12篇精选：本期收录 12 篇，重点看 RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-06-18"
cover_subtitle: "RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-06-18｜12篇精选

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **12** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**3** 篇
- 评测 / 安全 / 对齐：**6** 篇

这一版把今天最值得扫读的 12 篇合并成一篇，方便在公众号里一次读完：优先覆盖 Agent 系统、RAG/知识检索、多智能体、训练对齐与评测安全。排序按固定 rubric 和正文可读证据综合校准。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning | ⭐ 8/10 | RAG/知识检索 |
| RAG与知识检索 | 2 | LegalWorld: A Life-Cycle Interactive Environment for Legal Agents | ⭐ 8/10 | RAG/知识检索, Agent |
| RAG与知识检索 | 3 | MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval | ⭐ 7/10 | RAG/知识检索, benchmark |
| 多智能体与协作 | 1 | EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems | ⭐ 7/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 2 | Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents | ⭐ 7/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 3 | R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning | ⭐ 7/10 | 多智能体/协作, Agent |
| LLM训练与对齐 | 1 | Towards an Agent-First Web: Redesigning the Web for AI Agents | ⭐ 7/10 | LLM训练/对齐, Agent |
| LLM训练与对齐 | 2 | RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents | ⭐ 7/10 | LLM训练/对齐, Agent |
| 评测与安全 | 1 | The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs | ⭐ 8/10 | 评测/安全, LLM |
| 评测与安全 | 2 | TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology | ⭐ 8/10 | 评测/安全, Agent, benchmark |
| 评测与安全 | 3 | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents | ⭐ 7/10 | 评测/安全, Agent, benchmark |
| 评测与安全 | 4 | RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models | ⭐ 7/10 | 评测/安全, benchmark |

</span>

## 精选入选规则

默认按 ML 顶会审稿口径，用固定 rubric 打分：

- **新意（0–3）**：有没有明确的新方法、新任务设定或新范式
- **影响力（0–3）**：是不是对 Agent / LLM 主线方向有代表性，不只是特别窄的小点
- **证据强度（0–2）**：实验是否完整、对比是否靠谱、结论是否站得住
- **受众匹配度（0–2）**：是否贴近 Agent、LLM、多智能体、工具使用、RAG、对齐与评测等核心受众

分数校准：

- `6`：合格可读，但多半偏 incremental
- `7`：接近 strong accept，不是默认鼓励分
- `8+`：默认稀缺，只有当天明显强稿才配拿

本篇取当天综合排序前 **12** 篇合并成一篇，兼顾高分论文和方向覆盖；排序靠前不等于无条件背书，仍建议重点看实验设置、失败案例和真实使用边界。


## 🧠 LLM 推理 / 规划 / RAG


### [1] PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning

- **评分**：8/10
- **作者/机构**：作者：Bo Su, Ankit Shah, Thai Le
- **论文链接**：https://arxiv.org/abs/2606.18473
- **PDF**：https://arxiv.org/pdf/2606.18473
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Machine unlearning for large language mod-  els (LLMs) aims to remove specified knowl- edge while preserving the rest of the model’s capabilities. However, the boundary between knowledge to forget and knowledge to retain is often unclear, since relat。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [2] LegalWorld: A Life-Cycle Interactive Environment for Legal Agents

- **评分**：8/10
- **作者/机构**：作者：Songhan Zuo, Shengbin Yue, Tao Chiang, Guanying Li, Yun Song, Xuanjing Huang, Zhongyu Wei
- **论文链接**：https://arxiv.org/abs/2606.18728
- **PDF**：https://arxiv.org/pdf/2606.18728
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LegalWorld: A Life-Cycle Interactive Environment for Legal Agents”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Civil litigation is inherently a life-cycle process:  what a lawyer drafts on day one constrains what unfolds at trial months later. Yet existing le- gal benchmarks evaluate isolated subtasks, and prior legal-agent simulators reinitialize each scenar。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [3] MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval

- **评分**：7/10
- **作者/机构**：作者：Amirhossein Abaskohi, Raymond Li, Gaetano Cimino, Peter West, Giuseppe Carenini, Issam H. Laradji
- **论文链接**：https://arxiv.org/abs/2606.18508
- **PDF**：https://arxiv.org/pdf/2606.18508
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：search large corpora and often issue many retrieval calls before producing a final answer. Standard Retrieval-augmented generation (RAG) sys-  dense retrieval over fixed-size chunks (Zhao et al., tems depend critically on how documents are 2024) face。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---

## 🤝 多智能体 / 协作


### [4] EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems

- **评分**：7/10
- **作者/机构**：作者：Shuang Xie, Yunan Lu, Han Li, Lingyun Wang
- **论文链接**：https://arxiv.org/abs/2606.18668
- **PDF**：https://arxiv.org/pdf/2606.18668
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：et al., 2025; Gottweis et al., 2025; Swanson et al., In large-scale enterprise settings, centralized 2024; Fourney et al., 2024). In industry, a widely  multi-agent systems (MAS) are increasingly adopted design is the centralized MAS architec- adopte。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 多智能体与协作 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [5] Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents

- **评分**：7/10
- **作者/机构**：作者：Emmanuel Aboah Boateng, Kyle MacDonald, Amardeep Kumar, Siddharth Kodwani, Sudeep Das
- **论文链接**：https://arxiv.org/abs/2606.18947
- **PDF**：https://arxiv.org/pdf/2606.18947
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：Production LLM agents increasingly depend  on real-time search, yet native search ground- ing bundles retrieval policy, provider choice, evidence injection, cost, latency, and genera- tion behavior behind a single model-provider boundary. This coupli。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 多智能体与协作 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [6] R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning

- **评分**：7/10
- **作者/机构**：作者：Haobin Qin, Baofeng Zhang, Hidehisa Akiyama, Keisuke Fujii
- **论文链接**：https://arxiv.org/abs/2606.18786
- **PDF**：https://arxiv.org/pdf/2606.18786
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：Robot soccer is a challenging testbed for multi-agent reinforcement learning because it combines partial observability, cooperative and adversarial interaction, sparse rewards, and long-horizon tactical behavior. RoboCup 2D Soccer Simulation (RCSS2D)。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 多智能体与协作 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，且提供了可复用的系统、评测或机制视角。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [7] Towards an Agent-First Web: Redesigning the Web for AI Agents

- **评分**：7/10
- **作者/机构**：作者：Eranga Bandara, Ross Gore, Ravi Mukkamala, Asanga Gunaratna, Safdar H. Bouk, Xueping Liang, Peter Foytik, Abdul Rahman, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Tharaka Hewa, Amin Hass, Wathsala Herath, Aruna Withanage, Nilaan Loganathan, Atmaram Yarlagadda, Sachin Shetty
- **论文链接**：https://arxiv.org/abs/2606.19116
- **PDF**：https://arxiv.org/pdf/2606.19116
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Towards an Agent-First Web: Redesigning the Web for AI Agents”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：The World Wide Web was architected on a foundational assumption that has held for three decades: that the primary consumer of web content is a human being. This assumption permeates every layer of the web — its access model presumes human visitors, i。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 LLM训练与对齐 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 LLM训练与对齐 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [8] RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents

- **评分**：7/10
- **作者/机构**：作者：Ruishan Fang, Siyuan Lu, Chenyi Zhuang, Tao Lin
- **论文链接**：https://arxiv.org/abs/2606.19047
- **PDF**：https://arxiv.org/pdf/2606.19047
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：Multi-turn tool-use RL is bottlenecked by the rapid depletion of informative samples in static datasets. We observe that the gradient signal in GRPO concentrates on tasks with the highest rollout reward variance, a consequence of the Popoviciu upper。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 LLM训练与对齐 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 LLM训练与对齐 主线，且提供了可复用的系统、评测或机制视角。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [9] The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs

- **评分**：8/10
- **作者/机构**：作者：Naihao Deng, Yiming Feng, Chimaobi Okite, Kaijian Zou, Lu Wang, Rada Mihalcea, Yulong Chen
- **论文链接**：https://arxiv.org/abs/2606.18656
- **PDF**：https://arxiv.org/pdf/2606.18656
- **代码链接**：https://github.com/MichiganNLP/misfired-alignment

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Warning: This paper studies stereotypes and biases, and contains potentially disturbing examples, used for illustration purposes only. Our findings should not be interpreted as an argument against alignment. Instead, this paper highlights the need fo。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 评测与安全 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [10] TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology

- **评分**：8/10
- **作者/机构**：作者：Hannah Le, Ramesh Ramasamy, Alex Urrutia, Mahsa Yazdani, Tim Proctor, Kenny Workman
- **论文链接**：https://arxiv.org/abs/2606.19245
- **PDF**：https://arxiv.org/pdf/2606.19245
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Artificial intelligence (AI) agents promise to accelerate drug discovery by compressing interpretation and decision-making loops, but practical deployment requires trusted evaluation on realistic program deci- sions. We introduce TherapeuticsBench Pr。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 评测与安全 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [11] WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

- **评分**：7/10
- **作者/机构**：作者：Yehang Zhang, Jianchong Su, Haojian Huang, Yifan Chang, Tianhao Zhou, Xinli Xu, Yingjie Xu, Yinchuan Li, Zexi Li, Ying-Cong Chen
- **论文链接**：https://arxiv.org/abs/2606.18847
- **PDF**：https://arxiv.org/pdf/2606.18847
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents”，从题目和首页信息看，属于 评测与安全 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 评测与安全 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [12] RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models

- **评分**：7/10
- **作者/机构**：作者：San Kim, Daechul Ahn, Reokyoung Kim, Hyeonbeom Choi, Seungyeon Jwa, Jonghyun Choi
- **论文链接**：https://arxiv.org/abs/2606.18950
- **PDF**：https://arxiv.org/pdf/2606.18950
- **代码链接**：https://github.com/snumprlab/RTSGameBench

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：goals or vague phrases. - **Design Rule:** Keep the scenario brief SIMPLE, elegant, and focused on ONE core mechanic. If the user asked for "tower defense", make a tower defense — do not add economy puzzles, fog-of-war mechanics, or side objectives。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 评测与安全 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，且提供了可复用的系统、评测或机制视角。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
