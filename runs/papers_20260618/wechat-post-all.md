---
title: "Agent/LLM论文速递｜2026-06-18｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-06-18｜全量版：本期收录 83 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-06-18｜全量版：本期收录 83 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-06-18"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-06-18｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **83** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**3** 篇
- LLM 推理 / 规划 / RAG：**33** 篇
- 评测 / 安全 / 对齐：**25** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Code-Augur: Agentic Vulnerability Detection via Specification Inference | ⭐ 6/10 | Agent系统/工具使用, Agent |
| Agent系统与工具使用 | 2 | Reinforcement Learning Foundation Models Should Already Be A Thing | ⭐ 6/10 | Agent系统/工具使用 |
| Agent系统与工具使用 | 3 | Language Models as Interfaces, Not Oracles: A Hybrid LLM-ML System for Pediatric Appendicitis | ⭐ 6/10 | Agent系统/工具使用, LLM |
| RAG与知识检索 | 1 | PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning | ⭐ 8/10 | RAG/知识检索 |
| RAG与知识检索 | 2 | LegalWorld: A Life-Cycle Interactive Environment for Legal Agents | ⭐ 8/10 | RAG/知识检索, Agent |
| RAG与知识检索 | 3 | MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval | ⭐ 7/10 | RAG/知识检索, benchmark |
| RAG与知识检索 | 4 | Continuous Audio Thinking for Large Audio Language Models | ⭐ 7/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 5 | SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 6 | VISUALSKILL: Multimodal Skills for Computer-Use Agents | ⭐ 7/10 | RAG/知识检索, Agent |
| RAG与知识检索 | 7 | DeFAb: A Verifiable Benchmark for Defeasible Abduction in Foundation Models | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 8 | What Must Generalist Agents Remember? | ⭐ 7/10 | RAG/知识检索, Agent |
| RAG与知识检索 | 9 | GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents | ⭐ 7/10 | RAG/知识检索, Agent, benchmark |
| RAG与知识检索 | 10 | Sumi: Open Uniform Diffusion Language Model from Scratch | ⭐ 7/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 11 | IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages | ⭐ 7/10 | RAG/知识检索, benchmark |
| RAG与知识检索 | 12 | Are LLMs Ready to Assist Physicians? PhysAssistBench for Interactive Doctor-Patient-EHR Assistance | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 13 | Beyond Scalar Scores: Exploring LLM-based Metrics for Clinical Significance Evaluation in Radiology Reports | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 14 | SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG | ⭐ 6/10 | RAG/知识检索 |
| RAG与知识检索 | 15 | CaVe-VLM-CoT: An Interpretable Vision-Language Model Framework | ⭐ 6/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 16 | PragReST: Self-Reinforcing Counterfactual Reasoning for Pragmatic Language Understanding | ⭐ 6/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 17 | Generative-Model Predictive Planning for Navigation in Partially Observable Environments | ⭐ 6/10 | RAG/知识检索 |
| RAG与知识检索 | 18 | Skill-Guided Continuation Distillation for GUI Agents | ⭐ 6/10 | RAG/知识检索, Agent |
| RAG与知识检索 | 19 | From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions | ⭐ 6/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 20 | Bounded Context Management for Tabular Foundation Models on Stream Learning | ⭐ 6/10 | RAG/知识检索 |
| RAG与知识检索 | 21 | Leveraging Energy Features for Surface Classification with Deep Learning: A Comparative Analysis Across Three Independent Datasets | ⭐ 6/10 | RAG/知识检索 |
| RAG与知识检索 | 22 | Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs | ⭐ 6/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 23 | STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability | ⭐ 6/10 | RAG/知识检索 |
| LLM推理与规划 | 1 | HandwritingAgent: Language-Driven Handwriting Synthesis in Scalable Vector Space | ⭐ 6/10 | LLM推理/规划, Agent |
| LLM推理与规划 | 2 | As Easy as Rocket Science: Assessing the Ability of Large Language Models to Interpret Negation in Figurative Language | ⭐ 6/10 | LLM推理/规划, LLM |
| LLM推理与规划 | 3 | As You Wish: Mission Planning with Formal Verification using LLMs in Precision Agriculture | ⭐ 6/10 | LLM推理/规划, LLM |
| RAG与知识检索 | 24 | Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression | ⭐ 6/10 | RAG/知识检索 |
| RAG与知识检索 | 25 | Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems | ⭐ 6/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 26 | CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents | ⭐ 6/10 | RAG/知识检索, Agent, benchmark |
| RAG与知识检索 | 27 | User as Engram: Internalizing Per-User Memory as Local Parametric Edits | ⭐ 6/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 28 | Why SWAVE May Not Be All You Need:A Concept-Evolution Retrospective on Complex-Valued Recurrent Language Models | ⭐ 5/10 | RAG/知识检索, LLM |
| RAG与知识检索 | 29 | Correct Yourself, Keep My Trust: How Self-Correction and Social Connection Shape Credibility in Social Chatbots | ⭐ 5/10 | RAG/知识检索 |
| RAG与知识检索 | 30 | Improving Human-Robot Teamwork in Urban Search and Rescue Through Episodic Memory of Prior Collaboration | ⭐ 5/10 | RAG/知识检索 |
| 多智能体与协作 | 1 | EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems | ⭐ 7/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 2 | Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents | ⭐ 7/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 3 | Towards Multi-Agent-Simulation-Based Community Note Evaluation | ⭐ 7/10 | 多智能体/协作, Agent, benchmark |
| 多智能体与协作 | 4 | R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning | ⭐ 7/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 5 | SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration | ⭐ 7/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 6 | Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents | ⭐ 7/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 7 | AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces | ⭐ 7/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 8 | Caring Without Feeling: Affective Dynamics as the Control Layer of Human-AI Agent Collaboration | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 9 | Characterizing Opinion Evolution of Networked LLMs | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 10 | TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning | ⭐ 6/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 11 | Agentra: A Supervisable Multi-Agent Framework for Enterprise Intrusion Response | ⭐ 6/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 12 | Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 13 | Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 14 | CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 15 | LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 16 | PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning | ⭐ 6/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 17 | A Technical Taxonomy of LLM Agent Communication Protocols | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 18 | Simulating Hate Speech Cascades with Multi-LLM Agents: Empirical Grounding, Modeling Fidelity, and Intervention Strategies | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 19 | Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams | ⭐ 6/10 | 多智能体/协作, LLM |
| 多智能体与协作 | 20 | Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play | ⭐ 6/10 | 多智能体/协作, Agent |
| 多智能体与协作 | 21 | Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies | ⭐ 6/10 | 多智能体/协作, LLM, benchmark |
| 多智能体与协作 | 22 | Digital Speech Acts Retain Control of Copyright with People, Not Platforms | ⭐ 5/10 | 多智能体/协作 |
| LLM训练与对齐 | 1 | Towards an Agent-First Web: Redesigning the Web for AI Agents | ⭐ 7/10 | LLM训练/对齐, Agent |
| LLM训练与对齐 | 2 | RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents | ⭐ 7/10 | LLM训练/对齐, Agent |
| LLM训练与对齐 | 3 | How Well Do Large Language Models Capture Human Personality? | ⭐ 7/10 | LLM训练/对齐, LLM |
| LLM训练与对齐 | 4 | A Variational Framework for LLM Generator-Regulator Games | ⭐ 7/10 | LLM训练/对齐, LLM |
| LLM训练与对齐 | 5 | LLM Parameters for Math Across Languages: Shared or Separate? | ⭐ 6/10 | LLM训练/对齐, LLM |
| LLM训练与对齐 | 6 | ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch | ⭐ 6/10 | LLM训练/对齐, LLM |
| LLM训练与对齐 | 7 | Dango: A Strictly L1-Only Large Language Model for Studying Second Language Acquisition | ⭐ 6/10 | LLM训练/对齐, LLM |
| LLM训练与对齐 | 8 | Pareto Q-Learning with Reward Machines | ⭐ 5/10 | LLM训练/对齐 |
| LLM训练与对齐 | 9 | UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning | ⭐ 5/10 | LLM训练/对齐 |
| 评测与安全 | 1 | The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs | ⭐ 8/10 | 评测/安全, LLM |
| 评测与安全 | 2 | TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology | ⭐ 8/10 | 评测/安全, Agent, benchmark |
| 评测与安全 | 3 | Evaluating Prompting-Based Defenses Against Domain-Camouflaged Injection Attacks | ⭐ 7/10 | 评测/安全, benchmark |
| 评测与安全 | 4 | CEO-Bench: Can Agents Play the Long Game? | ⭐ 7/10 | 评测/安全, LLM, benchmark |
| 评测与安全 | 5 | LandslideAgent with Multimodal LandslideBench: A Domain-Rule-Augmented Agent for Autonomous Landslide Identification and Analysis | ⭐ 7/10 | 评测/安全, LLM, benchmark |
| 评测与安全 | 6 | SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents | ⭐ 7/10 | 评测/安全, Agent |
| 评测与安全 | 7 | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents | ⭐ 7/10 | 评测/安全, Agent, benchmark |
| 评测与安全 | 8 | RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models | ⭐ 7/10 | 评测/安全, benchmark |
| 评测与安全 | 9 | NAVI-Orbital: First In-Orbit Demonstration of a Zero-Shot Vision-Language Model for Autonomous Earth Observation | ⭐ 6/10 | 评测/安全 |
| 评测与安全 | 10 | Examining Human-Like Behaviors in LLMs: A Multi-Dimensional Analysis of Model Behaviors, User Factors, and System Prompts | ⭐ 6/10 | 评测/安全, LLM |
| 评测与安全 | 11 | LLMs Struggle to Measure What Distinguishes Students of Different Proficiency Levels: A Study of Item Discrimination in Reading Comprehension Assessment | ⭐ 6/10 | 评测/安全, LLM |
| 评测与安全 | 12 | Trade-offs in Medical LLM Adaptation: An Empirical Study in French QA | ⭐ 6/10 | 评测/安全, LLM |
| 评测与安全 | 13 | Mitigating Anchoring Bias in LLM-Based Agents for Energy-Efficient 6G Autonomous Networks | ⭐ 6/10 | 评测/安全, LLM |
| 评测与安全 | 14 | Better Adherence, Richer Context: A Field Evaluation of LLM-Powered Conversational Voice Diaries for Sleep | ⭐ 6/10 | 评测/安全, LLM, benchmark |
| 评测与安全 | 15 | Steerable Cultural Preference Optimization of Reward Models | ⭐ 6/10 | 评测/安全, LLM |
| 评测与安全 | 16 | Output Vector Editing for Memorization Mitigation in Large Language Models | ⭐ 6/10 | 评测/安全, LLM |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] Code-Augur: Agentic Vulnerability Detection via Specification Inference

- **评分**：6/10
- **作者/机构**：作者：Zhengxiong Luo, Mehtab Zafar, Dylan Wolff, Abhik Roychoudhury
- **论文链接**：https://arxiv.org/abs/2606.18619
- **PDF**：https://arxiv.org/pdf/2606.18619
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Code-Augur: Agentic Vulnerability Detection via Specification Inference”，从题目和首页信息看，属于 Agent系统与工具使用 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 Agent系统与工具使用 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策核心，围绕观察、计划、工具调用、执行反馈和状态更新组织系统链路。  
- **核心创新**：新意集中在 agent 工作流、工具接口或环境交互方式的重新组织。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 Agent系统与工具使用 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [2] Reinforcement Learning Foundation Models Should Already Be A Thing

- **评分**：6/10
- **作者/机构**：作者：Abdelrahman Zighem, Jill-Jênn Vie
- **论文链接**：https://arxiv.org/abs/2606.18812
- **PDF**：https://arxiv.org/pdf/2606.18812
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Reinforcement Learning Foundation Models Should Already Be A Thing”。从摘要和正文首页看，工作主要处理 Agent系统与工具使用 相关问题：language (Bommasani et al., 2021). TabPFN, TabICL and Foundation models for language and vision are their successors (Hollmann et al., 2023; 2025; Qu et al., 2025; 2026) showed that tabular classification problems  powered by internet-scale data, whi。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 Agent系统与工具使用 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策核心，围绕观察、计划、工具调用、执行反馈和状态更新组织系统链路。  
- **核心创新**：新意集中在 agent 工作流、工具接口或环境交互方式的重新组织。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 Agent系统与工具使用 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [3] Language Models as Interfaces, Not Oracles: A Hybrid LLM-ML System for Pediatric Appendicitis

- **评分**：6/10
- **作者/机构**：作者：Soheyl Bateni, Maryam Abdolali
- **论文链接**：https://arxiv.org/abs/2606.19183
- **PDF**：https://arxiv.org/pdf/2606.19183
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Language Models as Interfaces, Not Oracles: A Hybrid LLM-ML System for Pediatric Appendicitis”，从题目和首页信息看，属于 Agent系统与工具使用 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 Agent系统与工具使用 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策核心，围绕观察、计划、工具调用、执行反馈和状态更新组织系统链路。  
- **核心创新**：新意集中在 agent 工作流、工具接口或环境交互方式的重新组织。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 Agent系统与工具使用 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [4] PreUnlearn: Auditing Collateral Knowledge Damage Before Large Language Model Unlearning

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


### [5] LegalWorld: A Life-Cycle Interactive Environment for Legal Agents

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


### [6] MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval

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


### [7] Continuous Audio Thinking for Large Audio Language Models

- **评分**：7/10
- **作者/机构**：作者：Gyojin Han, Dong-Jae Lee, Changho Choi, Jongsuk Kim, Junmo Kim
- **论文链接**：https://arxiv.org/abs/2606.18273
- **PDF**：https://arxiv.org/pdf/2606.18273
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Continuous Audio Thinking for Large Audio Language Models”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Large audio language models (LALMs) have shown impressive capabilities on diverse audio understanding tasks, ranging from speech transcription to music analysis. However, because LALMs are typically trained to produce text-aligned responses, their hi。

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


### [8] SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents

- **评分**：7/10
- **作者/机构**：作者：Yuchuan Tian, Mengyu Zheng, Haocheng Mei, Ye Yuan, Chao Xu, Xinghao Chen, Hanting Chen, Yu Wang
- **论文链接**：https://arxiv.org/abs/2606.18356
- **PDF**：https://arxiv.org/pdf/2606.18356
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Tool-using language-model agents introduce security failures that go beyond unsafe text: they can disclose protected objects, write persistent memory, send messages, modify databases, or trigger harmful code and tool effects. Existing evaluations oft。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [9] VISUALSKILL: Multimodal Skills for Computer-Use Agents

- **评分**：7/10
- **作者/机构**：作者：Ziyan Jiang, Li An, Yujian Liu, Jiabao Ji, Qiucheng Wu, Jacob Andreas, Yang Zhang, Shiyu Chang
- **论文链接**：https://arxiv.org/abs/2606.18448
- **PDF**：https://arxiv.org/pdf/2606.18448
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“VISUALSKILL: Multimodal Skills for Computer-Use Agents”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：benchmarks such as OSWorld (Xie et al., 2024; Anthropic, 2026; Simular AI, 2026), yet they still Computer-use agents (CUAs) approach human-  level performance on standardised benchmarks struggle on complex, long-horizon tasks and gener- but still str。

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


### [10] DeFAb: A Verifiable Benchmark for Defeasible Abduction in Foundation Models

- **评分**：7/10
- **作者/机构**：作者：Patrick Cooper, Alvaro Velasquez
- **论文链接**：https://arxiv.org/abs/2606.18557
- **PDF**：https://arxiv.org/pdf/2606.18557
- **代码链接**：https://huggingface.co/datasets/PatrickAllenCooper/DeFAb

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“DeFAb: A Verifiable Benchmark for Defeasible Abduction in Foundation Models”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：A rule-based logic solver resolves every instance in our benchmark in under 50 microseconds with 100% accuracy. The best frontier language model achieves 65% at best, and drops to 23.5% under rendering-robust evaluation (worst case over four surface。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [11] What Must Generalist Agents Remember?

- **评分**：7/10
- **作者/机构**：作者：Khurram Yamin, Namrata Deka, Maitreyi Swaroop, Albert Ting, Jeff Schneider, Bryan Wilder
- **论文链接**：https://arxiv.org/abs/2606.18746
- **PDF**：https://arxiv.org/pdf/2606.18746
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“What Must Generalist Agents Remember?”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals. It shows that when two domains share an observational bottleneck but require incompatible optim。

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


### [12] GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

- **评分**：7/10
- **作者/机构**：作者：Zhe Ren, Yibo Yang, Yimeng Chen, Zijun Zhao, Benshuo Fu, Zhihao Shu, Bingjie Zhang, Yangyang Xu, Dandan Guo, Shuicheng Yan
- **论文链接**：https://arxiv.org/abs/2606.18829
- **PDF**：https://arxiv.org/pdf/2606.18829
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents”，从题目和首页信息看，属于 RAG与知识检索 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [13] Sumi: Open Uniform Diffusion Language Model from Scratch

- **评分**：7/10
- **作者/机构**：作者：Mengyu Ye, Keito Kudo, Wataru Ikeda, Ryosuke Matsuda, Keisuke Sakaguchi, Jun Suzuki
- **论文链接**：https://arxiv.org/abs/2606.19005
- **PDF**：https://arxiv.org/pdf/2606.19005
- **代码链接**：https://huggingface.co/collections/tohoku-nlp/sumi

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Sumi: Open Uniform Diffusion Language Model from Scratch”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Diffusion models have become a promising alternative to autoregressive models. Among  these, uniform diffusion language models (UDLMs) permit any token to be updated at any step, in principle enabling more flexible generation. However, no UDLM has ye。

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


### [14] IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages

- **评分**：7/10
- **作者/机构**：作者：Sakshi Joshi, Dhruv Subhash Rathi, Sanskar Singh, Eldho Ittan George, R J Hari, Kaushal Bhogale, Mitesh M. Khapra
- **论文链接**：https://arxiv.org/abs/2606.19157
- **PDF**：https://arxiv.org/pdf/2606.19157
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Table 1: Comparison of contextual ASR benchmarks. AudioLLMs enable speech recognition conditioned on textual  Benchmark Hours Domains Languages Audio prompts such as domain descriptions or entity lists. However, IndicContextEval 56 23 8 (Indic) Natur。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [15] Are LLMs Ready to Assist Physicians? PhysAssistBench for Interactive Doctor-Patient-EHR Assistance

- **评分**：7/10
- **作者/机构**：作者：Tianming Du, Peijie Yu, Sihan Shang, Danli Shi, My Linh Nguyen, Shengbo Gao, Guangyuan Li, Yinghong Yu, Yan Jiang, Qianlong Zhao, Behzad Bozorgtabar, Shaoxiong Ji, Jiazhen Pan, Daniel Rueckert, Jiancheng Yang
- **论文链接**：https://arxiv.org/abs/2606.18613
- **PDF**：https://arxiv.org/pdf/2606.18613
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Are LLMs Ready to Assist Physicians? PhysAssistBench for Interactive Doctor-Patient-EHR Assistance”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：performance drop. Similarly, Bean et al. (2026) found that LLMs performed strongly when tested The most plausible near-term role of medical  LLMs is to assist rather than replace physi- alone, but failed to improve user performance in a cians, yet cu。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [16] Beyond Scalar Scores: Exploring LLM-based Metrics for Clinical Significance Evaluation in Radiology Reports

- **评分**：7/10
- **作者/机构**：作者：Qingyu Lu, Ruochen Li, Liang Ding, Yufei Xia, Youxiang Zhu, Dacheng Tao
- **论文链接**：https://arxiv.org/abs/2606.18797
- **PDF**：https://arxiv.org/pdf/2606.18797
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond Scalar Scores: Exploring LLM-based Metrics for Clinical Significance Evaluation in Radiology Reports”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：100 1-Pass D<R 2-Pass GPT-5.1 Reliable evaluation of generated radiology re- Claude Sonnet 4.5 Gemini 3 Pro  ports requires strict clinical accuracy, as omit- 80 Qwen3-Max LingShu-32B ted critical findings or mischaracterized radio- HuluMed-32B Robus。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 RAG与知识检索 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [17] SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG

- **评分**：6/10
- **作者/机构**：作者：Amirhossein Abaskohi, Issam H. Laradji, Peter West, Giuseppe Carenini
- **论文链接**：https://arxiv.org/abs/2606.18381
- **PDF**：https://arxiv.org/pdf/2606.18381
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：knowledge-intensive tasks (Lewis et al., 2020; Au- genstein et al., 2024). As LLMs are increasingly  Retrieval-augmented generation (RAG) sys- applied to complex tasks involving long docu- tems must balance retrieval granularity with ments (Jin et al。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [18] CaVe-VLM-CoT: An Interpretable Vision-Language Model Framework

- **评分**：6/10
- **作者/机构**：作者：Sneha Rao, Shaina Raza, Dhanesh Ramachandram
- **论文链接**：https://arxiv.org/abs/2606.18385
- **PDF**：https://arxiv.org/pdf/2606.18385
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CaVe-VLM-CoT: An Interpretable Vision-Language Model Framework”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：rious concern in domains such as medicine, ﬁnance, and education, where errors are costly. Vision-Language Models (VLMs) remain prone to hallucinations, producing ﬂuent Two research directions partially address this prob- but visually unfaithful outp。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [19] PragReST: Self-Reinforcing Counterfactual Reasoning for Pragmatic Language Understanding

- **评分**：6/10
- **作者/机构**：作者：Jihyung Park, Minchao Huang, Leqi Liu, Elias Stengel-Eskin
- **论文链接**：https://arxiv.org/abs/2606.18624
- **PDF**：https://arxiv.org/pdf/2606.18624
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“PragReST: Self-Reinforcing Counterfactual Reasoning for Pragmatic Language Understanding”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Pragmatic Inference Scenario Mary and Ken are having breakfast. Ken asks Mary: "How would you like your Natural language understanding often depends tea, dear?" Mary responds, "In a cup." Why has Mary responded like this?  1. Mary wants Ken to serve。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [20] Generative-Model Predictive Planning for Navigation in Partially Observable Environments

- **评分**：6/10
- **作者/机构**：作者：Thomas Quilter, Yifan Zhu, Guorui Quan, Mingfei Sun, Samuel Kaski
- **论文链接**：https://arxiv.org/abs/2606.18888
- **PDF**：https://arxiv.org/pdf/2606.18888
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Generative-Model Predictive Planning for Navigation in Partially Observable Environments”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：environmental states that are consistent with observations, agents Navigation in partially observable environments presents a signifi- can make more informed decisions under uncertainty. Since the be- cant challenge for autonomous agents, requiring e。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [21] Skill-Guided Continuation Distillation for GUI Agents

- **评分**：6/10
- **作者/机构**：作者：Zhimin Fan, Hongwei Yu, Yeqing Shen, Haolong Yan, Guozhen Peng, Tianhao Peng, Yudong Zhang, Xiaowen Zhang, Kaijun Tan, Zheng Ge, Xiangyu Zhang, Daxin Jiang
- **论文链接**：https://arxiv.org/abs/2606.18890
- **PDF**：https://arxiv.org/pdf/2606.18890
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Skill-Guided Continuation Distillation for GUI Agents”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：2025; Wang et al., 2026b; Yan et al., 2025; Xu Improving GUI agents typically relies on be- et al., 2026; Xue et al., 2026), teaching task- specific behaviors, action formats, and procedu-  havior cloning on expert trajectories. However, as the curre。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [22] From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions

- **评分**：6/10
- **作者/机构**：作者：Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, Qingsong Wen
- **论文链接**：https://arxiv.org/abs/2606.18257
- **PDF**：https://arxiv.org/pdf/2606.18257
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Keywords While LLMs show promise in automating educational content cre- Large Language Models, Automated Educational Question Genera- ation, their ability to generate questions that stimulate higher-order tion, Bloom’s Taxonomy thinking remains under。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [23] Bounded Context Management for Tabular Foundation Models on Stream Learning

- **评分**：6/10
- **作者/机构**：作者：Jinmo Lee, Doyun Choi, Moongi Choi, Jaemin Yoo
- **论文链接**：https://arxiv.org/abs/2606.18677
- **PDF**：https://arxiv.org/pdf/2606.18677
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Bounded Context Management for Tabular Foundation Models on Stream Learning”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Recent tabular foundation models (TFMs) offer a different paradigm for tabular prediction. Given a labeled context D Tabular stream learning requires predictions on and a query x, TFMs directly output a posterior predictive  sequentially arriving exa。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [24] Leveraging Energy Features for Surface Classification with Deep Learning: A Comparative Analysis Across Three Independent Datasets

- **评分**：6/10
- **作者/机构**：作者：Alexander Belyaev, Oleg Kushnarev
- **论文链接**：https://arxiv.org/abs/2606.18698
- **PDF**：https://arxiv.org/pdf/2606.18698
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Leveraging Energy Features for Surface Classification with Deep Learning: A Comparative Analysis Across Three Independent Datasets”，从题目和首页信息看，属于 RAG与知识检索 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [25] Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs

- **评分**：6/10
- **作者/机构**：作者：Chris Lee, Flora Salim, Benjamin Tag, Francisco Cruz
- **论文链接**：https://arxiv.org/abs/2606.18747
- **PDF**：https://arxiv.org/pdf/2606.18747
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：and subjective nature of ex- ology, ensuring reproducibility in live deployment settings. pressiveness compared to the more functional dimensions of The phrases were designed to reflect casual, everyday speech relevance and fluidity. Apology showed t。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [26] STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability

- **评分**：6/10
- **作者/机构**：作者：Haipeng Luo, Qingfeng Sun, Songli Wu, Can Xu, Wenfeng Deng, Han Hu, Yansong Tang
- **论文链接**：https://arxiv.org/abs/2606.19236
- **PDF**：https://arxiv.org/pdf/2606.19236
- **代码链接**：https://github.com/hp-luo/STARE

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Reinforcement Learning with Verifiable Rewards algorithms like GRPO have emerged as the dominant post-training paradigm for complex reasoning in LLMs, yet commonly  suffer from policy entropy collapse during training. We conduct a first-order gradien。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [27] HandwritingAgent: Language-Driven Handwriting Synthesis in Scalable Vector Space

- **评分**：6/10
- **作者/机构**：作者：Jaward Sesay, Yue Yu, Börje F. Karlsson
- **论文链接**：https://arxiv.org/abs/2606.18788
- **PDF**：https://arxiv.org/pdf/2606.18788
- **代码链接**：https://github.com/Jaykef/HandwritingAgent

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“HandwritingAgent: Language-Driven Handwriting Synthesis in Scalable Vector Space”。从摘要和正文首页看，工作主要处理 LLM推理与规划 相关问题：ment. Generation is conditioned on texts provided in either conversational or non- Teaching machines to emulate natural hand- conversational mode, along with a refer- writing styles remains an open challenge, ence handwriting-style image. Experiments。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 LLM推理与规划 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：围绕推理链、搜索/规划、验证或分步决策组织模型调用，重点看中间状态如何被约束和复用。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [28] As Easy as Rocket Science: Assessing the Ability of Large Language Models to Interpret Negation in Figurative Language

- **评分**：6/10
- **作者/机构**：作者：Jasmine Owers, Edwin Simpson, Martha Lewis
- **论文链接**：https://arxiv.org/abs/2606.18922
- **PDF**：https://arxiv.org/pdf/2606.18922
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“As Easy as Rocket Science: Assessing the Ability of Large Language Models to Interpret Negation in Figurative Language”。从摘要和正文首页看，工作主要处理 LLM推理与规划 相关问题：(2022). In these cases, the models are tested on mostly conventional metaphor (Stowe et al., Figurative language and negation are two ar- 2022), or good performance is attained via fine- eas that challenge current language models,  tuning (Liu et al。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 LLM推理与规划 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：围绕推理链、搜索/规划、验证或分步决策组织模型调用，重点看中间状态如何被约束和复用。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [29] As You Wish: Mission Planning with Formal Verification using LLMs in Precision Agriculture

- **评分**：6/10
- **作者/机构**：作者：Marcos Abel Zuzuárregui, Stefano Carpin
- **论文链接**：https://arxiv.org/abs/2606.18519
- **PDF**：https://arxiv.org/pdf/2606.18519
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“As You Wish: Mission Planning with Formal Verification using LLMs in Precision Agriculture”。从摘要和正文首页看，工作主要处理 LLM推理与规划 相关问题：the tasks A. Verifying MP Problems from the above query to the figure. Note that since this paper In experimenting with verification, we explore mission focuses on mission precision, we have removed more generic themes of trivial, complex, conditiona。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 LLM推理与规划 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：围绕推理链、搜索/规划、验证或分步决策组织模型调用，重点看中间状态如何被约束和复用。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [30] Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression

- **评分**：6/10
- **作者/机构**：作者：Yifu Ding, Jiacheng Wang, Ge Yang, Yongcheng Jing, Jinyang Guo, Xianglong Liu, Dacheng Tao
- **论文链接**：https://arxiv.org/abs/2606.18304
- **PDF**：https://arxiv.org/pdf/2606.18304
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Importance estimation via attribution-based approximation 1.0  Mixture-of-Experts (MoE) models scale compute 0.8 Alignment-aware redistribution efficiently, yet they remain expensive to deploy 0.6 Score-coverage-based due to substantial memory footpr。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [31] Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems

- **评分**：6/10
- **作者/机构**：作者：Xinru Liu, Xianglong Zhang, Di Cai, Zhumin Chen, Pengfei Hu, Xin Xin
- **论文链接**：https://arxiv.org/abs/2606.18310
- **PDF**：https://arxiv.org/pdf/2606.18310
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems”，从题目和首页信息看，属于 RAG与知识检索 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [32] CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents

- **评分**：6/10
- **作者/机构**：作者：Jiaqi Chen, Yongqin Zeng, Shaoshen Chen, Yijian Zhang, Hai-Tao Zheng, Chunxia Ma, XiuTeng Zhou
- **论文链接**：https://arxiv.org/abs/2606.18406
- **PDF**：https://arxiv.org/pdf/2606.18406
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：agents that act as personal assistants, therapists, and Personalized dialogue agents require continu- continuous companions. As these agents transition  ous long-term memory to maintain coherent from cloud-exclusive deployments to consumer- interacti。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [33] User as Engram: Internalizing Per-User Memory as Local Parametric Edits

- **评分**：6/10
- **作者/机构**：作者：Bojie Li
- **论文链接**：https://arxiv.org/abs/2606.19172
- **PDF**：https://arxiv.org/pdf/2606.19172
- **代码链接**：https://github.com/19PINE-AI/user-as-engram

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“User as Engram: Internalizing Per-User Memory as Local Parametric Edits”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Personal memory in a language model is two problems, not one: content (the specific  facts about a user) and reasoning skill (the ability to turn those facts into answers). The brain keeps the two apart (a sparse, local engram in the hippocampus for。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 RAG与知识检索 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [34] Why SWAVE May Not Be All You Need:A Concept-Evolution Retrospective on Complex-Valued Recurrent Language Models

- **评分**：5/10
- **作者/机构**：作者：Ramprasath Ganesaraja, Swathika N, Sahil Dilip Panse
- **论文链接**：https://arxiv.org/abs/2606.18324
- **PDF**：https://arxiv.org/pdf/2606.18324
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Why SWAVE May Not Be All You Need:A Concept-Evolution Retrospective on Complex-Valued Recurrent Language Models”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：SWAVE is a complex-valued recurrent language model (169.26M parameters, D = 384, L = 16, T = 2048) trained on FineWeb-Edu using 2×H100 NVL. It was designed around three founding premises: that representing language as complex waves rather than real-v。

**☠️ 毒舌点评**  
相关但优先级一般：题目和设定贴近 Agent/LLM，但从可读信息看，贡献可能偏应用包装或评测切片。适合快速浏览，不必默认精读。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
目前更适合按标题和摘要快速定位，实验可信度与适用范围建议读者进入正文后再判断。

**💡 为什么值得看**  
保留在全量版中，方便读者按自己的方向检索，不作为今日优先精读。

</span>

---


### [35] Correct Yourself, Keep My Trust: How Self-Correction and Social Connection Shape Credibility in Social Chatbots

- **评分**：5/10
- **作者/机构**：作者：Biswadeep Sen, Yi-Chieh Lee
- **论文链接**：https://arxiv.org/abs/2606.19286
- **PDF**：https://arxiv.org/pdf/2606.19286
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Correct Yourself, Keep My Trust: How Self-Correction and Social Connection Shape Credibility in Social Chatbots”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：Research in cognitive psychology offers relevant insights. The When social chatbots make mistakes — and they do — how they Computers Are Social Actors (CASA) paradigm demonstrates that  recover determines whether users trust them again. Social chat-。

**☠️ 毒舌点评**  
相关但优先级一般：题目和设定贴近 Agent/LLM，但从可读信息看，贡献可能偏应用包装或评测切片。适合快速浏览，不必默认精读。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
目前更适合按标题和摘要快速定位，实验可信度与适用范围建议读者进入正文后再判断。

**💡 为什么值得看**  
保留在全量版中，方便读者按自己的方向检索，不作为今日优先精读。

</span>

---


### [36] Improving Human-Robot Teamwork in Urban Search and Rescue Through Episodic Memory of Prior Collaboration

- **评分**：5/10
- **作者/机构**：作者：Taewoon Kim, Emma van Zoelen, Mark Neerincx
- **论文链接**：https://arxiv.org/abs/2606.18836
- **PDF**：https://arxiv.org/pdf/2606.18836
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Improving Human-Robot Teamwork in Urban Search and Rescue Through Episodic Memory of Prior Collaboration”。从摘要和正文首页看，工作主要处理 RAG与知识检索 相关问题：syntax,” W3C recommendation, W3C, February 2014. https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/. This research was (partially) funded by the Hybrid In- [20] JanusGraph Contributors, “Janusgraph: an open-source, distributed telligence Center。

**☠️ 毒舌点评**  
相关但优先级一般：题目和设定贴近 Agent/LLM，但从可读信息看，贡献可能偏应用包装或评测切片。适合快速浏览，不必默认精读。

**🔧 技术方案**  
- **模型架构**：以检索、上下文选择、证据融合和生成为主链路，关注外部知识如何进入模型决策。  
- **核心创新**：新意集中在上下文选择、证据组织或 grounding 架构，试图减少检索与生成之间的错配。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
目前更适合按标题和摘要快速定位，实验可信度与适用范围建议读者进入正文后再判断。

**💡 为什么值得看**  
保留在全量版中，方便读者按自己的方向检索，不作为今日优先精读。

</span>

---

## 🤝 多智能体 / 协作


### [37] EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems

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


### [38] Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents

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


### [39] Towards Multi-Agent-Simulation-Based Community Note Evaluation

- **评分**：7/10
- **作者/机构**：作者：Changxi Wen, Shuning Zhang, Bohao Chu, Yuwei Chuai, Hui Wang, Dai Shi, Xin Yi, Hewu Li
- **论文链接**：https://arxiv.org/abs/2606.18268
- **PDF**：https://arxiv.org/pdf/2606.18268
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Towards Multi-Agent-Simulation-Based Community Note Evaluation”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：have been operational on platforms like X for over five years, spanning from early 2021 to 2026. Community-based fact-checking that relies on However, the debunking community notes still cross-consensus is expanding rapidly on so-  cial media platfor。

**☠️ 毒舌点评**  
值得优先看：它不是简单把 LLM 套到任务上，而是在 多智能体与协作 的任务定义、系统链路或评测方式上补了一个相对清楚的缺口。需要警惕的是，若实验只覆盖窄场景，结论外推仍要克制。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
论文提供了实验、案例或基准分析支撑核心结论；建议精读时重点核对消融、失败案例和是否覆盖强 baseline。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，且提供了可复用的系统、评测或机制视角。

</span>

---


### [40] R2D-RL: A RoboCup 2D Soccer Environment for Multi-Agent Reinforcement Learning

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


### [41] SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration

- **评分**：7/10
- **作者/机构**：作者：Ziyi Zhu, Luka Smyth, Saki Shinoda, Jinghong Chen
- **论文链接**：https://arxiv.org/abs/2606.18902
- **PDF**：https://arxiv.org/pdf/2606.18902
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：black-box optimization with expensive evalua- tions and rich local structure.  Context engineering has emerged as a primary This theoretical lens reveals fundamental limita- lever for improving AI systems without pa- tions of existing approaches: ram。

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


### [42] Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents

- **评分**：7/10
- **作者/机构**：作者：Anoushka Vyas, Aarushi Dhanuka, Sina Khoshfetrat Pakazad, Henrik Ohlsson
- **论文链接**：https://arxiv.org/abs/2606.19319
- **PDF**：https://arxiv.org/pdf/2606.19319
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：best prior system (per benchmark) DIA BIRD-Interact +33.0 Production data integration is bottlenecked by  Spider2-Lite +16.1 repeated, lossy handoffs between data owners, engineers, and analysts who must collabora- BIRD-Critic +15.4 tively discover。

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


### [43] AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces

- **评分**：7/10
- **作者/机构**：作者：Zongmin Zhang, Yuyang Lou, Bowen Zhang, Junwu Chen, Ryo Kuroki, Xuan Vu Nguyen, Edvin Fako, Lixue Cheng, Philippe Schwaller
- **论文链接**：https://arxiv.org/abs/2606.19152
- **PDF**：https://arxiv.org/pdf/2606.19152
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：Identifying the lowest-energy surface–adsorbate configuration is critical for modeling hetero- geneous catalysis, yet exhaustive exploration with ab initio calculations is computationally pro- hibitive. Machine-learning force fields (MLFFs) accelerat。

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


### [44] Caring Without Feeling: Affective Dynamics as the Control Layer of Human-AI Agent Collaboration

- **评分**：6/10
- **作者/机构**：作者：Junjie Xu, Xingjiao Wu, Zihao Zhang, Yujia Xu, Yuzhe Yang, Jin Zhu, Luwei Xiao, Wen Wu, Liang He
- **论文链接**：https://arxiv.org/abs/2606.18259
- **PDF**：https://arxiv.org/pdf/2606.18259
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Caring Without Feeling: Affective Dynamics as the Control Layer of Human-AI Agent Collaboration”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：AI agents that plan, retain memory across sessions, invoke external tools and act with partial auton- omy are transforming human–AI collaboration. Research on affective computing, simulated empathy in large language models, trust in automation and AI。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [45] Characterizing Opinion Evolution of Networked LLMs

- **评分**：6/10
- **作者/机构**：作者：Caleb Probine, Yigit Ege Bayiz, Filippos Fotiadis, Samuel Li, Yunhao Yang, Ufuk Topcu
- **论文链接**：https://arxiv.org/abs/2606.18276
- **PDF**：https://arxiv.org/pdf/2606.18276
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Characterizing Opinion Evolution of Networked LLMs”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：and bias drive belief evolution. Extending them to interacting LLMs may therefore provide a prin- Large language models (LLMs) increasingly in-  cipled framework for understanding emergent be- teract with one another in multi-agent systems, havior in。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [46] TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning

- **评分**：6/10
- **作者/机构**：作者：Zijie Meng, Ziwei Li, Yufei Liu, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Miao Zhang
- **论文链接**：https://arxiv.org/abs/2606.18308
- **PDF**：https://arxiv.org/pdf/2606.18308
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：a recommender or a chess engine that can afford a regret-then-improve curve, every unsafe action Safe coordination in networked cyber-physical  committed during training has physical, irreversible systems forces learning algorithms to simul- taneousl。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [47] Agentra: A Supervisable Multi-Agent Framework for Enterprise Intrusion Response

- **评分**：6/10
- **作者/机构**：作者：Raj Patel, Shaswata Mitra, Michele Guida, Stefano Iannucci, Sudip Mittal, Shahram Rahimi
- **论文链接**：https://arxiv.org/abs/2606.18325
- **PDF**：https://arxiv.org/pdf/2606.18325
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Agentra: A Supervisable Multi-Agent Framework for Enterprise Intrusion Response”，从题目和首页信息看，属于 多智能体与协作 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [48] Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications

- **评分**：6/10
- **作者/机构**：作者：Paresh Dashore, Shreyas Kulkarni, Uttam Gurram, Nadia Bathaee, Kartik Balasubramaniam, Genta Indra Winata, Sambit Sahu, Shi-Xiong Zhang
- **论文链接**：https://arxiv.org/abs/2606.18502
- **PDF**：https://arxiv.org/pdf/2606.18502
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：User Query Large language model (LLM)-based multi-  agent systems demonstrate strong perfor- j Understander Á Planner Û Evaluator mance on complex reasoning and task ex- ecution, enabling broad enterprise applica- tions. However, production deploymen。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [49] Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems

- **评分**：6/10
- **作者/机构**：作者：Hehai Lin, Qi Yang, Chengwei Qin
- **论文链接**：https://arxiv.org/abs/2606.18837
- **PDF**：https://arxiv.org/pdf/2606.18837
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：et al., 2025a; Lin et al., 2026). Consequently, automatic-MAS has emerged as a pivotal direction, Large Language Model (LLM)-based auto- aiming to automate the generation and optimization matic Multi-Agent Systems (MAS) generation of multi-agent arch。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [50] CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System

- **评分**：6/10
- **作者/机构**：作者：Marco Becattini, Niccolò Caselli, Matteo Minin, Roberto Verdecchia, Enrico Vicario
- **论文链接**：https://arxiv.org/abs/2606.18976
- **PDF**：https://arxiv.org/pdf/2606.18976
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：User superclass with Customer and Barber subclasses. However, the persistence design stores both roles in a single relational table: Users(email, name, surname, pass_hash, phone, role). The report never documents the mapping rule between the OO inher。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [51] LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents

- **评分**：6/10
- **作者/机构**：作者：Haoyang Fang, Wei Zhu, Boran Han, Alex Zhang, Zhenyu Pan, Shuo Yang, Shuai Zhang, Jiading Gai, Peng Tang, Cuixiong Hu, Xuan Zhu, Huzefa Rangwala, George Karypis, Bernie Wang
- **论文链接**：https://arxiv.org/abs/2606.18388
- **PDF**：https://arxiv.org/pdf/2606.18388
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：response length (Luo et al., 2025b; Chen et al., RL post-training strategies are dataset- 2025a; He et al., 2025; Hao et al., 2025; Xiaomi dependent and reveal a recurring empirical et al., 2025; Luo et al., 2025a; Chen et al., 2025b; pattern: capaci。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [52] PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning

- **评分**：6/10
- **作者/机构**：作者：Zhiyuan Wen, Jiannong Cao, Peng Gao, Haochen Shi, Wengpan Kuan, Bo Yuan, Xiuxiu Qi
- **论文链接**：https://arxiv.org/abs/2606.18633
- **PDF**：https://arxiv.org/pdf/2606.18633
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：goals into executable programs (Denny et al., 2024; Hsu, 2025). Programming learning often requires Effective programming education requires per- sonalized instruction adapted to diverse learner resource retrieval, prerequisite explanation, code back。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [53] A Technical Taxonomy of LLM Agent Communication Protocols

- **评分**：6/10
- **作者/机构**：作者：Linus Sander, Habtom Kahsay Gidey, Alexander Lenz, Alois Knoll
- **论文链接**：https://arxiv.org/abs/2606.19135
- **PDF**：https://arxiv.org/pdf/2606.19135
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“A Technical Taxonomy of LLM Agent Communication Protocols”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：As large language models (LLMs) advance and multi-agent systems aim to overcome the limits of standalone agents, robust communication protocols are becoming essential infrastructure for distributed agent networks. Nonetheless, the fragmented protocol。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [54] Simulating Hate Speech Cascades with Multi-LLM Agents: Empirical Grounding, Modeling Fidelity, and Intervention Strategies

- **评分**：6/10
- **作者/机构**：作者：Fan Huang
- **论文链接**：https://arxiv.org/abs/2606.18264
- **PDF**：https://arxiv.org/pdf/2606.18264
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Simulating Hate Speech Cascades with Multi-LLM Agents: Empirical Grounding, Modeling Fidelity, and Intervention Strategies”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：through follower networks, and which interven- tions dampen it without suppressing benign en- Faithful modeling of hateful-content propaga-  tion on online platforms remains an open prob- gagement? lem for moderation research. Classical cas- A simula。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [55] Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams

- **评分**：6/10
- **作者/机构**：作者：Haewoon Kwak
- **论文链接**：https://arxiv.org/abs/2606.19111
- **PDF**：https://arxiv.org/pdf/2606.19111
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：Team science holds that leadership is contingent: it helps only under specific conditions, and capable, autonomous teams may need none at all. We ask the analogous question for multi-agent LLM teams: under what measurable conditions does process-leve。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [56] Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play

- **评分**：6/10
- **作者/机构**：作者：Leyang Shen, Yang Zhang, Xiaoyan Zhao, Chun Kai Ling, Tat-Seng Chua
- **论文链接**：https://arxiv.org/abs/2606.19308
- **PDF**：https://arxiv.org/pdf/2606.19308
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious Play”，从题目和首页信息看，属于 多智能体与协作 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [57] Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies

- **评分**：6/10
- **作者/机构**：作者：Serena A. Hoffstedde, Machiko Hirota, Akshara Nadayanur Sathis Kanna, Rihito Kotani, Ujwal Kumar, Gabriele Trovato, Phan Xuan Tan
- **论文链接**：https://arxiv.org/abs/2606.18649
- **PDF**：https://arxiv.org/pdf/2606.18649
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies”，从题目和首页信息看，属于 多智能体与协作 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 多智能体与协作 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [58] Digital Speech Acts Retain Control of Copyright with People, Not Platforms

- **评分**：5/10
- **作者/机构**：作者：James Golike, Ehud Shapiro
- **论文链接**：https://arxiv.org/abs/2606.19263
- **PDF**：https://arxiv.org/pdf/2606.19263
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Digital Speech Acts Retain Control of Copyright with People, Not Platforms”。从摘要和正文首页看，工作主要处理 多智能体与协作 相关问题：Legal precedents protect computer code as copyrightable expression. They have enabled cen- tralized digital platforms—operating from corporate servers that hold all user data—to construct private governance regimes through the interaction of copyrigh。

**☠️ 毒舌点评**  
相关但优先级一般：题目和设定贴近 Agent/LLM，但从可读信息看，贡献可能偏应用包装或评测切片。适合快速浏览，不必默认精读。

**🔧 技术方案**  
- **模型架构**：由多个 LLM/Agent 角色或子系统协作完成任务，核心在通信、分工、聚合和可靠性控制。  
- **核心创新**：新意在于多角色/多主体之间的协作建模，以及对子智能体行为可信度的显式处理。  
- **训练 / 推理策略**：以推理时编排和系统设计为主，未必依赖重新训练；关键在提示、工具、检索和反馈闭环。

**📊 实验结果**  
目前更适合按标题和摘要快速定位，实验可信度与适用范围建议读者进入正文后再判断。

**💡 为什么值得看**  
保留在全量版中，方便读者按自己的方向检索，不作为今日优先精读。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [59] Towards an Agent-First Web: Redesigning the Web for AI Agents

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


### [60] RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents

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


### [61] How Well Do Large Language Models Capture Human Personality?

- **评分**：7/10
- **作者/机构**：作者：Aanisha Bhattacharyya, Yaman Kumar Singla, Rajiv Ratn Shah, Changyou Chen, Jitendra Ajmera
- **论文链接**：https://arxiv.org/abs/2606.18263
- **PDF**：https://arxiv.org/pdf/2606.18263
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“How Well Do Large Language Models Capture Human Personality?”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：Large language models (LLMs) are increasingly used to simulate human popu- lations via persona prompting, often under the assumptions that richer persona descriptions improve behavioral fidelity, similarly sized attribute combinations are equally sim。

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


### [62] A Variational Framework for LLM Generator-Regulator Games

- **评分**：7/10
- **作者/机构**：作者：Quanyan Zhu
- **论文链接**：https://arxiv.org/abs/2606.18424
- **PDF**：https://arxiv.org/pdf/2606.18424
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“A Variational Framework for LLM Generator-Regulator Games”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：class labels and scores; it does not enumerate restricted terms or provide evasion templates. applications and platforms studied across chat, live streaming, mobile games, open-source projects, WeChat, QQMail, search, translation, and related service。

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


### [63] LLM Parameters for Math Across Languages: Shared or Separate?

- **评分**：6/10
- **作者/机构**：作者：Behzad Shomali, Luisa Victor, Tim Selbach, Ali Hamza Bashir, David Berghaus, Joachim Koehler, Mehdi Ali, Markus Frey
- **论文链接**：https://arxiv.org/abs/2606.18453
- **PDF**：https://arxiv.org/pdf/2606.18453
- **代码链接**：https://github.com/luisavictor/math-

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LLM Parameters for Math Across Languages: Shared or Separate?”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：age forward-pass statistics (Sun et al., 2023). No- tably, Christ et al. (2025) introduced MathNeuro- Large language models (LLMs) exhibit sub-  surgery, isolating parameters critical to mathemat- stantial cross-lingual variation in mathematical ical。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 LLM训练与对齐 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [64] ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch

- **评分**：6/10
- **作者/机构**：作者：Tengfei Lyu, Zirui Yuan, Xu Liu, Kai Wan, Zihao Lu, Li Ma, Hao Liu
- **论文链接**：https://arxiv.org/abs/2606.18803
- **PDF**：https://arxiv.org/pdf/2606.18803
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：Order-Driver Pair OD Prediction ω Match Weight Matched Pair <latexit sha1_base64="igpFSm9Dzn9/gbnS418ACy1mCcM=">AAAB7nicbVDLSgNBEOyNrxhfUY9eBoPgKeyKr2PQi8cIxgSSJcxOZpMh81hmZoWw5CO8eFDEq9/jzb9xNtmDJhY0FFXddHdFCWfG+v63V1pZXVvfKG9WtrZ3dveq+wePRqWa0BZRXO。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 LLM训练与对齐 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [65] Dango: A Strictly L1-Only Large Language Model for Studying Second Language Acquisition

- **评分**：6/10
- **作者/机构**：作者：Shiho Matta, Yin Jou Huang, Fei Cheng, Takashi Kodama, Hirokazu Kiyomaru, Yugo Murawaki
- **论文链接**：https://arxiv.org/abs/2606.19170
- **PDF**：https://arxiv.org/pdf/2606.19170
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Dango: A Strictly L1-Only Large Language Model for Studying Second Language Acquisition”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：Trends \n ❌ [An article forming document level translation pair: Filtered] Japan is the land of trends. Nowhere else do trends arise, spread and \n die with such speed. The reasons for this are simple: affluent youth, merciless \n We introduce Dango。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 LLM训练与对齐 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [66] Pareto Q-Learning with Reward Machines

- **评分**：5/10
- **作者/机构**：作者：Arnaud Lequen, Clément Legrand-Lixon, Léo Saulières
- **论文链接**：https://arxiv.org/abs/2606.19134
- **PDF**：https://arxiv.org/pdf/2606.19134
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Pareto Q-Learning with Reward Machines”。从摘要和正文首页看，工作主要处理 LLM训练与对齐 相关问题：finite-state automaton that encodes the reward structure of a  task in a modular and structured way. This representation of- We present Pareto Q-Learning with Reward Machines fers several advantages. First, it provides an interpretable de- (PQLRM), a。

**☠️ 毒舌点评**  
相关但优先级一般：题目和设定贴近 Agent/LLM，但从可读信息看，贡献可能偏应用包装或评测切片。适合快速浏览，不必默认精读。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
目前更适合按标题和摘要快速定位，实验可信度与适用范围建议读者进入正文后再判断。

**💡 为什么值得看**  
保留在全量版中，方便读者按自己的方向检索，不作为今日优先精读。

</span>

---


### [67] UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning

- **评分**：5/10
- **作者/机构**：作者：Mohamed Nabail, Leo Cheng, Jingmin Wang, Nicholas Rhinehart
- **论文链接**：https://arxiv.org/abs/2606.19328
- **PDF**：https://arxiv.org/pdf/2606.19328
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning”，从题目和首页信息看，属于 LLM训练与对齐 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
相关但优先级一般：题目和设定贴近 Agent/LLM，但从可读信息看，贡献可能偏应用包装或评测切片。适合快速浏览，不必默认精读。

**🔧 技术方案**  
- **模型架构**：围绕参数编辑、偏好/奖励信号、遗忘或对齐诊断展开，关注训练目标与行为变化之间的关系。  
- **核心创新**：主要新意来自问题设定、方法组合或面向特定任务的系统化验证。  
- **训练 / 推理策略**：涉及参数编辑、遗忘、奖励/偏好信号或对齐诊断；需要看行为改善是否伴随副作用。

**📊 实验结果**  
目前更适合按标题和摘要快速定位，实验可信度与适用范围建议读者进入正文后再判断。

**💡 为什么值得看**  
保留在全量版中，方便读者按自己的方向检索，不作为今日优先精读。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [68] The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs

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


### [69] TxBench-PP: Analyzing AI Agent Performance on Small-Molecule Preclinical Pharmacology

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


### [70] Evaluating Prompting-Based Defenses Against Domain-Camouflaged Injection Attacks

- **评分**：7/10
- **作者/机构**：作者：Aaditya Pai
- **论文链接**：https://arxiv.org/abs/2606.18530
- **PDF**：https://arxiv.org/pdf/2606.18530
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Evaluating Prompting-Based Defenses Against Domain-Camouflaged Injection Attacks”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Domain-camouflaged injection attacks embed malicious instructions in retrieved content using domain-appropriate vocabulary, evading standard detectors that rely on syntactic injection markers. When detection fails, prac- titioners need to know which。

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


### [71] CEO-Bench: Can Agents Play the Long Game?

- **评分**：7/10
- **作者/机构**：作者：Haozhe Chen, Karthik Narasimhan, Zhuang Liu
- **论文链接**：https://arxiv.org/abs/2606.18543
- **PDF**：https://arxiv.org/pdf/2606.18543
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CEO-Bench: Can Agents Play the Long Game?”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Language model agents are becoming proficient executors at isolated, short-horizon tasks such as software engineering and customer service. Yet real-world challenges require a combination of sophisticated skills that remain largely untested in agents。

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


### [72] LandslideAgent with Multimodal LandslideBench: A Domain-Rule-Augmented Agent for Autonomous Landslide Identification and Analysis

- **评分**：7/10
- **作者/机构**：作者：Chengfu Liu, Dongyang Hou, Junwu Xiang, Cheng Yang, Xuezhi Cui, Zeyuan Wang, Liangtian Liu, Zelang Miao
- **论文链接**：https://arxiv.org/abs/2606.18661
- **PDF**：https://arxiv.org/pdf/2606.18661
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LandslideAgent with Multimodal LandslideBench: A Domain-Rule-Augmented Agent for Autonomous Landslide Identification and Analysis”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Intelligent landslide hazard interpretation is critical for disaster prevention, yet current paradigms struggle to simultaneously extract visual features and high-level geoscientific semantics, while general-purpose vision–language models (VLMs) suff。

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


### [73] SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents

- **评分**：7/10
- **作者/机构**：作者：Qiao Zhao, JianYing Qu, Jun Zhang, Yehua Yang, Hanwen Du, Zhongkai Sun
- **论文链接**：https://arxiv.org/abs/2606.18733
- **PDF**：https://arxiv.org/pdf/2606.18733
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Realistic coding-agent benchmarks often replay public GitHub issues and pull requests, mak- ing them vulnerable to overlap with model pretraining, fine-tuning, synthetic-data generation, or benchmark-driven model selection. Fully synthetic tasks avoi。

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


### [74] WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

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


### [75] RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models

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


### [76] NAVI-Orbital: First In-Orbit Demonstration of a Zero-Shot Vision-Language Model for Autonomous Earth Observation

- **评分**：6/10
- **作者/机构**：作者：Juan Manuel Delfa Victoria, Taran Cyriac John, Andrew W. Herson
- **论文链接**：https://arxiv.org/abs/2606.18271
- **PDF**：https://arxiv.org/pdf/2606.18271
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“NAVI-Orbital: First In-Orbit Demonstration of a Zero-Shot Vision-Language Model for Autonomous Earth Observation”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：base B. NAVI-Orbital Software Architecture class is implemented by GemmaVLAdapter (HuggingFace NAVI-Orbital implements a hierarchical, agentic architec- pipeline) and LlamaCppAdapter (GGUF via llama.cpp ture designed to operate autonomously within th。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [77] Examining Human-Like Behaviors in LLMs: A Multi-Dimensional Analysis of Model Behaviors, User Factors, and System Prompts

- **评分**：6/10
- **作者/机构**：作者：Sunnie S. Y. Kim, Margit Bowler, Leon A Gatys
- **论文链接**：https://arxiv.org/abs/2606.18258
- **PDF**：https://arxiv.org/pdf/2606.18258
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Examining Human-Like Behaviors in LLMs: A Multi-Dimensional Analysis of Model Behaviors, User Factors, and System Prompts”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Large language models (LLMs) exhibit a wide range of human-like behaviors, from expressing thoughts and emotions, to engaging in relationship-building with users, to refusing requests and maintaining boundaries. Despite their prevalence, researchers。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [78] LLMs Struggle to Measure What Distinguishes Students of Different Proficiency Levels: A Study of Item Discrimination in Reading Comprehension Assessment

- **评分**：6/10
- **作者/机构**：作者：Han Chen, Ming Li, Chenguang Wang, Yijun Liang, Dawei Zhou, Hong jiao, Tianyi Zhou
- **论文链接**：https://arxiv.org/abs/2606.18709
- **PDF**：https://arxiv.org/pdf/2606.18709
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LLMs Struggle to Measure What Distinguishes Students of Different Proficiency Levels: A Study of Item Discrimination in Reading Comprehension Assessment”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：and Rodriguez, 2013). In classical test theory (CTT), this property is commonly captured by Item discrimination is a fundamental psycho-  metric property of educational assessment, item discrimination, often measured as the correla- which measures wh。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [79] Trade-offs in Medical LLM Adaptation: An Empirical Study in French QA

- **评分**：6/10
- **作者/机构**：作者：Ikram Belmadani, Oumaima El Khettari, Carlos Ramisch, Frederic Bechet, Richard Dufour, Benoit Favre
- **论文链接**：https://arxiv.org/abs/2606.19266
- **PDF**：https://arxiv.org/pdf/2606.19266
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Trade-offs in Medical LLM Adaptation: An Empirical Study in French QA”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Despite their widespread use, the relative effec- tiveness of these strategies remains unclear. Their  The development of large language models impact depends on training scale, data composi- (LLMs) has led to an increased focus on their tion, and op。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [80] Mitigating Anchoring Bias in LLM-Based Agents for Energy-Efficient 6G Autonomous Networks

- **评分**：6/10
- **作者/机构**：作者：Hatim Chergui, Claudia Carballo González, Farhad Rezazadeh, Merouane Debbah
- **论文链接**：https://arxiv.org/abs/2606.18272
- **PDF**：https://arxiv.org/pdf/2606.18272
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Mitigating Anchoring Bias in LLM-Based Agents for Energy-Efficient 6G Autonomous Networks”，从题目和首页信息看，属于 评测与安全 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [81] Better Adherence, Richer Context: A Field Evaluation of LLM-Powered Conversational Voice Diaries for Sleep

- **评分**：6/10
- **作者/机构**：作者：Amama Mahmood, Bokyung Kim, Honghao Zhao, Molly E. Atwood, Luis F. Buenaver, Michael T. Smith, Chien-Ming Huang
- **论文链接**：https://arxiv.org/abs/2606.18596
- **PDF**：https://arxiv.org/pdf/2606.18596
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Better Adherence, Richer Context: A Field Evaluation of LLM-Powered Conversational Voice Diaries for Sleep”，从题目和首页信息看，属于 评测与安全 方向；可作为今天 Agent/LLM 论文池里的定位型线索，建议读者结合正文进一步判断深读价值。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：主要新意在于提出新的任务集合、评价维度或诊断协议，用来暴露常规指标不容易看到的能力差异。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [82] Steerable Cultural Preference Optimization of Reward Models

- **评分**：6/10
- **作者/机构**：作者：Minsik Oh, Advit Deepak, Sophie Wu, Douwe Kiela, Ekaterina Shutova
- **论文链接**：https://arxiv.org/abs/2606.18606
- **PDF**：https://arxiv.org/pdf/2606.18606
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Steerable Cultural Preference Optimization of Reward Models”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：ulations, grouped into U.S. states and other demographic factors (Santurkar et al., 2023) and distinct countries (Dur- It is essential for large language model (LLM) mus et al., 2024). LLMs are known to reflect opinions technology to serve many diffe。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---


### [83] Output Vector Editing for Memorization Mitigation in Large Language Models

- **评分**：6/10
- **作者/机构**：作者：Ahmad Dawar Hakimi, Kaiwei Lei, Isabelle Augenstein, Hinrich Schütze
- **论文链接**：https://arxiv.org/abs/2606.18767
- **PDF**：https://arxiv.org/pdf/2606.18767
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Output Vector Editing for Memorization Mitigation in Large Language Models”。从摘要和正文首页看，工作主要处理 评测与安全 相关问题：Large language models memorize and reproduce sequences from their training data, creating privacy, copyright, and security risks. Existing neuron-level mitigation methods equate editing with zeroing out neuron activations, but the activation only con。

**☠️ 毒舌点评**  
可读但别急着封神：论文和 评测与安全 主线相关，问题意识明确，不过目前更像一个有用的增量组件或场景化验证。建议重点检查对照组、失败案例和真实使用成本。

**🔧 技术方案**  
- **模型架构**：以 benchmark、审计指标、风险定位或可靠性评估为主，重点暴露现有模型的能力边界。  
- **核心创新**：新意在于把风险、偏差或能力失效拆成更可观察的评测切片。  
- **训练 / 推理策略**：多数属于评测或应用层研究，训练细节不是主轴；应关注实验协议和评估有效性。

**📊 实验结果**  
作者给出相应实验或案例结果，但证据强度仍需读正文确认，尤其是样本规模、对照设置和统计稳定性。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者扫读，能补充一个具体任务或方法侧面的观察。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
