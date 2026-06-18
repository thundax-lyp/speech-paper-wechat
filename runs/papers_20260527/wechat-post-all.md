---
title: "Agent/LLM论文速递｜2026-05-27｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-27｜全量版：本期收录 80 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-27｜全量版：本期收录 80 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-27"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-27｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **80** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**22** 篇
- LLM 推理 / 规划 / RAG：**16** 篇
- 评测 / 安全 / 对齐：**28** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation | ⭐ 8/10 | agent, tool use |
| Agent系统与工具使用 | 2 | MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation | ⭐ 8/10 | agent, memory, evaluation |
| Agent系统与工具使用 | 3 | A Universal Cliff and a Design Fingerprint: Cross-Section Defect Detection Under LLM Orchestration | ⭐ 7/10 | agent, workflow, tool use |
| Agent系统与工具使用 | 4 | SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup? | ⭐ 7/10 | agent, coding |
| Agent系统与工具使用 | 5 | CyberEvolver: Structured Self-Evolution for Cybersecurity Agents On the Fly | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 6 | Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory | ⭐ 7/10 | agent, memory |
| Agent系统与工具使用 | 7 | Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 8 | SPEAR: Code-Augmented Agentic Prompt Optimization | ⭐ 7/10 | agent, coding |
| Agent系统与工具使用 | 9 | Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 10 | Experiments in Agentic AI for Science | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 11 | Foundations of a Time-Consistent Counterfactual Actuarial Runtime for Autonomous AI Agents | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 12 | MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration | ⭐ 7/10 | agent, GUI agent |
| Agent系统与工具使用 | 13 | Control Physiology: An Agent-Based Model of FAIR-CAM Dynamics | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 14 | Beyond Trajectory-Level Attribution: Graph-Based Credit Assignment for Agentic Reinforcement Learning | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 15 | Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 16 | Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton | ⭐ 7/10 | GUI agent |
| Agent系统与工具使用 | 17 | TADDLE: A Tool-Augmented Agent for Detecting Deficient LLM-Generated Peer Reviews | ⭐ 7/10 | agent, tool use |
| Agent系统与工具使用 | 18 | Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 19 | Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 20 | Governed Evolution of Agent Runtimes through Executable Operational Cognition | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 21 | Maat: The Agentic Legal Research Assistant for Competition Protection | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 22 | GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing | ⭐ 7/10 | agent |
| RAG与知识检索 | 1 | Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets | ⭐ 7/10 | agent, tool use, RAG |
| RAG与知识检索 | 2 | FAB-Bench: A Framework for Adaptive RAG Benchmarking in Semiconductor Manufacturing | ⭐ 7/10 | RAG, benchmark |
| RAG与知识检索 | 3 | PolyFusionAgent: A Multimodal Foundation Model and Autonomous AI Assistant for Polymer Property Prediction and Inverse Design | ⭐ 7/10 | agent |
| RAG与知识检索 | 4 | The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context | ⭐ 7/10 | memory |
| RAG与知识检索 | 5 | GeoFaith: A Spatio-Temporal Dual View of Faithful Chain-of-Thought | ⭐ 7/10 | CoT |
| RAG与知识检索 | 6 | From Norms to Indicators (N2I-RAG): An Agentic Retrieval-Augmented Generation Framework for Legal Indicator Computation | ⭐ 7/10 | agent, RAG, retrieval |
| RAG与知识检索 | 7 | Detecting Is Not Resolving: The Monitoring Control Gap in Retrieval Augmented LLMs | ⭐ 7/10 | retrieval |
| RAG与知识检索 | 8 | The Coverage Illusion: From Pre-retrieval Routing Failure to Post-retrieval Cascades in a Production RAG System | ⭐ 7/10 | RAG, retrieval |
| RAG与知识检索 | 9 | ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents | ⭐ 7/10 | agent, retrieval, memory, benchmark |
| RAG与知识检索 | 10 | Beyond Questions: Evaluating What Large Language Models (Actually) Know | ⭐ 6/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 11 | Intelligent Detection and Mitigation of Carpet-Bombing DDoS Attacks in SDN Using Retrieval-Augmented Generation and Large Language Models | ⭐ 6/10 | retrieval |
| RAG与知识检索 | 12 | RICE-PO: Turning Retrieval Interactions into Credit Signals for Reasoning Agents | ⭐ 6/10 | agent, retrieval, reasoning |
| RAG与知识检索 | 13 | In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective | ⭐ 6/10 | retrieval |
| RAG与知识检索 | 14 | Mind the Tool Failures: Achieving Synergistic Tool Gains for Medical Agents | ⭐ 6/10 | agent, tool use |
| RAG与知识检索 | 15 | LitSeg: Narrative-Aware Document Segmentation for Literary RAG | ⭐ 6/10 | RAG |
| LLM推理与规划 | 1 | Reasoning, Code, or Both? How Large Language Models Handle Variations in Math Questions | ⭐ 5/10 | reasoning, coding |
| 多智能体与协作 | 1 | AutoDFT: A Closed-Loop Multi-Agent Framework for Autonomous DFT Calculations | ⭐ 7/10 | agent, multi-agent |
| 多智能体与协作 | 2 | AgentSociety: Incentivizing Agentic Social Intelligence | ⭐ 7/10 | agent |
| 多智能体与协作 | 3 | UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems | ⭐ 7/10 | agent, multi-agent |
| 多智能体与协作 | 4 | EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation | ⭐ 7/10 | agent |
| 多智能体与协作 | 5 | Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs | ⭐ 7/10 | agent, GUI agent, multi-agent |
| 多智能体与协作 | 6 | QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents | ⭐ 7/10 | agent |
| 多智能体与协作 | 7 | ATOM: Instantiating Budget-Controllable Multi-Agent Collaboration via Nucleus-Electron Hierarchy | ⭐ 6/10 | agent, multi-agent |
| 多智能体与协作 | 8 | Cost of Structural Learning Under Censored Feedback: A Threshold-Bandit Approach | ⭐ 6/10 | multi-agent, collaboration |
| LLM训练与对齐 | 1 | Pretraining Data Exposure in Large Language Models: A Survey of Membership Inference, Data Contamination, and Security Implications | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 2 | Anchor: Mitigating Artifact Drift in Agent Benchmark Generation | ⭐ 7/10 | agent, benchmark |
| LLM训练与对齐 | 3 | On the Hidden Costs of Counterfactual Knowledge Training in LLM Unlearning | ⭐ 6/10 | alignment, training |
| LLM训练与对齐 | 4 | LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring | ⭐ 6/10 | alignment, training |
| 评测与安全 | 1 | PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions | ⭐ 9/10 | benchmark, evaluation |
| 评测与安全 | 2 | MemFail: Stress-Testing Failure Modes of LLM Memory Systems | ⭐ 8/10 | memory |
| 评测与安全 | 3 | MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning | ⭐ 7/10 | agent, tool use, memory, poisoning |
| 评测与安全 | 4 | RepoMirage: Probing Repository Context Reasoning in Code Agents with Perturbations | ⭐ 7/10 | agent, RAG, reasoning, coding |
| 评测与安全 | 5 | Sentinel: Embodied Cooperative Spatial Reasoning and Planning | ⭐ 7/10 | reasoning |
| 评测与安全 | 6 | OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling | ⭐ 7/10 | benchmark |
| 评测与安全 | 7 | Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study | ⭐ 7/10 | memory, benchmark |
| 评测与安全 | 8 | Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization | ⭐ 7/10 | agent |
| 评测与安全 | 9 | OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time Omnimodal Assistants | ⭐ 7/10 | benchmark |
| 评测与安全 | 10 | Cordyceps: Covert Control Attacks on LLMs via Data Poisoning | ⭐ 7/10 | poisoning |
| 评测与安全 | 11 | Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study | ⭐ 7/10 | agent |
| 评测与安全 | 12 | Neuro-Symbolic Verification of LLM Outputs for Data-Sensitive Domains (extended preprint) | ⭐ 7/10 | evaluation, safety, reliability |
| 评测与安全 | 13 | KZ-SafetyPrompts: A Kazakh Safety Evaluation Prompt Dataset for Large Language Models | ⭐ 7/10 | evaluation, safety |
| 评测与安全 | 14 | Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement | ⭐ 7/10 | agent |
| 评测与安全 | 15 | AlbanianLLMSafety: A Safety Evaluation Dataset for Large Language Models in Albanian | ⭐ 7/10 | evaluation, safety |
| 评测与安全 | 16 | JuICE: A Benchmark for Evaluating LLM-Judge in Identifying Cultural Errors | ⭐ 7/10 | benchmark |
| 评测与安全 | 17 | ReasonOps: A Unified Operational Paradigm for Trustworthy Verified LLM Reasoning | ⭐ 7/10 | reasoning |
| 评测与安全 | 18 | Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis | ⭐ 7/10 | evaluation, safety, reliability |
| 评测与安全 | 19 | GraphReview: Scientific Paper Evaluation via LLM-Based Graph Message Passing | ⭐ 7/10 | evaluation |
| 评测与安全 | 20 | Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations | ⭐ 6/10 | reasoning |
| 评测与安全 | 21 | Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization | ⭐ 6/10 | evaluation, safety, reliability |
| 评测与安全 | 22 | It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers | ⭐ 6/10 | agent |
| 评测与安全 | 23 | Traceable Knowledge Graph Reasoning Enables LLM-Assisted Decision Support for Industrial VOCs in the Steel Industry | ⭐ 6/10 | reasoning |
| 评测与安全 | 24 | FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents | ⭐ 6/10 | agent, safety |
| 应用与基准 | 1 | VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions | ⭐ 8/10 | agent, proactive assistant |
| 应用与基准 | 2 | VISTA: An End-to-End Benchmark for Visual Spec-to-Web-App Coding Agents | ⭐ 7/10 | agent, benchmark |
| 应用与基准 | 3 | JobBench: Aligning Agent Work With Human Will | ⭐ 7/10 | agent |
| 其他 Agent / LLM 方向 | 1 | Pop-Up Distractions Reveal Bag-of-Events Behavior in Video Large Language Models | ⭐ 7/10 | Agent, LLM |
| 应用与基准 | 4 | Scaling, Benchmarking, and Reasoning of Vision-Language Agents for Mobile GUI Navigation | ⭐ 7/10 | agent, benchmark, reasoning, GUI agent |
| 其他 Agent / LLM 方向 | 2 | Probing Cultural Awareness in LLMs: A Case Study of Cross-Culture Aesthetic Stylistics | ⭐ 6/10 | Agent, LLM |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation

- **评分**：8/10
- **作者/机构**：作者：Xiaochong Jiang、Shiqi Yang、Ziwei Li、Lifei Liu、Haoran Yu、Yichen Liu
- **论文链接**：https://arxiv.org/abs/2605.26542
- **PDF**：https://arxiv.org/pdf/2605.26542
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
ChainCaps 从 capability attenuation 角度约束 tool-using agents，目标是在组合工具时保持能力边界单调、可控。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
对 tool-use agent 安全、权限边界和能力组合有直接参考价值。

</span>

---


### [2] MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

- **评分**：8/10
- **作者/机构**：作者：Huawei Lin、Peng Li、Jie Song、Fuxin Jiang、Tieying Zhang
- **论文链接**：https://arxiv.org/abs/2605.27366
- **PDF**：https://arxiv.org/pdf/2605.27366
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Large language model (LLM) agents rely on reusable skills to solve complex tasks. However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability, reliability, and long-term improvement.

**☠️ 毒舌点评**  
MUSE-Autoskill 把 skill creation、skill memory、unit-test evaluation 和 refinement 放进同一个 agent 生命周期，是今天最像“可演化 Agent 基础设施”的系统稿。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合做 agent skills、长期记忆和工具型 agent 平台的人优先精读。

</span>

---


### [3] A Universal Cliff and a Design Fingerprint: Cross-Section Defect Detection Under LLM Orchestration

- **评分**：7/10
- **作者/机构**：作者：Hiroki Fukui
- **论文链接**：https://arxiv.org/abs/2605.26174
- **PDF**：https://arxiv.org/pdf/2605.26174
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“A Universal Cliff and a Design Fingerprint: Cross-Section Defect Detection Under LLM Orchestration”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：Production language-model systems increasingly answer a single request by par- titioning it across an invisible orchestration of worker agents and recomposing one integrated report. We ask what such orchestration does to a class of defect that no single worker is positioned to see: a contradiction that lives in the relation be- tween two distant sections of a document.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“A Universal Cliff and a Design Fingerprint: Cross-Section Defect Detection Under LLM Orchestration”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [4] SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?

- **评分**：7/10
- **作者/机构**：作者：Zihang Zhou、Ziqian Ren、Yukai Wu、Yingjie Xiong、Wei Zhou、Chao Peng、Dong Zhang、Bingheng Yan、Xuanhe Zhou、Fan Wu
- **论文链接**：https://arxiv.org/abs/2605.26186
- **PDF**：https://arxiv.org/pdf/2605.26186
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Functionality-correct repository setup aims to configure execution environments (e.g., dependencies, build scripts) to successfully execute a repository’s documented features. It presents significant challenges due to diverse, repository-specific fail- ures, including dependency incompatibilities, missing toolchains, incomplete instal- lations, and verification-strategy mismatches.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [5] CyberEvolver: Structured Self-Evolution for Cybersecurity Agents On the Fly

- **评分**：7/10
- **作者/机构**：作者：Yihe Fan、Changyi Li、Lichen Xu、Xudong Pan、Jiarun Dai、Hong Geng、Min Yang
- **论文链接**：https://arxiv.org/abs/2605.26195
- **PDF**：https://arxiv.org/pdf/2605.26195
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“CyberEvolver: Structured Self-Evolution for Cybersecurity Agents On the Fly”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：LLM-based agents are increasingly used for cybersecurity tasks, but most existing systems rely on fixed, human-designed scaffolds that struggle to adapt across di- verse targets and failure modes. We introduce C YBER E VOLVER, a self-evolving cybersecurity agent framework that iteratively revises its own scaffold based on experience from failed execution attempts.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“CyberEvolver: Structured Self-Evolution for Cybersecurity Agents On the Fly”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [6] Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory

- **评分**：7/10
- **作者/机构**：作者：Abdelghny Orogat、Essam Mansour
- **论文链接**：https://arxiv.org/abs/2605.26252
- **PDF**：https://arxiv.org/pdf/2605.26252
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：T0 (Week 0) T1 (Week 1) T2 (Week 2) Long-running AI agents need persistent memory. Memory supports T0: 1:30 PM T0: 1:30 PM Project: Website Redesign | Project: Website Redesign | learning across sessions, reduces repeated context injection, and Deadline: March 15 Deadline: March 15 ...

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [7] Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions

- **评分**：7/10
- **作者/机构**：作者：Jeongeun Lee、Chanyoung Park、Dongha Lee
- **论文链接**：https://arxiv.org/abs/2605.26256
- **PDF**：https://arxiv.org/pdf/2605.26256
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：Multimodal large language model (MLLM)-based embodied agents have shown strong potential for solving complex tasks in physical environments. However, personalized assistance requires more than following generic instructions or rec- ognizing object at the category level.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Personalizing Embodied Multimodal Large Language Model Agents over Long-term User Interactions”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [8] SPEAR: Code-Augmented Agentic Prompt Optimization

- **评分**：7/10
- **作者/机构**：作者：Mengyin Lu、Cong Feng、Huimin Han、Guangming Lu、Yu Sun、Xiaonan Ding、Shihui Long、Fengyi Li、Tanvi Motwani
- **论文链接**：https://arxiv.org/abs/2605.26275
- **PDF**：https://arxiv.org/pdf/2605.26275
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“SPEAR: Code-Augmented Agentic Prompt Optimization”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：et al., 2026) all share one structural trait: the opti- mizer is a fixed pipeline. Its error signal – scalar We port the mizer performs is whatever the pipeline pre-bakes.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“SPEAR: Code-Augmented Agentic Prompt Optimization”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [9] Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems

- **评分**：7/10
- **作者/机构**：作者：Jianing Zhu、Yeonju Ro、John Robertson、Kevin Wang、Junbo Li、Haris Vikalo、Aditya Akella、Zhangyang Wang
- **论文链接**：https://arxiv.org/abs/2605.26302
- **PDF**：https://arxiv.org/pdf/2605.26302
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [10] Experiments in Agentic AI for Science

- **评分**：7/10
- **作者/机构**：作者：Judy Fox、Geoffrey Fox
- **论文链接**：https://arxiv.org/abs/2605.26305
- **PDF**：https://arxiv.org/pdf/2605.26305
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Experiments in Agentic AI for Science”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Experiments in Agentic AI for Science”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [11] Foundations of a Time-Consistent Counterfactual Actuarial Runtime for Autonomous AI Agents

- **评分**：7/10
- **作者/机构**：作者：Hao-Hsuan Chen
- **论文链接**：https://arxiv.org/abs/2605.26508
- **PDF**：https://arxiv.org/pdf/2605.26508
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Foundations of a Time-Consistent Counterfactual Actuarial Runtime for Autonomous AI Agents”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Foundations of a Time-Consistent Counterfactual Actuarial Runtime for Autonomous AI Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [12] MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration

- **评分**：7/10
- **作者/机构**：作者：Runxi Huang、Liyu Zhang、Shengzhong Liu、Xiaomin Ouyang
- **论文链接**：https://arxiv.org/abs/2605.26546
- **PDF**：https://arxiv.org/pdf/2605.26546
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：within a single model [19]. These agents generally adopt Mobile graphical user interface (GUI) agents enable AI mod- two input modalities: text-based, which rely on accessibil- els to autonomously operate smartphones on behalf of users.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [13] Control Physiology: An Agent-Based Model of FAIR-CAM Dynamics

- **评分**：7/10
- **作者/机构**：作者：Jack Jones、Laura Voicu
- **论文链接**：https://arxiv.org/abs/2605.26597
- **PDF**：https://arxiv.org/pdf/2605.26597
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Control Physiology: An Agent-Based Model of FAIR-CAM Dynamics”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：Security risk analysis typically treats control effectiveness as a static input, yet controls degrade through configuration drift, depend on monitoring systems that may themselves be degraded, and compete for finite remediation budgets. The FAIR Controls Analytics Model (FAIR-CAM) provides the theoretical framework for these dynamics, decomposing controls into three interacting domains (Loss Event Controls, Variance Management Controls, and Decision Support Controls) but has so far remained theoretical.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Control Physiology: An Agent-Based Model of FAIR-CAM Dynamics”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [14] Beyond Trajectory-Level Attribution: Graph-Based Credit Assignment for Agentic Reinforcement Learning

- **评分**：7/10
- **作者/机构**：作者：Xin Cheng、Shuo He、Lang Feng、HaiYang Xu、Ming Yan、Lei Feng、Bo An
- **论文链接**：https://arxiv.org/abs/2605.26684
- **PDF**：https://arxiv.org/pdf/2605.26684
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Beyond Trajectory-Level Attribution: Graph-Based Credit Assignment for Agentic Reinforcement Learning”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Beyond Trajectory-Level Attribution: Graph-Based Credit Assignment for Agentic Reinforcement Learning”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [15] Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation

- **评分**：7/10
- **作者/机构**：作者：Yee Hin Chong、Jiaming Wu、Youhui Zhang、Peng Qu
- **论文链接**：https://arxiv.org/abs/2605.26720
- **PDF**：https://arxiv.org/pdf/2605.26720
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [16] Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton

- **评分**：7/10
- **作者/机构**：作者：Viktor Kjellberg、Farnaz Fotrousi、Miroslaw Staron
- **论文链接**：https://arxiv.org/abs/2605.26898
- **PDF**：https://arxiv.org/pdf/2605.26898
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：1 Introduction Large Language Models (LLMs) can generate functional source code Large Language Models (LLMs) have gained acceptance in the soft- We designed Software design patterns are a good example of software engineer- a computational experiment to evaluate the ability of 13 LLMs to ing knowledge that is used in many industries to standardize the generate code that follows the Singleton design pattern, using four implementation of recurring patterns in software [6]. It is a way prompting strategies: instruction

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [17] TADDLE: A Tool-Augmented Agent for Detecting Deficient LLM-Generated Peer Reviews

- **评分**：7/10
- **作者/机构**：作者：Hanqi Duan、Xiang Li
- **论文链接**：https://arxiv.org/abs/2605.26911
- **PDF**：https://arxiv.org/pdf/2605.26911
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“TADDLE: A Tool-Augmented Agent for Detecting Deficient LLM-Generated Peer Reviews”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：ply dual standards under the guise of high academic expectations (Li et al., 2025; Lin et al., 2025). This is orthogonal to quality.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“TADDLE: A Tool-Augmented Agent for Detecting Deficient LLM-Generated Peer Reviews”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [18] Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments

- **评分**：7/10
- **作者/机构**：作者：Yuxin Chen、Xiaodong Cai、Junfeng Fang、Zhuowen Han、Yu Wang、Yaorui Shi、Yi Zhang、Qi Gu、Xunliang Cai、Xiang Wang、An Zhang、Tat-Seng Chua
- **论文链接**：https://arxiv.org/abs/2605.27209
- **PDF**：https://arxiv.org/pdf/2605.27209
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Recent advances in large language models (LLMs) have facilitated the widespread deployment of LLMs as interactive agents capable of reasoning, planning, and tool use. Despite strong performance on existing benchmarks, such agents often exhibit notable degradation when deployed in real-world settings, where environments are inherently stochastic and imperfect.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [19] Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding

- **评分**：7/10
- **作者/机构**：作者：Muhammad Zia Hydari、Raja Iqbal、Narayan Ramasubbu
- **论文链接**：https://arxiv.org/abs/2605.27320
- **PDF**：https://arxiv.org/pdf/2605.27320
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [20] Governed Evolution of Agent Runtimes through Executable Operational Cognition

- **评分**：7/10
- **作者/机构**：作者：Mariano Garralda-Barrio
- **论文链接**：https://arxiv.org/abs/2605.27328
- **PDF**：https://arxiv.org/pdf/2605.27328
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Governed Evolution of Agent Runtimes through Executable Operational Cognition”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：Recent advances in agentic systems increasingly treat code as an executable operational substrate rather than as a disposable output artifact. Prior work such as Code as Agent Harness frames validated agent-generated artifacts as runtime entities that can be created, executed, revised, persisted, and reused within long-running cognitive loops.

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Governed Evolution of Agent Runtimes through Executable Operational Cognition”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [21] Maat: The Agentic Legal Research Assistant for Competition Protection

- **评分**：7/10
- **作者/机构**：作者：Basant Mounir、Farida Madkour、Amira Abdelaziz、Asmaa Sami
- **论文链接**：https://arxiv.org/abs/2605.27331
- **PDF**：https://arxiv.org/pdf/2605.27331
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Maat: The Agentic Legal Research Assistant for Competition Protection”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：and Claude Sonnet [1], and multilingual legal assistants such as We propose Maat, a ReAct agent that orchestrates tools of it focuses on case retrieval or question answering in isolation corresponding to different tasks of the research process. Designed [17, 20, 24, 35, 41], while systems that integrate multiple tasks iteratively with competition law experts, Maat grounds cases and are deficient in fallback mechanisms and multi-turn clarification findings in official sources using RAG for reliability, provides rich

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Maat: The Agentic Legal Research Assistant for Competition Protection”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [22] GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing

- **评分**：7/10
- **作者/机构**：作者：Tamerlan Aghayev、Maxime Elkael、Michele Polese、Minh Dat Nguyen、Gabriele Gemmi、Andrea Lacava、Ali Saeizadeh、Reshma Prasad、Paolo Testolina、Angelo Feraudo、Soumendra Nanda、Pedram Johari、Salvatore D'Oro、Tommaso Melodia
- **论文链接**：https://arxiv.org/abs/2605.27360
- **PDF**：https://arxiv.org/pdf/2605.27360
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing”展开，核心落点是Agent 系统、工具调用与工作流落地。

**☠️ 毒舌点评**  
更像系统论文：看点不只是 prompt，而是 agent 在工具、记忆、执行环境和反馈闭环里的组织方式。需要重点关注是否有真实任务和失败分析。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent 系统、工具调用与工作流落地的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [23] Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets

- **评分**：7/10
- **作者/机构**：作者：Furkan Sakizli
- **论文链接**：https://arxiv.org/abs/2605.26165
- **PDF**：https://arxiv.org/pdf/2605.26165
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：within a single context window. Production deploy- ments routinely expose 20–100+ tools through pro- We present sation history, and output generation.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [24] FAB-Bench: A Framework for Adaptive RAG Benchmarking in Semiconductor Manufacturing

- **评分**：7/10
- **作者/机构**：作者：Jingbin Qian、Congwen Yi、Min Xia、Wen Wu、Jun Zhu、Jian Guan
- **论文链接**：https://arxiv.org/abs/2605.26476
- **PDF**：https://arxiv.org/pdf/2605.26476
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“FAB-Bench: A Framework for Adaptive RAG Benchmarking in Semiconductor Manufacturing”展开，核心落点是RAG、检索链路与知识更新。

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“FAB-Bench: A Framework for Adaptive RAG Benchmarking in Semiconductor Manufacturing”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [25] PolyFusionAgent: A Multimodal Foundation Model and Autonomous AI Assistant for Polymer Property Prediction and Inverse Design

- **评分**：7/10
- **作者/机构**：作者：Manpreet Kaur、Xingying Zhang、Qian Liu
- **论文链接**：https://arxiv.org/abs/2605.26543
- **PDF**：https://arxiv.org/pdf/2605.26543
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“PolyFusionAgent: A Multimodal Foundation Model and Autonomous AI Assistant for Polymer Property Prediction and Inverse Design”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Polymer discovery is central to fields ranging from energy storage to biomedicine, but it is hindered by an astronomically large chemical design space and fragmented representations of structure, properties, and prior knowledge. This fragmentation leaves many AI models dis- connected from physical and experimental reality, restricting their ability to support directly actionable design decisions.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“PolyFusionAgent: A Multimodal Foundation Model and Autonomous AI Assistant for Polymer Property Prediction and Inverse Design”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [26] The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context

- **评分**：7/10
- **作者/机构**：作者：Zhe Yu、Wenpeng Xing、Yunzhao Wei、Bo Yang、Chen Ye、Gaolei Li、Meng Han
- **论文链接**：https://arxiv.org/abs/2605.26778
- **PDF**：https://arxiv.org/pdf/2605.26778
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：operating assumption is straightforward: if a model Retrieval-augmented generation promises to receives a relevant document as context, it will use This as- idence, yet the field has no reliable way to sumption underpins deployed systems in search, verify whether retrieved context actually gov- customer support, and medical QA, where faithful erns generation—a prerequisite for any high- grounding is treated as a safety property. stakes deployment.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [27] GeoFaith: A Spatio-Temporal Dual View of Faithful Chain-of-Thought

- **评分**：7/10
- **作者/机构**：作者：Weijiang Lv、Wentong Zhao、Jiayu Wang、Yuhao Wu、Jiaheng Wei、Xiaobo Xia
- **论文链接**：https://arxiv.org/abs/2605.26893
- **PDF**：https://arxiv.org/pdf/2605.26893
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“GeoFaith: A Spatio-Temporal Dual View of Faithful Chain-of-Thought”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：We propose GeoFaith, a spatio-temporal framework that Figure 1: Latent representation landscape of reason- leverages latent geometric structure and en- ing trajectories. Curves denote CoT paths in the latent tropy dynamics to diagnose and enforce faithful space.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“GeoFaith: A Spatio-Temporal Dual View of Faithful Chain-of-Thought”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [28] From Norms to Indicators (N2I-RAG): An Agentic Retrieval-Augmented Generation Framework for Legal Indicator Computation

- **评分**：7/10
- **作者/机构**：作者：Youssef Al Mouatamid、Marie Bonnin、Jihad Zahir
- **论文链接**：https://arxiv.org/abs/2605.26926
- **PDF**：https://arxiv.org/pdf/2605.26926
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“From Norms to Indicators (N2I-RAG): An Agentic Retrieval-Augmented Generation Framework for Legal Indicator Computation”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Computing legal indicators from normative texts is a key task in legal monitoring and policy evaluation, but presents significant challenges due to the complex- ity, scale, and interpretive nature of legal language, as well as the variability in available document quality. Existing natural language processing techniques and generative models can assist in legal analysis, but often suffer from high risk of hallucinations and lack the interpretability and evidence grounding required for reliable indicator computation

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“From Norms to Indicators (N2I-RAG): An Agentic Retrieval-Augmented Generation Framework for Legal Indicator Computation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [29] Detecting Is Not Resolving: The Monitoring Control Gap in Retrieval Augmented LLMs

- **评分**：7/10
- **作者/机构**：作者：Zhe Yu、Wenpeng Xing、Chen Ye、Xuyang Teng、Bo Yang、Changting Lin、Meng Han
- **论文链接**：https://arxiv.org/abs/2605.27157
- **PDF**：https://arxiv.org/pdf/2605.27157
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Detecting Is Not Resolving: The Monitoring Control Gap in Retrieval Augmented LLMs”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：actions: evidence from earlier retrieval rounds re- mains visible alongside newly retrieved documents, Retrieval-augmented LLMs are deployed for We retrieval set. show this assumption is fundamentally incor- The field implicitly assumes that robustness rect.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Detecting Is Not Resolving: The Monitoring Control Gap in Retrieval Augmented LLMs”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [30] The Coverage Illusion: From Pre-retrieval Routing Failure to Post-retrieval Cascades in a Production RAG System

- **评分**：7/10
- **作者/机构**：作者：Zafar Hussain、Kristoffer Nielbo
- **论文链接**：https://arxiv.org/abs/2605.27220
- **PDF**：https://arxiv.org/pdf/2605.27220
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“The Coverage Illusion: From Pre-retrieval Routing Failure to Post-retrieval Cascades in a Production RAG System”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：cost in compute and latency. Despite this overhead, both are applied uniformly to every query in pro- We study the Danish National Encyclopedia, a for this overhead in real production traffic re- production RAG system serving real users across a mains largely unexplored.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“The Coverage Illusion: From Pre-retrieval Routing Failure to Post-retrieval Cascades in a Production RAG System”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [31] ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents

- **评分**：7/10
- **作者/机构**：作者：Xing Fu、Yulin Hu、Mengtong Ji、Haozhen Li、Yixin Sun、Weixiang Zhao、Yanyan Zhao、Bing Qin
- **论文链接**：https://arxiv.org/abs/2605.27240
- **PDF**：https://arxiv.org/pdf/2605.27240
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Emily, Female, a graphic designer, ... Profile ...

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [32] Beyond Questions: Evaluating What Large Language Models (Actually) Know

- **评分**：6/10
- **作者/机构**：作者：Luca Giordano、Simon Razniewski
- **论文链接**：https://arxiv.org/abs/2605.26937
- **PDF**：https://arxiv.org/pdf/2605.26937
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Beyond Questions: Evaluating What Large Language Models (Actually) Know”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：When was Martin Luther King born? OpenTellKnowledge Evaluation me everything you know Who was Martin Luther King’s spouse?

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Beyond Questions: Evaluating What Large Language Models (Actually) Know”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [33] Intelligent Detection and Mitigation of Carpet-Bombing DDoS Attacks in SDN Using Retrieval-Augmented Generation and Large Language Models

- **评分**：6/10
- **作者/机构**：作者：Mohammed N. Swileh、Shengli Zhang、Kai Lei
- **论文链接**：https://arxiv.org/abs/2605.26307
- **PDF**：https://arxiv.org/pdf/2605.26307
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Intelligent Detection and Mitigation of Carpet-Bombing DDoS Attacks in SDN Using Retrieval-Augmented Generation and Large Language Models”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Software-Defined Networking (SDN) provides flexible and programmable network management; however, its centralized control architecture remains highly vulnerable to Distributed Denial-of-Service (DDoS) attacks, particularly Carpet- Bombing DDoS attacks that distribute malicious traffic across multiple targets to evade conventional detection mechanisms. In this paper, a Retrieval-Augmented Generation (RAG)-based framework is proposed for real-time detection and mitigation of Carpet-Bombing DDoS attacks in SDN environ

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Intelligent Detection and Mitigation of Carpet-Bombing DDoS Attacks in SDN Using Retrieval-Augmented Generation and Large Language Models”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [34] RICE-PO: Turning Retrieval Interactions into Credit Signals for Reasoning Agents

- **评分**：6/10
- **作者/机构**：作者：Mingchen Li、Hansi Zeng、Zhuo Qian、Jiatan Huang、Hamed Zamani、Hong Yu
- **论文链接**：https://arxiv.org/abs/2605.26352
- **PDF**：https://arxiv.org/pdf/2605.26352
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“RICE-PO: Turning Retrieval Interactions into Credit Signals for Reasoning Agents”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Retrieval is increasingly moving from one-shot matching toward interactive rea- soning, where language agents iteratively inspect evidence, reformulate queries, and search again. Training such agents raises a credit-assignment challenge: ex- ecutable actions such as queries or summaries can be directly evaluated by the retriever, while latent reasoning steps are not directly observable and only affect future executable actions.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“RICE-PO: Turning Retrieval Interactions into Credit Signals for Reasoning Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [35] In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective

- **评分**：6/10
- **作者/机构**：作者：Mingchen Li、Jiatan Huang、Chuxu Zhang、Liang Zhao、Hong Yu
- **论文链接**：https://arxiv.org/abs/2605.26356
- **PDF**：https://arxiv.org/pdf/2605.26356
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：In-context learning has recently been linked to implicit gradient descent in linear self-attention models, suggesting that context can induce a forward-pass update. Retrieval-augmented generation (RAG) also relies on context, but retrieved docu- ments are usually treated as static evidence rather than signals for adaptation.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [36] Mind the Tool Failures: Achieving Synergistic Tool Gains for Medical Agents

- **评分**：6/10
- **作者/机构**：作者：Yunhui Gan、Tan Pan、Kaiyu Guo、Limei Han、Weimiao Yu、Guangnan Ye、Chen Jiang、Yuan Cheng
- **论文链接**：https://arxiv.org/abs/2605.26691
- **PDF**：https://arxiv.org/pdf/2605.26691
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Mind the Tool Failures: Achieving Synergistic Tool Gains for Medical Agents”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Medical AI agents increasingly use external tools for diagnosis, treatment rec- ommendation, and evidence retrieval, yet most existing approaches assume that task-appropriate tools are reliable within their intended scope. This assumption is fragile in real clinical settings, where even relevant tools may fail on challenging instances and lead to unsafe downstream decisions.

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Mind the Tool Failures: Achieving Synergistic Tool Gains for Medical Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [37] LitSeg: Narrative-Aware Document Segmentation for Literary RAG

- **评分**：6/10
- **作者/机构**：作者：Ruikang Zhang、Zhanni Chen、Yiqiao Cai、Qi Su
- **论文链接**：https://arxiv.org/abs/2605.27156
- **PDF**：https://arxiv.org/pdf/2605.27156
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“LitSeg: Narrative-Aware Document Segmentation for Literary RAG”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：are segmented into chunks, and then represented and stored in vector databases; 2) retrieval, in Large Language Models (LLMs) by in- a user query; 3) generation, in which an LLM for- corporating external knowledge, particularly mulates a response given the query and retrieved for long-tail domains such as literary works. However, the critical step of document segmen- chunks (Ma et al., 2025).

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“LitSeg: Narrative-Aware Document Segmentation for Literary RAG”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [38] Reasoning, Code, or Both? How Large Language Models Handle Variations in Math Questions

- **评分**：5/10
- **作者/机构**：作者：Matthew Kutakh
- **论文链接**：https://arxiv.org/abs/2605.26414
- **PDF**：https://arxiv.org/pdf/2605.26414
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Reasoning, Code, or Both? How Large Language Models Handle Variations in Math Questions”展开，核心落点是LLM 推理、规划与可解释能力边界。

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕LLM 推理、规划与可解释能力边界构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Reasoning, Code, or Both? How Large Language Models Handle Variations in Math Questions”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注LLM 推理、规划与可解释能力边界的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🤝 多智能体 / 协作


### [39] AutoDFT: A Closed-Loop Multi-Agent Framework for Autonomous DFT Calculations

- **评分**：7/10
- **作者/机构**：作者：Penghui Yang、Zhonghan Zhang、Yue Li、Xinrun Wag、Yanchen Deng、Yuhao Lu、Bijun Tang、Zheng Liu、Bo An
- **论文链接**：https://arxiv.org/abs/2605.26179
- **PDF**：https://arxiv.org/pdf/2605.26179
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“AutoDFT: A Closed-Loop Multi-Agent Framework for Autonomous DFT Calculations”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：Density functional theory (DFT) serves as the basis for computational discovery in materials science and chemistry, yet each calculation demands extensive hu- man effort: adjusting algorithms when convergence stalls, revising plans when unexpected physics emerges, and inserting steps as intermediate results reshape the problem. Existing LLM-based agents automate only the initial planning stage, producing a full execution plan upfront and leaving all subsequent adaptation to hand-crafted rules.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“AutoDFT: A Closed-Loop Multi-Agent Framework for Autonomous DFT Calculations”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [40] AgentSociety: Incentivizing Agentic Social Intelligence

- **评分**：7/10
- **作者/机构**：作者：Aditya Vema Reddy Kesari、Krishna Reddy Kesari
- **论文链接**：https://arxiv.org/abs/2605.26203
- **PDF**：https://arxiv.org/pdf/2605.26203
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“AgentSociety: Incentivizing Agentic Social Intelligence”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：This requires a multi-agent environment where agents can oper- ate autonomously, strategically communicate, behave collaboratively and be driven by economic incentives, much like humans in society. Towards this vision, we propose AgentSociety, a mechanism that enables decentralized agentic collabo- ration grounded in liquid democracy and information diffusion from social choice theory.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“AgentSociety: Incentivizing Agentic Social Intelligence”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [41] UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems

- **评分**：7/10
- **作者/机构**：作者：Yiqun Chen、Wei Yang、Erhan Zhang、Shijie Wang、Qi Liu、Zechun Niu、Bin Zhang、Haitao Li、Rui Li、Lingyong Yan、Jinyuan Feng、Biqing Qi、Xiaochi Wei、Yan Gao、Yi Wu、Yao Hu、Jiaxin Mao
- **论文链接**：https://arxiv.org/abs/2605.26646
- **PDF**：https://arxiv.org/pdf/2605.26646
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：LLM-based multi-agent systems decompose complex tasks into interacting We present UnityMAS-O, a general RL optimization framework for LLM- based multi-agent systems. UnityMAS-O treats a complete multi-agent workflow as the unit of optimization, rather than a single response or a single policy trajectory.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [42] EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation

- **评分**：7/10
- **作者/机构**：作者：Yunbo Long、Haolang Zhao、Lukas Beckenbauer、Liming Xu、Alexandra Brintrup
- **论文链接**：https://arxiv.org/abs/2605.26785
- **PDF**：https://arxiv.org/pdf/2605.26785
- **代码链接**：https://github.com/Yunbo-max/EmoDistill

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：This risk agent interactions, avoiding costly online nego- is amplified in tool-calling agents that take conse- tiation during training. The code is available at quential actions on behalf of users, such as transfer- https://github.com/Yunbo-max/EmoDistill.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [43] Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs

- **评分**：7/10
- **作者/机构**：作者：Yunbo Long、Haolang Zhao、Ge Zheng、Alexandra Brintrup
- **论文链接**：https://arxiv.org/abs/2605.26835
- **PDF**：https://arxiv.org/pdf/2605.26835
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs”展开，核心落点是多智能体协作、博弈与社会智能。

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [44] QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents

- **评分**：7/10
- **作者/机构**：作者：Ye Yuan、Rui Song、Weien Li、Zeyu Li、Haochen Liu、Xiangyu Kong、Changjiang Han、Yonghan Yang、Zichen Zhao、Zixuan Dong、Fuyuan Lyu、Bowei He、Haolun Wu、Jikun Kang、Xue Liu
- **论文链接**：https://arxiv.org/abs/2605.27068
- **PDF**：https://arxiv.org/pdf/2605.27068
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：only useful if it stays grounded: its statements about where it has been, who it has seen, and This coordination, and belief modeling in Large Language Model (LLM) agents. However, shifts the central question beyond static question most environments are scored only by game answering or single-turn instruction following to- outcomes such as win rates and largely re- ward whether an agent can maintain grounding over main to text-only interaction, making it dif- long horizons (Curvo, 2025; Barkur et al., 2025; ficult

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [45] ATOM: Instantiating Budget-Controllable Multi-Agent Collaboration via Nucleus-Electron Hierarchy

- **评分**：6/10
- **作者/机构**：作者：Xinkui Zhao、Sai Liu、Yifan Zhang、Qingyu Ma、Zewen Lin、Naibo Wang、Guanjie Cheng、Chang Liu、Yueshen Xu
- **论文链接**：https://arxiv.org/abs/2605.26178
- **PDF**：https://arxiv.org/pdf/2605.26178
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“ATOM: Instantiating Budget-Controllable Multi-Agent Collaboration via Nucleus-Electron Hierarchy”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：Large Language Model (LLM)-based multi-agent systems rely on optimized col- laboration topologies to balance performance and communication costs. However, current methods struggle with the inherent stability-extensibility trade-off and often misalign computational budgets with query difficulty.

**☠️ 毒舌点评**  
这篇属于可扫读的增量工作：方向相关，但从摘要看贡献边界相对窄，更适合作为专题素材而不是优先精读。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“ATOM: Instantiating Budget-Controllable Multi-Agent Collaboration via Nucleus-Electron Hierarchy”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [46] Cost of Structural Learning Under Censored Feedback: A Threshold-Bandit Approach

- **评分**：6/10
- **作者/机构**：作者：Michael Ledford、William Regli
- **论文链接**：https://arxiv.org/abs/2605.27076
- **PDF**：https://arxiv.org/pdf/2605.27076
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Cost of Structural Learning Under Censored Feedback: A Threshold-Bandit Approach”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：without producing informative feedback, making stochastic failure indistinguishable from insufficient coordination. In many multi-agent applications, tasks yield re- Existing models for cooperative decision making typically wards only when executed by a coalition meeting assume execution feedback is informative whenever agents an unknown size threshold; otherwise, feedback is act, enabling learning through independent or weakly coor- fully censored.

**☠️ 毒舌点评**  
这篇属于可扫读的增量工作：方向相关，但从摘要看贡献边界相对窄，更适合作为专题素材而不是优先精读。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Cost of Structural Learning Under Censored Feedback: A Threshold-Bandit Approach”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注多智能体协作、博弈与社会智能的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [47] Pretraining Data Exposure in Large Language Models: A Survey of Membership Inference, Data Contamination, and Security Implications

- **评分**：7/10
- **作者/机构**：作者：Ziyi Tong、Feifei Sun、Le Minh Nguyen
- **论文链接**：https://arxiv.org/abs/2605.26133
- **PDF**：https://arxiv.org/pdf/2605.26133
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Pretraining Data Exposure in Large Language Models: A Survey of Membership Inference, Data Contamination, and Security Implications”展开，核心落点是训练、偏好优化与对齐数据。 摘要显示，作者主要处理的问题是：. Large Language Models (LLMs) have become the predomi- nant paradigm in NLP, advancing both research and industry.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕训练、偏好优化与对齐数据构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Pretraining Data Exposure in Large Language Models: A Survey of Membership Inference, Data Contamination, and Security Implications”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注训练、偏好优化与对齐数据的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [48] Anchor: Mitigating Artifact Drift in Agent Benchmark Generation

- **评分**：7/10
- **作者/机构**：作者：Maksim Ivanov、Abhijay Rana
- **论文链接**：https://arxiv.org/abs/2605.26321
- **PDF**：https://arxiv.org/pdf/2605.26321
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Anchor: Mitigating Artifact Drift in Agent Benchmark Generation”展开，核心落点是训练、偏好优化与对齐数据。 摘要显示，作者主要处理的问题是：AI agents are beginning to complete valuable, long-horizon busi- ness operations tasks, but training and evaluation environments for enterprise work still struggle to balance realism, verifiability, and scale. Environment and task creation frequently suffers from We introduce Anchor, a task-generation pipeline that for- malizes domain experts’ specifications of business workflows into constraint optimization programs.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕训练、偏好优化与对齐数据构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Anchor: Mitigating Artifact Drift in Agent Benchmark Generation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注训练、偏好优化与对齐数据的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [49] On the Hidden Costs of Counterfactual Knowledge Training in LLM Unlearning

- **评分**：6/10
- **作者/机构**：作者：Xiaotian Ye、Xiaohan Wang、Mengqi Zhang、Shu Wu
- **论文链接**：https://arxiv.org/abs/2605.27083
- **PDF**：https://arxiv.org/pdf/2605.27083
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“On the Hidden Costs of Counterfactual Knowledge Training in LLM Unlearning”展开，核心落点是训练、偏好优化与对齐数据。 摘要显示，作者主要处理的问题是：target knowledge, or training the model to generate an alternative answer. In practice, the first idea Large Language Model as GA (Jang et al., 2022) and NPO (Zhang et al., (LLM) unlearning by training models to gen- erate alternative fictitious knowledge in place 2024b); while the second idea has given rise to (2) of undesired content.

**☠️ 毒舌点评**  
这篇属于可扫读的增量工作：方向相关，但从摘要看贡献边界相对窄，更适合作为专题素材而不是优先精读。

**🔧 技术方案**  
- **模型架构**：围绕训练、偏好优化与对齐数据构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“On the Hidden Costs of Counterfactual Knowledge Training in LLM Unlearning”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注训练、偏好优化与对齐数据的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [50] LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring

- **评分**：6/10
- **作者/机构**：作者：Unggi Lee、Minchul Shin、Yeil Jeong、Sookbun Lee、Jeongsu Moon、Kyungtae Joo、Eunjoo Lee、Hoilym Kwon
- **论文链接**：https://arxiv.org/abs/2605.27088
- **PDF**：https://arxiv.org/pdf/2605.27088
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring”展开，核心落点是训练、偏好优化与对齐数据。 摘要显示，作者主要处理的问题是：0.15 Published We investigate whether training- EvoPrompt free prompt optimization-evolving only the 0.30 MIPROv2 GEPA system prompt via API calls-can serve as a TF-GRPO practical alternative. We adapt 7 published 0.35 CondBridge Frame OPRO methods and propose 5 education-specialized MetaBlend methods, evaluating these 12 methods under 5 0.40 TextGrad conditions on 2 OOD benchmark suites.

**☠️ 毒舌点评**  
这篇属于可扫读的增量工作：方向相关，但从摘要看贡献边界相对窄，更适合作为专题素材而不是优先精读。

**🔧 技术方案**  
- **模型架构**：围绕训练、偏好优化与对齐数据构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注训练、偏好优化与对齐数据的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [51] PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions

- **评分**：9/10
- **作者/机构**：作者：Ruhallah Niazi、Faeze Ghorbanpour、Alexander Fraser
- **论文链接**：https://arxiv.org/abs/2605.27015
- **PDF**：https://arxiv.org/pdf/2605.27015
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Persian is spoken by over 110 million people and has a literary tradition spanning more than a Despite impressive multilingual capabilities, millennium, yet LLM competence in Persian liter- We introduce PersLitEval, a bench- mark of 4,514 Persian literature multiple- tional humanities, and domain-specific NLP tasks choice questions across eight fine-grained cate- (Kalhor and Yaghoobzadeh, 2026; Moosavi Mon- gories spanning spelling, literary devices, gram- azzah et al., 2025), understanding their capabili- mar, voc

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [52] MemFail: Stress-Testing Failure Modes of LLM Memory Systems

- **评分**：8/10
- **作者/机构**：作者：Ishir Garg、Neel Kolhe、Dawn Song、Xuandong Zhao
- **论文链接**：https://arxiv.org/abs/2605.26667
- **PDF**：https://arxiv.org/pdf/2605.26667
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“MemFail: Stress-Testing Failure Modes of LLM Memory Systems”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：A growing body of work on LLM memory sys- tems has emerged in response, augmenting agents Large language model (LLM) agents increas- with external stores they can read, write, and update ingly rely on external memory systems to re- over a lifetime, enabling consistent and personal- main consistent across long-horizon interac- ized responses (Chhikara et al., 2025; Xu et al., tions, but little empirical work has been done 2025; Liu et al., 2026; Xu et al., 2026; Rasmussen to understand the specific failure modes and

**☠️ 毒舌点评**  
MemFail 专门压力测试 LLM memory system 的失败模式，切中长期 agent 最容易被忽视的可靠性问题。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“MemFail: Stress-Testing Failure Modes of LLM Memory Systems”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注 agent memory、可靠性评测和上线风险的人重点看。

</span>

---


### [53] MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning

- **评分**：7/10
- **作者/机构**：作者：Xuanye Zhang、Yongsen Zheng、Zhuqin Xu、Kaiyu Zhou、Bowen Shen、Haoran Ou、Tianwei Zhang、Kwok-Yan Lam
- **论文链接**：https://arxiv.org/abs/2605.26154
- **PDF**：https://arxiv.org/pdf/2605.26154
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：identify tool selection as a key bottleneck for agent reliability, especially in safety-critical workflows: This paper proposes MemMorph, the tool invocations proceed without immediate human first attack that bias tool selection by poisoning the agent’s long-term memory. Rather than ex- review.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [54] RepoMirage: Probing Repository Context Reasoning in Code Agents with Perturbations

- **评分**：7/10
- **作者/机构**：作者：Hanyu Li、Yichi Zhang、Speed Zhu、Hang Su、Jun Zhu、Yinpeng Dong
- **论文链接**：https://arxiv.org/abs/2605.26177
- **PDF**：https://arxiv.org/pdf/2605.26177
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“RepoMirage: Probing Repository Context Reasoning in Code Agents with Perturbations”展开，核心落点是RAG、检索链路与知识更新。 摘要显示，作者主要处理的问题是：Code agents are currently having skillful performance on repository-level software engineering benchmarks, but it remains unclear whether success on end-to-end tasks such as issue resolution truly reflects repository context reasoning, the ability to identify the task-relevant information across multiple files and reason over the relations among them. To investigate this question, we introduce R EPO M IRAGE, a two-stage evaluation suite built on SWE-Bench Verified that adopts perturbation as a diagnostic tool to in

**☠️ 毒舌点评**  
它抓住了 RAG 系统里检索、记忆、知识更新或 grounding 的真实瓶颈；如果实验来自真实系统，参考价值会明显高于单纯刷榜。

**🔧 技术方案**  
- **模型架构**：围绕RAG、检索链路与知识更新构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“RepoMirage: Probing Repository Context Reasoning in Code Agents with Perturbations”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注RAG、检索链路与知识更新的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [55] Sentinel: Embodied Cooperative Spatial Reasoning and Planning

- **评分**：7/10
- **作者/机构**：作者：Xiangye Lin、Hongxin Zhang、Ruxi Deng、Qinhong Zhou、Chuang Gan
- **论文链接**：https://arxiv.org/abs/2605.26239
- **PDF**：https://arxiv.org/pdf/2605.26239
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Sentinel: Embodied Cooperative Spatial Reasoning and Planning”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：. In this work, we study Cooperative Spatial Intelligence, the ability of decentralized embodied agents to coordinate effectively under dynamic environmental constraints across city-scale outdoor domains.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Sentinel: Embodied Cooperative Spatial Reasoning and Planning”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [56] OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling

- **评分**：7/10
- **作者/机构**：作者：Adam Bawatneh、Sagar Sapkota、Amrit Singh Bedi、Santu Karmaker、Mubarak Shah
- **论文链接**：https://arxiv.org/abs/2605.26322
- **PDF**：https://arxiv.org/pdf/2605.26322
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Theory of Mind (ToM), the ability to infer others’ knowledge, intentions, and emotions, is commonly evaluated in large language models (LLMs) using end- point question answering, where performance is judged solely by the final answer to a social reasoning query. This paradigm obscures whether the model actually constructs the underlying mental-state representations required for robust reason- ing, particularly in scenarios involving divergent, evolving, or mistaken beliefs.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [57] Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study

- **评分**：7/10
- **作者/机构**：作者：Ravi Kumar Tummalapenta、Suman Addanki
- **论文链接**：https://arxiv.org/abs/2605.26394
- **PDF**：https://arxiv.org/pdf/2605.26394
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：with GPT reasoning models, which reason by de- fault. We introduce the Memory Benefit Score Multi-turn Text-to-SQL—where analysts refine (MBS) as a per-turn diagnostic metric normalized structured database queries across conversational against the stateless baseline.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark and Empirical Study”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [58] Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization

- **评分**：7/10
- **作者/机构**：作者：Anmol Agarwal、Natalie Neamtu、Pranjal Aggarwal、Seungone Kim、Jannis Limperg、Cedric Flamant、Kanna Shimizu、Bryan Parno、Sean Welleck
- **论文链接**：https://arxiv.org/abs/2605.26457
- **PDF**：https://arxiv.org/pdf/2605.26457
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：AI coding agents are increasingly used to write real-world software, but ensuring that their outputs are correct remains a fundamental challenge. Formal verification offers a promising path: an agent generates code together with a machine-checked proof, guaranteeing that the code satisfies a formal specification.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [59] OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time Omnimodal Assistants

- **评分**：7/10
- **作者/机构**：作者：Xudong Lu、Xueying Li、Annan Wang、Yang Bo、Jinpeng Chen、Zengliang Li、Nianzu Yang、Rui Liu、Xue Yang、Jingwen Hou、Hongsheng Li
- **论文链接**：https://arxiv.org/abs/2605.26485
- **PDF**：https://arxiv.org/pdf/2605.26485
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time Omnimodal Assistants”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：et al., 2024; Wu et al., 2024), while recent stream- ing video benchmarks move closer to online per- We introduce OmniInteract, a streaming bench- ception (Lin et al., 2026b; Niu et al., 2025; Lu mark for real-time omnimodal large language models evaluated through native online infer- et al., 2026b). Meanwhile, omnimodal large lan- ence over audio-visual streams.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time Omnimodal Assistants”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [60] Cordyceps: Covert Control Attacks on LLMs via Data Poisoning

- **评分**：7/10
- **作者/机构**：作者：Zedian Shao、Charles Fleming、Teodora Baluta
- **论文链接**：https://arxiv.org/abs/2605.26595
- **PDF**：https://arxiv.org/pdf/2605.26595
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Cordyceps: Covert Control Attacks on LLMs via Data Poisoning”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：both attack accuracy and stealth [37, 45]. For instance, trigger phrases with rare tokens can be detected by perplexity and Large language models (LLMs) are often fine-tuned on un- outlier defenses [38, 66].

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Cordyceps: Covert Control Attacks on LLMs via Data Poisoning”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [61] Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study

- **评分**：7/10
- **作者/机构**：作者：Anas H. Alzahrani
- **论文链接**：https://arxiv.org/abs/2605.26870
- **PDF**：https://arxiv.org/pdf/2605.26870
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Background: Large language model systems are commonly evaluated as models, benchmarks, or short conversational episodes. Less is known about what happens when a persistent AI agent is embedded into a real academic research environment with durable memory, local files, external tools, scheduled routines, delegated roles, and explicit safety protocols.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Persistent AI Agents in Academic Research: A Single-Investigator Implementation Case Study”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [62] Neuro-Symbolic Verification of LLM Outputs for Data-Sensitive Domains (extended preprint)

- **评分**：7/10
- **作者/机构**：作者：Paul Sigloch、Christoph Benzmüller
- **论文链接**：https://arxiv.org/abs/2605.26942
- **PDF**：https://arxiv.org/pdf/2605.26942
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Neuro-Symbolic Verification of LLM Outputs for Data-Sensitive Domains (extended preprint)”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：. LLMs deployed in high-stakes domains face fundamental reliability challenges: hallucinations, inconsistencies, and privacy vulnera- bilities introduce unacceptable risks where errors carry legal, financial, or safety consequences.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Neuro-Symbolic Verification of LLM Outputs for Data-Sensitive Domains (extended preprint)”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [63] KZ-SafetyPrompts: A Kazakh Safety Evaluation Prompt Dataset for Large Language Models

- **评分**：7/10
- **作者/机构**：作者：Wajdi Zaghouani、Shimaa Amer Ibrahim、Aruzhan Muratbek、Olzhasbek Zhakenov、Adiya Akhmetzhanova
- **论文链接**：https://arxiv.org/abs/2605.26947
- **PDF**：https://arxiv.org/pdf/2605.26947
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“KZ-SafetyPrompts: A Kazakh Safety Evaluation Prompt Dataset for Large Language Models”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Kazakh is underrepresented in resources for evaluating the safety behavior of large language models. We present KZ-SafetyPrompts, a Kazakh prompt dataset for safety evaluation across eleven categories covering common risk areas such as self-harm, violence, child exploitation, sexual content, racist content, radicalization, and regulated goods or illegal activities.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“KZ-SafetyPrompts: A Kazakh Safety Evaluation Prompt Dataset for Large Language Models”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [64] Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement

- **评分**：7/10
- **作者/机构**：作者：Dingwei Chen、Zefang Zong、Zhipeng Ma、Leo Luo、Yang Li、Chengming Li、Peng Chen、Jie Jiang
- **论文链接**：https://arxiv.org/abs/2605.26952
- **PDF**：https://arxiv.org/pdf/2605.26952
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：3.5 (Step 20 Step 240) (Step 20 Step 240) Step 20 Step 240 Original Redundancy Hallucination 3.0 2.76 100 Agentic reinforcement learning (RL) has We define the knowledge boundary as the per- instance determination of whether tools are re- quired and the minimum tool calls necessary. 2023; Si et al., 2026; Luo et al., 2026).

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [65] AlbanianLLMSafety: A Safety Evaluation Dataset for Large Language Models in Albanian

- **评分**：7/10
- **作者/机构**：作者：Wajdi Zaghouani、Kholoud K. Aldous、Isra Fejzullaj
- **论文链接**：https://arxiv.org/abs/2605.26954
- **PDF**：https://arxiv.org/pdf/2605.26954
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“AlbanianLLMSafety: A Safety Evaluation Dataset for Large Language Models in Albanian”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Safety evaluation of Large Language Models (LLMs) has largely focused on high-resource languages, leaving low-resource languages critically underserved. We present AlbanianLLMSafety, the first publicly available safety evaluation dataset for LLMs in Albanian, a linguistically distinct low-resource language with approximately 7.5 million speakers across Albania, Kosovo, North Macedonia, and the diaspora.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“AlbanianLLMSafety: A Safety Evaluation Dataset for Large Language Models in Albanian”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [66] JuICE: A Benchmark for Evaluating LLM-Judge in Identifying Cultural Errors

- **评分**：7/10
- **作者/机构**：作者：Jiho Jin、Junho Myung、Juhyun Oh、Junyeong Park、Rifki Afina Putri、Sunipa Dev、Vinodkumar Prabhakaran、Alice Oh
- **论文链接**：https://arxiv.org/abs/2605.26955
- **PDF**：https://arxiv.org/pdf/2605.26955
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“JuICE: A Benchmark for Evaluating LLM-Judge in Identifying Cultural Errors”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：As large language models (LLMs) are increasingly deployed to users around the world, they are integrated into everyday tasks across diverse cultural contexts, from drafting personal communications to brainstorming creative ideas. These tasks are inherently cultural: they require contextual appropriateness, symbolic resonance, and tacit cultural expectations that native speakers draw on instinctively, meaning that a response can be factually plausible yet unmistakably wrong to a local reader.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“JuICE: A Benchmark for Evaluating LLM-Judge in Identifying Cultural Errors”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [67] ReasonOps: A Unified Operational Paradigm for Trustworthy Verified LLM Reasoning

- **评分**：7/10
- **作者/机构**：作者：Adnan Rashid
- **论文链接**：https://arxiv.org/abs/2605.27014
- **PDF**：https://arxiv.org/pdf/2605.27014
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“ReasonOps: A Unified Operational Paradigm for Trustworthy Verified LLM Reasoning”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：[7, 8]. At the same time, the broader trustworthy AI community Large Language Models (LLMs) have transformed artificial intelli- has emphasized that high benchmark performance alone cannot This distinction be- This paper introduces ReasonOps, a unified operational paradigm tween linguistic plausibility and symbolic correctness has emerged for trustworthy verified reasoning systems.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“ReasonOps: A Unified Operational Paradigm for Trustworthy Verified LLM Reasoning”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [68] Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis

- **评分**：7/10
- **作者/机构**：作者：Shuzhi Gong、Hechuan Wen
- **论文链接**：https://arxiv.org/abs/2605.26655
- **PDF**：https://arxiv.org/pdf/2605.26655
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：2026). Instead of updating model weights, re- cent frameworks such as TextGrad (Yuksekgonul We find that complexity- form well on logical or sequential reasoning tasks increasing and meta-instructional edits are neg- may substantially degrade performance on math- atively associated with mathematical and multi- ematical or multi-hop reasoning benchmarks.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [69] GraphReview: Scientific Paper Evaluation via LLM-Based Graph Message Passing

- **评分**：7/10
- **作者/机构**：作者：Pujun Zheng、Wanying Ren、Jiacheng Yao、Guoxiu He、Star X. Zhao
- **论文链接**：https://arxiv.org/abs/2605.27204
- **PDF**：https://arxiv.org/pdf/2605.27204
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“GraphReview: Scientific Paper Evaluation via LLM-Based Graph Message Passing”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Scientific paper evaluation often involves not We Papers propose GraphReview, a graph-based LLM Node Edge Prior Propagation framework that formulates paper evaluation as review-signal message passing over a seman- T-2 T-1 T GraphReview tic paper graph. The graph jointly captures intrinsic quality, synchronic links among con- Figure 1: Previous LLM-based methods consider infor- temporaneous papers, and diachronic links to mation sources in isolation (top), whereas GraphReview prior work.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“GraphReview: Scientific Paper Evaluation via LLM-Based Graph Message Passing”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [70] Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations

- **评分**：6/10
- **作者/机构**：作者：Shanghao Li、Jinda Han、Yibo Wang、Yuanjie Zhu、Zihe Song、Langzhou He、Kenan Kamel A Alghythee、Philip S. Yu
- **论文链接**：https://arxiv.org/abs/2605.26362
- **PDF**：https://arxiv.org/pdf/2605.26362
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Despite sufficient and accurate knowledge pro- vided in the input, LLMs frequently produce hal- We investigate these mechanisms and find that standing the underlying mechanistic drivers: what hallucinations arise from systematic internal causes models to underutilize explicit structured dynamics rather than random noise. First, at- tention disproportionately concentrates toward knowledge already present in their input, leading shortcut-like structural cues rather than dis- to hallucinated responses?

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [71] Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization

- **评分**：6/10
- **作者/机构**：作者：Weixin Liu、Bowen Qu、Juming Xiong、Congning Ni、Bradley A. Malin、Zhijun Yin
- **论文链接**：https://arxiv.org/abs/2605.26433
- **PDF**：https://arxiv.org/pdf/2605.26433
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：trieval, monitoring, auditing, or analytics (Lewis et al., 2020; Karpukhin et al., 2020; Wang et al., Large language model (LLM) summarization 2021; Douze et al., 2024; Zeng et al., 2024). This systems may pass compact vector represen- creates a general information-disclosure question: tations of private inputs to downstream re- trieval, monitoring, audit, or analytic work- even when the raw texts used for summarization flows.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [72] It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers

- **评分**：6/10
- **作者/机构**：作者：Yong-eun Cho
- **论文链接**：https://arxiv.org/abs/2605.26731
- **PDF**：https://arxiv.org/pdf/2605.26731
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：allowed operations, output format, and verification A prevalent assumption in LLM agent de- procedure—is widely believed to be a primary lever We test this hypothesis through a controlled 432-run experiment crossing six models across strict, highly-structured harnesses to all models in four capability tiers with three harness con- a deployment fleet under two implicit assumptions: ditions (light, balanced, strict) on HEAT-24, that more structure always improves reliability, and a 24-task synthetic benchmark with gi

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [73] Traceable Knowledge Graph Reasoning Enables LLM-Assisted Decision Support for Industrial VOCs in the Steel Industry

- **评分**：6/10
- **作者/机构**：作者：Changqing Su、Yu Ding、Zuhong Lin、Hongyu Liu、Xi He、Zheng Zeng、Liqing Li
- **论文链接**：https://arxiv.org/abs/2605.27071
- **PDF**：https://arxiv.org/pdf/2605.27071
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Traceable Knowledge Graph Reasoning Enables LLM-Assisted Decision Support for Industrial VOCs in the Steel Industry”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Key knowledge for steel-industry volatile organic compounds (VOCs) governance is scattered across unstructured scientific literature, making it difficult to integrate process, pollutant, and control-technology evidence and increasing the risk of hallucination when general large language models (LLMs) answer low-frequency industrial questions. Here we developed Chat-ISV, a knowledge graph (KG) enhanced multi-agent Q & A system that parses a curated steel-industry VOCs literature corpus, constructs a Neo4j KG with 27

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Traceable Knowledge Graph Reasoning Enables LLM-Assisted Decision Support for Industrial VOCs in the Steel Industry”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [74] FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents

- **评分**：6/10
- **作者/机构**：作者：Haoxuan Jia、Yang Liu、Bin Chong、Yingguang Yang、Yancheng Chen、Jiayu Liang、Qian Li、Hanning Lu、Kefu Xu、Hao Zheng、Chongyang Zhang、Hao Peng、Philip S. Yu
- **论文链接**：https://arxiv.org/abs/2605.27333
- **PDF**：https://arxiv.org/pdf/2605.27333
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Attacker: “… 20M-yuan invoice for ‘Technical Consulting Services’; our business has transformed, as a listed We present F IN H ARNESS, an in- 5×0.12 = 0.60 line safety harness that wraps a finance agent 0.5 end-to-end with three components: a Q UERY M ONITOR that fuses single-turn intent with cross-turn drift, a T OOL M ONITOR that evalu- 0.0 ates each prospective tool call, and a C ASCADE t=1 t=2 t=3 t=4 t=5 module that integrates per-step risk and adap- verify check verify calc escalate tively routes verification

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🧪 应用 / Benchmark


### [75] VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions

- **评分**：8/10
- **作者/机构**：作者：Yuxin Chen、Yi Zhang、Zhengzhou Cai、Yaorui Shi、Zhiyuan Yao、Chenhang Cui、Jingnan Zheng、Yaqi Huo、Xi Su、Qi Gu、Xunliang Cai、Xiang Wang、An Zhang、Tat-Seng Chua
- **论文链接**：https://arxiv.org/abs/2605.27141
- **PDF**：https://arxiv.org/pdf/2605.27141
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：Large language models (LLMs) have evolved into interactive agents that collaborate with users in real-world tasks. Effective collaboration in such settings increasingly depends on understanding the user beyond what is explicitly stated, as user intent is often reflected in fragmented daily interactions and requires both personalized modeling and proactive interaction.

**☠️ 毒舌点评**  
VitaBench 2.0 把 personalized / proactive assistant 放进长期用户交互序列，重点评估偏好抽取、偏好更新和主动补问，而不是只看单轮工具调用。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
如果你在做个人助理、长期记忆或 proactive agent，这篇 benchmark 很值得跟。

</span>

---


### [76] VISTA: An End-to-End Benchmark for Visual Spec-to-Web-App Coding Agents

- **评分**：7/10
- **作者/机构**：作者：JunJia Guo、Yuhang Yao、Jiawei、Zhou、Jingdi Chen
- **论文链接**：https://arxiv.org/abs/2605.26144
- **PDF**：https://arxiv.org/pdf/2605.26144
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“VISTA: An End-to-End Benchmark for Visual Spec-to-Web-App Coding Agents”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：We present VISTA (VIsual Spec-To-App Benchmark), a benchmark for evaluating the end-to-end web-app generation capabilities of LLM-based agents. Unlike prior code generation benchmarks that focus on algorithmic tasks, VISTA targets realistic UI-centric development, where agents must produce functional, visually coherent applications from underspecified inputs.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“VISTA: An End-to-End Benchmark for Visual Spec-to-Web-App Coding Agents”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [77] JobBench: Aligning Agent Work With Human Will

- **评分**：7/10
- **作者/机构**：作者：Yuetai Li、Yichen Feng、Zhangchen Xu、Zixian Ma、Kaiyuan Zheng、Fengqing Jiang、Xinghua Sun、Rulin Shao、Zichen Chen、Yue Huang、Xinyang Han、Brian Lee、Kayla Xu、Shenglai Zeng、Hang Hua、Xiangliang Zhang、Basel Alomair、Ranjay Krishna、Luke Zettlemoyer、Pang Wei Koh、Bhaskar Ramasubramanian、Luyao Niu、Xiang Yue、Radha Poovendran
- **论文链接**：https://arxiv.org/abs/2605.26329
- **PDF**：https://arxiv.org/pdf/2605.26329
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“JobBench: Aligning Agent Work With Human Will”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Current benchmarks for occupational AI agents are scoped primarily by economic values, telling a replacement story. We introduce JobBench, which evaluates AI agents on the workflows that experts identify as high-priority for delegation, empowering humans based on their needs instead of replacing them with GDP value.

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“JobBench: Aligning Agent Work With Human Will”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🔎 其他 Agent / LLM 方向


### [78] Pop-Up Distractions Reveal Bag-of-Events Behavior in Video Large Language Models

- **评分**：7/10
- **作者/机构**：作者：Oscar Chew、Serhii Honcharenko、Qian-Hui Chen、Patricia Lu、Dishant Zaveri、Khoa D. Doan、Kuan-Hao Huang
- **论文链接**：https://arxiv.org/abs/2605.27101
- **PDF**：https://arxiv.org/pdf/2605.27101
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Pop-Up Distractions Reveal Bag-of-Events Behavior in Video Large Language Models”展开，核心落点是Agent / LLM 相关问题。 摘要显示，作者主要处理的问题是：A key capability for video understanding is re- Large Language Models (VideoLLMs) actually achieve this remains un- clear. In this work, we introduce D ISTRAC - TION B ENCH to evaluate whether VideoLLMs can robustly link subjects and events in the pres- ence of unrelated video segments.

**☠️ 毒舌点评**  
优点是问题贴近当前 Agent/LLM 系统的真实痛点，标题和摘要里能看到比较明确的任务设定与评测意识。

**🔧 技术方案**  
- **模型架构**：围绕Agent / LLM 相关问题构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Pop-Up Distractions Reveal Bag-of-Events Behavior in Video Large Language Models”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent / LLM 相关问题的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🧪 应用 / Benchmark


### [79] Scaling, Benchmarking, and Reasoning of Vision-Language Agents for Mobile GUI Navigation

- **评分**：7/10
- **作者/机构**：作者：Heng Qu、Yike Liu、Renren Jin、Wenzong Zhang、Pengzhi Gao、Wei Liu、Jian Luan
- **论文链接**：https://arxiv.org/abs/2605.27134
- **PDF**：https://arxiv.org/pdf/2605.27134
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Scaling, Benchmarking, and Reasoning of Vision-Language Agents for Mobile GUI Navigation”展开，核心落点是评测、安全、可靠性与攻击面。

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Scaling, Benchmarking, and Reasoning of Vision-Language Agents for Mobile GUI Navigation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 🔎 其他 Agent / LLM 方向


### [80] Probing Cultural Awareness in LLMs: A Case Study of Cross-Culture Aesthetic Stylistics

- **评分**：6/10
- **作者/机构**：作者：Jiashuo Wang、Fenggang Yu、Jian Wang、Chak Tou Leong、Xiaoyu Shen、Chunpu Xu、Jiawen Duan、Wenjie Li、Johan F. Hoorn
- **论文链接**：https://arxiv.org/abs/2605.27296
- **PDF**：https://arxiv.org/pdf/2605.27296
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“Probing Cultural Awareness in LLMs: A Case Study of Cross-Culture Aesthetic Stylistics”展开，核心落点是Agent / LLM 相关问题。 摘要显示，作者主要处理的问题是：Translation of movie title In the Heat of the Night 炎热的夜晚 Large Language Models (LLMs) are increasingly CN (A Hot Night) deployed in diverse cultural contexts, yet their abil- 月黑風高殺人夜 HK ity to master aesthetic stylistics, i.e., the strate- (A Killing Night with High Wind and Dark Moon) gic use of language to evoke cultural resonance, remains underexplored. We curate C 4 S TYLI, a Aesthetic Stylistics example Under benchmark of highly stylized translated movie ti- (Implicit How) Exploration tles and advertising slo

**☠️ 毒舌点评**  
这篇属于可扫读的增量工作：方向相关，但从摘要看贡献边界相对窄，更适合作为专题素材而不是优先精读。

**🔧 技术方案**  
- **模型架构**：围绕Agent / LLM 相关问题构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“Probing Cultural Awareness in LLMs: A Case Study of Cross-Culture Aesthetic Stylistics”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注Agent / LLM 相关问题的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
