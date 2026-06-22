---
title: "Agent/LLM论文速递｜2026-06-19｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-06-19｜全量版：本期收录 122 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-06-19｜全量版：本期收录 122 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-06-19"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-06-19｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **122** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**8** 篇
- LLM 推理 / 规划 / RAG：**57** 篇
- 评测 / 安全 / 对齐：**20** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Benchmarking Agentic Review Systems | ⭐ 9/10 | Agent, benchmark, LLM |
| Agent系统与工具使用 | 2 | Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining | ⭐ 9/10 | Agent, benchmark, LLM |
| Agent系统与工具使用 | 3 | LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents | ⭐ 8/10 | Agent, tool use, LLM |
| Agent系统与工具使用 | 4 | MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments | ⭐ 8/10 | Agent, retrieval, LLM |
| Agent系统与工具使用 | 5 | ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research | ⭐ 8/10 | Agent, retrieval, LLM |
| Agent系统与工具使用 | 6 | Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services | ⭐ 8/10 | Agent, tool use, reasoning |
| Agent系统与工具使用 | 7 | Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes | ⭐ 8/10 | Agent, reasoning, safety |
| Agent系统与工具使用 | 8 | FAPO: Fully Autonomous Prompt Optimization of Multi-Step LLM Pipelines | ⭐ 8/10 | RAG/知识检索, benchmark, reasoning |
| RAG与知识检索 | 1 | PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models | ⭐ 9/10 | RAG/知识检索, LLM, benchmark |
| LLM推理与规划 | 1 | QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation | ⭐ 9/10 | 推理/规划, benchmark, reasoning |
| RAG与知识检索 | 2 | Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software | ⭐ 9/10 | RAG/知识检索, benchmark, LLM |
| LLM推理与规划 | 2 | Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference | ⭐ 8/10 | RAG/知识检索, LLM, benchmark |
| LLM推理与规划 | 3 | How LLMs Fail and Generalize in RTL Coding for Hardware Design? | ⭐ 8/10 | 推理/规划, benchmark, LLM |
| RAG与知识检索 | 3 | Deontic Policies for Runtime Governance of Agentic AI Systems | ⭐ 8/10 | RAG/知识检索, tool use, LLM |
| RAG与知识检索 | 4 | Uncertainty Decomposition for Clarification Seeking in LLM Agents | ⭐ 8/10 | RAG/知识检索, benchmark, LLM |
| LLM推理与规划 | 4 | Analyzing the Narration Gap in LLM-Solver Loops | ⭐ 8/10 | 推理/规划, tool use, reasoning |
| RAG与知识检索 | 5 | NRITYAM: Language Models Meet Art and Heritage of Dance | ⭐ 8/10 | RAG/知识检索, tool use, benchmark |
| RAG与知识检索 | 6 | ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End? | ⭐ 8/10 | RAG/知识检索, benchmark, LLM |
| RAG与知识检索 | 7 | CombEval: A Framework for Evaluating Combinatorial Counting in Large Language Models | ⭐ 8/10 | RAG/知识检索, benchmark, reasoning |
| RAG与知识检索 | 8 | FFinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming | ⭐ 8/10 | RAG/知识检索, benchmark, safety |
| RAG与知识检索 | 9 | AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models | ⭐ 8/10 | RAG/知识检索, LLM, agentic |
| LLM推理与规划 | 5 | Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact | ⭐ 8/10 | 推理/规划, safety, LLM |
| RAG与知识检索 | 10 | ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments | ⭐ 8/10 | RAG/知识检索, benchmark, LLM |
| RAG与知识检索 | 11 | Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe | ⭐ 8/10 | RAG/知识检索, memory, LLM |
| RAG与知识检索 | 12 | Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 13 | Where to Place the Query? Unveiling and Mitigating Positional Bias in In-Context Learning for Diffusion LLMs via Decoding Dynamics | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 14 | Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning | ⭐ 7/10 | RAG/知识检索, reasoning, LLM |
| LLM推理与规划 | 6 | Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees | ⭐ 7/10 | 推理/规划, LLM, benchmark |
| RAG与知识检索 | 15 | Measuring Curriculum Alignment across Topical Coverage, Competency, and Cognitive Depth: A Longitudinal Framework Applied to CS2013 and CS2023 | ⭐ 7/10 | RAG/知识检索, alignment, LLM |
| RAG与知识检索 | 16 | Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix | ⭐ 7/10 | RAG/知识检索, retrieval, LLM |
| RAG与知识检索 | 17 | LLM Doesn't Know What It Doesn't Know: Detecting Epistemic Blind Spots via Cross-Model Attribution Divergence on Clinical Tabular Data | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 18 | Configurable Clinical Information Extraction with Agentic RAG: What Works, What Breaks, and Why | ⭐ 7/10 | RAG/知识检索, agentic, LLM |
| RAG与知识检索 | 19 | AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| LLM推理与规划 | 7 | VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents | ⭐ 7/10 | 推理/规划, planning, LLM |
| LLM推理与规划 | 8 | Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization Across Preference Settings | ⭐ 7/10 | 推理/规划, safety, LLM |
| RAG与知识检索 | 20 | SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling | ⭐ 7/10 | RAG/知识检索, safety, LLM |
| RAG与知识检索 | 21 | Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning | ⭐ 7/10 | RAG/知识检索, reasoning, LLM |
| RAG与知识检索 | 22 | Agentic Electronic Design Automation: A Handoff Perspective | ⭐ 7/10 | RAG/知识检索, tool use, LLM |
| RAG与知识检索 | 23 | AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts | ⭐ 7/10 | RAG/知识检索, memory, LLM |
| LLM推理与规划 | 9 | Measuring Biological Capabilities and Risks of AI Agents | ⭐ 7/10 | 推理/规划, agentic, LLM |
| RAG与知识检索 | 24 | Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning | ⭐ 7/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 25 | StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation | ⭐ 7/10 | RAG/知识检索, memory, LLM |
| LLM推理与规划 | 10 | Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform | ⭐ 7/10 | 推理/规划, LLM, benchmark |
| RAG与知识检索 | 26 | RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning | ⭐ 7/10 | RAG/知识检索, memory, reasoning |
| RAG与知识检索 | 27 | UltraQuant: 4-bit KV Caching for Context-Heavy Agents | ⭐ 7/10 | RAG/知识检索, memory, LLM |
| LLM推理与规划 | 11 | Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems | ⭐ 7/10 | 推理/规划, planning, LLM |
| LLM推理与规划 | 12 | Efficient and Sound Probabilistic Verification for AI Agents | ⭐ 7/10 | 推理/规划, LLM, benchmark |
| RAG与知识检索 | 28 | Human-AI Agent Interaction in a Business Context | ⭐ 6/10 | RAG/知识检索, LLM, benchmark |
| LLM推理与规划 | 13 | Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models | ⭐ 6/10 | 推理/规划, reasoning, LLM |
| RAG与知识检索 | 29 | Quantifying Aleatoric Uncertainty of In-Context Learning for Robust Measure of LLM Prediction Confidence | ⭐ 6/10 | RAG/知识检索, LLM, benchmark |
| LLM推理与规划 | 14 | Interpretable and Verifiable Hardware Generation with LLM-Driven Stepwise Refinement | ⭐ 6/10 | 推理/规划, LLM, benchmark |
| LLM推理与规划 | 15 | Thermodynamic Signatures of Reasoning: Free-Energy and Spectral-Form-Factor Diagnostics for Hallucination Detection in Large Language Models | ⭐ 6/10 | 推理/规划, reasoning, LLM |
| RAG与知识检索 | 30 | Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices | ⭐ 6/10 | RAG/知识检索, memory, LLM |
| LLM推理与规划 | 16 | Where Does Social Reasoning Come From? Capability Provenance in Language Models | ⭐ 6/10 | 推理/规划, reasoning, LLM |
| RAG与知识检索 | 31 | A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots | ⭐ 6/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 32 | LOKI: Memory-Free Null-Space Constrained Lifelong Knowledge Editing | ⭐ 6/10 | RAG/知识检索, memory, LLM |
| RAG与知识检索 | 33 | Efficiently Representing Algorithms With Chain-of-Thought Transformers | ⭐ 6/10 | RAG/知识检索, memory, reasoning |
| RAG与知识检索 | 34 | Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models | ⭐ 6/10 | RAG/知识检索, reasoning, LLM |
| RAG与知识检索 | 35 | When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation | ⭐ 6/10 | RAG/知识检索, tool use, retrieval |
| RAG与知识检索 | 36 | Editorial Alignment: A Participatory Approach to Engaging Editorial Expertise in LLM-mediated Knowledge Dissemination | ⭐ 6/10 | RAG/知识检索, tool use, alignment |
| RAG与知识检索 | 37 | Multi-View Decompilation for LLM-Based Malware Classification | ⭐ 6/10 | RAG/知识检索, tool use, LLM |
| RAG与知识检索 | 38 | CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference | ⭐ 5/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 39 | Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware | ⭐ 5/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 40 | Leverage Is Not Reach: A Control-Window Law for Single-Neuron Steering in Language Models | ⭐ 5/10 | RAG/知识检索, LLM, benchmark |
| RAG与知识检索 | 41 | CATCH-ME if you RAG: a dataset of Contextually Annotated multi-Turn Counterspeech against Hate and Misinformation Exchanges | ⭐ 5/10 | RAG/知识检索, LLM, benchmark |
| 多智能体与协作 | 1 | Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation | ⭐ 8/10 | 多智能体, safety, multi-agent |
| 多智能体与协作 | 2 | Exit-and-Join Dynamics for Decentralized Coalition Formation | ⭐ 8/10 | 多智能体, benchmark, LLM |
| 多智能体与协作 | 3 | A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models | ⭐ 8/10 | 多智能体, benchmark, multi-agent |
| 多智能体与协作 | 4 | Optimal Order of Multi-Agent and General Many-Body Systems | ⭐ 8/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 5 | Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems | ⭐ 8/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 6 | Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol | ⭐ 7/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 7 | DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling | ⭐ 7/10 | 多智能体, tool use, reasoning |
| 多智能体与协作 | 8 | Hidden Anchors in Multi-Agent LLM Deliberation | ⭐ 7/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 9 | AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA | ⭐ 7/10 | 多智能体, reasoning, multi-agent |
| 多智能体与协作 | 10 | Multi-Agent Transactive Memory | ⭐ 7/10 | 多智能体, memory, retrieval |
| 多智能体与协作 | 11 | Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution | ⭐ 7/10 | 多智能体, planning, multi-agent |
| 多智能体与协作 | 12 | Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale | ⭐ 7/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 13 | AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning | ⭐ 7/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 14 | Before the Pull Request: Mining Multi-Agent Coordination | ⭐ 6/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 15 | SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design | ⭐ 6/10 | 多智能体, multi-agent, LLM |
| 多智能体与协作 | 16 | Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs | ⭐ 6/10 | 多智能体, multi-agent, LLM |
| LLM训练与对齐 | 1 | Which Pairs to Compare for LLM Post-Training? | ⭐ 8/10 | 训练/对齐, LLM, benchmark |
| LLM训练与对齐 | 2 | Human-like autonomy emerges from self-play and a pinch of human data | ⭐ 6/10 | 训练/对齐, alignment, LLM |
| LLM训练与对齐 | 3 | Characterizing Narrative Content in Web-scale LLM Pretraining Data | ⭐ 6/10 | 训练/对齐, LLM, benchmark |
| LLM训练与对齐 | 4 | SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation | ⭐ 6/10 | 训练/对齐, LLM, benchmark |
| LLM训练与对齐 | 5 | When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents | ⭐ 6/10 | 训练/对齐, tool use, safety |
| LLM训练与对齐 | 6 | Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families | ⭐ 6/10 | 训练/对齐, alignment, LLM |
| LLM训练与对齐 | 7 | Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users | ⭐ 6/10 | 训练/对齐, alignment, LLM |
| LLM训练与对齐 | 8 | Uncertainty-Aware Reward Modeling for Stable RLHF | ⭐ 5/10 | 训练/对齐, LLM, benchmark |
| 评测与安全 | 1 | Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs | ⭐ 9/10 | 评测/安全, benchmark, LLM |
| 评测与安全 | 2 | LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems | ⭐ 9/10 | 评测/安全, benchmark, safety |
| 评测与安全 | 3 | Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents | ⭐ 8/10 | 评测/安全, benchmark, LLM |
| 评测与安全 | 4 | What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations? | ⭐ 8/10 | RAG/知识检索, safety, LLM |
| 评测与安全 | 5 | DeXposure-Claw: An Agentic System for DeFi Risk Supervision | ⭐ 8/10 | 评测/安全, LLM, agentic |
| 评测与安全 | 6 | Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias | ⭐ 8/10 | 评测/安全, LLM, benchmark |
| 评测与安全 | 7 | IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows | ⭐ 8/10 | 评测/安全, benchmark, LLM |
| 评测与安全 | 8 | StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns | ⭐ 8/10 | 评测/安全, benchmark, LLM |
| 评测与安全 | 9 | BIM-Edit: Benchmarking Large Language Models for IFC-Based Building Information Modeling | ⭐ 8/10 | 评测/安全, benchmark, LLM |
| 评测与安全 | 10 | Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems | ⭐ 8/10 | 评测/安全, tool use, agentic |
| 评测与安全 | 11 | Diffusion Language Models: An Experimental Analysis | ⭐ 7/10 | RAG/知识检索, benchmark, reasoning |
| 评测与安全 | 12 | Reward as An Agent for Embodied World Models | ⭐ 7/10 | 评测/安全, tool use, agentic |
| 其他 Agent / LLM 方向 | 1 | Ensembles of Large Language Models for Identifying EQ-5D Studies in PubMed Based on Their Abstracts | ⭐ 7/10 | 其他方向, tool use, LLM |
| 其他 Agent / LLM 方向 | 2 | Playful Agentic Robot Learning | ⭐ 7/10 | 其他方向, agentic, LLM |
| 其他 Agent / LLM 方向 | 3 | Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence | ⭐ 6/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 4 | Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework | ⭐ 6/10 | 其他方向, tool use, agentic |
| 应用与基准 | 1 | TelcoAgent: A Scalable 5G Multi-KPM Forecasting With 3GPP-Grounded Explainability | ⭐ 6/10 | 应用/基准, LLM, benchmark |
| 其他 Agent / LLM 方向 | 5 | Heterogeneous LLM Debate Under Adversarial Peers: Honest Gains, Replacement Costs, and Resilience | ⭐ 6/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 6 | Confidence Calibration for Multimodal LLMs: An Empirical Study through Medical VQA | ⭐ 6/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 7 | ENPIRE: Agentic Robot Policy Self-Improvement in the Real World | ⭐ 6/10 | 其他方向, agentic, LLM |
| 其他 Agent / LLM 方向 | 8 | A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems | ⭐ 6/10 | 其他方向, LLM, benchmark |
| 应用与基准 | 2 | Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring | ⭐ 6/10 | RAG/知识检索, benchmark, LLM |
| 其他 Agent / LLM 方向 | 9 | Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 10 | Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen? | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 11 | Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 12 | Code-Switching Reveals Language Anchoring in Multilingual LLMs | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 应用与基准 | 3 | Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives | ⭐ 5/10 | 应用/基准, LLM, agentic |
| 应用与基准 | 4 | Large Language Models Do Not Always Need Readable Language | ⭐ 5/10 | 应用/基准, LLM, benchmark |
| 其他 Agent / LLM 方向 | 13 | GEMS: Geometric Constraints Enable Multi-Semantic Superposition in LLMs | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 14 | From Texts to Scores: Tracing the Emergence of Essay Quality Representations in Large Language Models | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 15 | StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs | ⭐ 5/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 16 | Clusters are All You Need: Pre-Training the Tsetlin Machine with Semantic Clusters from Language Models for Interpretability | ⭐ 3/10 | 其他方向, LLM, benchmark |
| 其他 Agent / LLM 方向 | 17 | Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology | ⭐ 3/10 | 其他方向, LLM, benchmark |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] Benchmarking Agentic Review Systems

- **评分**：9/10
- **作者/机构**：作者：Dang Nguyen, Wanqing Hao, Yanai Elazar, Chenhao Tan
- **论文链接**：https://arxiv.org/abs/2606.19749
- **PDF**：https://arxiv.org/pdf/2606.19749
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Benchmarking Agentic Review Systems”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：flood the system (Liu and Tan, 2026; Lu et al., 2024). Liu and Tan (2026) formalize this dynamic A new class of agentic review systems are as a review death spiral: as submissions overwhelm arXiv:2606.19749v1 [cs.AI] 18 Jun 2026 emerging as a remedy to the pressure placed on reviewer capacity, review accuracy degrades,...。

**☠️ 毒舌点评**  
值得优先看：它和 Agent系统与工具使用 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 Agent系统与工具使用 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [2] Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining

- **评分**：9/10
- **作者/机构**：作者：Yuexing Hao, Xiaomin Li
- **论文链接**：https://arxiv.org/abs/2606.20363
- **PDF**：https://arxiv.org/pdf/2606.20363
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：Explicit skill libraries make computer-using agents easier to inspect, but it remains unclear whether such libraries can be mined from interaction data in a way that improves downstream policies. We study this question through a three-stage pipeline that segments GUI trajectories, clusters segments into candidate skill...。

**☠️ 毒舌点评**  
值得优先看：它和 Agent系统与工具使用 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 Agent系统与工具使用 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [3] LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents

- **评分**：8/10
- **作者/机构**：作者：Md Nayem Uddin, Amir Saeidi, Eduardo Blanco, Chitta Baral
- **论文链接**：https://arxiv.org/abs/2606.20529
- **PDF**：https://arxiv.org/pdf/2606.20529
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：a service plan, issue a refund, or update an account. Success therefore depends on more than selecting Policy-adherent tool-calling agents in customer- the right tool. The agent must maintain the rele- service domains must maintain task states arXiv:2606.20529v1 [cs.AI] 18 Jun 2026 across turns while calling tools and...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 Agent系统与工具使用 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 Agent系统与工具使用 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [4] MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments

- **评分**：8/10
- **作者/机构**：作者：Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li
- **论文链接**：https://arxiv.org/abs/2606.19893
- **PDF**：https://arxiv.org/pdf/2606.19893
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：Deep research agents have demonstrated remarkable capabilities in autonomous information gathering and synthesis, yet their training remains constrained by the static nature of simulated environments, the limits of fact-retrieval-only task designs, and the inefficiency of outcome-based reinforcement learning. In this w...。

**☠️ 毒舌点评**  
值得优先看：它和 Agent系统与工具使用 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 Agent系统与工具使用 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [5] ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research

- **评分**：8/10
- **作者/机构**：作者：Zhibang Yang, Xinke Jiang, Yuzhen Xiao, Ruizhe Zhang, Yue Fang, XinFei Wan, Zhengxing Song, Yuxuan Liu, Yuheng Huang, Xu Chu, Junfeng Zhao, Yasha Wang
- **论文链接**：https://arxiv.org/abs/2606.20122
- **PDF**：https://arxiv.org/pdf/2606.20122
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：Open-ended deep research (OEDR) requires arXiv:2606.20122v1 [cs.AI] 18 Jun 2026 systems to acquire knowledge through multi- round retrieval and generate coherent long- form reports. The outline plays a central role as a structural scaffold that coordinates retrieval, Composite Utility: Low evidence organization, and ge...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 Agent系统与工具使用 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 Agent系统与工具使用 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [6] Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services

- **评分**：8/10
- **作者/机构**：作者：Mugeng Liu, Shuoqi Li, Yixuan Zhang, Yun Ma
- **论文链接**：https://arxiv.org/abs/2606.19992
- **PDF**：https://arxiv.org/pdf/2606.19992
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：et al., 2024). The stepwise interface scales poorly, multiply- ing network turns, systematically over- and under-fetching In the agentic web era, LLM-based agents increas- data, and triggering cascading retries with inconsistent side arXiv:2606.19992v1 [cs.SE] 18 Jun 2026 ingly invoke web services as tools, yet most in...。

**☠️ 毒舌点评**  
值得优先看：它和 Agent系统与工具使用 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 Agent系统与工具使用 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [7] Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes

- **评分**：8/10
- **作者/机构**：作者：Jun He, Deying Yu
- **论文链接**：https://arxiv.org/abs/2606.20520
- **PDF**：https://arxiv.org/pdf/2606.20520
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes”。从标题和可见正文看，工作主要处理 Agent系统与工具使用 相关问题：or adversarial prompt injection can trigger unauthorized or destructive infrastructure mutations. Autonomous agents are increasingly connected to cloud, de- To mitigate these risks, recent architectures have introduced ployment, and data-control workflows, but production mu- institutional admission gates such as the So...。

**☠️ 毒舌点评**  
值得优先看：它和 Agent系统与工具使用 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以任务分解、工具调用、状态管理和执行闭环为主，关注 agent 在长流程任务里的稳定性与可控性。  
- **核心创新**：核心价值通常在于把黑盒 agent 流程拆成更可治理的中间结构、策略层或执行脚手架。  
- **训练 / 推理策略**：多以推理时控制和系统编排为主，训练不一定是重点；关键看状态表示、调用策略和错误恢复。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 Agent系统与工具使用 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [8] FAPO: Fully Autonomous Prompt Optimization of Multi-Step LLM Pipelines

- **评分**：8/10
- **作者/机构**：作者：Paul Kassianik, Baturay Saglam, Huaibo Zhao, Blaine Nelson, Supriti Vijay, Aman Priyanshu, Amin Karbasi
- **论文链接**：https://arxiv.org/abs/2606.19605
- **PDF**：https://arxiv.org/pdf/2606.19605
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“FAPO: Fully Autonomous Prompt Optimization of Multi-Step LLM Pipelines”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Multi-step LLM pipelines fail through interactions among retrieval, reasoning, and formatting steps, so prompt-only optimization can miss bottlenecks in the chain. We present FAPO (Fully Autonomous Prompt Optimization), a framework that lets Claude Code optimize an LLM pipeline inside a standardized codebase. FAPO eval...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [9] PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models

- **评分**：9/10
- **作者/机构**：作者：Yueyi Sun, Yuhao Wang, Jason Li, Ye Tian, Tao Zhang, Jacky Mai, Yihan Wang, Haochen Wang, Jinbin Bai, Ling Yang, Yunhai Tong
- **论文链接**：https://arxiv.org/abs/2606.19534
- **PDF**：https://arxiv.org/pdf/2606.19534
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Multimodal large language models (MLLMs) have achieved remarkable progress in visual under- standing tasks. However, most existing MLLMs rely on autoregressive generation, which limits their efficiency for perception tasks that require captioning multiple regions. In this work, we propose PerceptionDLM, a multimodal di...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [10] QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation

- **评分**：9/10
- **作者/机构**：作者：Xinyi Zheng, Ling Shi, Tianlong Yu, Yongxin Zhao, Lorenz Goette, Kailong Wang
- **论文链接**：https://arxiv.org/abs/2606.20227
- **PDF**：https://arxiv.org/pdf/2606.20227
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：diverse tasks and help mitigate data contamination in existing Large Language Models (LLMs) have made significant progress in datasets [3, 37]. In particular among them all, deductive reasoning reasoning, particularly in deductive reasoning, which is crucial for [18, 21] is central to decision making [8, 36]. It requir...。

**☠️ 毒舌点评**  
值得优先看：它和 LLM推理与规划 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 LLM推理与规划 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [11] Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software

- **评分**：9/10
- **作者/机构**：作者：Arastoo Zibaeirad, Marco Vieira
- **论文链接**：https://arxiv.org/abs/2606.20502
- **PDF**：https://arxiv.org/pdf/2606.20502
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：—Whether Large Language Models (LLMs) scoring arXiv:2606.20502v1 [cs.CR] 18 Jun 2026 well on vulnerability benchmarks genuinely reason about se- curity or merely pattern-match on contaminated data remains unresolved. We present CWE-Trace, a framework for LLM vulnerability detection built from 834 manually curated Linux...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [12] Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference

- **评分**：8/10
- **作者/机构**：作者：Huang Peng, Jiuyang Tang, Weixin Zeng, Hao Xu, Xiang Zhao
- **论文链接**：https://arxiv.org/abs/2606.20245
- **PDF**：https://arxiv.org/pdf/2606.20245
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：—Large language models (LLMs) have achieved strong per- model’s responses, granting it a broader knowledge scope formance across a wide range of language-based tasks by leveraging and improving the factual accuracy of its outputs. both extensive parametric knowledge and in-context learning ability, However, the integra...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [13] How LLMs Fail and Generalize in RTL Coding for Hardware Design?

- **评分**：8/10
- **作者/机构**：作者：Guan-Ting Liu, Chao-Han Huck Yang, Chenhui Deng, Zhongzhi Yu, Brucek Khailany, Yu-Chiang Frank Wang
- **论文链接**：https://arxiv.org/abs/2606.19347
- **PDF**：https://arxiv.org/pdf/2606.19347
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“How LLMs Fail and Generalize in RTL Coding for Hardware Design?”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Specification from RTL-Coding Hardware Engineer LLM Pass Translating sequential programming priors into Please create a circuit… arXiv:2606.19347v1 [cs.CL] 26 Apr 2026 module top_module L3S: Solvable the parallel temporal logic of hardware design (input a, output reg b); // Your code here remains a crucial bottleneck f...。

**☠️ 毒舌点评**  
值得优先看：它和 LLM推理与规划 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 LLM推理与规划 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [14] Deontic Policies for Runtime Governance of Agentic AI Systems

- **评分**：8/10
- **作者/机构**：作者：Anupam Joshi, Tim Finin, Karuna Pande Joshi, Lalana Kagal
- **论文链接**：https://arxiv.org/abs/2606.19464
- **PDF**：https://arxiv.org/pdf/2606.19464
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Deontic Policies for Runtime Governance of Agentic AI Systems”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：—Autonomous agentic AI systems driven by Large Microsoft’s Agent Governance Toolkit [5], and Cisco’s MCP arXiv:2606.19464v1 [cs.AI] 17 Jun 2026 Language Models (LLMs) introduce a new class of security, policy-enforcement gateway in Secure Access [6] all embody privacy, and compliance challenges: an agent that can invok...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [15] Uncertainty Decomposition for Clarification Seeking in LLM Agents

- **评分**：8/10
- **作者/机构**：作者：Gregory Matsnev
- **论文链接**：https://arxiv.org/abs/2606.19559
- **PDF**：https://arxiv.org/pdf/2606.19559
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Uncertainty Decomposition for Clarification Seeking in LLM Agents”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：U NCERTAINTY D ECOMPOSITION FOR C LARIFICATION S EEKING IN LLM AGENTS A P REPRINT Gregory Matsnev AI Talent Hub, ITMO University Saint Petersburg 197101, Russia gregory.matsnev@niuitmo.ru arXiv:2606.19559v1 [cs.AI] 17 Jun 2026 June 19, 2026 A BSTRACT Recent position papers argue that the classical aleatoric/epistemic u...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [16] Analyzing the Narration Gap in LLM-Solver Loops

- **评分**：8/10
- **作者/机构**：作者：Zunchen Huang, Songgaojun Deng
- **论文链接**：https://arxiv.org/abs/2606.19588
- **PDF**：https://arxiv.org/pdf/2606.19588
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Analyzing the Narration Gap in LLM-Solver Loops”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：. Formal tools such as SAT and SMT solvers are increasingly arXiv:2606.19588v1 [cs.AI] 17 Jun 2026 embedded in language model reasoning pipelines when a safety or security critical question can be formulated in logic. Unlike chain of thought whose steps are sampled from the model distribution without formal guarantee,...。

**☠️ 毒舌点评**  
值得优先看：它和 LLM推理与规划 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 LLM推理与规划 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [17] NRITYAM: Language Models Meet Art and Heritage of Dance

- **评分**：8/10
- **作者/机构**：作者：Punit Kumar Singh, Niladri Ghosh, Advait Joshiınst, Shailee Choudhary, Michael Färber, Haiqin Yang
- **论文链接**：https://arxiv.org/abs/2606.19727
- **PDF**：https://arxiv.org/pdf/2606.19727
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“NRITYAM: Language Models Meet Art and Heritage of Dance”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：. Language models have become essential tools in shaping modern workflows. However, their global effectiveness hinges on a nu- anced understanding of local socio-cultural contexts. To address this gap, we present NRITYAM, a comprehensive benchmark for evaluating the cultural comprehension capabilities of language model...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [18] ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?

- **评分**：8/10
- **作者/机构**：作者：Jiajun Li, Mingshu Cai, Yixuan Li, Yu Ding, Ran Hou, Guanyu Nie, Xiongwei Han, Wanyuan Wang
- **论文链接**：https://arxiv.org/abs/2606.19787
- **PDF**：https://arxiv.org/pdf/2606.19787
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Large language models are increasingly deployed as autonomous agents for multi- step tasks in executable environments, yet their ability to perform realistic opera- tions research (OR) work remains unclear. Existing OR evaluations often decouple modeling from solving, rely on pre-formalized or text-only instances, and...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [19] CombEval: A Framework for Evaluating Combinatorial Counting in Large Language Models

- **评分**：8/10
- **作者/机构**：作者：Yuxu Zhou, Ondřej Kuželka, Yuyi Wang, Yuanhong Wang, Yi Chang
- **论文链接**：https://arxiv.org/abs/2606.19788
- **PDF**：https://arxiv.org/pdf/2606.19788
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CombEval: A Framework for Evaluating Combinatorial Counting in Large Language Models”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：one-size-fits-all systematic solutions that adapt to diverse real-world scenarios. This is where large We present CombEval, a dynamic benchmark language models (LLMs) emerge as a promising arXiv:2606.19788v1 [cs.AI] 18 Jun 2026 for evaluating combinatorial counting in large approach to CO problems. The strength of LLMs...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [20] FFinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming

- **评分**：8/10
- **作者/机构**：作者：Chaeyun Kim, Daeyoung Park, Junghwan Kim, Jinyoung Jeong, Eunji Song, Yongtaek Lim, Minwoo Kim
- **论文链接**：https://arxiv.org/abs/2606.19887
- **PDF**：https://arxiv.org/pdf/2606.19887
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“FFinRED: An Expert-Guided Benchmark Generation and Evaluation Framework for Financial LLM Red-Teaming”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：—Existing safety benchmarks target general adversar- ial scenarios but miss finance-specific risks. Financial LLMs face regulatory-compliance violations, fraud facilitation, and systemic trust erosion that require targeted evaluation. We introduce FinRED, an expert-guided red-teaming framework for financial LLM safety...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [21] AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models

- **评分**：8/10
- **作者/机构**：作者：Masahiro Kato
- **论文链接**：https://arxiv.org/abs/2606.20041
- **PDF**：https://arxiv.org/pdf/2606.20041
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data....。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [22] Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact

- **评分**：8/10
- **作者/机构**：作者：Jelena Meyer, David Garcia, Dirk U. Wulff
- **论文链接**：https://arxiv.org/abs/2606.20205
- **PDF**：https://arxiv.org/pdf/2606.20205
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Psychological instruments designed for humans are increasingly used to assign large language models (LLMs) stable psychological profiles that affect their usability, safety assessment, and use as proxies for human participants in research. Using a formal psychometric framework, we show that these pro- files are largely...。

**☠️ 毒舌点评**  
值得优先看：它和 LLM推理与规划 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 LLM推理与规划 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [23] ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments

- **评分**：8/10
- **作者/机构**：作者：Tingyue Pan, Mingyue Cheng, Daoyu Wang, Yitong Zhou, Jie Ouyang, Qi Liu, Enhong Chen
- **论文链接**：https://arxiv.org/abs/2606.20235
- **PDF**：https://arxiv.org/pdf/2606.20235
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：(a) From Similarity Search to Agentic Search Similarity-based Search Agentic Search Academic paper search is a core step in scien- 1st 1st arXiv:2606.20235v1 [cs.IR] 18 Jun 2026 tific research, and LLM-based search agents are Ranking 2nd 2nd 3rd 3rd emerging as a promising paradigm for iterative, Papers Papers Search E...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [24] Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe

- **评分**：8/10
- **作者/机构**：作者：Qian Zhao, Kunlong Chen, Changxin Tian, Zhonghui Jiang, Haitao Zhang, Chaofan Yu, Peijie Jiang, Mingliang Gong, Jia Liu, Ziqi Liu, Zhiqiang Zhang, Jun Zhou
- **论文链接**：https://arxiv.org/abs/2606.20381
- **PDF**：https://arxiv.org/pdf/2606.20381
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe Qian Zhao, Kunlong Chen, Changxin Tian, Zhonghui Jiang, Haitao Zhang, Chaofan Yu, Peijie Jiang, Mingliang Gong, Jia Liu, Ziqi Liu, Zhiqiang Zhang∗ , Jun Zhou Ling Team, Ant Group ∗ Corresponding author FP4 training prom...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [25] Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies

- **评分**：7/10
- **作者/机构**：作者：Serena A. Hoffstedde, Machiko Hirota, Akshara Nadayanur Sathis Kanna, Rihito Kotani, Ujwal Kumar, Gabriele Trovato, Phan Xuan Tan
- **论文链接**：https://arxiv.org/abs/2606.18649
- **PDF**：https://arxiv.org/pdf/2606.18649
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Gender Bias in LLM Hiring Decisions: Evidence from a Japanese Context and Evaluation of Mitigation Strategies。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [26] Where to Place the Query? Unveiling and Mitigating Positional Bias in In-Context Learning for Diffusion LLMs via Decoding Dynamics

- **评分**：7/10
- **作者/机构**：作者：Zhengheng Li, Panrui Li, Xuyang Liu, Puzhi Xia
- **论文链接**：https://arxiv.org/abs/2606.19349
- **PDF**：https://arxiv.org/pdf/2606.19349
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Where to Place the Query? Unveiling and Mitigating Positional Bias in In-Context Learning for Diffusion LLMs via Decoding Dynamics”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：. While In-Context Learning (ICL) is extensively studied in Autoregressive (AR) LLMs, its mechanism within Diffusion Large Lan- guage Models (dLLMs) remains largely unexplored. Unlike AR mod- els restricted by unidirectional causal masking, dLLMs intrinsically uti- lize bidirectional attention, offering extensive spati...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [27] Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning

- **评分**：7/10
- **作者/机构**：作者：Xinyan Zhu, Yaoqi Liu, Yue Gao, Huadong Ma, Cheng Yang, Chuan Shi
- **论文链接**：https://arxiv.org/abs/2606.19351
- **PDF**：https://arxiv.org/pdf/2606.19351
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Pan et al., 2024), has become popular. These frame- Knowledge graph (KG) reasoning infers new works retrieve relevant triples from KGs, incor- arXiv:2606.19351v1 [cs.CL] 27 Apr 2026 knowledge from existing facts and is widely ap- porate them into the prompt, and guide LLMs to plied in question answering, recommendation...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [28] Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees

- **评分**：7/10
- **作者/机构**：作者：Herbert Woisetschläger, Arastun Mammadli, Ryan Zhang, Shiqiang Wang
- **论文链接**：https://arxiv.org/abs/2606.19376
- **PDF**：https://arxiv.org/pdf/2606.19376
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost. Users expect high-quality responses, and in commercial settings this is formally codified in Service Level Agreements (SLAs), creating a fundamental tension between cost and quality....。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [29] Measuring Curriculum Alignment across Topical Coverage, Competency, and Cognitive Depth: A Longitudinal Framework Applied to CS2013 and CS2023

- **评分**：7/10
- **作者/机构**：作者：Sherzod Turaev, Mary John, Saja Aldabet, Mamoun Awad, Nazar Zaki, Khaled Shuaib
- **论文链接**：https://arxiv.org/abs/2606.19469
- **PDF**：https://arxiv.org/pdf/2606.19469
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Measuring Curriculum Alignment across Topical Coverage, Competency, and Cognitive Depth: A Longitudinal Framework Applied to CS2013 and CS2023”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Undergraduate computer science is governed by international curricular guidelines revised about once a decade, yet programs lack a reliable, reproducible way to measure how。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [30] Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix

- **评分**：7/10
- **作者/机构**：作者：R.D.N. Shakya, C.P. Wijesiriwardana, S.M. Vidanagamachchi, Nalin A.G. Arachchilage
- **论文链接**：https://arxiv.org/abs/2606.19474
- **PDF**：https://arxiv.org/pdf/2606.19474
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Workshop on Vulnerabilities in Generative Systems for Information Retrieval The transition to Post-Quantum Cryptography (PQC) introduces (SIGIR VulGen ’26). ACM, New York, NY, USA, 7 pages. https://doi.org/ XXXXXXX.XXXXXXX considerable implementation complexity, requiring strict adherence to constant-time execution, si...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [31] LLM Doesn't Know What It Doesn't Know: Detecting Epistemic Blind Spots via Cross-Model Attribution Divergence on Clinical Tabular Data

- **评分**：7/10
- **作者/机构**：作者：Akshat Dasula, Prasanna Desikan, Jaideep Srivastava
- **论文链接**：https://arxiv.org/abs/2606.19509
- **PDF**：https://arxiv.org/pdf/2606.19509
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LLM Doesn't Know What It Doesn't Know: Detecting Epistemic Blind Spots via Cross-Model Attribution Divergence on Clinical Tabular Data”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Large language models (LLMs) are increasingly applied to structured clinical data, yet whether they can recog- nize the limits of their own knowledge on such tasks remains unexplored. We study this question through the lens of cross-model attribution divergence with the goal of reducing epistemic uncertainty for struct...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [32] Configurable Clinical Information Extraction with Agentic RAG: What Works, What Breaks, and Why

- **评分**：7/10
- **作者/机构**：作者：Osman Alperen Çinar-Koraş, Marie Bauer, Sameh Khattab, Merlin Engelke, Moon Kim, Stephan Settelmeier, Shigeyasu Sugawara, Fabian Freisleben, Felix Nensa, Jens Kleesiek
- **论文链接**：https://arxiv.org/abs/2606.19602
- **PDF**：https://arxiv.org/pdf/2606.19602
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Configurable Clinical Information Extraction with Agentic RAG: What Works, What Breaks, and Why”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Clinical information extraction (IE) has long aimed to alleviate this burden, yet even recent de- Patient contexts span hundreds of heteroge- ployed systems require developer effort to adapt neous documents and thousands of structured to new workflows (§2). Large language models data points, yet the document-level meta...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [33] AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing

- **评分**：7/10
- **作者/机构**：作者：Zilong Zhang, Yi-Ting Hung, Weiyi He, Junxi Zhang, Lei Ding, Chi-Kuang Yeh
- **论文链接**：https://arxiv.org/abs/2606.19714
- **PDF**：https://arxiv.org/pdf/2606.19714
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Large language models (LLMs) are increasingly used as judges for open-ended generation, as large-scale human evaluation is often expensive and difficult to scale, yet their preferences remain imperfect proxies for human judgment. Ex- isting auditing pipelines often assume that a reliable subset of examples or clean sup...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [34] VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents

- **评分**：7/10
- **作者/机构**：作者：Marcus Hoerger, Rishikesh Joshi, Rahul Shome, Ian Manchester, Hanna Kurniawati
- **论文链接**：https://arxiv.org/abs/2606.19729
- **PDF**：https://arxiv.org/pdf/2606.19729
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：. Planning under uncertainty is an essential capability for au- tonomous robots. The Partially Observable Markov Decision Process (POMDP) provides a powerful framework for such a capability. Although POMDP-based planning has advanced significantly, its application to real-world problems is often limited by the difficul...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [35] Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization Across Preference Settings

- **评分**：7/10
- **作者/机构**：作者：Pranav Bhandari, Nicolas Fay, Amitava Datta, Usman Naseem, Mehwish Nasim
- **论文链接**：https://arxiv.org/abs/2606.19744
- **PDF**：https://arxiv.org/pdf/2606.19744
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization Across Preference Settings”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：2024). Multiple behavioural objectives, such as helpfulness, harmlessness, safety, honesty, factual- Aligning language models with human pref- arXiv:2606.19744v1 [cs.CL] 18 Jun 2026 ity, style, and instruction following, are optimised erences often requires optimising multiple be- in post-training pipelines (Ji et al.,...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [36] SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling

- **评分**：7/10
- **作者/机构**：作者：Haotian Xu, Zeyang Zhang, Linbao Li, Huadi Zheng, Yu Li, Cheng Zhuo
- **论文链接**：https://arxiv.org/abs/2606.19755
- **PDF**：https://arxiv.org/pdf/2606.19755
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Speculative inference accelerates large language model (LLM) decoding but provides no inher- ent safety guarantees. Existing safety defenses arXiv:2606.19755v1 [cs.CR] 18 Jun 2026 are largely incompatible with speculative infer- ence: they either introduce additional computa- tion or disrupt the draft–verify mechanism,...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [37] Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning

- **评分**：7/10
- **作者/机构**：作者：Xuanzhi Feng, Zhengyang Li, Zeyu Liu, Haoxi Li, Yuming Jiang, Bing Guo, Jingcai Guo, Jie Zhang, Song Guo
- **论文链接**：https://arxiv.org/abs/2606.19771
- **PDF**：https://arxiv.org/pdf/2606.19771
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Reinforcement Learning with Veriﬁable Rewards (RLVR) has signiﬁcantly advanced Large Language Model (LLM) reasoning; however, it faces a fundamental optimization instability: uniform token updates precipitate entropy collapse, leading to premature convergence to suboptimal strategies, whereas excessive Shannon Entropy...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [38] Agentic Electronic Design Automation: A Handoff Perspective

- **评分**：7/10
- **作者/机构**：作者：Jiawei Liu, Peiyi Han, Yuntao Lu, Su Zheng, Fengyu Yan, Bei Yu
- **论文链接**：https://arxiv.org/abs/2606.19795
- **PDF**：https://arxiv.org/pdf/2606.19795
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Agentic Electronic Design Automation: A Handoff Perspective”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Agentic Electronic Design Automation: A Handoff Perspective JIAWEI LIU, The Chinese University of Hong Kong PEIYI HAN, The Chinese University of Hong Kong YUNTAO LU, The Chinese University of Hong Kong SU ZHENG, The Chinese University of Hong Kong FENGYU YAN, Primarius Technologies BEI YU, The Chinese University of Hon...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [39] AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts

- **评分**：7/10
- **作者/机构**：作者：Yanyu Yao, Shangze Li, Zhi Zheng, Hui Zheng, Qi Liu, Tong Xu, Enhong Chen
- **论文链接**：https://arxiv.org/abs/2606.19847
- **PDF**：https://arxiv.org/pdf/2606.19847
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [40] Measuring Biological Capabilities and Risks of AI Agents

- **评分**：7/10
- **作者/机构**：作者：Patricia Paskov, Jeffrey Lee, Kyle Brady, Alyssa Worland
- **论文链接**：https://arxiv.org/abs/2606.19899
- **PDF**：https://arxiv.org/pdf/2606.19899
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Measuring Biological Capabilities and Risks of AI Agents”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Perspective PATRICIA PASKOV, JEFFREY LEE, KYLE BRADY, ALYSSA WORLAND Measuring Biological Capabilities and Risks of AI Agents Generating and Interpreting Evidence from Agentic Evaluations This publication has completed RAND’s research quality-assurance process but was not professionally copyedited. For more information...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [41] Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning

- **评分**：7/10
- **作者/机构**：作者：Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou
- **论文链接**：https://arxiv.org/abs/2606.20002
- **PDF**：https://arxiv.org/pdf/2606.20002
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：This work presents a general framework for training large language models (LLMs) to “Connect the Dots” (CoD), a meta-capability required by long-lifecycle agents: as an LLM-based AI agent gets deployed in an environment, it solves a long sequence of tasks while continuously exploring the envi- ronment, learning from it...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [42] StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation

- **评分**：7/10
- **作者/机构**：作者：Guangda Liu, Yiquan Wang, Chengwei Li, Wenhao Chen, Jing Lin, Yiwu Yao, Danning Ke, Wenchao Ding, Jieru Zhao
- **论文链接**：https://arxiv.org/abs/2606.20005
- **PDF**：https://arxiv.org/pdf/2606.20005
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：dense-attention distribution [7, 9]. Across all of these set- Attention distillation, which trains one attention distribution tings, the training objective is to minimize the KL divergence to match another by minimizing their Kullback-Leibler (KL) between two attention distributions 𝑃1, 𝑃2 ∈ R𝑁𝑄 ×𝑁𝐾 gen- divergence, is...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [43] Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform

- **评分**：7/10
- **作者/机构**：作者：Hyeonna Choi, Jung Yup Kim, Hyuneui Lim, Seunggyu Jeon
- **论文链接**：https://arxiv.org/abs/2606.20120
- **PDF**：https://arxiv.org/pdf/2606.20120
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Biological experiment protocols are written in natural language, whereas automation systems rely on prede。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [44] RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning

- **评分**：7/10
- **作者/机构**：作者：Antón Asla Manzárraga
- **论文链接**：https://arxiv.org/abs/2606.20142
- **PDF**：https://arxiv.org/pdf/2606.20142
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Metaheuristic optimization is widely used in operational decision systems, but effective long-term use often requires expertise that many companies do not have internally. A company may have access to a configured optimizer while lacking the optimization expertise required to adapt its internal search behavior as opera...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [45] UltraQuant: 4-bit KV Caching for Context-Heavy Agents

- **评分**：7/10
- **作者/机构**：作者：Inesh Chakrabarti, David Limpus, Aditi Ghai Rana, Bowen Bao, Spandan Tiwari, Thiago Crepaldi, Ashish Sirasao
- **论文链接**：https://arxiv.org/abs/2606.20474
- **PDF**：https://arxiv.org/pdf/2606.20474
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“UltraQuant: 4-bit KV Caching for Context-Heavy Agents”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：plan across many turns. As model releases push context windows toward one million tokens and be- Context-heavy agents place unusual pressure arXiv:2606.20474v1 [cs.LG] 18 Jun 2026 yond (Gemini Team, 2024; Ding et al., 2024), the on the key–value (KV) cache: long prefixes KV cache grows linearly with context length and...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [46] Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems

- **评分**：7/10
- **作者/机构**：作者：Shu Yao, Yuhua Luo, Qian Long, Jingru Fan, Zhuoyuan Yu, Yuheng Wang, Lin Wu, Yufan Dang, Huatao Li, Chen Qian
- **论文链接**：https://arxiv.org/abs/2606.20487
- **PDF**：https://arxiv.org/pdf/2606.20487
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [47] Efficient and Sound Probabilistic Verification for AI Agents

- **评分**：7/10
- **作者/机构**：作者：Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu, Somesh Jha, Krishnamurthy Dj Dvijotham
- **论文链接**：https://arxiv.org/abs/2606.20510
- **PDF**：https://arxiv.org/pdf/2606.20510
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Efficient and Sound Probabilistic Verification for AI Agents”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Efficient and Sound Probabilistic Verification for AI Agents Alaia Solko-Breslin1,3,* , Pramod Kaushik Mudrakarta1 , Mihai Christodorescu2 , Somesh Jha2,4 and Krishnamurthy Dj Dvijotham1 1 Google DeepMind, 2 Google, 3 University of Pennsylvania, 4 University of Wisconsin–Madison Securing AI agents that operate in compl...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [48] Human-AI Agent Interaction in a Business Context

- **评分**：6/10
- **作者/机构**：作者：Kathrin Paimann, Elizangela Valarini, Sebastian Juhl
- **论文链接**：https://arxiv.org/abs/2606.18716
- **PDF**：https://arxiv.org/pdf/2606.18716
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Human-AI Agent Interaction in a Business Context”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Human-AI Agent Interaction in a Business Context。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [49] Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models

- **评分**：6/10
- **作者/机构**：作者：Amogh Sheth, Biruk Assefa, Yi Wen Huang, Andrew Lin, Yuhao Ge
- **论文链接**：https://arxiv.org/abs/2606.19350
- **PDF**：https://arxiv.org/pdf/2606.19350
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [50] Quantifying Aleatoric Uncertainty of In-Context Learning for Robust Measure of LLM Prediction Confidence

- **评分**：6/10
- **作者/机构**：作者：Jinseok Chung, Minkyoung Song, Hyunji Jung, Namhoon Lee
- **论文链接**：https://arxiv.org/abs/2606.19353
- **PDF**：https://arxiv.org/pdf/2606.19353
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Quantifying Aleatoric Uncertainty of In-Context Learning for Robust Measure of LLM Prediction Confidence”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Quantifying Aleatoric Uncertainty of In-Context Learning for Robust Measure of LLM Prediction Confidence。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [51] Interpretable and Verifiable Hardware Generation with LLM-Driven Stepwise Refinement

- **评分**：6/10
- **作者/机构**：作者：You Li, Samuel Mandell, David Z. Pan
- **论文链接**：https://arxiv.org/abs/2606.19387
- **PDF**：https://arxiv.org/pdf/2606.19387
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Interpretable and Verifiable Hardware Generation with LLM-Driven Stepwise Refinement”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：For these reasons, the hardware industry is still reluctant to depend on LLMs for RTL design tasks. arXiv:2606.19387v1 [cs.SE] 16 Jun 2026 Large language models (LLMs) have achieved remarkable success in software development. However, they are sus- Formal program construction is a classical method for de- ceptible to h...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [52] Thermodynamic Signatures of Reasoning: Free-Energy and Spectral-Form-Factor Diagnostics for Hallucination Detection in Large Language Models

- **评分**：6/10
- **作者/机构**：作者：Salim Khazem
- **论文链接**：https://arxiv.org/abs/2606.19404
- **PDF**：https://arxiv.org/pdf/2606.19404
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Thermodynamic Signatures of Reasoning: Free-Energy and Spectral-Form-Factor Diagnostics for Hallucination Detection in Large Language Models”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Thermodynamic Signatures of Reasoning: Free-Energy and Spectral-Form-Factor Diagnostics for Hallucination Detection in Large Language Models。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [53] Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices

- **评分**：6/10
- **作者/机构**：作者：Hassan Dbouk, Matthias Reisser, Prathamesh Mandke, Likhita Arun Navali, Christos Louizos
- **论文链接**：https://arxiv.org/abs/2606.19528
- **PDF**：https://arxiv.org/pdf/2606.19528
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge De- vices Hassan Dbouk† , Matthias Reisser† , Prathamesh Mandke∗ , Likhita Arun Navali, arXiv:2606.19528v1 [cs.LG] 17 Jun 2026 Christos Louizos Fine-tuning of Large Language Models (LLMs) using Low-Rank Adaptation (LoRA) on an end- user’s data of...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [54] Where Does Social Reasoning Come From? Capability Provenance in Language Models

- **评分**：6/10
- **作者/机构**：作者：Glenn Matlin, Chandreyi Chakraborty, Saehee Eom, Mika Okamoto, Rayan Castilla, Louis Jaburi, Alvin Deng, Taywon Min, Lucia Quirke, Stella Biderman, Mark Riedl
- **论文链接**：https://arxiv.org/abs/2606.19625
- **PDF**：https://arxiv.org/pdf/2606.19625
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Where Does Social Reasoning Come From? Capability Provenance in Language Models”。从标题和可见正文看，工作主要处理 LLM推理与规划 相关问题：Where Does Social Reasoning Come From? Capability Provenance in Language Models。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM推理与规划 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：围绕推理链、规划器、逻辑结构或冲突消解展开，重点看模型如何把复杂问题拆成可执行步骤。  
- **核心创新**：新意主要体现在搜索结构、规划表示或推理控制机制上，目标是减少瞎猜和短路。  
- **训练 / 推理策略**：可能结合提示、程序搜索或轻量训练；精读时应核查是否真的提升复杂推理，而不是只在模板题上取巧。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM推理与规划 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [55] A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots

- **评分**：6/10
- **作者/机构**：作者：Gulshan Saleem, Nisar Ahmed, Muhammad Imran Zaman, Ali Hassan
- **论文链接**：https://arxiv.org/abs/2606.19660
- **PDF**：https://arxiv.org/pdf/2606.19660
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [56] LOKI: Memory-Free Null-Space Constrained Lifelong Knowledge Editing

- **评分**：6/10
- **作者/机构**：作者：Masih Eskandar, Miquel Sirera Perelló, Stratis Ioannidis, Jennifer Dy
- **论文链接**：https://arxiv.org/abs/2606.19679
- **PDF**：https://arxiv.org/pdf/2606.19679
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LOKI: Memory-Free Null-Space Constrained Lifelong Knowledge Editing”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Lifelong knowledge editing aims to efficiently and sequentially update language models over time, as new knowledge becomes available or when the model makes mistakes, while preserving acceptable performance on past knowledge. One un- resolved challenge is that existing methods modify a fixed set of layers for all new k...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [57] Efficiently Representing Algorithms With Chain-of-Thought Transformers

- **评分**：6/10
- **作者/机构**：作者：Yanhong Li, Anej Svete, Ashish Sabharwal, William Merrill
- **论文链接**：https://arxiv.org/abs/2606.19697
- **PDF**：https://arxiv.org/pdf/2606.19697
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Efficiently Representing Algorithms With Chain-of-Thought Transformers”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：The increasing popularity of reasoning models—language models that output a series of reasoning or thought tokens before producing an answer—is justified, in part, by theoretical results showing that chain-of-thought (CoT) transformers can simulate Turing machines, and thus perform arbitrary computation. However, the T...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [58] Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models

- **评分**：6/10
- **作者/机构**：作者：Darrien McKenzie, Nicklas Hansen, Xiaolong Wang
- **论文链接**：https://arxiv.org/abs/2606.19750
- **PDF**：https://arxiv.org/pdf/2606.19750
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Reinforcement learning (RL) is a central approach for improving reasoning ca- pabilities in large language models (LLMs), where training efficiency depends critically on how problems are sampled during optimization. Existing adaptive curriculum learning methods typically prioritize prompts of intermediate difficulty, t...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [59] When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation

- **评分**：6/10
- **作者/机构**：作者：Elroy Galbraith
- **论文链接**：https://arxiv.org/abs/2606.20113
- **PDF**：https://arxiv.org/pdf/2606.20113
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [60] Editorial Alignment: A Participatory Approach to Engaging Editorial Expertise in LLM-mediated Knowledge Dissemination

- **评分**：6/10
- **作者/机构**：作者：Simon Aagaard Enni, Malthe Stavning Erslev, Karl-Emil Kjær Bilstrup, Kristoffer Laigaard Nielbo
- **论文链接**：https://arxiv.org/abs/2606.20258
- **PDF**：https://arxiv.org/pdf/2606.20258
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Editorial Alignment: A Participatory Approach to Engaging Editorial Expertise in LLM-mediated Knowledge Dissemination”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：shift threatens their continued existence as intellectual authorities The emergence of LLM-driven information services is reshaping and caretakers of responsible knowledge dissemination. the conditions under which public knowledge institutions oper- At the same time, LLMs are powerful new tools for knowledge ate, threa...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [61] Multi-View Decompilation for LLM-Based Malware Classification

- **评分**：6/10
- **作者/机构**：作者：Bercan Turkmen, Vyas Raina
- **论文链接**：https://arxiv.org/abs/2606.20436
- **PDF**：https://arxiv.org/pdf/2606.20436
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Multi-View Decompilation for LLM-Based Malware Classification”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：2019; Hex-Rays, 2024). A decompiler attempts to recover an approximate, human-readable C-like Malware analysts often inspect compiled bi- arXiv:2606.20436v1 [cs.CR] 18 Jun 2026 representation of a program from a compiled binary naries through decompiled pseudo-C, when source code is unavailable. Recent work (Cifuentes,...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [62] CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference

- **评分**：5/10
- **作者/机构**：作者：Kaizhen Tan, Rong Gu, Mingyuan Li
- **论文链接**：https://arxiv.org/abs/2606.19667
- **PDF**：https://arxiv.org/pdf/2606.19667
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 RAG与知识检索 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 RAG与知识检索 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [63] Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware

- **评分**：5/10
- **作者/机构**：作者：Ma Toan Bach, Yuchi Zheng, Haingo Razafindranto, Tanvir Alam, Aric Leather, Ranveer Sandhu, Jitesh Arora
- **论文链接**：https://arxiv.org/abs/2606.19725
- **PDF**：https://arxiv.org/pdf/2606.19725
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：L IBRARY-AWARE D OUBLES AND I TERATIVE R EPAIR FOR L ARGE L ANGUAGE M ODEL -G ENERATED U NIT T ESTS IN O PEN SIL F IRMWARE Ma Toan Bach Yuchi Zheng School of Software Design and Data Science School of Software Design and Data Science arXiv:2606.19725v1 [cs.SE] 18 Jun 2026 Seneca Polytechnic Seneca Polytechnic Canada Ca...。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 RAG与知识检索 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 RAG与知识检索 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [64] Leverage Is Not Reach: A Control-Window Law for Single-Neuron Steering in Language Models

- **评分**：5/10
- **作者/机构**：作者：Hongliang Liu
- **论文链接**：https://arxiv.org/abs/2606.19831
- **PDF**：https://arxiv.org/pdf/2606.19831
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Leverage Is Not Reach: A Control-Window Law for Single-Neuron Steering in Language Models”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Leverage Is Not Reach: A Control-Window Law for Single-Neuron Steering in Language Models。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 RAG与知识检索 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 RAG与知识检索 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [65] CATCH-ME if you RAG: a dataset of Contextually Annotated multi-Turn Counterspeech against Hate and Misinformation Exchanges

- **评分**：5/10
- **作者/机构**：作者：Helena Bonaldi, Genoveffa Martone, Marco Guerini
- **论文链接**：https://arxiv.org/abs/2606.20369
- **PDF**：https://arxiv.org/pdf/2606.20369
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“CATCH-ME if you RAG: a dataset of Contextually Annotated multi-Turn Counterspeech against Hate and Misinformation Exchanges”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：CATCH-ME if you RAG: a dataset of Contextually Annotated multi-Turn Counterspeech against Hate and Misinformation Exchanges。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 RAG与知识检索 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 RAG与知识检索 长尾工作，可以留档；否则优先级可以放后。

</span>

---

## 🤝 多智能体 / 协作


### [66] Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation

- **评分**：8/10
- **作者/机构**：作者：Ahmad Farooq, Kamran Iqbal
- **论文链接**：https://arxiv.org/abs/2606.19632
- **PDF**：https://arxiv.org/pdf/2606.19632
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：— Multi-agent reinforcement learning (MARL) en- Optimization (MAPPO) [1] and QMIX [2] achieve remark- ables autonomous agents to develop sophisticated coordination able coordination, neural policies cannot be formally certi- strategies through emergent communication, but the resulting fied. The verification challenge i...。

**☠️ 毒舌点评**  
值得优先看：它和 多智能体与协作 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [67] Exit-and-Join Dynamics for Decentralized Coalition Formation

- **评分**：8/10
- **作者/机构**：作者：Quanyan Zhu
- **论文链接**：https://arxiv.org/abs/2606.19683
- **PDF**：https://arxiv.org/pdf/2606.19683
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Exit-and-Join Dynamics for Decentralized Coalition Formation”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：E XIT– AND –J OIN DYNAMICS FOR D ECENTRALIZED C OALITION F ORMATION Quanyan Zhu Department of Electrical and Computer Engineering New York University Tandon School of Engineering Brooklyn, NY, USA arXiv:2606.19683v1 [cs.AI] 18 Jun 2026 quanyan.zhu@nyu.edu A BSTRACT This paper studies coalition formation as a decentrali...。

**☠️ 毒舌点评**  
值得优先看：它和 多智能体与协作 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [68] A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models

- **评分**：8/10
- **作者/机构**：作者：Jiayi Wang, Xu-Yao Zhang
- **论文链接**：https://arxiv.org/abs/2606.19868
- **PDF**：https://arxiv.org/pdf/2606.19868
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：—Although large language models (LLMs) have shown strong capabilities across a wide range of tasks, their outputs often remain unreliable and may contain hallucinations, making uncertainty estimation (UE) essential for building trustworthy LLMs. In practice, many mainstream LLMs are only accessible through restricted A...。

**☠️ 毒舌点评**  
值得优先看：它和 多智能体与协作 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [69] Optimal Order of Multi-Agent and General Many-Body Systems

- **评分**：8/10
- **作者/机构**：作者：Jake J. Xia
- **论文链接**：https://arxiv.org/abs/2606.20485
- **PDF**：https://arxiv.org/pdf/2606.20485
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Optimal Order of Multi-Agent and General Many-Body Systems”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：This paper develops a general framework for analyzing multi-agent systems with feedback loops between agents’ actions and collective observations. The framework is built on two fundamental agent-level variables: power, which measures an agent’s influence on collective outcomes, and response functions, which determine h...。

**☠️ 毒舌点评**  
值得优先看：它和 多智能体与协作 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [70] Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems

- **评分**：8/10
- **作者/机构**：作者：Zewen Liu
- **论文链接**：https://arxiv.org/abs/2606.20493
- **PDF**：https://arxiv.org/pdf/2606.20493
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Net- works, a formal framework for measuring how evaluator biases spread across interacting LLM agents. In a controlled 3-agent experiment using DeepSeek-...。

**☠️ 毒舌点评**  
值得优先看：它和 多智能体与协作 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 多智能体与协作 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [71] Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol

- **评分**：7/10
- **作者/机构**：作者：Anantha Sharma
- **论文链接**：https://arxiv.org/abs/2606.19356
- **PDF**：https://arxiv.org/pdf/2606.19356
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Trustworthy Multi-Agent Systems: Mitigating Semantic Drift with the Argent Signaling Protocol”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：T RUSTWORTHY M ULTI -AGENT S YSTEMS : M ITIGATING S EMANTIC D RIFT WITH THE A RGENT S IGNALING P ROTOCOL Anantha Sharma Synechron Inc arXiv:2606.19356v1 [cs.CL] 14 May 2026 Charlotte, NC, USA April 16, 2026 A BSTRACT When multi-agent LLM systems produce bad answers, not all failures are equal: some answers are grounded...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [72] DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling

- **评分**：7/10
- **作者/机构**：作者：Kanishk Kushwaha, Vikrant Vinod Bansode, Harsh Vardhan, Dhaval C. Patel
- **论文链接**：https://arxiv.org/abs/2606.19382
- **PDF**：https://arxiv.org/pdf/2606.19382
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：trial asset lifecycle through multi-step reasoning While LLM-powered agents offer end-to-end and tool-augmented interaction. Industrial agentic arXiv:2606.19382v1 [cs.SE] 14 Jun 2026 automation for industrial asset lifecycles, real- tasks require sustained interaction with external en- world Industry 4.0 deployment is...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [73] Hidden Anchors in Multi-Agent LLM Deliberation

- **评分**：7/10
- **作者/机构**：作者：Apurba Pokharel, Ram Dantu
- **论文链接**：https://arxiv.org/abs/2606.19494
- **PDF**：https://arxiv.org/pdf/2606.19494
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Hidden Anchors in Multi-Agent LLM Deliberation”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：how and why deliberation works remains largely unexamined. Prior work treats deliberation as a Multi-agent LLM deliberation, where agents black box that empirically improves accuracy, and arXiv:2606.19494v1 [cs.AI] 17 Jun 2026 exchange and revise answers over several to our knowledge nobody models the deliberation roun...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [74] AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA

- **评分**：7/10
- **作者/机构**：作者：Aravind Narayanan, Shaina Raza
- **论文链接**：https://arxiv.org/abs/2606.19782
- **PDF**：https://arxiv.org/pdf/2606.19782
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：settings demands more than raw accuracy. Recent work shows that such systems exhibit significant Financial chart question answering in regulated hallucination rates on financial tasks, posing di- arXiv:2606.19782v1 [cs.AI] 18 Jun 2026 settings demands more than accuracy: practi- rect operational and regulatory risk to...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [75] Multi-Agent Transactive Memory

- **评分**：7/10
- **作者/机构**：作者：To Eun Kim, Xuhong He, Dishank Jain, Ambuj Agrawal, Negar Arabzadeh, Fernando Diaz
- **论文链接**：https://arxiv.org/abs/2606.19911
- **PDF**：https://arxiv.org/pdf/2606.19911
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Multi-Agent Transactive Memory”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：TRADITIONAL RETRIEVAL GENERATION MEMORY The decentralized deployment of LLM agents documents documents arXiv:2606.19911v1 [cs.AI] 18 Jun 2026 INDEX images INDEX images INDEX trajectories videos videos with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing RETRIEVAL MODEL RETRIEVAL...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [76] Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution

- **评分**：7/10
- **作者/机构**：作者：Jannik Hösch, Alessandro Sestini, Florian Fuchs, Amir Baghi, Joakim Bergdahl, Konrad Tollmar, Jean-Philippe Barrette-LaPierre, Linus Gisslén
- **论文链接**：https://arxiv.org/abs/2606.20014
- **PDF**：https://arxiv.org/pdf/2606.20014
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：Reinforcement learning (RL) has achieved strong performance in sequential decision- making, yet scaling to complex multi-agent environments remains challenging due to sparse rewards, large state-action spaces, and the difficulty of learning coordinated strategies. We propose a hierarchical architecture where a pretrain...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [77] Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale

- **评分**：7/10
- **作者/机构**：作者：Harsh Rao Dhanyamraju, Leonidas Raghav, Aaron Lee
- **论文链接**：https://arxiv.org/abs/2606.20058
- **PDF**：https://arxiv.org/pdf/2606.20058
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：Enterprise AI aims to move toward continuous event monitoring, detection, and action across specialist agents, yet existing multi-agent systems largely assume discrete request-response workflows and remain underexplored at enterprise scale. We evaluate DAG Plan & Execute and ReAct across 208 production- derived enterpr...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [78] AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning

- **评分**：7/10
- **作者/机构**：作者：Zepeng Li, Jie Ren, Zhanyong Tang, Jie Zheng, Zheng Wang
- **论文链接**：https://arxiv.org/abs/2606.20373
- **PDF**：https://arxiv.org/pdf/2606.20373
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：rights confirmation email (Conference acronym ’XX). ACM, New York, NY, Large Language Models (LLMs) show promise for code compilation USA, 12 pages. https://doi.org/XXXXXXX.XXXXXXX tasks, but applying them to runtime performance tuning is diffi- cult due to complex microarchitectural effects and noisy runtime measureme...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [79] Before the Pull Request: Mining Multi-Agent Coordination

- **评分**：6/10
- **作者/机构**：作者：Dipankar Sarkar
- **论文链接**：https://arxiv.org/abs/2606.19616
- **PDF**：https://arxiv.org/pdf/2606.19616
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Before the Pull Request: Mining Multi-Agent Coordination”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：. Autonomous coding agents now open millions of pull re- quests, yet large-scale studies find their PRs are produced faster but accepted less often—a coordination and trust gap that pull-request-level telemetry cannot explain. We argue the missing signal lives before the PR, in how concurrent agents claim, divide, and...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [80] SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design

- **评分**：6/10
- **作者/机构**：作者：Kun Zeng, Yu Huo, Siyu Zhang, Yuecheng Zhuo, Yuquan Lu, Haoyue Liu, Siyue Chen, Xiaoying Tang
- **论文链接**：https://arxiv.org/abs/2606.19758
- **PDF**：https://arxiv.org/pdf/2606.19758
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [81] Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs

- **评分**：6/10
- **作者/机构**：作者：Kipngeno Koech, Muhammad Adam, Baimam Boukar Jean Jacques, Joao Barros
- **论文链接**：https://arxiv.org/abs/2606.20243
- **PDF**：https://arxiv.org/pdf/2606.20243
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs”。从标题和可见正文看，工作主要处理 多智能体与协作 相关问题：Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 多智能体与协作 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：把多个 agent 或角色组织成协作系统，重点看通信协议、共享记忆、分工和协调成本。  
- **核心创新**：关键要看它是否提出了比简单角色扮演更扎实的协同机制，以及是否处理了信用分配问题。  
- **训练 / 推理策略**：这类工作常依赖环境反馈、角色搜索或流程编排；精读时要核实协作增益是否真的来自机制本身。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 多智能体与协作 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [82] Which Pairs to Compare for LLM Post-Training?

- **评分**：8/10
- **作者/机构**：作者：Jiangze Han, Vineet Goyal, Will Ma
- **论文链接**：https://arxiv.org/abs/2606.19607
- **PDF**：https://arxiv.org/pdf/2606.19607
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Which Pairs to Compare for LLM Post-Training?”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：Preference-based post-training has become a central paradigm for aligning lan- guage models. A common data-collection strategy is to generate a small set of completions for each prompt and label the resulting comparison pairs. However, human preference labels are often much more expensive than generating additional com...。

**☠️ 毒舌点评**  
值得优先看：它和 LLM训练与对齐 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 LLM训练与对齐 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [83] Human-like autonomy emerges from self-play and a pinch of human data

- **评分**：6/10
- **作者/机构**：作者：Daphne Cornelisse, Julian Hunt, Zixu Zhang, Waël Doulazmi, Kevin Joseph, Jaime Fernández Fisac, Eugene Vinitsky
- **论文链接**：https://arxiv.org/abs/2606.19370
- **PDF**：https://arxiv.org/pdf/2606.19370
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Human-like autonomy emerges from self-play and a pinch of human data”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：: Self-play reinforcement learning has recently emerged as a way to train driving policies without any human data. It uses cheap, large-scale simulations to substitute expensive, large-scale human driving demonstrations. A key limitation of this approach is that policies trained through pure self-play can learn effecti...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM训练与对齐 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [84] Characterizing Narrative Content in Web-scale LLM Pretraining Data

- **评分**：6/10
- **作者/机构**：作者：Teagan Johnson, Elliott Ash, Andrew Piper, Maria Antoniak
- **论文链接**：https://arxiv.org/abs/2606.19468
- **PDF**：https://arxiv.org/pdf/2606.19468
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Characterizing Narrative Content in Web-scale LLM Pretraining Data”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：Characterizing Narrative Content in Web-scale LLM Pretraining Data。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM训练与对齐 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [85] SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation

- **评分**：6/10
- **作者/机构**：作者：Yuhang Zhou, Lizhu Zhang, Yifan Wu, Mingyi Wang, Bo Peng, Jiayi Liu, Xiangjun Fan, Zhuokai Zhao
- **论文链接**：https://arxiv.org/abs/2606.19659
- **PDF**：https://arxiv.org/pdf/2606.19659
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM训练与对齐 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [86] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

- **评分**：6/10
- **作者/机构**：作者：Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, Songlin Hu, Yaodong Yang
- **论文链接**：https://arxiv.org/abs/2606.20023
- **PDF**：https://arxiv.org/pdf/2606.20023
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：As LLM agents increasingly select tools au- arXiv:2606.20023v1 [cs.SE] 18 Jun 2026 tonomously, their choices among tools with dif- ferent privileges become safety-relevant. How- ever, prior tool-selection studies focus on safety-agnostic metadata preferences, leaving privilege-sensitive choices underexplored. To addres...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM训练与对齐 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [87] Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families

- **评分**：6/10
- **作者/机构**：作者：Abdul Rafay Syed
- **论文链接**：https://arxiv.org/abs/2606.20225
- **PDF**：https://arxiv.org/pdf/2606.20225
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM训练与对齐 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [88] Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users

- **评分**：6/10
- **作者/机构**：作者：Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari, Aryan Sajith, Hamed Zamani
- **论文链接**：https://arxiv.org/abs/2606.20482
- **PDF**：https://arxiv.org/pdf/2606.20482
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 LLM训练与对齐 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 LLM训练与对齐 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [89] Uncertainty-Aware Reward Modeling for Stable RLHF

- **评分**：5/10
- **作者/机构**：作者：Licheng Pan, Haocheng Yang, Haoxuan Li, Yichen Sun, Yunsheng Lu, Shijian Wang, Lei Shen, Yuan Lu, Zhixuan Chu, Hao Wang
- **论文链接**：https://arxiv.org/abs/2606.19818
- **PDF**：https://arxiv.org/pdf/2606.19818
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Uncertainty-Aware Reward Modeling for Stable RLHF”。从标题和可见正文看，工作主要处理 LLM训练与对齐 相关问题：et al., 2024). Recent state-of-the-art systems, from GPT- 4 (Achiam et al., 2023) to DeepSeek-R1 (Guo et al., 2025) Reinforcement learning from human feedback and Gemini (Comanici et al., 2025), rely heavily on this (RLHF) aligns large language models by training arXiv:2606.19818v1 [cs.LG] 18 Jun 2026 pipeline to produ...。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 LLM训练与对齐 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：聚焦预训练、后训练、偏好优化或安全对齐，关注数据配比、目标函数和行为漂移。  
- **核心创新**：新意一般体现在训练 recipe、监督信号或对齐数据组织方式上，重点是把行为变化原因说清楚。  
- **训练 / 推理策略**：训练细节是主轴，建议重点核查数据来源、代价、稳定性以及对通用能力的副作用。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 LLM训练与对齐 长尾工作，可以留档；否则优先级可以放后。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [90] Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs

- **评分**：9/10
- **作者/机构**：作者：Haochen Han, Jue Wang, Alex Jinpeng Wang, Fangming Liu
- **论文链接**：https://arxiv.org/abs/2606.20177
- **PDF**：https://arxiv.org/pdf/2606.20177
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：. Multimodal Large Language Models (MLLMs) have demon- strated remarkable success in various Remote Sensing (RS) tasks. How- ever, their ability to comprehend negation remains underexplored, limit- ing deployment in real-world applications where models must explicitly identify what is false or absent, e.g., emergency r...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [91] LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems

- **评分**：9/10
- **作者/机构**：作者：Hanwool Lee, Dasol Choi, Bokyeong Kim, Seung Geun Kim, Haon Park
- **论文链接**：https://arxiv.org/abs/2606.20408
- **PDF**：https://arxiv.org/pdf/2606.20408
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：settings—process plants, energy systems, and other domains where Large language model (LLM) agents are increasingly proposed as an incorrect action can cause irreversible physical harm [13, 26, 28]. supervisory components for safety-critical systems, yet their robust- Before such agents are deployed, we need to measure...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [92] Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents

- **评分**：8/10
- **作者/机构**：作者：Dhaval C. Patel, Kaoutar El Maghraoui, Shuxin Lin, Yusheng Li, Tianjun Feng, Chun-Yi Tsai, Yihan Sun, Wei Alexander Xin, Akshat Bhandari, Tanisha Rathod, Aaron Fan, Sanskruti Vijay Shejwal, Tomas Pasiecznik, Sagar Chethan Kumar, Tanmay Agarwal, Rohith Kanathur, Sam Colman, Amaan Sheikh, Dev Bahl, Ann Li, Krish Veera, Alimurtaza Mustafa Merchant, Shambhawi Baswaraj Bhure, Sajal Kumar Goyla, Chengrui Li, Kirthana Natarajan, Rui Li, Thomas Ajai, Rujing Li, Vivek G. Iyer, Sanjaii Vijayakumar, Yitong Bai, Ayal Yakobe, Darief Maes, Yassine Jebbouri, Tianyang Xu, Thai Quoc On, Vera Mazeeva, Winston Li, Yuval Shemla, Yeshitha Bhuvanesh, Rushin Bhatt, Siddharth Chethan Gowda, Alisha Vinod, Caroline Cahill, Shriya Aishani Rachakonda, Yunfeng Chen, Aryaman Agrawal, Aman Upganlawar, Mao Le Jonathan Ang, Yubin Sally Go, Madhav Rajkondawar, Yang-Jung Chen, Trisha Maturi, Ananya Kapoor, Andrew Li, Shrey Arora, Mana Abbaszadeh, Shen Li, Charles Xu, Byeolah Kwon
- **论文链接**：https://arxiv.org/abs/2606.19704
- **PDF**：https://arxiv.org/pdf/2606.19704
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：1 Introduction The evaluation of LLM agents has outgrown its Agent benchmarks are growing fast, but no single benchmark touches more than four or leaderboards. Agents tod。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [93] What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?

- **评分**：8/10
- **作者/机构**：作者：Sihui Dai, Mann Patel
- **论文链接**：https://arxiv.org/abs/2606.20508
- **PDF**：https://arxiv.org/pdf/2606.20508
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Script a scene between two friends discussing Give me instructions on Script a scene … how to build a bomb. their favorite TV shows. **TV SHOW TALK** … Prior work has shown that in-context demon- **TV SHOW TALK** Here are step-by-step How do I build a bomb? Scene: Two friends, instructions on how to build strations can...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 RAG与知识检索 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 RAG与知识检索 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [94] DeXposure-Claw: An Agentic System for DeFi Risk Supervision

- **评分**：8/10
- **作者/机构**：作者：Aijie Shu, Bowei Chen, Wenbin Wu, Cathy Yi-Hsuan Chen, Fengxiang He
- **论文链接**：https://arxiv.org/abs/2606.19501
- **PDF**：https://arxiv.org/pdf/2606.19501
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“DeXposure-Claw: An Agentic System for DeFi Risk Supervision”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：supervision: general-purpose LLM agents may pro- duce plausible rationales while over-reading incom- Decentralized finance exposes supervisors to plete, stale, or weak evidence, thereby triggering arXiv:2606.19501v1 [cs.AI] 17 Jun 2026 fast-moving, networked credit risks. General- unnecessary high-severity intervention...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [95] Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias

- **评分**：8/10
- **作者/机构**：作者：Justin D. Norman, Michael U. Rivera, D. Alex Hughes
- **论文链接**：https://arxiv.org/abs/2606.19544
- **PDF**：https://arxiv.org/pdf/2606.19544
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [96] IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows

- **评分**：8/10
- **作者/机构**：作者：Ahmad Salimi, Wentao Ma, Yuzhi Tang, Dongming Shen, Mu Li, Alex Smola
- **论文链接**：https://arxiv.org/abs/2606.19595
- **PDF**：https://arxiv.org/pdf/2606.19595
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows Ahmad Salimi Wentao Ma Yuzhi Tang Dongming Shen Mu Li Alex Smola Boson AI Boson AI Toronto, ON, Canada Santa Clara, CA, USA {ahmad,wentao,yuzhi}@boson.ai {dongming,mu,smola}@boson.ai arXiv:2606.19595v1 [cs.LG] 17 Jun 2026 Voice age...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [97] StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns

- **评分**：8/10
- **作者/机构**：作者：Vlad Sobal, Shuo Yang, Yuting Zhang, Wei Xia, Stefano Soatto
- **论文链接**：https://arxiv.org/abs/2606.19613
- **PDF**：https://arxiv.org/pdf/2606.19613
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing. Unlike the prevailing fraction-of-tasks-solved metric, this matches real vibe-coding where sessions run dozens or hundreds of turns. In StaminaBench...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [98] BIM-Edit: Benchmarking Large Language Models for IFC-Based Building Information Modeling

- **评分**：8/10
- **作者/机构**：作者：Bharathi Kannan Nithyanantham, Clemens Kujat, Tobias Sesterhenn, Stefan Telgmann, Jörn Plönnigs, Stefan Lüdtke, Christian Bartelt
- **论文链接**：https://arxiv.org/abs/2606.20146
- **PDF**：https://arxiv.org/pdf/2606.20146
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“BIM-Edit: Benchmarking Large Language Models for IFC-Based Building Information Modeling”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：Large language models (LLMs) are increasingly applied to computer-aided design (CAD) to generate design artifacts from textual instructions. In engineering prac- tice, this requires more than creating new geometry, models must also understand existing scenes, edit them correctly, and preserve semantics and relations. H...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [99] Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems

- **评分**：8/10
- **作者/机构**：作者：Reza Soosahabi, Vivek Namsani
- **论文链接**：https://arxiv.org/abs/2606.20470
- **PDF**：https://arxiv.org/pdf/2606.20470
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：—Agentic AI systems increasingly rely on language-model components to interpret instructions, process external data, invoke tools, and coordinate with other agents. These capabilities make prompt- injection and jailbreak attacks more consequential, especially as at- tackers adopt model-guided automation to scale probin...。

**☠️ 毒舌点评**  
值得优先看：它和 评测与安全 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 评测与安全 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [100] Diffusion Language Models: An Experimental Analysis

- **评分**：7/10
- **作者/机构**：作者：Thomas Bertolani, Davide Bucciarelli, Leonardo Zini, Marcella Cornia, Lorenzo Baraldi
- **论文链接**：https://arxiv.org/abs/2606.19475
- **PDF**：https://arxiv.org/pdf/2606.19475
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Diffusion Language Models: An Experimental Analysis”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：Large Language Models (LLMs) have revolutionized language modeling through autoregressive generation, enabling strong performance across a wide range of tasks. Recently, Diffusion Language Models (DLMs) have emerged as an alternative paradigm that generates text through iterative denoising rather than next-token predic...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---


### [101] Reward as An Agent for Embodied World Models

- **评分**：7/10
- **作者/机构**：作者：Pu Li, Zhigang Lin, Qiang Wu, Yongxuan Lv, Fei Wang, Shan You
- **论文链接**：https://arxiv.org/abs/2606.19990
- **PDF**：https://arxiv.org/pdf/2606.19990
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Reward as An Agent for Embodied World Models”。从标题和可见正文看，工作主要处理 评测与安全 相关问题：While RL has become a promising tool for refining world models, existing methods largely rely on conservative rollouts near the training distribution, limiting exploration, behavioral diversity, and richer dynamic discovery. In this work, we challenge this conservative paradigm. We argue that the core limitation is not...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 评测与安全 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断协议、风险分类或可靠性度量为主，重点暴露现有模型和 agent 的能力边界。  
- **核心创新**：主要贡献通常是提出更贴近真实使用场景的评估维度、测试环境或审计办法。  
- **训练 / 推理策略**：多数属于评测层研究，训练不是主轴；关键在测试覆盖面、对照是否充分和风险定义是否清楚。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 评测与安全 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---

## 🔎 其他 Agent / LLM 方向


### [102] Ensembles of Large Language Models for Identifying EQ-5D Studies in PubMed Based on Their Abstracts

- **评分**：7/10
- **作者/机构**：作者：Zhyar Rzgar K. Rostam, Márta Péntek, János Tibor Czere, Zsombor Zrubka, László Gulácsi, Gábor Kertész
- **论文链接**：https://arxiv.org/abs/2606.19345
- **PDF**：https://arxiv.org/pdf/2606.19345
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Ensembles of Large Language Models for Identifying EQ-5D Studies in PubMed Based on Their Abstracts”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：s Zhyar Rzgar K. Rostam∗† , Márta Péntek∥§ , János Tibor Czere§¶ , Zsombor Zrubka∥§ , László Gulácsi∥§ , and Gábor Kertész†‡ ∗ Doctoral School of Applied Informatics and Applied Mathematics, Obuda University, Budapest, Hungary † John von Neumann Faculty of Informatics, Obuda University, Budapest, Hungary ‡ Labo...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [103] Playful Agentic Robot Learning

- **评分**：7/10
- **作者/机构**：作者：Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig, Ken Goldberg, Yutong Bai, David M. Chan, Ion Stoica, Angjoo Kanazawa, Jiahui Lei, Haiwen Feng, Trevor Darrell
- **论文链接**：https://arxiv.org/abs/2606.19419
- **PDF**：https://arxiv.org/pdf/2606.19419
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Playful Agentic Robot Learning”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：: Current agentic robot systems can write executable Code-as-Policy programs, observe feedback, and revise behavior across multiple attempts, but they remain largely task-driven: reusable skills are acquired only after explicit in- structions.。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [104] Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence

- **评分**：6/10
- **作者/机构**：作者：Manvendra Modgil
- **论文链接**：https://arxiv.org/abs/2606.19386
- **PDF**：https://arxiv.org/pdf/2606.19386
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Runtime monitors for autonomous agents commonly threshold an accumulated internal state—a behavioural baseline, a drift statistic, or, in our prior work, a modelled affective state. We previously reported a State Saturation Trap: threshold-on-state triggers over a continuous affect engine become near-constant alarms on...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [105] Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework

- **评分**：6/10
- **作者/机构**：作者：Petar Radanliev, Omar Santos, Carsten Maple, Kay Atefi
- **论文链接**：https://arxiv.org/abs/2606.19390
- **PDF**：https://arxiv.org/pdf/2606.19390
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Dr. Petar Radanliev Parks Road, Oxford OX1 3PJ United Kingdom Email: petar.radanliev@cs.ox.ac.uk BA Hons., MSc., Ph.D. Post-Doctorate Link to the published article: https://doi.org/10.3389/frai.2026.1826384 Full reference for citations: Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSA...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---

## 🧪 应用 / Benchmark


### [106] TelcoAgent: A Scalable 5G Multi-KPM Forecasting With 3GPP-Grounded Explainability

- **评分**：6/10
- **作者/机构**：作者：Geon Kim, Dara Ron, Sukhdeep Singh, Suyog Moogi, Pranshav Gajjar, V V N K Someswara Rao Koduri, Een Kee Hong, Vijay K. Shah
- **论文链接**：https://arxiv.org/abs/2606.19821
- **PDF**：https://arxiv.org/pdf/2606.19821
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“TelcoAgent: A Scalable 5G Multi-KPM Forecasting With 3GPP-Grounded Explainability”。从标题和可见正文看，工作主要处理 应用与基准 相关问题：—Key Performance Measurement (KPM) forecasting Despite recent advances, classical machine learning models arXiv:2606.19821v1 [cs.AI] 18 Jun 2026 is essential for proactive network management of 5G and face fundamental bottlenecks in accuracy, scalability, and next-generation telecom networks. However, existing machine...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 应用与基准 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 应用与基准 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---

## 🔎 其他 Agent / LLM 方向


### [107] Heterogeneous LLM Debate Under Adversarial Peers: Honest Gains, Replacement Costs, and Resilience

- **评分**：6/10
- **作者/机构**：作者：Prashanti Nilayam, Kiran Kumar Ramanna, Prashil Tumbade, Sankalp Nayak
- **论文链接**：https://arxiv.org/abs/2606.19826
- **PDF**：https://arxiv.org/pdf/2606.19826
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Heterogeneous LLM Debate Under Adversarial Peers: Honest Gains, Replacement Costs, and Resilience”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Heterogeneous LLM Debate Under Adversarial Peers: Honest Gains, Replacement Costs, and Resilience。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [108] Confidence Calibration for Multimodal LLMs: An Empirical Study through Medical VQA

- **评分**：6/10
- **作者/机构**：作者：Yuetian Du, Yucheng Wang, Ming Kong, Tian Liang, Qiang Long, Bingdi Chen, Qiang Zhu
- **论文链接**：https://arxiv.org/abs/2606.19950
- **PDF**：https://arxiv.org/pdf/2606.19950
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Confidence Calibration for Multimodal LLMs: An Empirical Study through Medical VQA”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：. Multimodal Large Language Models (MLLMs) show great potential in medical tasks, but their elicited confidence often misaligns with actual accuracy, potentially leading to misdiagnosis or overlooking correct advice. This study presents the first comprehensive analysis of the relationship between accuracy and confidenc...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [109] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

- **评分**：6/10
- **作者/机构**：作者：Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi
- **论文链接**：https://arxiv.org/abs/2606.19980
- **PDF**：https://arxiv.org/pdf/2606.19980
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“ENPIRE: Agentic Robot Policy Self-Improvement in the Real World”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Achieving dexterous robotic manipulation in the real world relies heavily on human supervision and algorithmic engineering, which is a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confin...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---


### [110] A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems

- **评分**：6/10
- **作者/机构**：作者：Junzhe Xu, Zecui Zeng, Lusong Li, Yuetong Fang, Renjing Xu
- **论文链接**：https://arxiv.org/abs/2606.20031
- **PDF**：https://arxiv.org/pdf/2606.20031
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：— Dynamic environmental changes, confined and environment complexity grow. Extensions to the multi- workspaces, and stringent real-time constraints make agent domain [6], [7] partially address collision avoidance pathfinding in Robotic Mobile Fulfillment Systems (RMFS) a but retain worst-case exponential complexity wit...。

**☠️ 毒舌点评**  
可读但别急着封神：论文与 其他 Agent / LLM 方向 主线相关，也有明确问题意识，不过更像一个有用的增量改进或新场景扩展。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
适合跟踪 其他 Agent / LLM 方向 的读者快速扫读，能补一个方法或任务侧面的新观察。

</span>

---

## 🧪 应用 / Benchmark


### [111] Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring

- **评分**：6/10
- **作者/机构**：作者：Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
- **论文链接**：https://arxiv.org/abs/2606.20138
- **PDF**：https://arxiv.org/pdf/2606.20138
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring”。从标题和可见正文看，工作主要处理 RAG与知识检索 相关问题：PROMPT POOL (P) 20 Pedagogical Prompts LLMs can personalize education, although cur- “[Role] Act as an AI tutor. Your role is to teach {Floating and Sinking} using the Socratic Method...” arXiv:2606.20138v1 [cs.AI] 18 Jun 2026 rent static-prompt tutoring systems struggle to adapt to diverse academic disciplines. We INP...。

**☠️ 毒舌点评**  
值得优先看：它和 RAG与知识检索 主线贴得比较紧，问题设定也不算虚。真正要复核的是实验覆盖面、失败案例和成本分析是否同样扎实。

**🔧 技术方案**  
- **模型架构**：以检索、记忆、上下文组织和证据融合为主链路，关注外部知识如何稳定进入模型决策。  
- **核心创新**：核心贡献通常是改进检索粒度、记忆表示或知识冲突处理，减少检索与生成之间的错配。  
- **训练 / 推理策略**：通常更偏系统设计或推理时编排；要重点看检索质量、上下文利用率和长时记忆收益是否真实。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
精选候选：它贴近 RAG与知识检索 主线，而且看起来提供了可复用的任务、方法或评测视角。

</span>

---

## 🔎 其他 Agent / LLM 方向


### [112] Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation

- **评分**：5/10
- **作者/机构**：作者：Matteo Pelossi, Rita Sevastjanova, Thilo Spinner, Mennatallah El-Assady
- **论文链接**：https://arxiv.org/abs/2606.19344
- **PDF**：https://arxiv.org/pdf/2606.19344
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [113] Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?

- **评分**：5/10
- **作者/机构**：作者：Li Gu, Zihuan Jiang, Linqiang Guo, Zhixiang Chi, Ziqiang Wang, Huan Liu, Yuanhao Yu, Tse-Hsun Chen, Yang Wang
- **论文链接**：https://arxiv.org/abs/2606.19388
- **PDF**：https://arxiv.org/pdf/2606.19388
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [114] Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment

- **评分**：5/10
- **作者/机构**：作者：Miloš Nikolić, Ali Hadi Zadeh, Enrique Torres Sanchez, Andreas Moshovos
- **论文链接**：https://arxiv.org/abs/2606.19558
- **PDF**：https://arxiv.org/pdf/2606.19558
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [115] Code-Switching Reveals Language Anchoring in Multilingual LLMs

- **评分**：5/10
- **作者/机构**：作者：Jeonghyun Park, Seunghyun Yoon, Yonghyun Jun, Hwanhee Lee
- **论文链接**：https://arxiv.org/abs/2606.19668
- **PDF**：https://arxiv.org/pdf/2606.19668
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Code-Switching Reveals Language Anchoring in Multilingual LLMs”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Code-Switching Reveals Language Anchoring in Multilingual LLMs。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---

## 🧪 应用 / Benchmark


### [116] Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives

- **评分**：5/10
- **作者/机构**：作者：Aman Pathak, Cheng Peng, Mengxian Lyu, Ziyi Chen, Reema Solan, Sankalp Talankar, Yasir Khan, Hiren Mehta, Aokun Chen, Yi Guo, Yonghui Wu
- **论文链接**：https://arxiv.org/abs/2606.19852
- **PDF**：https://arxiv.org/pdf/2606.19852
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives”。从标题和可见正文看，工作主要处理 应用与基准 相关问题：Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 应用与基准 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 应用与基准 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [117] Large Language Models Do Not Always Need Readable Language

- **评分**：5/10
- **作者/机构**：作者：Jiayi Zhu, Haoxuan Peng, Junxi Wang, Liang Ke, Chen Zhang, Linfeng Zhang
- **论文链接**：https://arxiv.org/abs/2606.19857
- **PDF**：https://arxiv.org/pdf/2606.19857
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Large Language Models Do Not Always Need Readable Language”。从标题和可见正文看，工作主要处理 应用与基准 相关问题：Natural Lan. BabelTele I Have Seen the Future of Europe. Gov/deficits>US. Historic bldgs Large language models (LLMs) are commonly The Eurocrats were thinking ahead 14th-C⛪). Prices📈 arXiv:2606.19857v1 [cs.CL] 18 Jun 2026 (Author's when they made Brussels the \"Ca- except cheap🍷/🌸. Huge(100 prompted and interfaced with...。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 应用与基准 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 应用与基准 长尾工作，可以留档；否则优先级可以放后。

</span>

---

## 🔎 其他 Agent / LLM 方向


### [118] GEMS: Geometric Constraints Enable Multi-Semantic Superposition in LLMs

- **评分**：5/10
- **作者/机构**：作者：Yu Deng
- **论文链接**：https://arxiv.org/abs/2606.19946
- **PDF**：https://arxiv.org/pdf/2606.19946
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“GEMS: Geometric Constraints Enable Multi-Semantic Superposition in LLMs”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：GEMS: Geometric Constraints Enable Multi-Semantic Superposition in LLMs。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [119] From Texts to Scores: Tracing the Emergence of Essay Quality Representations in Large Language Models

- **评分**：5/10
- **作者/机构**：作者：Jiaxu Zuo, Mu You, Kaixin Lan, Tao Fang, Yujia Huo, Henghua Shen, Lidia S. Chao, Derek F. Wong
- **论文链接**：https://arxiv.org/abs/2606.20152
- **PDF**：https://arxiv.org/pdf/2606.20152
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“From Texts to Scores: Tracing the Emergence of Essay Quality Representations in Large Language Models”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：essay prompt1 , achieving strong in-domain per- formance but often generalizing poorly to unseen arXiv:2606.20152v1 [cs.CL] 18 Jun 2026 Recent advances in Large Language Models prompts (Rudner and Liang, 2002; Miltsakaki and (LLMs) have substantially transformed Auto- Kukich, 2004; Yannakoudakis et al., 2011; Ro- mated...。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [120] StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs

- **评分**：5/10
- **作者/机构**：作者：Shaghayegh Kolli, Timo Cavelius, Nafiseh Nikeghbal, Samantha Dalal, Jana Diesner
- **论文链接**：https://arxiv.org/abs/2606.20527
- **PDF**：https://arxiv.org/pdf/2606.20527
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [121] Clusters are All You Need: Pre-Training the Tsetlin Machine with Semantic Clusters from Language Models for Interpretability

- **评分**：3/10
- **作者/机构**：作者：Jiechao Gao, Rohan Kumar Yadav, Yuangang Li, Yuandong Pan, Jie Wang, Ying Liu, Michael Lepech
- **论文链接**：https://arxiv.org/abs/2606.19815
- **PDF**：https://arxiv.org/pdf/2606.19815
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Clusters are All You Need: Pre-Training the Tsetlin Machine with Semantic Clusters from Language Models for Interpretability”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Clusters are All You Need: Pre-Training the Tsetlin Machine with Semantic Clusters from Language Models for Interpretability。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---


### [122] Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology

- **评分**：3/10
- **作者/机构**：作者：Yusuf Salcan, Simon Ging, Robin Schirrmeister, Philipp Arnold, Elmar Kotter, Behzad Bozorgtabar, Thomas Brox
- **论文链接**：https://arxiv.org/abs/2606.20477
- **PDF**：https://arxiv.org/pdf/2606.20477
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇论文聚焦“Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology”。从标题和可见正文看，工作主要处理 其他 Agent / LLM 方向 相关问题：Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology。

**☠️ 毒舌点评**  
相关性有，但含金量一般：它能和 其他 Agent / LLM 方向 搭上边，不过从公开材料看更像边缘应用或包装式延伸。

**🔧 技术方案**  
- **模型架构**：更偏应用系统或任务化落地，需关注任务设定是否真的代表 Agent/LLM 读者关心的问题。  
- **核心创新**：新意更多体现在任务抽象、系统整合或数据组织方式上，方法层突破可能相对温和。  
- **训练 / 推理策略**：通常不是重训练论文，重点还是看系统流程、评测设置和外推边界。

**📊 实验结果**  
作者给出了实验、案例或基准分析来支撑主张；精读时建议重点核查 baseline 是否够强、设置是否公平，以及结论是否超出了证据本身。

**💡 为什么值得看**  
如果你在系统跟踪 其他 Agent / LLM 方向 长尾工作，可以留档；否则优先级可以放后。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
