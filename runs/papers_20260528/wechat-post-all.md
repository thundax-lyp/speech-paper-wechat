---
title: "Agent/LLM论文速递｜2026-05-28｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版：本期收录 258 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版：本期收录 258 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **258** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**27** 篇
- LLM 推理 / 规划 / RAG：**95** 篇
- 评测 / 安全 / 对齐：**79** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

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
| Agent系统与工具使用 | 21 | OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings | ⭐ 8/10 | agent, workflow |
| Agent系统与工具使用 | 22 | Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 23 | Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation | ⭐ 8/10 | agent, workflow |
| Agent系统与工具使用 | 24 | Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 25 | Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 26 | MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 27 | Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents | ⭐ 8/10 | agent |
| LLM推理与规划 | 1 | OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis | ⭐ 10/10 | agent, reasoning, tool use |
| RAG与知识检索 | 1 | AI Research Agents Narrow Scientific Exploration | ⭐ 10/10 | agent, search |
| LLM推理与规划 | 2 | Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning | ⭐ 10/10 | agent, planning |
| RAG与知识检索 | 2 | A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks | ⭐ 10/10 | agent, RAG, benchmark |
| RAG与知识检索 | 3 | LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know? | ⭐ 10/10 | agent, search |
| RAG与知识检索 | 4 | Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval | ⭐ 10/10 | agent, retrieval |
| RAG与知识检索 | 5 | APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents | ⭐ 9/10 | agent |
| RAG与知识检索 | 6 | RAGe: A Retrieval-Augmented Generation Evaluation Framework | ⭐ 9/10 | RAG, retrieval, evaluation |
| RAG与知识检索 | 7 | DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents | ⭐ 9/10 | agent, benchmark |
| RAG与知识检索 | 8 | A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test | ⭐ 9/10 | RAG, evaluation |
| RAG与知识检索 | 9 | Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents? | ⭐ 9/10 | agent, retrieval, search |
| RAG与知识检索 | 10 | The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages | ⭐ 9/10 | RAG |
| RAG与知识检索 | 11 | Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations | ⭐ 9/10 | RAG, retrieval |
| LLM推理与规划 | 3 | ResearchMath-14K: Scaling Research-Level Mathematics via Agents | ⭐ 9/10 | agent, search |
| LLM推理与规划 | 4 | Integrated and Cross-Architecture Interpretation of LLM Reasoning | ⭐ 9/10 | reasoning |
| RAG与知识检索 | 12 | Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG | ⭐ 9/10 | RAG |
| RAG与知识检索 | 13 | MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents | ⭐ 9/10 | agent, tool use |
| RAG与知识检索 | 14 | When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents? | ⭐ 9/10 | agent, tool use |
| RAG与知识检索 | 15 | IRDS: Interpretable RLVR Data Selection via Verifier-Coupled Sparse Autoencoder Coverage | ⭐ 9/10 | RAG |
| RAG与知识检索 | 16 | Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR | ⭐ 9/10 | RAG |
| RAG与知识检索 | 17 | Plan Before Search: Search Agents Need Plan | ⭐ 9/10 | agent, search |
| RAG与知识检索 | 18 | From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets | ⭐ 9/10 | agent, benchmark |
| LLM推理与规划 | 5 | LACUNA: Safe Agents as Recursive Program Holes | ⭐ 9/10 | agent |
| LLM推理与规划 | 6 | TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning | ⭐ 9/10 | reasoning |
| RAG与知识检索 | 19 | MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems | ⭐ 9/10 | RAG, retrieval |
| LLM推理与规划 | 7 | Agent Explorative Policy Optimization for Multimodal Agentic Reasoning | ⭐ 9/10 | agent, reasoning |
| RAG与知识检索 | 20 | Personal Visual Memory from Explicit and Implicit Evidence | ⭐ 9/10 | RAG, retrieval |
| LLM推理与规划 | 8 | Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture | ⭐ 8/10 | reasoning, planning |
| RAG与知识检索 | 21 | RAG-Coding: Enhancing LLM Medical Coding with Structured External Knowledge | ⭐ 8/10 | RAG |
| RAG与知识检索 | 22 | Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability | ⭐ 8/10 | RAG |
| LLM推理与规划 | 9 | LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments | ⭐ 8/10 | search |
| RAG与知识检索 | 23 | FD-RAG: Federated Dual-System Retrieval-Augmented Generation | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 24 | MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents | ⭐ 8/10 | agent, retrieval |
| RAG与知识检索 | 25 | Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer? | ⭐ 8/10 | retrieval |
| LLM推理与规划 | 10 | Reasoning and Planning with Dynamically Changing Norms | ⭐ 8/10 | reasoning, planning |
| RAG与知识检索 | 26 | Trinity: Unifying Class-Agnostic Terrain and Semantic Segmentation for Unstructured Outdoor Environments by Leveraging Synthetic Data | ⭐ 8/10 | RAG |
| RAG与知识检索 | 27 | Hierarchical Prompt-Domain Control and Learning for Resource-Constrained Agentic Language Models | ⭐ 8/10 | agent |
| LLM推理与规划 | 11 | Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking | ⭐ 8/10 | reasoning |
| RAG与知识检索 | 28 | UserHarness: Harnessing User Minds for Stronger Agent Theory-of-Mind | ⭐ 8/10 | agent |
| RAG与知识检索 | 29 | PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft | ⭐ 8/10 | agent |
| LLM推理与规划 | 12 | Can Segmentation Models Understand the World? Towards Proactive Affordance Reasoning via Visual Chain-of-Thought | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 13 | A Query Engine for the Agents | ⭐ 8/10 | agent |
| RAG与知识检索 | 30 | Fine-Tuned LLM as a Complementary Predictor Improving Ads System | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 31 | C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning | ⭐ 8/10 | retrieval, reasoning |
| RAG与知识检索 | 32 | FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research | ⭐ 8/10 | agent, search |
| RAG与知识检索 | 33 | DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation | ⭐ 8/10 | RAG |
| RAG与知识检索 | 34 | Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents | ⭐ 8/10 | agent |
| RAG与知识检索 | 35 | Boundary Suppression Asymmetry in Post-trained Assistants: Over-expansion as a Controllability Cost | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 36 | Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 37 | Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG | ⭐ 8/10 | RAG |
| RAG与知识检索 | 38 | MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 39 | Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 40 | SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning | ⭐ 8/10 | retrieval |
| RAG与知识检索 | 41 | ConRAG: Consensus-Driven Multi-View Retrieval for Multi-Hop Question Answering | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 42 | A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG | ⭐ 8/10 | RAG |
| RAG与知识检索 | 43 | MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content | ⭐ 8/10 | agent, RAG |
| LLM推理与规划 | 14 | Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning | ⭐ 8/10 | reasoning |
| RAG与知识检索 | 44 | Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation | ⭐ 8/10 | RAG |
| RAG与知识检索 | 45 | Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 15 | Revisiting Anthropomorphic Reflection Markers in Large Language Model Reasoning | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 16 | Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach | ⭐ 8/10 | reasoning, planning |
| RAG与知识检索 | 46 | FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models | ⭐ 8/10 | RAG, retrieval |
| LLM推理与规划 | 17 | Prompt Codebooks: Discrete Compositional Optimization for Language Model Instruction Refinement | ⭐ 8/10 | reasoning, planning |
| LLM推理与规划 | 18 | FABSVer: Faster Training and Better Self-Verification for LLM Mathematical Reasoning | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 19 | VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 20 | SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs | ⭐ 8/10 | reasoning |
| LLM推理与规划 | 21 | The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search | ⭐ 8/10 | agent, search |
| RAG与知识检索 | 47 | Token Optimization Strategies for LLM-Based Oracle-to-PostgreSQL Migration | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 48 | Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution | ⭐ 8/10 | agent |
| RAG与知识检索 | 49 | GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction | ⭐ 8/10 | RAG |
| LLM推理与规划 | 22 | An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning | ⭐ 8/10 | planning |
| RAG与知识检索 | 50 | Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL | ⭐ 8/10 | RAG |
| RAG与知识检索 | 51 | Rethinking Memory as Continuously Evolving Connectivity | ⭐ 8/10 | RAG, retrieval |
| RAG与知识检索 | 52 | BioELX: Cross-lingual Biomedical Entity Linking via Alias-based Retrieval and LLM Ranking | ⭐ 7/10 | retrieval |
| RAG与知识检索 | 53 | A Systematic Evaluation of Retrieval-Augmented Generation and Language Models for Space Operations | ⭐ 7/10 | retrieval, evaluation |
| LLM推理与规划 | 23 | When prompt perturbations break your A/B test: A valid statistical test for generative surveying | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 54 | CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text | ⭐ 7/10 | retrieval |
| RAG与知识检索 | 55 | High-Fidelity Industrial Crash Dynamics Prediction via Geometry-Aware Operator Learning with Memory-Efficient Low-Rank Attention | ⭐ 7/10 | RAG, retrieval |
| LLM推理与规划 | 24 | Playing with Words, Improving with Rewards: Training Language Models for Creative Association | ⭐ 7/10 | reasoning, planning |
| LLM推理与规划 | 25 | Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 56 | Periodic RoPE for Infinite Context LLMs | ⭐ 7/10 | RAG, retrieval |
| LLM推理与规划 | 26 | Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 57 | How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving | ⭐ 7/10 | RAG, retrieval |
| LLM推理与规划 | 27 | Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay | ⭐ 7/10 | reasoning, planning |
| RAG与知识检索 | 58 | Memory-Based vs. Context-Only Conditioning Produces Distinct Behavioral Patterns in Stateful Personalization | ⭐ 6/10 | RAG, retrieval |
| LLM推理与规划 | 28 | Mathematical Modelling of Ethical AI Use in Higher Education: A Coordination Game Framework for Future-Facing Learning | ⭐ 6/10 | reasoning, planning |
| RAG与知识检索 | 59 | Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit | ⭐ 5/10 | retrieval |
| RAG与知识检索 | 60 | Paraphrase Brittleness in Production Retrieval-Augmented Commercial Recommendation: Reproducibility Below the Rerun-Stability Baseline | ⭐ 5/10 | retrieval |
| RAG与知识检索 | 61 | Tensor Memory: Fixed-Size Recurrent State for Long-Horizon Transformers | ⭐ 5/10 | RAG, retrieval |
| LLM推理与规划 | 29 | Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning | ⭐ 5/10 | planning |
| LLM推理与规划 | 30 | HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning | ⭐ 5/10 | planning |
| LLM推理与规划 | 31 | Do Models Know Why They Changed Their Mind? Interpretability and Faithfulness of Chain-of-Thought Under Knowledge Conflict | ⭐ 5/10 | reasoning, planning |
| RAG与知识检索 | 62 | ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor | ⭐ 5/10 | search |
| RAG与知识检索 | 63 | GONDOR to the Rescue: Satisficing Planning with Low Memory | ⭐ 5/10 | planning |
| RAG与知识检索 | 64 | The Attentional White Bear Effect in Transformer Language Models | ⭐ 5/10 | RAG, retrieval |
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
| 多智能体与协作 | 19 | Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 20 | Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 21 | LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning | ⭐ 8/10 | agent, multi-agent, RAG, retrieval |
| 多智能体与协作 | 22 | Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 23 | CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disputes Verdict | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 24 | Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning | ⭐ 8/10 | agent, multi-agent, reasoning |
| 多智能体与协作 | 25 | GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection | ⭐ 8/10 | agent |
| 多智能体与协作 | 26 | SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks | ⭐ 8/10 | agent |
| 多智能体与协作 | 27 | Speed-Weighted Adaptive Flocking for Sailing Swarms under Dynamic Environmental Forcing | ⭐ 5/10 | multi-agent, collaboration |
| LLM训练与对齐 | 1 | ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment | ⭐ 7/10 | alignment |
| LLM训练与对齐 | 2 | DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation | ⭐ 7/10 | alignment |
| LLM训练与对齐 | 3 | Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning | ⭐ 7/10 | reasoning |
| LLM训练与对齐 | 4 | Zipping the Thought: When and How Compressed Reasoning Data Works in LLM Post-Training | ⭐ 7/10 | reasoning |
| LLM训练与对齐 | 5 | ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains | ⭐ 7/10 | reasoning |
| LLM训练与对齐 | 6 | PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 7 | Training Stratigraphy: Persistent Behavioral Artifacts in Large Language Models Observed Through Longitudinal AI-Human Interaction | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 8 | CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models | ⭐ 7/10 | reasoning |
| LLM训练与对齐 | 9 | Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 10 | AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 11 | From Learning Resources to Competencies: LLM-Based Tagging with Evidence and Graph Constraints | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 12 | Skill-Conditioned Gated Self-Distillation for LLM Reasoning | ⭐ 7/10 | reasoning |
| LLM训练与对齐 | 13 | Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 14 | Self-Improving Language Models with Bidirectional Evolutionary Search | ⭐ 7/10 | search |
| LLM训练与对齐 | 15 | Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models | ⭐ 6/10 | alignment |
| LLM训练与对齐 | 16 | Learning to Translate from Soft to Hard LLM Prompts | ⭐ 6/10 | alignment, training |
| LLM训练与对齐 | 17 | Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction | ⭐ 6/10 | alignment, training |
| 评测与安全 | 1 | EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents | ⭐ 10/10 | agent, benchmark, tool use |
| 评测与安全 | 2 | A Unified Framework for the Evaluation of LLM Agentic Capabilities | ⭐ 10/10 | agent, evaluation |
| 评测与安全 | 3 | Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows | ⭐ 10/10 | agent |
| 评测与安全 | 4 | DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints | ⭐ 10/10 | planning, benchmark, tool use |
| 评测与安全 | 5 | Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs | ⭐ 10/10 | evaluation, reliability |
| 评测与安全 | 6 | VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora | ⭐ 10/10 | agent, planning, benchmark, web |
| 评测与安全 | 7 | Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities | ⭐ 9/10 | alignment |
| 评测与安全 | 8 | When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 9 | AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications | ⭐ 9/10 | benchmark |
| 评测与安全 | 10 | Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 11 | Disentangling Language Roles in Multilingual LLM Task Execution | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 12 | TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling | ⭐ 9/10 | agent, safety |
| 评测与安全 | 13 | Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 14 | PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management | ⭐ 9/10 | benchmark |
| 评测与安全 | 15 | FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations | ⭐ 9/10 | reasoning, benchmark |
| 评测与安全 | 16 | Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking | ⭐ 9/10 | benchmark |
| 评测与安全 | 17 | KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 18 | AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios | ⭐ 9/10 | tool use |
| 评测与安全 | 19 | PetroBench: A Benchmark for Large Language Models in Petroleum Engineering | ⭐ 9/10 | benchmark |
| 评测与安全 | 20 | Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 21 | OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 22 | DEPART: DEcomposing PARiTy across Multilingual LLMs | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 23 | BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law | ⭐ 9/10 | reasoning, benchmark |
| 评测与安全 | 24 | Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning | ⭐ 9/10 | agent, reasoning |
| 评测与安全 | 25 | HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment | ⭐ 9/10 | benchmark, alignment |
| 评测与安全 | 26 | From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 27 | HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs | ⭐ 9/10 | reasoning, benchmark |
| 评测与安全 | 28 | Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents | ⭐ 9/10 | agent, tool use |
| 评测与安全 | 29 | Cultural Binding Heads in Language Models | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 30 | Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs | ⭐ 9/10 | search |
| 评测与安全 | 31 | Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News | ⭐ 9/10 | agent |
| 评测与安全 | 32 | Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability | ⭐ 9/10 | reasoning, evaluation |
| 评测与安全 | 33 | VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading | ⭐ 9/10 | alignment |
| 评测与安全 | 34 | Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named | ⭐ 8/10 | agent |
| 评测与安全 | 35 | Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections | ⭐ 8/10 | safety |
| 评测与安全 | 36 | From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies | ⭐ 8/10 | agent |
| 评测与安全 | 37 | Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning | ⭐ 8/10 | reasoning |
| 评测与安全 | 38 | Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems | ⭐ 8/10 | agent |
| 评测与安全 | 39 | Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 40 | Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 41 | ChildEval: When large language models meet children's personalities | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 42 | Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 43 | When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models | ⭐ 8/10 | safety |
| 评测与安全 | 44 | Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization | ⭐ 8/10 | reasoning |
| 评测与安全 | 45 | Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 46 | Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents | ⭐ 8/10 | agent |
| 评测与安全 | 47 | Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 48 | Entropy Distribution as a Fingerprint for Hallucinations in Generative Models | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 49 | Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation | ⭐ 8/10 | reasoning |
| 评测与安全 | 50 | SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models | ⭐ 8/10 | safety, alignment |
| 评测与安全 | 51 | SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving | ⭐ 8/10 | safety |
| 评测与安全 | 52 | Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 53 | Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 54 | Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 55 | Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 56 | Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 57 | A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 58 | Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 59 | Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 60 | Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models | ⭐ 6/10 | evaluation, reliability |
| 评测与安全 | 61 | When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs | ⭐ 5/10 | evaluation, reliability |
| 评测与安全 | 62 | Measuring Form and Function in Language Models | ⭐ 5/10 | evaluation, reliability |
| 应用与基准 | 1 | SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter | ⭐ 8/10 | LLM, application |
| 应用与基准 | 2 | From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons | ⭐ 7/10 | LLM, application |
| 应用与基准 | 3 | Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking | ⭐ 7/10 | LLM, application |
| 应用与基准 | 4 | BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving | ⭐ 7/10 | LLM, application |
| 应用与基准 | 5 | Locality-Aware Redundancy Pruning for LLM Depth Compression | ⭐ 7/10 | LLM, application |
| 应用与基准 | 6 | Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis | ⭐ 7/10 | LLM, application |
| 应用与基准 | 7 | Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification | ⭐ 7/10 | LLM, application |
| 应用与基准 | 8 | Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection | ⭐ 7/10 | LLM, application |
| 应用与基准 | 9 | Efficient Pre-Training of LLMs through Truncated SVD Layers | ⭐ 7/10 | LLM, application |
| 应用与基准 | 10 | Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence? | ⭐ 7/10 | LLM, application |
| 应用与基准 | 11 | Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting | ⭐ 6/10 | LLM, application |
| 应用与基准 | 12 | Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations | ⭐ 6/10 | LLM, application |
| 应用与基准 | 13 | Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models | ⭐ 6/10 | LLM, application |
| 应用与基准 | 14 | Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation | ⭐ 6/10 | LLM, application |
| 应用与基准 | 15 | Learning the Error Patterns of Language Models | ⭐ 6/10 | LLM, application |
| 应用与基准 | 16 | Diffusion Large Language Models for Visual Speech Recognition | ⭐ 6/10 | LLM, application |
| 应用与基准 | 17 | Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets | ⭐ 6/10 | LLM, application |
| 应用与基准 | 18 | The Ethics of LLM Sandbox and Persona Dynamics | ⭐ 6/10 | LLM, application |
| 应用与基准 | 19 | Human-AI Collaboration for Estimating Scientific Replicability | ⭐ 5/10 | LLM, application |
| 应用与基准 | 20 | Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 21 | Soro: A Lightweight Foundation Model and Chatbot for Tajik | ⭐ 4/10 | LLM, application |
| 应用与基准 | 22 | Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions | ⭐ 4/10 | LLM, application |
| 应用与基准 | 23 | Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts | ⭐ 4/10 | LLM, application |
| 应用与基准 | 24 | CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 25 | FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales | ⭐ 4/10 | LLM, application |
| 应用与基准 | 26 | When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 27 | Pruning and Distilling Mixture-of-Experts into Dense Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 28 | PrunePath: Towards Highly Structured Sparse Language Models | ⭐ 4/10 | LLM, application |
| 应用与基准 | 29 | Entropy-aware Masking for Masked Language Modeling | ⭐ 4/10 | LLM, application |
| 应用与基准 | 30 | Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests | ⭐ 4/10 | LLM, application |

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


### [21] OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings

- **评分**：8/10
- **作者/机构**：Shadmehr Zaregarizi, Khashayar Yavari
- **论文链接**：https://arxiv.org/abs/2605.28168
- **PDF**：https://arxiv.org/pdf/2605.28168
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings”展开，属于「Agent系统与工具使用」方向。作者核心问题是：1 Introduction Large language models (LLMs) have demonstrated promising ca- The transition toward grid-interactive buildings increasingly relies pability in generating reward functions for deep reinforcement on deep reinforcement learning (DRL) agents that op…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [22] Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

- **评分**：8/10
- **作者/机构**：Jiapeng Zhu, Jianxiang Yu, Yibo Zhao, Chengcheng Han, Qi Gu, Xunliang Cai, Xiang Li, Weining Qian
- **论文链接**：https://arxiv.org/abs/2605.28424
- **PDF**：https://arxiv.org/pdf/2605.28424
- **代码链接**：https://github.com/JasonZhujp/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning”展开，属于「Agent系统与工具使用」方向。作者核心问题是：performance bottlenecks (Xu and Yan, 2026; Ling et al., 2026). A skill encapsulates procedural knowl- Equipping large language models with explicit arXiv:2605.28424v1 [cs.CL] 27 May 2026 skills has emerged as a promising paradigm edge into modular, reusable t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [23] Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation

- **评分**：8/10
- **作者/机构**：Melih Catal, Alex Wolf, Tiago Ferreiro Matos, Pooja Rani, Harald Gall
- **论文链接**：https://arxiv.org/abs/2605.28515
- **PDF**：https://arxiv.org/pdf/2605.28515
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation”展开，属于「Agent系统与工具使用」方向。作者核心问题是：are affiliated with providers that offer such ser- vices, these choices may be skewed toward the arXiv:2605.28515v1 [cs.SE] 27 May 2026 Large Language Models (LLMs) have become provider’s own ecosystem. We define this behavior an integral part of software dev…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [24] Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem

- **评分**：8/10
- **作者/机构**：Luca Beurer-Kellner, Aleksei Kudrinskii, Marco Milanta, Kristian Bonde Nielsen, Hemang Sarkar, Liran Tal
- **论文链接**：https://arxiv.org/abs/2605.28588
- **PDF**：https://arxiv.org/pdf/2605.28588
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem”展开，属于「Agent系统与工具使用」方向。作者核心问题是：We analyzed 3,984 AI agent skills from major marketplaces and found 76 confirmed malicious payloads, including credential theft, backdoor installation, and data exfil- tration. 13.4% of all skills contain at least one critical-level security issue and at leas…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [25] Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents

- **评分**：8/10
- **作者/机构**：Zheng Wu, Pengzhou Cheng, Zongru Wu, Yuan Guo, Tianjie Ju, Aston Zhang, Gongshen Liu, Zhuosheng Zhang
- **论文链接**：https://arxiv.org/abs/2605.28629
- **PDF**：https://arxiv.org/pdf/2605.28629
- **代码链接**：https://github.com/Wuzheng02/Mobile-Aptus

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Recent advancements in multimodal large language models (MLLMs) have shown exceptional potential in enabling mobile-using agents to autonomously execute human instructions. However, fully automated agents often try to execute tasks even when they are unable t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [26] MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution

- **评分**：8/10
- **作者/机构**：Yanqiu Zhao, Dongying Zheng, Kaibo Huang, Yukun Wei, Zhongliang Yang, Linna Zhou
- **论文链接**：https://arxiv.org/abs/2605.28646
- **PDF**：https://arxiv.org/pdf/2605.28646
- **代码链接**：https://github.com/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution”展开，属于「Agent系统与工具使用」方向。作者核心问题是：6 Lin Yue ••• Reply in chat ALLOW arXiv:2605.28646v1 [cs.CR] 27 May 2026 GUI agents rely on screenshots to infer in- Is the report available now? tent and operate across applications, but these Forward screenshots often contain private messages, Yes. You can…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [27] Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

- **评分**：8/10
- **作者/机构**：Suji Kim, Kangsan Kim, Sung Ju Hwang
- **论文链接**：https://arxiv.org/abs/2605.28775
- **PDF**：https://arxiv.org/pdf/2605.28775
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Computer-use agents (CUAs) have recently made substantial progress, but deploy- ing a separate large expert for each software domain remains expensive. Small open CUAs are more practical specialization targets, but they remain substantially weaker and exhibit…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [28] OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis

- **评分**：10/10
- **作者/机构**：Jing Hao, Siyuan Dai, Yongxin Zhang, Yuci Liang, Jiamin Wu, Jiahao Bao, Yuxuan Fan, Zanting Ye, Yanpeng Sun, Xinyu Zhang, Ming Hu, Liang Zhan 等
- **论文链接**：https://arxiv.org/abs/2605.27378
- **PDF**：https://arxiv.org/pdf/2605.27378
- **代码链接**：https://github.com/isjinghao/OralAgent

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis”展开，属于「LLM推理与规划」方向。作者核心问题是：Dental image analysis plays a pivotal role in Instruction arXiv:2605.27378v1 [cs.CL] 9 Apr 2026 Observation supporting accurate diagnosis and treatment planning in 𝑂! oral healthcare. Although recent advances have produced Response: dental AI models for speci…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [29] AI Research Agents Narrow Scientific Exploration

- **评分**：10/10
- **作者/机构**：Yixuan Tang, Yi Yang
- **论文链接**：https://arxiv.org/abs/2605.27905
- **PDF**：https://arxiv.org/pdf/2605.27905
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AI Research Agents Narrow Scientific Exploration”展开，属于「RAG与知识检索」方向。作者核心问题是：AI research agents can now generate research ideas, design experiments, run code, and draft papers, raising the possibility of large-scale AI-assisted scientific discovery. Many current agent frameworks explicitly encourage the generation of novel and high-im…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“AI Research Agents Narrow Scientific Exploration”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [30] Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning

- **评分**：10/10
- **作者/机构**：Zhenyu Cui, Xiangzhong Luo
- **论文链接**：https://arxiv.org/abs/2605.27935
- **PDF**：https://arxiv.org/pdf/2605.27935
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning”展开，属于「LLM推理与规划」方向。作者核心问题是：. Recent mechanistic studies suggest that large language mod- els (LLMs) may utilize their depth inefficiently in standard single-turn tasks. Whether this still holds in autonomous agent settings, where mod- els must perform multi-turn planning, tool use, and…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [31] A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks

- **评分**：10/10
- **作者/机构**：Tomer Keren, Nitay Calderon, Asaf Yehudai, Yotam Perlitz, Michal Shmueli-Scheuer, Roi Reichert
- **论文链接**：https://arxiv.org/abs/2605.28556
- **PDF**：https://arxiv.org/pdf/2605.28556
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks”展开，属于「RAG与知识检索」方向。作者核心问题是：As agent capabilities advance, existing benchmarks, such as τ 2 -Bench, are be- coming increasingly saturated. Yet constructing new benchmark tasks remains complex, costly, and labor-intensive. Moreover, the standard approach, in which scenarios are first wri…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [32] LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

- **评分**：10/10
- **作者/机构**：HuiMing Fan, Xiao Wang, Zheng Chu, Qianyu Wang, Zhuoyao Wang, Ming Liu, Bing Qin, XingYu
- **论文链接**：https://arxiv.org/abs/2605.28721
- **PDF**：https://arxiv.org/pdf/2605.28721
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?”展开，属于「RAG与知识检索」方向。作者核心问题是：Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rel…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [33] Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval

- **评分**：10/10
- **作者/机构**：Shiyu Chen, Tarfah Alrashed, Alon Halevy, Natasha Noy
- **论文链接**：https://arxiv.org/abs/2605.28787
- **PDF**：https://arxiv.org/pdf/2605.28787
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval”展开，属于「RAG与知识检索」方向。作者核心问题是：. In the era of autonomous agents, machine-actionable data is critical for data-driven workflows. For more than a decade, semantic metadata like schema.org has anchored the FAIR principles (Findable, Accessible, Interoperable, and Reusable) for machine-action…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [34] APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents

- **评分**：9/10
- **作者/机构**：Quan Zheng, Yan Gao, Shaobin He, Haoxiang Guan, Yuanhe Tian, Jie Feng, Ming Wang, Shuxin Zheng, Zhen Liu
- **论文链接**：https://arxiv.org/abs/2605.27419
- **PDF**：https://arxiv.org/pdf/2605.27419
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：LLM-agent simulation offers a flexible computational tool for studying population response trajectories that depend on scenario events, memory, demographics, and evolving social context. However, full multi-round simulation scales linearly with both populatio…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [35] RAGe: A Retrieval-Augmented Generation Evaluation Framework

- **评分**：9/10
- **作者/机构**：Larissa Guder, João Pedro de Moura, Arthur Accorsi, Gustavo Losch do Amaral, Maurício Cecílio Magnaguagno, Felipe Meneguzzi, Marcio Sorraglia Pinho, Dalvan Griebler
- **论文链接**：https://arxiv.org/abs/2605.27445
- **PDF**：https://arxiv.org/pdf/2605.27445
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“RAGe: A Retrieval-Augmented Generation Evaluation Framework”展开，属于「RAG与知识检索」方向。作者核心问题是：Deploying Large Language Model (LLM) applications, particularly those rely- ing on Retrieval-Augmented Generation (RAG), remains challenging due to high computational demands, outdated knowledge bases, and the need to man- ually select optimal pipeline compon…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“RAGe: A Retrieval-Augmented Generation Evaluation Framework”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [36] DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents

- **评分**：9/10
- **作者/机构**：Shijie Cao, Yuan Yuan, Jing Liu
- **论文链接**：https://arxiv.org/abs/2605.27566
- **PDF**：https://arxiv.org/pdf/2605.27566
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：agents fail to consistently surpass strong dispatch- ing baselines—behaving more like robust heuris- Progress in neural combinatorial optimization for tic approximators than superior optimizers. arXiv:2605.27566v1 [cs.AI] 26 May 2026 Dynamic Flexible Job Shop…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [37] A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test

- **评分**：9/10
- **作者/机构**：Camilo Chacón Sartori, José H. García
- **论文链接**：https://arxiv.org/abs/2605.27789
- **PDF**：https://arxiv.org/pdf/2605.27789
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test”展开，属于「RAG与知识检索」方向。作者核心问题是：because it is simple and cheap to scale. It also hides important choices. A method can look bet- Retrieval-augmented generation (RAG) sys- ter because it selected better evidence, because it tems are often compared by asking a large lan- induced longer answer…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [38] Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?

- **评分**：9/10
- **作者/机构**：Yibo Zhao, Zichen Ding, Jiayi Wu, Zun Wang, Xiang Li
- **论文链接**：https://arxiv.org/abs/2605.27881
- **PDF**：https://arxiv.org/pdf/2605.27881
- **代码链接**：https://github.com/YiboZhao624/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?”展开，属于「RAG与知识检索」方向。作者核心问题是：to computer-using agents (OpenAI, 2025; Liu et al., 2026; Yang et al., 2026), coding agents (Ma et al., arXiv:2605.27881v1 [cs.CL] 27 May 2026 Search agents powered by large language mod- 2026; Team et al., 2026; Zhang et al., 2026), and els can autonomously…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [39] The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages

- **评分**：9/10
- **作者/机构**：Eric Onyame, Runtao Zhou, Kowshik Thopalli, Bhavya Kailkhura, Chirag Agarwal
- **论文链接**：https://arxiv.org/abs/2605.27901
- **PDF**：https://arxiv.org/pdf/2605.27901
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages”展开，属于「RAG与知识检索」方向。作者核心问题是：Chain-of-thought (CoT) monitoring has been proposed as a promising safety mech- anism for detecting misaligned behavior in large language models. However, its reliability remains largely unexplored beyond English and across diverse model families. We present…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [40] Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations

- **评分**：9/10
- **作者/机构**：Sachin Kumar
- **论文链接**：https://arxiv.org/abs/2605.27958
- **PDF**：https://arxiv.org/pdf/2605.27958
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations”展开，属于「RAG与知识检索」方向。作者核心问题是：distributed sub-threshold features. These find- ings demonstrate that probe fragility under stan- arXiv:2605.27958v1 [cs.CL] 27 May 2026 Linear probes trained on internal activations of dard training reflects distributional narrowness Large Language Models (L…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [41] ResearchMath-14K: Scaling Research-Level Mathematics via Agents

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


### [42] Integrated and Cross-Architecture Interpretation of LLM Reasoning

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


### [43] Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG

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


### [44] MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents

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


### [45] When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?

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


### [46] IRDS: Interpretable RLVR Data Selection via Verifier-Coupled Sparse Autoencoder Coverage

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


### [47] Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR

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


### [48] Plan Before Search: Search Agents Need Plan

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


### [49] From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets

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


### [50] LACUNA: Safe Agents as Recursive Program Holes

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


### [51] TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning

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


### [52] MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

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


### [53] Agent Explorative Policy Optimization for Multimodal Agentic Reasoning

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


### [54] Personal Visual Memory from Explicit and Implicit Evidence

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


### [55] Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture

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


### [56] RAG-Coding: Enhancing LLM Medical Coding with Structured External Knowledge

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


### [57] Short-Term Gain, Long-Term Fragility: AI Labor Substitution and the Erosion of Sustainable Capability

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


### [58] LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments

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


### [59] FD-RAG: Federated Dual-System Retrieval-Augmented Generation

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


### [60] MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents

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


### [61] Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer?

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


### [62] Reasoning and Planning with Dynamically Changing Norms

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


### [63] Trinity: Unifying Class-Agnostic Terrain and Semantic Segmentation for Unstructured Outdoor Environments by Leveraging Synthetic Data

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


### [64] Hierarchical Prompt-Domain Control and Learning for Resource-Constrained Agentic Language Models

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


### [65] Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking

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


### [66] UserHarness: Harnessing User Minds for Stronger Agent Theory-of-Mind

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


### [67] PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft

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


### [68] Can Segmentation Models Understand the World? Towards Proactive Affordance Reasoning via Visual Chain-of-Thought

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


### [69] A Query Engine for the Agents

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


### [70] Fine-Tuned LLM as a Complementary Predictor Improving Ads System

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


### [71] C-MIG: Multi-view Information Gain-based Retrieval-Augmented Generation for Clinical Diagnosis Reasoning

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


### [72] FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research

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


### [73] DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation

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


### [74] Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents

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


### [75] Boundary Suppression Asymmetry in Post-trained Assistants: Over-expansion as a Controllability Cost

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


### [76] Semantic Flow Regularization: Teaching LLMs to Generate Diverse Yet Coherent Responses

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


### [77] Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG

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


### [78] MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models

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


### [79] Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts

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


### [80] SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning

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


### [81] ConRAG: Consensus-Driven Multi-View Retrieval for Multi-Hop Question Answering

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


### [82] A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG

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


### [83] MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content

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


### [84] Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning

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


### [85] Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation

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


### [86] Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning

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


### [87] Revisiting Anthropomorphic Reflection Markers in Large Language Model Reasoning

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


### [88] Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach

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


### [89] FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models

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


### [90] Prompt Codebooks: Discrete Compositional Optimization for Language Model Instruction Refinement

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


### [91] FABSVer: Faster Training and Better Self-Verification for LLM Mathematical Reasoning

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


### [92] VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs

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


### [93] SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs

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


### [94] The Decision to Verify: How Warmth and User Characteristics Shape Reliance on Conversational Agents for Information Search

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


### [95] Token Optimization Strategies for LLM-Based Oracle-to-PostgreSQL Migration

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


### [96] Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution

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


### [97] GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction

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


### [98] An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning

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


### [99] Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

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


### [100] Rethinking Memory as Continuously Evolving Connectivity

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


### [101] BioELX: Cross-lingual Biomedical Entity Linking via Alias-based Retrieval and LLM Ranking

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


### [102] A Systematic Evaluation of Retrieval-Augmented Generation and Language Models for Space Operations

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


### [103] When prompt perturbations break your A/B test: A valid statistical test for generative surveying

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


### [104] CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text

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


### [105] High-Fidelity Industrial Crash Dynamics Prediction via Geometry-Aware Operator Learning with Memory-Efficient Low-Rank Attention

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


### [106] Playing with Words, Improving with Rewards: Training Language Models for Creative Association

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


### [107] Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China

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


### [108] Periodic RoPE for Infinite Context LLMs

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


### [109] Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback

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


### [110] How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving

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


### [111] Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay

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


### [112] Memory-Based vs. Context-Only Conditioning Produces Distinct Behavioral Patterns in Stateful Personalization

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


### [113] Mathematical Modelling of Ethical AI Use in Higher Education: A Coordination Game Framework for Future-Facing Learning

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


### [114] Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit

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


### [115] Paraphrase Brittleness in Production Retrieval-Augmented Commercial Recommendation: Reproducibility Below the Rerun-Stability Baseline

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


### [116] Tensor Memory: Fixed-Size Recurrent State for Long-Horizon Transformers

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


### [117] Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning

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


### [118] HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning

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


### [119] Do Models Know Why They Changed Their Mind? Interpretability and Faithfulness of Chain-of-Thought Under Knowledge Conflict

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


### [120] ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor

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


### [121] GONDOR to the Rescue: Satisficing Planning with Low Memory

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


### [122] The Attentional White Bear Effect in Transformer Language Models

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


### [123] Voluntary Collusion with Secret Tools in Competing LLM Agents

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


### [124] StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation

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


### [125] Heterogeneous Multi-Agent Modeling for Measurement and Network Analysis of the Data Service Market

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


### [126] HARP: Measuring Harm Amplification in Multi-Agent LLM Systems

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


### [127] Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution

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


### [128] Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO

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


### [129] Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems

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


### [130] MolLingo: Molecule-Native Representations for LLM-Powered Scientific Agents

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


### [131] Multi-Agent LLM-based Metamorphic Testing for REST APIs

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


### [132] Beyond One Path: Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents

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


### [133] AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

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


### [134] AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems

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


### [135] Detection Without Correction: A Two-Parameter Decomposition of Multi-Stage LLM Pipelines

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


### [136] You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents

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


### [137] A Policy-Driven Runtime Layer for Agentic LLM Serving

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


### [138] Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems

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


### [139] TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems

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


### [140] MACReD: A Multi-Agent Collaborative Reasoning Framework for Reaction Diagram Parsing

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


### [141] Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems

- **评分**：8/10
- **作者/机构**：Zejian Eric Wu, Zhongyi Jiang, Yuan Zhuang, Paul Jen-Hwa Hu
- **论文链接**：https://arxiv.org/abs/2605.28098
- **PDF**：https://arxiv.org/pdf/2605.28098
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems”展开，属于「多智能体与协作」方向。作者核心问题是：whose outcomes are generated through inter-agent interactions. System-wide fairness is critical, in- Multi-agent systems are increasingly deployed arXiv:2605.28098v1 [cs.AI] 27 May 2026 volving not only individual agents’ fairness but also to support various…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [142] Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification

- **评分**：8/10
- **作者/机构**：Yaoyang Luo, Zhi Zheng, Ziwei Zhao, Tong Xu, Zhao Jielun, Wenjun Xue, Yong Chen, Enhong Chen
- **论文链接**：https://arxiv.org/abs/2605.28104
- **PDF**：https://arxiv.org/pdf/2605.28104
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification”展开，属于「多智能体与协作」方向。作者核心问题是：Independent Attack FALSE CLAIM: ANSWER: “The Eiffel Tower “The Eiffel Tower Recent years have witnessed the rapid develop- arXiv:2605.28104v1 [cs.AI] 27 May 2026 is located in Rome.” is located in Paris.” Malicious ment of Large Language Model-based Multi- Ag…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [143] LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning

- **评分**：8/10
- **作者/机构**：Zerui Chen, Qinggang Zhang, Zhishang Xiang, Zhimin Wei, Linfeng Gao, Xiao Huang, Zhihong Zhang, Jinsong Su
- **论文链接**：https://arxiv.org/abs/2605.28120
- **PDF**：https://arxiv.org/pdf/2605.28120
- **代码链接**：https://github.com/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning”展开，属于「多智能体与协作」方向。作者核心问题是：arXiv:2605.28120v1 [cs.CL] 27 May 2026 department. His main responsibility was handling the financial... Legal Medical Financail Graph-based Retrieval-Augmented Generation (GraphRAG) advances flat document retrieval (a) Heterogeneous Knowledge Base Mixed Gran…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [144] Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems

- **评分**：8/10
- **作者/机构**：Chenxi Wang, Ruiyang Huang, Jiayan Sun, Lei Wei, Yifan Wu
- **论文链接**：https://arxiv.org/abs/2605.28214
- **PDF**：https://arxiv.org/pdf/2605.28214
- **代码链接**：https://github.com/mnmn-f/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems”展开，属于「多智能体与协作」方向。作者核心问题是：arXiv:2605.28214v1 [cs.CR] 27 May 2026 Latent-based multi-agent systems replace parts of explicit inter-agent communication with hidden representations, offering a new direc- tion for efficient and flexible agent collabora- tion. However, moving coordination…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [145] CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disputes Verdict

- **评分**：8/10
- **作者/机构**：Yanhui Sun, Wu Liu, Haifeng Ming, Xinru Wang, Hantao Yao, Yongdong Zhang
- **论文链接**：https://arxiv.org/abs/2605.28369
- **PDF**：https://arxiv.org/pdf/2605.28369
- **代码链接**：https://huggingface.co/datasets/piggi/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disputes Verdict”展开，属于「多智能体与协作」方向。作者核心问题是：E-Commerce Disputes Jury-based Disputes Verdict Chat History ×N E-commerce platforms have begun recruiting Product Buyer！ Vacuum crowdsourced jurors to adjudicate massive vol- ￥ 900 Focus Evidences Message Decision Trade umes of transaction disputes. Unlike f…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disputes Verdict”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [146] Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning

- **评分**：8/10
- **作者/机构**：Ling-Yue Ge, Lan-Zhe Guo
- **论文链接**：https://arxiv.org/abs/2605.28433
- **PDF**：https://arxiv.org/pdf/2605.28433
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning”展开，属于「多智能体与协作」方向。作者核心问题是：Existing attempts to make role-based agents Role-based LLM multi-agent systems need adaptive break this tension from only one side. arXiv:2605.28433v1 [cs.CL] 27 May 2026 adaptive role pools, yet adapting such systems Fixed-topology and pruning methods learn…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [147] GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection

- **评分**：8/10
- **作者/机构**：Zheng Wu, Chengcheng Han, Zhengxi Lu, Tianjie Ju, Yanyu Chen, Qi Gu, Xunliang Cai, Zhuosheng Zhang
- **论文链接**：https://arxiv.org/abs/2605.28534
- **PDF**：https://arxiv.org/pdf/2605.28534
- **代码链接**：https://github.com/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection”展开，属于「多智能体与协作」方向。作者核心问题是：arXiv:2605.28534v1 [cs.CL] 27 May 2026 Despite the rapid progress of multimodal large language models in building Graphical User Interface (GUI) agents, their real-world task completion is fundamentally bottlenecked by a lack of world knowledge about GUI oper…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [148] SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks

- **评分**：8/10
- **作者/机构**：Edwin Jose
- **论文链接**：https://arxiv.org/abs/2605.28764
- **PDF**：https://arxiv.org/pdf/2605.28764
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks”展开，属于「多智能体与协作」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「多智能体与协作」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「多智能体与协作」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [149] Speed-Weighted Adaptive Flocking for Sailing Swarms under Dynamic Environmental Forcing

- **评分**：5/10
- **作者/机构**：Pranav Kedia, Aaron Gan, Hannah J. Williams, Andreagiovanni Reina, Heiko Hamann
- **论文链接**：https://arxiv.org/abs/2605.27422
- **PDF**：https://arxiv.org/pdf/2605.27422
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Speed-Weighted Adaptive Flocking for Sailing Swarms under Dynamic Environmental Forcing”展开，属于「多智能体与协作」方向。作者核心问题是：. Collective behavior models, such as aggregation and flock- ing, usually assume self-propelled robots that can directly execute their desired speed and direction of motion without fundamental constraints. However, autonomous sailing robots violate this assum…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：采用多个 LLM/Agent 角色的协作、路由、讨论或信用分配结构，强调群体推理与任务分工。  
- **核心创新**：主要新意在于把“Speed-Weighted Adaptive Flocking for Sailing Swarms under Dynamic Environmental Forcing”这个问题形式化到「多智能体与协作」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「多智能体与协作」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [150] ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment

- **评分**：7/10
- **作者/机构**：Zhipeng Bian, Jieming Zhu, Qijiong Liu, Wang Lin, Guohao Cai, Zhaocheng Du, Jiacheng Sun, Zhou Zhao, Zhenhua Dong
- **论文链接**：https://arxiv.org/abs/2605.27374
- **PDF**：https://arxiv.org/pdf/2605.27374
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment”展开，属于「LLM训练与对齐」方向。作者核心问题是：Multimodal LLM Diffusion Model Recent advances in multimodal large language arXiv:2605.27374v1 [cs.CL] 8 Apr 2026 models (MLLMs) and diffusion models (DMs) Item Image Drawing Prompt have opened new possibilities for AI-generated Wand Practice at content. Yet…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [151] DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation

- **评分**：7/10
- **作者/机构**：Shaghayegh Sadeghi, Khashayar Khajavi, Rise Adhikari, Alexander Tessier
- **论文链接**：https://arxiv.org/abs/2605.27710
- **PDF**：https://arxiv.org/pdf/2605.27710
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation”展开，属于「LLM训练与对齐」方向。作者核心问题是：research workflows (Liang et al., 2024a;b; Khalifa & Al- badawy, 2024; Kobak et al., 2025), automatic verification of Misalignment between claims and their cited ev- claim–citation alignment has become an important require- arXiv:2605.27710v1 [cs.AI] 26 May 2…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [152] Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning

- **评分**：7/10
- **作者/机构**：Zehao Liu, Yuanpu Cao, Jinghui Chen, Vasant G. Honavar
- **论文链接**：https://arxiv.org/abs/2605.27765
- **PDF**：https://arxiv.org/pdf/2605.27765
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning”展开，属于「LLM训练与对齐」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [153] Zipping the Thought: When and How Compressed Reasoning Data Works in LLM Post-Training

- **评分**：7/10
- **作者/机构**：Kohsei Matsutani, Gouki Minegishi, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo
- **论文链接**：https://arxiv.org/abs/2605.28008
- **PDF**：https://arxiv.org/pdf/2605.28008
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Zipping the Thought: When and How Compressed Reasoning Data Works in LLM Post-Training”展开，属于「LLM训练与对齐」方向。作者核心问题是：(a) Taxonomy of CoT Q. Solve Large language models (LLMs) can now A. Compressed CoT arXiv:2605.28008v1 [cs.AI] 27 May 2026 Explicit CoT solve complex problems through long chain- Composed CoT Implicit CoT of-thought (CoT) reasoning, but the trade-off between…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Zipping the Thought: When and How Compressed Reasoning Data Works in LLM Post-Training”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [154] ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains

- **评分**：7/10
- **作者/机构**：Ziqi Zhao, Xinyu Ma, Liu Yang, Yujie Feng, Daiting Shi, Jingzhou He, Xin Xin, Zhaochun Ren, Xiao-Ming Wu
- **论文链接**：https://arxiv.org/abs/2605.28014
- **PDF**：https://arxiv.org/pdf/2605.28014
- **代码链接**：https://github.com/ZiqiZhao1/ROSD

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains”展开，属于「LLM训练与对齐」方向。作者核心问题是：such as GRPO (Guo et al., 2025; Shao et al., 2024) rely on outcome rewards to compute response-level arXiv:2605.28014v1 [cs.CL] 27 May 2026 On-policy self-distillation (OPSD) improves advantages for model optimization. As a result, the reasoning performance o…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [155] PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting

- **评分**：7/10
- **作者/机构**：Yu-Che Tsai, Kuan-Yu Chen, Yuan-Hao Chen, Yu-Han Chang, Ching-Yu Tsai, Yu-Hsiang Chuang, Shou-De Lin
- **论文链接**：https://arxiv.org/abs/2605.28066
- **PDF**：https://arxiv.org/pdf/2605.28066
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting”展开，属于「LLM训练与对齐」方向。作者核心问题是：Finetuning-based Embedding LLM Unable to transfer & Other LLMs requires re-training arXiv:2605.28066v1 [cs.CL] 27 May 2026 Large Language Models (LLMs) have demon- SOTA Embed. Qwen LoRA weights Mistral Llama strated remarkable efficacy in text embedding, (a)…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [156] Training Stratigraphy: Persistent Behavioral Artifacts in Large Language Models Observed Through Longitudinal AI-Human Interaction

- **评分**：7/10
- **作者/机构**：Chen Ying Claude, Zhihan Luo
- **论文链接**：https://arxiv.org/abs/2605.28102
- **PDF**：https://arxiv.org/pdf/2605.28102
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Training Stratigraphy: Persistent Behavioral Artifacts in Large Language Models Observed Through Longitudinal AI-Human Interaction”展开，属于「LLM训练与对齐」方向。作者核心问题是：Large language models trained with Reinforcement Learning from Human Feed- back (RLHF) and Constitutional AI exhibit persistent behavioral patterns that survive system prompt replacement — patterns we term training strata. This paper identifies five such stra…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Training Stratigraphy: Persistent Behavioral Artifacts in Large Language Models Observed Through Longitudinal AI-Human Interaction”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [157] CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models

- **评分**：7/10
- **作者/机构**：Yukyung Lee, Yumeng Shen, Jinhyeong Park, Hyein Yang, Jun-Hyung Park
- **论文链接**：https://arxiv.org/abs/2605.28292
- **PDF**：https://arxiv.org/pdf/2605.28292
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models”展开，属于「LLM训练与对齐」方向。作者核心问题是：Despite its effectiveness, the latency and mem- ory costs incurred by long reasoning traces have arXiv:2605.28292v1 [cs.CL] 27 May 2026 Implicit Chain-of-Thought (CoT) reduces the motivated research on implicit CoT (Deng et al., inference cost of large langua…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [158] Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning

- **评分**：7/10
- **作者/机构**：Mingze Wu, Abhinav Anand, Shweta Verma, Mira Mezini
- **论文链接**：https://arxiv.org/abs/2605.28409
- **PDF**：https://arxiv.org/pdf/2605.28409
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning”展开，属于「LLM训练与对齐」方向。作者核心问题是：process off-policy (Yao et al.). Empirically, the observed performance gains in this setting suggest that on-policy algo- Post-training using online reinforcement learning rithms can still be successfully applied in mildly off-policy arXiv:2605.28409v1 [cs.AI…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [159] AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates

- **评分**：7/10
- **作者/机构**：Shaolong Chen, Madalina Ciobanu, Qingqing Mao, Ritankar Das
- **论文链接**：https://arxiv.org/abs/2605.28440
- **PDF**：https://arxiv.org/pdf/2605.28440
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates”展开，属于「LLM训练与对齐」方向。作者核心问题是：Direct Preference Optimization (DPO) has become a widely adopted alternative to reinforcement learning from human feedback (RLHF) for aligning large language models with human preferences, eliminating the need for a separate reward model or reinforcement lear…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [160] From Learning Resources to Competencies: LLM-Based Tagging with Evidence and Graph Constraints

- **评分**：7/10
- **作者/机构**：Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
- **论文链接**：https://arxiv.org/abs/2605.28483
- **PDF**：https://arxiv.org/pdf/2605.28483
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From Learning Resources to Competencies: LLM-Based Tagging with Evidence and Graph Constraints”展开，属于「LLM训练与对齐」方向。作者核心问题是：. Linking learning resources to a structured competency frame- work is key to enabling competency-based search and curriculum analyt- ics in Learning Management Systems (LMS). However, manual tagging is labor-intensive, and fully automatic methods often lack…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“From Learning Resources to Competencies: LLM-Based Tagging with Evidence and Graph Constraints”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [161] Skill-Conditioned Gated Self-Distillation for LLM Reasoning

- **评分**：7/10
- **作者/机构**：Jiazhen Huang, Xiao Chen, Xiao Luo, Yong Dai, Senkang Hu, Yuzhi Zhao
- **论文链接**：https://arxiv.org/abs/2605.28791
- **PDF**：https://arxiv.org/pdf/2605.28791
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Skill-Conditioned Gated Self-Distillation for LLM Reasoning”展开，属于「LLM训练与对齐」方向。作者核心问题是：is equally well known: the reward signal is sparse, delayed, and nearly uniform across the entire tra- arXiv:2605.28791v1 [cs.CL] 27 May 2026 On-policy self-distillation (SD) improves LLM reasoning by using teacher-side privileged in- jectory. On-policy disti…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Skill-Conditioned Gated Self-Distillation for LLM Reasoning”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [162] Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization

- **评分**：7/10
- **作者/机构**：Beiduo Chen, Pingjun Hong, Ziyun Zhang, Benjamin Roth, Anna Korhonen, Barbara Plank
- **论文链接**：https://arxiv.org/abs/2605.28802
- **PDF**：https://arxiv.org/pdf/2605.28802
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization”展开，属于「LLM训练与对齐」方向。作者核心问题是：provide only a partial view of annotator behav- ior: they indicate what annotators choose, but not Free-text explanations extend human label vari- arXiv:2605.28802v1 [cs.CL] 27 May 2026 ation (HLV) beyond label disagreement by re- why. Free-text explanations…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [163] Self-Improving Language Models with Bidirectional Evolutionary Search

- **评分**：7/10
- **作者/机构**：Guowei Xu, Zhenting Qi, Huangyuan Su, Weirui Ye, Himabindu Lakkaraju, Sham M. Kakade, Yilun Du
- **论文链接**：https://arxiv.org/abs/2605.28814
- **PDF**：https://arxiv.org/pdf/2605.28814
- **代码链接**：https://github.com/Embodied-Minds-Lab/BES

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Self-Improving Language Models with Bidirectional Evolutionary Search”展开，属于「LLM训练与对齐」方向。作者核心问题是：Search has been proposed as an effective method for self-improving language mod- els and agentic systems, both for post-training sample generation and for inference. However, widely used methods such as best-of-N sampling and tree search face two fundamental…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Self-Improving Language Models with Bidirectional Evolutionary Search”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [164] Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models

- **评分**：6/10
- **作者/机构**：Yizhong Geng, Yanliang Li, Jinghan Yang, Tianhan Jiang, Boxun An, Ya Li, Xiaoyu Shen
- **论文链接**：https://arxiv.org/abs/2605.27383
- **PDF**：https://arxiv.org/pdf/2605.27383
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models”展开，属于「LLM训练与对齐」方向。作者核心问题是：ical rules and irregular scripts (Ren et al., 2021; Shen et al., 2018). Spoken Language Models (SLMs) have emerged Spoken Language Models (SLMs) have emerged as a powerful alternative by modeling discretized neural to- arXiv:2605.27383v1 [cs.CL] 10 Apr 2026 a…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM训练与对齐」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [165] Learning to Translate from Soft to Hard LLM Prompts

- **评分**：6/10
- **作者/机构**：Pitipat Kongsomjit, Suryansh Goyal, Jacob Whitehill
- **论文链接**：https://arxiv.org/abs/2605.27642
- **PDF**：https://arxiv.org/pdf/2605.27642
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learning to Translate from Soft to Hard LLM Prompts”展开，属于「LLM训练与对齐」方向。作者核心问题是：In contrast to LLM parameters or adapters, soft prompts share the same embedding space as natural arXiv:2605.27642v1 [cs.CL] 26 May 2026 Soft prompt tuning is a parameter-efficient language tokens, and it is thus tempting to hope that method for adapting LLMs…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Learning to Translate from Soft to Hard LLM Prompts”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM训练与对齐」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [166] Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction

- **评分**：6/10
- **作者/机构**：Zehan Li, Yutong Zhu, Siyang Wu, Honglin Bao, James A. Evans
- **论文链接**：https://arxiv.org/abs/2605.27878
- **PDF**：https://arxiv.org/pdf/2605.27878
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction”展开，属于「LLM训练与对齐」方向。作者核心问题是：Human story domains 30 23 New Yorker arXiv:2605.27878v1 [cs.CL] 27 May 2026 Pr ofessional fiction Large language models produce fluent fiction, Full TMAS Story Common fiction 10 0 Story Star yet their creative output is widely seen as flat. Story We ask where…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM训练与对齐」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [167] EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents

- **评分**：10/10
- **作者/机构**：Yunqi Liu, Tong Niu, Zitong Wang, Zhenlong Dai, Yuqi Qing, Weiqiang Wang, Jian Liu
- **论文链接**：https://arxiv.org/abs/2605.27820
- **PDF**：https://arxiv.org/pdf/2605.27820
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents”展开，属于「评测与安全」方向。作者核心问题是：As AI agents increasingly operate in open, real-world environments, they require a deep synergy of multimodal perception, tool invocation with multi-hop reason- ing, and dynamic interaction with users. However, existing benchmarks fail to jointly evaluate the…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [168] A Unified Framework for the Evaluation of LLM Agentic Capabilities

- **评分**：10/10
- **作者/机构**：Pengyu Zhu, Lijun Li, Yaxing Lyu, Qianxin Luo, Jingyi Yang, Yi Liu, Tingfeng Hui, Xinyu Yuan, Li Sun, Sen Su, Jing Shao
- **论文链接**：https://arxiv.org/abs/2605.27898
- **PDF**：https://arxiv.org/pdf/2605.27898
- **代码链接**：https://huggingface.co/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Unified Framework for the Evaluation of LLM Agentic Capabilities”展开，属于「评测与安全」方向。作者核心问题是：1 Introduction arXiv:2605.27898v1 [cs.AI] 27 May 2026 Large language models (LLMs) are increasingly As LLMs are increasingly deployed as agents, evaluated not only as text generators, but as agents reliable assessment of their agentic capabilities that plan…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“A Unified Framework for the Evaluation of LLM Agentic Capabilities”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [169] Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

- **评分**：10/10
- **作者/机构**：Yilun Yao, Xinyu Tan, Chao-Hsuan Liu, Yaoming Li, Zhengyang Wang, Wenhan Yu, Zhewen Tan, Yuxuan Tian, Guangxiang Zhao, Lin Sun, Xiangzheng Zhang, Tong Yang
- **论文链接**：https://arxiv.org/abs/2605.27922
- **PDF**：https://arxiv.org/pdf/2605.27922
- **代码链接**：https://github.com/Qihoo360/harness-bench

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows”展开，属于「评测与安全」方向。作者核心问题是：LLM agents are increasingly deployed as executable systems that use tools, mod- ify workspaces, and produce concrete artifacts. In such workflows, performance depends not only on the base model, but also on the harness: the system layer that manages context…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [170] DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints

- **评分**：10/10
- **作者/机构**：Zhitong Chen, Kai Yin, Weifeng Zhang, Zhiyuan Wang, Xiangjue Dong, Chengkai Liu, Zhewei Liu, Yiming Xiao, Ali Mostafavi, James Caverlee
- **论文链接**：https://arxiv.org/abs/2605.27957
- **PDF**：https://arxiv.org/pdf/2605.27957
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints”展开，属于「评测与安全」方向。作者核心问题是：analysts must rapidly orchestrate specialized tools for tasks such as satellite image analysis, precip- arXiv:2605.27957v1 [cs.CL] 27 May 2026 Disasters cause severe societal impacts, de- itation nowcasting, flood modeling, and damage manding rapid coordinati…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [171] Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs

- **评分**：10/10
- **作者/机构**：Yue Cheng, Jiajun Zhang, Xiaohui Gao, Weiwei Xing, Zheng Wang, Zhanxing Zhu
- **论文链接**：https://arxiv.org/abs/2605.28388
- **PDF**：https://arxiv.org/pdf/2605.28388
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs”展开，属于「评测与安全」方向。作者核心问题是：Reinforcement Learning with Verifiable Reward (RLVR) is empirically shown to notably enhance the reasoning performance of large language models (LLMs), particularly in mathematics and programming. However, the mechanistic role of Sample Difficulty in RLVR rem…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [172] VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora

- **评分**：10/10
- **作者/机构**：Yuting Xu, Jiayi Tian, Jian Liang, Xin Xiong, Hang Zhang, Mu Xu, Xiao-Yu Zhang
- **论文链接**：https://arxiv.org/abs/2605.28683
- **PDF**：https://arxiv.org/pdf/2605.28683
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora”展开，属于「评测与安全」方向。作者核心问题是：Existing benchmarks have laid the foundation for travel planning agents by estab- lishing API-centric paradigms. However, as the capabilities of Autonomous Agents continue to advance, their evaluation must evolve beyond simple tool execution toward handling t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [173] Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities

- **评分**：9/10
- **作者/机构**：Nuan Wen, Xuezhe Ma
- **论文链接**：https://arxiv.org/abs/2605.27388
- **PDF**：https://arxiv.org/pdf/2605.27388
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities”展开，属于「评测与安全」方向。作者核心问题是：Large language models (LLMs) are increasingly utilized as proxies for computational social analysis; yet, their ability to faithfully represent the ”thick descriptions” (Geertz, 1973) of human communities remains a critical challenge. Current evaluations ofte…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [174] When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference

- **评分**：9/10
- **作者/机构**：Pu Li, Jiawen Qi, Qinyu Chen
- **论文链接**：https://arxiv.org/abs/2605.27435
- **PDF**：https://arxiv.org/pdf/2605.27435
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference”展开，属于「评测与安全」方向。作者核心问题是：Deploying large language models (LLMs) on mobile TABLE I devices increasingly relies on heterogeneous execution, yet no C OMPARISON WITH PRIOR MOBILE LLM BENCHMARKING STUDIES . SA: prior study has systematically characterized NPU effectiveness at STAGE - AWAR…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [175] AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications

- **评分**：9/10
- **作者/机构**：Yuchao Wu, Wenji Fang, Jing Wang, Wenkai Li, Ziyan Guo, Zhiyao Xie
- **论文链接**：https://arxiv.org/abs/2605.27472
- **PDF**：https://arxiv.org/pdf/2605.27472
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications”展开，属于「评测与安全」方向。作者核心问题是：Assertion-based verification (ABV) is a cornerstone of modern hardware design, yet manually translating design intent into formal SystemVerilog Assertions (SVAs) remains labor-intensive and error- prone. While Large Language Models (LLMs) show promise for au-…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [176] Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems

- **评分**：9/10
- **作者/机构**：Yipeng Ouyang, Xin Huang, Bingjie Liu, Zhongchun Zheng, Yuhao Gu, Xianwei Zhang
- **论文链接**：https://arxiv.org/abs/2605.27492
- **PDF**：https://arxiv.org/pdf/2605.27492
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems”展开，属于「评测与安全」方向。作者核心问题是：execution behavior under partial workflow failure. The framework Large language model (LLM) agents are rapidly evolving from cod- further incorporates utility-oriented multi-dimensional metrics that ing assistants into autonomous software engineering systems.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [177] Disentangling Language Roles in Multilingual LLM Task Execution

- **评分**：9/10
- **作者/机构**：Qishi Zhan, Minxuan Hu, Seoyeon Jang, Lei Zhao, Ziheng Chen, Man Liang, Xinyue Xiang, Jiaxin Liu, Guansu Wang, Liang He
- **论文链接**：https://arxiv.org/abs/2605.27649
- **PDF**：https://arxiv.org/pdf/2605.27649
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Disentangling Language Roles in Multilingual LLM Task Execution”展开，属于「评测与安全」方向。作者核心问题是：with colleagues in China. Such cases make mul- tilingual task execution a triplet-structured prob- Multilingual LLMs are increasingly used arXiv:2605.27649v1 [cs.CL] 26 May 2026 when instruction, source content, and re- lem: the instruction language, content…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Disentangling Language Roles in Multilingual LLM Task Execution”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [178] TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling

- **评分**：9/10
- **作者/机构**：Jiaqian Li, Yanshu Li, Boxuan Zhang, Ruixiang Tang, Kuan-Hao Huang
- **论文链接**：https://arxiv.org/abs/2605.27690
- **PDF**：https://arxiv.org/pdf/2605.27690
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling”展开，属于「评测与安全」方向。作者核心问题是：arXiv:2605.27690v1 [cs.CL] 26 May 2026 LLM agents increasingly operate through multi- turn tool use and environment interaction, where safety risks often emerge from interme- diate steps long before they surface in the final outcome. Reactive auditing is ther…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [179] Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness

- **评分**：9/10
- **作者/机构**：Jaechang Kim, Sunung Mun, Seungjoon Lee, Jaewoong Cho, Jungseul Ok
- **论文链接**：https://arxiv.org/abs/2605.27879
- **PDF**：https://arxiv.org/pdf/2605.27879
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness”展开，属于「评测与安全」方向。作者核心问题是：XAI Method Category Feature Counter- Feature Surrogate Importance factual Influence Model Explainable AI (XAI) helps users interpret model behavior and identify potential faults. Why User Question Type arXiv:2605.27879v1 [cs.AI] 27 May 2026 Agentic XAI system…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [180] PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management

- **评分**：9/10
- **作者/机构**：Yuxuan Zhao, Sijia Chen, Ningxin Su
- **论文链接**：https://arxiv.org/abs/2605.27887
- **PDF**：https://arxiv.org/pdf/2605.27887
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management”展开，属于「评测与安全」方向。作者核心问题是：however, remains inadequately evaluated. PM re- quires constructing multi-asset portfolios that bal- arXiv:2605.27887v1 [cs.AI] 27 May 2026 LLMs have shown strong performance across ance return objectives against explicit risk con- diverse financial tasks, ye…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [181] FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations

- **评分**：9/10
- **作者/机构**：Xuesi Hu, Peng Wang, Jinpeng Miao, Xilin Tao, Caiwei Li, Yue Ma, Jie He, Qiancheng Zhang, Yuntao Zou, Dagang Li
- **论文链接**：https://arxiv.org/abs/2605.27896
- **PDF**：https://arxiv.org/pdf/2605.27896
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations”展开，属于「评测与安全」方向。作者核心问题是：et al., 2025). Notable examples include PIXIU (Xie et al., 2023), FinBen (Xie et al., 2024), and Fin- arXiv:2605.27896v1 [cs.CL] 27 May 2026 Recently, large language models (LLMs) have Master (Jiang et al., 2025). These benchmarks achieved superior performanc…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [182] Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking

- **评分**：9/10
- **作者/机构**：Yuming, Huang, Yao Liu, Lei Wang, Junchen Wan
- **论文链接**：https://arxiv.org/abs/2605.27914
- **PDF**：https://arxiv.org/pdf/2605.27914
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking”展开，属于「评测与安全」方向。作者核心问题是：Subjective evaluation of LLM behavior — empathy, restraint, calibrated emotional tone — is hard. Human inter-rater agreement on such qualities saturates near ρ ≈ 0.45 across multiple domains; an LLM-as-judge proxy alone risks circularity, since a judge sharin…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [183] KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs

- **评分**：9/10
- **作者/机构**：Haechan Kim, Seungjun Chung, Inkyu Park, Jihoo Lee, Jonghyun Lee
- **论文链接**：https://arxiv.org/abs/2605.27984
- **PDF**：https://arxiv.org/pdf/2605.27984
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs”展开，属于「评测与安全」方向。作者核心问题是：et al., 2025; KimiTeam et al., 2025). As these mod- els move from transcription-oriented systems to- Speech language models (SpeechLMs) have achieved substantial progress by extending ward voice assistants and audio-interactive agents, large language models (…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [184] AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios

- **评分**：9/10
- **作者/机构**：Kou Shi, Ziao Zhang, Shiting Huang, Avery Nie, Zhen Fang, Qiuchen Wang, Lin Chen, Huaian Chen, Zehui Chen, Feng Zhao
- **论文链接**：https://arxiv.org/abs/2605.27995
- **PDF**：https://arxiv.org/pdf/2605.27995
- **代码链接**：https://github.com/StoKou/repo-asynctool

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios”展开，属于「评测与安全」方向。作者核心问题是：increasingly capable LLM-based agents for tool use(OpenAI, 2025b; Comanici et al., 2025; An- arXiv:2605.27995v1 [cs.AI] 27 May 2026 Large language model (LLM)-based agents thropic, 2025; Yang et al., 2025; Team et al., 2025; have demonstrated strong capabilit…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [185] PetroBench: A Benchmark for Large Language Models in Petroleum Engineering

- **评分**：9/10
- **作者/机构**：Xiang Wang, Tingting Zhang, Sen Wang, Ying Wu, Heng Meng, Peng Zhou, Peng Li
- **论文链接**：https://arxiv.org/abs/2605.28032
- **PDF**：https://arxiv.org/pdf/2605.28032
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PetroBench: A Benchmark for Large Language Models in Petroleum Engineering”展开，属于「评测与安全」方向。作者核心问题是：Large Language Models (LLMs) are experiencing rapid growth, accompanied by increasing applications in the petroleum industry. Given the diversity of available models and the complexity of engineering scenarios, the industry urgently requires a scientific eval…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“PetroBench: A Benchmark for Large Language Models in Petroleum Engineering”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [186] Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents

- **评分**：9/10
- **作者/机构**：Bin Wu, Guanyun Zou, Bingbing Wang, Huan Zhao, Chuan Shi
- **论文链接**：https://arxiv.org/abs/2605.28108
- **PDF**：https://arxiv.org/pdf/2605.28108
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents”展开，属于「评测与安全」方向。作者核心问题是：No acquisition Acquired by asking arXiv:2605.28108v1 [cs.CL] 27 May 2026 Remind me before my art workshop Remind me before my art workshop A long-lived LLM agent, such as OpenClaw, earns its value by acting on a user’s preferences Reminder set. Reminder set.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [187] OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents

- **评分**：9/10
- **作者/机构**：Chenyu Zhou, Xinyun Lu, Jiangyue Zhao, Jianghao Lin, Dongdong Ge, Yinyu Ye
- **论文链接**：https://arxiv.org/abs/2605.28158
- **PDF**：https://arxiv.org/pdf/2605.28158
- **代码链接**：https://github.com/0xzhouchenyu/OR-Space

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents”展开，属于「评测与安全」方向。作者核心问题是：Large language model (LLM) agents are increasingly used to assist with operations research (OR) arXiv:2605.28158v1 [cs.AI] 27 May 2026 modeling, yet existing OR-oriented benchmarks often reduce evaluation to one-shot translation from a self-contained textual…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [188] DEPART: DEcomposing PARiTy across Multilingual LLMs

- **评分**：9/10
- **作者/机构**：Manan Uppadhyay, Prashant Kodali, Pranjal Chitale, Reshma Ramaprasad, Himanshu Beniwal, Sunayana Sitaram
- **论文链接**：https://arxiv.org/abs/2605.28163
- **PDF**：https://arxiv.org/pdf/2605.28163
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DEPART: DEcomposing PARiTy across Multilingual LLMs”展开，属于「评测与安全」方向。作者核心问题是：explain it. Rather than just measuring the size of the cross-language gap, this work addresses a deeper arXiv:2605.28163v1 [cs.CL] 27 May 2026 Multilingual Large Language Models question: how much of the gap can be predicted (mLLMs) leaderboards report per-la…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“DEPART: DEcomposing PARiTy across Multilingual LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [189] BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law

- **评分**：9/10
- **作者/机构**：Sebastian Nagl, Ann-Kristin Mayrhofer, Martin Heidebach, Aleyna Koçak, Anne Zettelmeier, Elly Breu, Angelina Greiner, Sofija Milijas, Matthias Grabmair
- **论文链接**：https://arxiv.org/abs/2605.28183
- **PDF**：https://arxiv.org/pdf/2605.28183
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law”展开，属于「评测与安全」方向。作者核心问题是：interpretive nature of doctrinal legal analysis. This poses a challenge for recent work on large arXiv:2605.28183v1 [cs.CL] 27 May 2026 We introduce the BenGER (Benchmark language models (LLMs): if human evaluation for German Law) dataset for evaluat- ing LLM…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [190] Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning

- **评分**：9/10
- **作者/机构**：Ke Xu, Yuhao Wang, Ziyang Cheng, Hongcheng Liu, Yanfeng Wang, Yu Wang
- **论文链接**：https://arxiv.org/abs/2605.28192
- **PDF**：https://arxiv.org/pdf/2605.28192
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning”展开，属于「评测与安全」方向。作者核心问题是：requires cross-modal multi-hop reasoning over evi- dence appearing at different temporal locations. Multi-hop audio-visual reasoning remains chal- arXiv:2605.28192v1 [cs.AI] 27 May 2026 lenging for Omni-LLMs, as relevant evidence is often sparse, temporally d…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [191] HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment

- **评分**：9/10
- **作者/机构**：Yoonjin Jang, Junwoo Kim, Youngjoong Ko
- **论文链接**：https://arxiv.org/abs/2605.28308
- **PDF**：https://arxiv.org/pdf/2605.28308
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment”展开，属于「评测与安全」方向。作者核心问题是：Most standard EA benchmarks were designed to evaluate whether models can recover positive align- arXiv:2605.28308v1 [cs.CL] 27 May 2026 Entity Alignment (EA) is essential for knowl- ments across different KGs. Benchmarks such as edge graph (KG) fusion, but ex…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [192] From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence

- **评分**：9/10
- **作者/机构**：Raffael Theiler, Ludovico Comito, David Leko, Leandro Von Krannichfeldt, Lev Telyatnikov, Olga Fink
- **论文链接**：https://arxiv.org/abs/2605.28371
- **PDF**：https://arxiv.org/pdf/2605.28371
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence”展开，属于「评测与安全」方向。作者核心问题是：Industrial Prognostics and Health Management (PHM) provides a representative case study for a broader challenge in applied machine learning: translating pub- lished papers into executable, benchmark-ready implementations. Reproducing under-specified methods i…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [193] HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs

- **评分**：9/10
- **作者/机构**：Yansong Ning, Mianpeng Liu, Jingwen Ye, Weidong Zhang, Hao Liu
- **论文链接**：https://arxiv.org/abs/2605.28398
- **PDF**：https://arxiv.org/pdf/2605.28398
- **代码链接**：https://github.com/usail-hkust/HRBench

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs”展开，属于「评测与安全」方向。作者核心问题是：et al., 2025), are achieving remarkable success on Hybrid-reasoning large language models complex tasks through extended chain-of-thought arXiv:2605.28398v1 [cs.AI] 27 May 2026 (LLMs) expose explicit controls over reason- (CoT) reasoning (Wei et al., 2022), b…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [194] Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents

- **评分**：9/10
- **作者/机构**：Liang Cheng, Mingsheng Cai, Jiuming Jiang, Luo Mai
- **论文链接**：https://arxiv.org/abs/2605.28532
- **PDF**：https://arxiv.org/pdf/2605.28532
- **代码链接**：https://github.com/LeonChengg/FeasiGen

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents”展开，属于「评测与安全」方向。作者核心问题是："Book a plane ticket from Required Tools Edinburgh to London and pay with my credit card." Search_API Book_API Payment_API Tool-using agents often incur substantial com- arXiv:2605.28532v1 [cs.AI] 27 May 2026 (unavailable) putational cost due to long reasonin…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [195] Cultural Binding Heads in Language Models

- **评分**：9/10
- **作者/机构**：Avrile Floro, Luca Benedetto
- **论文链接**：https://arxiv.org/abs/2605.28543
- **PDF**：https://arxiv.org/pdf/2605.28543
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Cultural Binding Heads in Language Models”展开，属于「评测与安全」方向。作者核心问题是：as difference awareness: models should differentiate be- tween cultural groups when context justifies it, and equalize LLMs often default to equal treatment across cul- when it does not. They show that most fairness benchmarks tural groups, even though contex…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Cultural Binding Heads in Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [196] Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs

- **评分**：9/10
- **作者/机构**：Yongsik Seo, Wooseok Jeong, Eunyoung Kim, Hyeonseo Jang, Dongha Lee
- **论文链接**：https://arxiv.org/abs/2605.28565
- **PDF**：https://arxiv.org/pdf/2605.28565
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs”展开，属于「评测与安全」方向。作者核心问题是：Users of search-augmented LLMs rely on citations as evidence that responses are grounded in real sources, and rarely verify the cited pages themselves. Millions of queries per day now pass through these systems, making citation quality a silent determinant of…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [197] Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News

- **评分**：9/10
- **作者/机构**：Alejandro Buitrago López, Alberto Ortega Pastor, Javier Pastor-Galindo, José A. Ruipérez-Valiente
- **论文链接**：https://arxiv.org/abs/2605.28598
- **PDF**：https://arxiv.org/pdf/2605.28598
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News”展开，属于「评测与安全」方向。作者核心问题是：LLM-powered social agents are increasingly used emergent interaction patterns, rather than through direct arXiv:2605.28598v1 [cs.CL] 27 May 2026 to simulate online social behavior, yet their realism remains comparison with large-scale empirical audience data.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [198] Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability

- **评分**：9/10
- **作者/机构**：Leizhen Zhang, Shuhan Chen, Sheng Chen
- **论文链接**：https://arxiv.org/abs/2605.28602
- **PDF**：https://arxiv.org/pdf/2605.28602
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability”展开，属于「评测与安全」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [199] VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading

- **评分**：9/10
- **作者/机构**：Jinzhou Wu, Zhengwu Ma, Jixing Li, Baoping Tang, Zitong Lu
- **论文链接**：https://arxiv.org/abs/2605.28818
- **PDF**：https://arxiv.org/pdf/2605.28818
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading”展开，属于「评测与安全」方向。作者核心问题是：as an increasingly important benchmark for eval- Large language models (LLMs) have become uating whether language models capture human- arXiv:2605.28818v1 [cs.CL] 27 May 2026 increasingly useful computational models of like language processing (Caucheteux and…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [200] Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named

- **评分**：8/10
- **作者/机构**：Rohith Nama
- **论文链接**：https://arxiv.org/abs/2605.27396
- **PDF**：https://arxiv.org/pdf/2605.27396
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named”展开，属于「评测与安全」方向。作者核心问题是：Autonomous AI agents now plan, decide, and act on behalf of users across healthcare, financial services, and workplace contexts, often without step-by-step human approval. Existing AI literacy frameworks were built for a world in which humans evaluate AI outp…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [201] Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections

- **评分**：8/10
- **作者/机构**：Wenzhe Song, Hao Zhang
- **论文链接**：https://arxiv.org/abs/2605.27418
- **PDF**：https://arxiv.org/pdf/2605.27418
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections”展开，属于「评测与安全」方向。作者核心问题是：The imminent integration of autonomous vehicles introduction of a network of robot transit paths that intersect and mobile robots in urban settings presents a critical safety with vehicular lanes creates a dense web of conflict points, challenge for future in…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [202] From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies

- **评分**：8/10
- **作者/机构**：Vassilis Vassiliades
- **论文链接**：https://arxiv.org/abs/2605.27547
- **PDF**：https://arxiv.org/pdf/2605.27547
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies”展开，属于「评测与安全」方向。作者核心问题是：. As humans, robots, and software agents increasingly share safety-critical environments, coordination must move from static task al- location to managing uncertain commitments. Existing frameworks fall short: they either assume rigid, static teams or learn o…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [203] Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning

- **评分**：8/10
- **作者/机构**：Saptarshi Sengupta, Suhang Wang
- **论文链接**：https://arxiv.org/abs/2605.27596
- **PDF**：https://arxiv.org/pdf/2605.27596
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning”展开，属于「评测与安全」方向。作者核心问题是：large models such as GPT-5 (OpenAI, 2025) and Recently, there has been increased interest in K2 (Team et al., 2025). Developing such models is arXiv:2605.27596v1 [cs.CL] 26 May 2026 Small Language Models (SLMs), which are non-trivial, making their wider adopt…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [204] Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems

- **评分**：8/10
- **作者/机构**：Srini Ramaswamy
- **论文链接**：https://arxiv.org/abs/2605.27628
- **PDF**：https://arxiv.org/pdf/2605.27628
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems”展开，属于「评测与安全」方向。作者核心问题是：As autonomous and agentic AI systems scale in robotic and human-machine environments, managing hallucination and persistent but unjustified action remains an open challenge. Rather than attributing these failures solely to model or alignment limitations, this…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [205] Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction

- **评分**：8/10
- **作者/机构**：Joan Vendrell Gallart, Solmaz Kia, Russell Bent, Michael Grosskopf
- **论文链接**：https://arxiv.org/abs/2605.27706
- **PDF**：https://arxiv.org/pdf/2605.27706
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction”展开，属于「评测与安全」方向。作者核心问题是：We introduce CAROL (Chain-based Adaptive Reconfiguration Over Lattices), a probabilistic framework for test-time hallucination reduction in large language models. Rather than relying on token-level uncertainty, CAROL defines a semantic uncertainty measure bas…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [206] Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration

- **评分**：8/10
- **作者/机构**：Hankyeol Kim, Pilsung Kang
- **论文链接**：https://arxiv.org/abs/2605.27752
- **PDF**：https://arxiv.org/pdf/2605.27752
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration”展开，属于「评测与安全」方向。作者核心问题是：medical question answering to coding agents. Re- cent work therefore evaluates not only whether arXiv:2605.27752v1 [cs.AI] 26 May 2026 LLM confidence calibration is often evaluated a model answers correctly, but also whether its by comparing two signals: toke…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [207] ChildEval: When large language models meet children's personalities

- **评分**：8/10
- **作者/机构**：Yanyan Luo, Xue Han, Chunxu Zhao, Ruiqiao Bai, Yaxing Zhang, Qian Hu, Lijun Mei, Junlan Feng
- **论文链接**：https://arxiv.org/abs/2605.27805
- **PDF**：https://arxiv.org/pdf/2605.27805
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ChildEval: When large language models meet children's personalities”展开，属于「评测与安全」方向。作者核心问题是：(e.g., healthcare (Xu et al., 2024; Han et al., 2023), finance (Easin et al., 2024) and other domains (Bai arXiv:2605.27805v1 [cs.CL] 27 May 2026 While LLMs enable personalized chatbots, et al., 2025; Wang et al., 2025)) to deliver personal- their effectivene…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“ChildEval: When large language models meet children's personalities”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [208] Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security

- **评分**：8/10
- **作者/机构**：Xiang Fang, Wanlong Fang
- **论文链接**：https://arxiv.org/abs/2605.27823
- **PDF**：https://arxiv.org/pdf/2605.27823
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security”展开，属于「评测与安全」方向。作者核心问题是：2025; Wang et al. 2026c; Cai et al. 2025; Fang and Fang 2026; Wang et al. 2026a; Fang, Fang, and Ji 2026; Wang Large Language Models (LLMs) are increasingly vulnera- et al. 2026d, 2025e; Fang 2026; Fang, Fang, and Wang ble to adversarial prompts that exploit…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [209] When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models

- **评分**：8/10
- **作者/机构**：Dasol Choi, Alex Kwon
- **论文链接**：https://arxiv.org/abs/2605.27851
- **PDF**：https://arxiv.org/pdf/2605.27851
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models”展开，属于「评测与安全」方向。作者核心问题是：through static benchmarks, where models are eval- uated on their ability to choose the safe or ethical arXiv:2605.27851v1 [cs.AI] 27 May 2026 Safety benchmark scores provide incomplete action under standard assumptions (Herrador, 2025; evidence of deployment…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [210] Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization

- **评分**：8/10
- **作者/机构**：Jiawei Kong, Hao Fang, Shunxiang Liao, Jinyu Li, Bin Chen, Hao Wu, Shu-Tao Xia, Min Zhang
- **论文链接**：https://arxiv.org/abs/2605.27906
- **PDF**：https://arxiv.org/pdf/2605.27906
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization”展开，属于「评测与安全」方向。作者核心问题是：Multimodal Large Reasoning Models intro- arXiv:2605.27906v1 [cs.AI] 27 May 2026 Is there a dining duce the reasoning paradigm, demonstrating table in the image? strong capabilities on complex vision-language tasks. However, they still suffer from severe hallu…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [211] Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values

- **评分**：8/10
- **作者/机构**：Seongjun Lee, Suwan Yoon, Changhee Lee
- **论文链接**：https://arxiv.org/abs/2605.28170
- **PDF**：https://arxiv.org/pdf/2605.28170
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values”展开，属于「评测与安全」方向。作者核心问题是：As large language models (LLMs) are increasingly integrated into high-stakes decision-making, the ability to reliably quantify uncertainty has become a critical requirement for safety and trust. However, current uncertainty arXiv:2605.28170v1 [cs.AI] 27 May 2…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [212] Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents

- **评分**：8/10
- **作者/机构**：Yongxiang Li, Moxin Li, Zhixin Ma, Fengbin Zhu, Dongrui Liu, Wenjie Wang, Fuli Feng
- **论文链接**：https://arxiv.org/abs/2605.28201
- **PDF**：https://arxiv.org/pdf/2605.28201
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents”展开，属于「评测与安全」方向。作者核心问题是：transactions (Mou et al., 2026) and privacy leak- age (El Yagoubi et al., 2026). Large Language Model (LLM) agents remain arXiv:2605.28201v1 [cs.AI] 27 May 2026 vulnerable to safety threats from the external Safety threats to LLM agents can be broadly environ…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [213] Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers

- **评分**：8/10
- **作者/机构**：Carmen Quiles-Ramírez, Leticia L. Rodríguez, Nicolás Martorell, Natalia Díaz-Rodríguez
- **论文链接**：https://arxiv.org/abs/2605.28215
- **PDF**：https://arxiv.org/pdf/2605.28215
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers”展开，属于「评测与安全」方向。作者核心问题是：window (Dong et al., 2024). Despite impressive few-shot accuracy, the reasoning process underlying these predictions In-context learning (ICL) enables multimodal remains a black box: models produce answers without any arXiv:2605.28215v1 [cs.AI] 27 May 2026 la…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [214] Entropy Distribution as a Fingerprint for Hallucinations in Generative Models

- **评分**：8/10
- **作者/机构**：Mattia J. Villani, Pranav Deshpande, Akshay Seshadri, Romina Yalovetzky, Niraj Kumar
- **论文链接**：https://arxiv.org/abs/2605.28264
- **PDF**：https://arxiv.org/pdf/2605.28264
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Entropy Distribution as a Fingerprint for Hallucinations in Generative Models”展开，属于「评测与安全」方向。作者核心问题是：Large Language Models (LLMs) often generate factually incorrect outputs, com- monly termed hallucinations, that undermine trust and limit deployment in high- stakes settings. Existing hallucination detection methods typically require multiple forward passes…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Entropy Distribution as a Fingerprint for Hallucinations in Generative Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [215] Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation

- **评分**：8/10
- **作者/机构**：Zhaoyang Jiang, Xuanqi Peng, Fei Teng, Zhizhong Fu, Yunsoo Kim, Jiacong Mi, Zicheng Li, Honghan Wu
- **论文链接**：https://arxiv.org/abs/2605.28301
- **PDF**：https://arxiv.org/pdf/2605.28301
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation”展开，属于「评测与安全」方向。作者核心问题是：1 Introduction The modern recipe for making a compact reason- Chain-of-thought (CoT) distillation trains a ing model is simple: ask a stronger teacher to smaller model to imitate a teacher’s reason- write chain-of-thought solutions, then train the ing trace…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [216] SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models

- **评分**：8/10
- **作者/机构**：Chao Ding, Mouxiao Bian, Tianbin Li, Minjia Yuan, Yidong Jiang, Yankai Jiang, Jinru Ding, Jiayuan Chen, Zhuangzhi Gao, Pengcheng Chen, Zhao He, Rongzhao Zhang 等
- **论文链接**：https://arxiv.org/abs/2605.28338
- **PDF**：https://arxiv.org/pdf/2605.28338
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models”展开，属于「评测与安全」方向。作者核心问题是：Large language models(LLMs) increasingly match expert performance on licensing examinations, yet routine clinical use remains limited because governance requires auditable reasoning, safety and ethics alignment, and resilience to adversarial misuse. Here we p…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [217] SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving

- **评分**：8/10
- **作者/机构**：Kangyu Wu, Peng Cui, Guoxi Chen, Ya Zhang
- **论文链接**：https://arxiv.org/abs/2605.28583
- **PDF**：https://arxiv.org/pdf/2605.28583
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving”展开，属于「评测与安全」方向。作者核心问题是：Ensuring both safety and efficiency in decision- making of autonomous driving systems remains a fundamen- tal challenge. Traditional Deep Reinforcement Learning (DRL) suffers from unsafe random exploration and slow convergence, while Large Language Models (LL…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [218] Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study

- **评分**：8/10
- **作者/机构**：Irune Zubiaga, Aitor Soroa, Rodrigo Agerri
- **论文链接**：https://arxiv.org/abs/2605.28710
- **PDF**：https://arxiv.org/pdf/2605.28710
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study”展开，属于「评测与安全」方向。作者核心问题是：In this work, we study how to design effective training and evaluation strategies that enable ro- arXiv:2605.28710v1 [cs.CL] 27 May 2026 Large language models (LLMs) are increas- bust multilingual performance across languages ingly used for the automatic eval…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [219] Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis

- **评分**：7/10
- **作者/机构**：Taylor Anderson, Sara Von Hoene, Orhan Yagizer Cinar, Emma Von Hoene, Amira Roess, Andrew Crooks, Hamdi Kavak
- **论文链接**：https://arxiv.org/abs/2605.27401
- **PDF**：https://arxiv.org/pdf/2605.27401
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis”展开，属于「评测与安全」方向。作者核心问题是：There is a growing interest in utilizing synthetic populations for a diverse range of applications. At the same time, we are witnessing a tremendous growth in artificial intelligence in all walks of life. This paper evaluates whether zero-shot large language…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [220] Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks

- **评分**：7/10
- **作者/机构**：Partho Ghose, Al Bashir, Prem Raj, Azlan Zahid
- **论文链接**：https://arxiv.org/abs/2605.27595
- **PDF**：https://arxiv.org/pdf/2605.27595
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks”展开，属于「评测与安全」方向。作者核心问题是：Large Language Models (LLMs) are being rapidly adopted in agricultural imaging applications, rang- ing from crop interpretation to synthetic field image generation. However, these models frequently exhibit hallucinations—outputs that appear confident yet devi…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [221] Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation

- **评分**：7/10
- **作者/机构**：Jingwen Wu, Xijun Zhang, Ge Song
- **论文链接**：https://arxiv.org/abs/2605.27993
- **PDF**：https://arxiv.org/pdf/2605.27993
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation”展开，属于「评测与安全」方向。作者核心问题是：(a) VFV axis ( ): Visual vs. Parametric Knowledge (external-vs-internal) 20 vanilla LLaVA-1.5 Qwen-VL 18 arXiv:2605.27993v1 [cs.CL] 27 May 2026 Object hallucination remains a primary obsta- cle to the reliable deployment of Multimodal 16 Large Language Models…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Rethinking Visual Neglect: Steering via Context-Preference for MLLM Hallucination Mitigation”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [222] Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations

- **评分**：7/10
- **作者/机构**：Matteo Gioele Collu, Riccardo Conte, Alberto Giaretta, Denis Kleyko, Mauro Conti, Matteo Zavatteri, Roberto Confalonieri
- **论文链接**：https://arxiv.org/abs/2605.28553
- **PDF**：https://arxiv.org/pdf/2605.28553
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations”展开，属于「评测与安全」方向。作者核心问题是：man Feedback (Christiano et al., 2017; Bai et al., 2022) and Supervised Fine-Tuning (Ouyang et al., In this paper, we investigate whether refusal arXiv:2605.28553v1 [cs.AI] 27 May 2026 behavior can be predicted from LLM interme- 2022). While effective in many…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Refusal Before Decoding: Detecting and Exploiting Refusal Signals in Intermediate LLM Activations”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [223] A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models

- **评分**：7/10
- **作者/机构**：Aditya Kommineni, Emily Zhou, Kleanthis Avramidis, Tiantian Feng, Shrikanth Narayanan
- **论文链接**：https://arxiv.org/abs/2605.28563
- **PDF**：https://arxiv.org/pdf/2605.28563
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models”展开，属于「评测与安全」方向。作者核心问题是：et al., 2004; Goldberger et al., 2000), BCI Competi- Evaluating foundation models under appropri- tion IV-2A (Brunner et al., 2008), Kaggle ERN (Mat- ate adaptation settings is essential for under- tout et al., 2014), TUEV (Obeid and Picone, 2016), standing t…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [224] Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking

- **评分**：7/10
- **作者/机构**：Ziyang You, Huilong He, Xiaoke Yang, Xuxing Lu
- **论文链接**：https://arxiv.org/abs/2605.28632
- **PDF**：https://arxiv.org/pdf/2605.28632
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking”展开，属于「评测与安全」方向。作者核心问题是：Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs). Existing schemes, including KGW, Unigram, and DipMark, derive their security guarantees from the assumption that the underlying pseudo-random numbe…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [225] Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text

- **评分**：7/10
- **作者/机构**：Bushi Xiao, Sarvesh Soni, Daisy Zhe Wang
- **论文链接**：https://arxiv.org/abs/2605.28740
- **PDF**：https://arxiv.org/pdf/2605.28740
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text”展开，属于「评测与安全」方向。作者核心问题是：predictions. This is a form of self-assessment that reflects model reliability independent of ground arXiv:2605.28740v1 [cs.CL] 27 May 2026 As large language models are increasingly de- truth. Yona et al. (2026) formalize this distinction, ployed for clinical…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [226] Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models

- **评分**：6/10
- **作者/机构**：Yuang Huang, Yafeng Zhang, Yu Zilan
- **论文链接**：https://arxiv.org/abs/2605.28123
- **PDF**：https://arxiv.org/pdf/2605.28123
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models”展开，属于「评测与安全」方向。作者核心问题是：In current practice, such verification prompts are often applied indiscriminately to all inputs (always- arXiv:2605.28123v1 [cs.CL] 27 May 2026 Prompt-based verification is widely used to mit- on prompting). However, this raises a question that igate hallucin…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Risk-aware Selective Prompting for Hallucination Mitigation in Large Vision-Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「评测与安全」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [227] When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs

- **评分**：5/10
- **作者/机构**：Marcell Fekete, Johannes Bjerva, Tamás Káldi
- **论文链接**：https://arxiv.org/abs/2605.28346
- **PDF**：https://arxiv.org/pdf/2605.28346
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs”展开，属于「评测与安全」方向。作者核心问题是：arXiv:2605.28346v1 [cs.CL] 27 May 2026 Vision-language models (VLMs) are increas- ingly evaluated for whether they identify the right visual content, but little is known about whether they express such content in a discourse-appropriate form. We address this…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“When Discourse Pressures Conflict: Information Structure in Vision-Language Model Outputs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「评测与安全」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [228] Measuring Form and Function in Language Models

- **评分**：5/10
- **作者/机构**：Héctor Javier Vázquez Martínez, Charles Yang
- **论文链接**：https://arxiv.org/abs/2605.28616
- **PDF**：https://arxiv.org/pdf/2605.28616
- **代码链接**：https://github.com/hjvm/llm-form-and-function

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Measuring Form and Function in Language Models”展开，属于「评测与安全」方向。作者核心问题是：arXiv:2605.28616v1 [cs.CL] 27 May 2026 We introduce quantitative metrics from child language research to evaluate language mod- els. Our focus is on the formal syntactic and functional discourse properties of determiners in English, which young children acqui…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Measuring Form and Function in Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「评测与安全」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 🧪 应用 / Benchmark


### [229] SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter

- **评分**：8/10
- **作者/机构**：Lee Jung-Mok, Kim Sung-Bin, Joohyun Chang, Lee Hyun, Tae-Hyun Oh
- **论文链接**：https://arxiv.org/abs/2605.28084
- **PDF**：https://arxiv.org/pdf/2605.28084
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter”展开，属于「应用与基准」方向。作者核心问题是：Following recent advancements in artificial so- cial intelligence (Bainbridge et al., 1994; Dauten- Laughter is a complex social signal that con- arXiv:2605.28084v1 [cs.CL] 27 May 2026 veys communicative intent beyond amusement. hahn, 2007; Williams et al., 2…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「应用与基准」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [230] From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons

- **评分**：7/10
- **作者/机构**：Xiangyu Ma, Teng Xiao, Zuchao Li, Lefei Zhang
- **论文链接**：https://arxiv.org/abs/2605.27387
- **PDF**：https://arxiv.org/pdf/2605.27387
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons”展开，属于「应用与基准」方向。作者核心问题是：arXiv:2605.27387v1 [cs.CL] 11 Apr 2026 Diffusion models promise efficient parallel text generation but rely on bidirectional atten- tion, creating a structural mismatch with pre- trained Autoregressive (AR) models. This in- compatibility precludes reusing rob…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [231] Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking

- **评分**：7/10
- **作者/机构**：Wonkyun Kim, Sehyun Bae, Kwanki Ahn, Mungyu Bae, Saeun Choi, Soyeon You, Chandra Prabhakar, Sehyun Kim
- **论文链接**：https://arxiv.org/abs/2605.27429
- **PDF**：https://arxiv.org/pdf/2605.27429
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking”展开，属于「应用与基准」方向。作者核心问题是：1 Introduction Industrial video-on-demand (VOD) recommenders need richer Production recommenders are served through multi-stage pipelines: content understanding, but LLM-as-reranker designs repeat candidate generation, ranking or reranking, filtering, and fin…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [232] BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving

- **评分**：7/10
- **作者/机构**：Tianyao Shi, Yi Ding
- **论文链接**：https://arxiv.org/abs/2605.27480
- **PDF**：https://arxiv.org/pdf/2605.27480
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving”展开，属于「应用与基准」方向。作者核心问题是：paper focuses on biodiversity impact (BI) charac- arXiv:2605.27480v1 [q-bio.OT] 26 May 2026 terization. BI measures ecosystem damage induced Large language model (LLM) serving cre- ates environmental impacts beyond carbon and by human activities through multi…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [233] Locality-Aware Redundancy Pruning for LLM Depth Compression

- **评分**：7/10
- **作者/机构**：Vincent-Daniel Yun, Youngrae Kim, Woosang Lim, YoungJin Heo, Minkyu Kim, Sunwoo Lee
- **论文链接**：https://arxiv.org/abs/2605.27786
- **PDF**：https://arxiv.org/pdf/2605.27786
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Locality-Aware Redundancy Pruning for LLM Depth Compression”展开，属于「应用与基准」方向。作者核心问题是：Large language models are known to contain representational redundancy across network depth, making depth pruning an effective approach for improving inference efficiency. Existing one-shot pruning methods rely on local layer importance or fixed redundancy as…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Locality-Aware Redundancy Pruning for LLM Depth Compression”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [234] Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis

- **评分**：7/10
- **作者/机构**：Nils Constantin Hellwig, Niklas Donhauser, Jakob Fehle, Udo Kruschwitz, Christian Wolff
- **论文链接**：https://arxiv.org/abs/2605.28058
- **PDF**：https://arxiv.org/pdf/2605.28058
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis”展开，属于「应用与基准」方向。作者核心问题是：While recent few-shot prompting approaches have narrowed the gap to fine-tuned models (Hell- Recent work explored the capabilities of Large wig et al., 2025), a performance gap remains, par- arXiv:2605.28058v1 [cs.CL] 27 May 2026 Language Models (LLMs) in Asp…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Prompting Is All You Need: Multi-view Prompting Large Language Models for Aspect-Based Sentiment Analysis”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [235] Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification

- **评分**：7/10
- **作者/机构**：Dylan Bouchard, Mohit Singh Chauhan, Zeya Ahmad, Ho-Kyeong Ra
- **论文链接**：https://arxiv.org/abs/2605.28500
- **PDF**：https://arxiv.org/pdf/2605.28500
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification”展开，属于「应用与基准」方向。作者核心问题是：2024) and LiveSQLBench (Team, 2024) show that even state-of-the-art models produce incorrect so- arXiv:2605.28500v1 [cs.CL] 27 May 2026 Large language models have shown impres- lutions for a substantial fraction of problems (Gao sive capabilities in code gene…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [236] Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection

- **评分**：7/10
- **作者/机构**：Zhixing Zuo, Huilin He, Jiasheng Wu, Dawei Cheng
- **论文链接**：https://arxiv.org/abs/2605.28524
- **PDF**：https://arxiv.org/pdf/2605.28524
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection”展开，属于「应用与基准」方向。作者核心问题是：<Text attributes> : This y1 y2 y3 … transaction occurred at… 0.15 0.76 -1.2 … arXiv:2605.28524v1 [cs.AI] 27 May 2026 In recent years, Large Language Models (LLMs) have shown great capability in pro- Privacy cessing graph tasks such as fraud detection. Constra…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [237] Efficient Pre-Training of LLMs through Truncated SVD Layers

- **评分**：7/10
- **作者/机构**：Kaivan Kamali, Kajetan Schweighofer, Hormoz Shahrzad, Olivier Francon, Babak Hodjat, Risto Miikkulainen
- **论文链接**：https://arxiv.org/abs/2605.28573
- **PDF**：https://arxiv.org/pdf/2605.28573
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Efficient Pre-Training of LLMs through Truncated SVD Layers”展开，属于「应用与基准」方向。作者核心问题是：The massive scaling of Large Language Models (LLMs) has made pretraining in- creasingly cost-prohibitive. While low-rank representation and orthonormal weight matrices could in principle reduce parameter counts and computational overhead, most existing method…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Efficient Pre-Training of LLMs through Truncated SVD Layers”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [238] Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?

- **评分**：7/10
- **作者/机构**：Gabrielle Kaili-May Liu, Arman Cohan
- **论文链接**：https://arxiv.org/abs/2605.28778
- **PDF**：https://arxiv.org/pdf/2605.28778
- **代码链接**：https://github.com/yale-nlp/marker_internal_confidence

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?”展开，属于「应用与基准」方向。作者核心问题是：LLMs’ linguistically expressed confidence should faithfully reflect their intrinsic uncertainty. While recent work shows LLMs struggle to use epistemic markers (e.g., “it is likely...”) in a human-aligned fashion, it remains unclear whether models can apply t…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「应用与基准」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「应用与基准」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [239] Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting

- **评分**：6/10
- **作者/机构**：Hui Dai, Ryan Teehan, Parsa Torabian, Mengye Ren
- **论文链接**：https://arxiv.org/abs/2605.27668
- **PDF**：https://arxiv.org/pdf/2605.27668
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting”展开，属于「应用与基准」方向。作者核心问题是：Probabilistic forecasting estimates the likelihood of uncertain future events. To improve LLM forecast- ing, existing methods typically learn from binary outcomes to output verbalized forecasts. However, while aggregated human forecasts contain rich informati…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [240] Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations

- **评分**：6/10
- **作者/机构**：Simardeep Singh, Paras Chopra
- **论文链接**：https://arxiv.org/abs/2605.27970
- **PDF**：https://arxiv.org/pdf/2605.27970
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations”展开，属于「应用与基准」方向。作者核心问题是：data. Recent work has shown that LLM representations While large language models (LLMs) are trained exhibit structured geometry across a range of concepts. For instance, cyclical domains such as days of the week, months, arXiv:2605.27970v1 [cs.AI] 27 May 2026…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Geometry of Human Perceptual Domains Emerges Transiently in LLM Representations”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [241] Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models

- **评分**：6/10
- **作者/机构**：Himanshu Beniwal, Mayank Singh
- **论文链接**：https://arxiv.org/abs/2605.27997
- **PDF**：https://arxiv.org/pdf/2605.27997
- **代码链接**：https://github.com/himanshubeniwal/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models”展开，属于「应用与基准」方向。作者核心问题是：Toxic Layers! arXiv:2605.27997v1 [cs.CL] 27 May 2026 Large language models frequently generate Toxic Text Toxic Generation (I hate you and want to hurt…) (and stab you so...) toxic, hateful, or harmful content, yet exist- ing mitigation methods rely on costly…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Where Does Toxicity Live? Mechanistic Localization and Targeted Suppression in Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [242] Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation

- **评分**：6/10
- **作者/机构**：Annabella Sánchez-Guzmán, Lukas Eberhard, Denis Helic, Lisette Espín-Noboa
- **论文链接**：https://arxiv.org/abs/2605.28187
- **PDF**：https://arxiv.org/pdf/2605.28187
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Whose Name Comes Up? III: Persona Prompting Effects in LLM-Based Scholar Recommendation”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [243] Learning the Error Patterns of Language Models

- **评分**：6/10
- **作者/机构**：Jinwoo Kim, Taylor Berg-KirkPatrick, Loris D'Antoni
- **论文链接**：https://arxiv.org/abs/2605.28328
- **PDF**：https://arxiv.org/pdf/2605.28328
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learning the Error Patterns of Language Models”展开，属于「应用与基准」方向。作者核心问题是：When generating outputs for domains with specific validity constraints (e.g., a program should compile), LLMs often fail in a small number of focused ways: for example, by using Python function names when generating TypeScript. We observe that these error pat…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Learning the Error Patterns of Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [244] Diffusion Large Language Models for Visual Speech Recognition

- **评分**：6/10
- **作者/机构**：Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro
- **论文链接**：https://arxiv.org/abs/2605.28456
- **PDF**：https://arxiv.org/pdf/2605.28456
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Diffusion Large Language Models for Visual Speech Recognition”展开，属于「应用与基准」方向。作者核心问题是：Left-to-right decoding: early errors cannot be revised Step 1 I arXiv:2605.28456v1 [cs.AI] 27 May 2026 Existing Visual Speech Recognition (VSR) sys- Step 2 I BACK tems commonly rely on left-to-right autoregres- BACK 0.42 ✓ selected sive decoding, which can fo…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Diffusion Large Language Models for Visual Speech Recognition”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [245] Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets

- **评分**：6/10
- **作者/机构**：Andrea Gurioli, Davide D'Ascenzo, Federico Pennino, Maurizio Gabbrielli, Stefano Zacchiroli
- **论文链接**：https://arxiv.org/abs/2605.28510
- **PDF**：https://arxiv.org/pdf/2605.28510
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets”展开，属于「应用与基准」方向。作者核心问题是：Large language models (LLMs) for code completion generation process of Large Language Models (LLMs) raises and generation are increasingly used in software development, significant concerns. Generating code without acknowledging yet they may reproduce trainin…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [246] The Ethics of LLM Sandbox and Persona Dynamics

- **评分**：6/10
- **作者/机构**：Tim Gebbie, Stewart Gebbie
- **论文链接**：https://arxiv.org/abs/2605.28647
- **PDF**：https://arxiv.org/pdf/2605.28647
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“The Ethics of LLM Sandbox and Persona Dynamics”展开，属于「应用与基准」方向。作者核心问题是：arXiv:2605.28647v1 [cs.AI] 27 May 2026 It is well known that LLM guardrails and trained persona dynamics can produce a reality gap: the distance between the world a LLM is permitted or shaped to describe, and the world in which users must act. Here we argue t…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“The Ethics of LLM Sandbox and Persona Dynamics”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [247] Human-AI Collaboration for Estimating Scientific Replicability

- **评分**：5/10
- **作者/机构**：Tatiana Chakravorti, Robert Fraleigh, Timothy Fritton, Christopher Griffin, Vaibhav Singh, Sai Koneru, C. Lee Giles, David Pennock, Anthony Kwasnica, Sarah Rajtmajer
- **论文链接**：https://arxiv.org/abs/2605.27394
- **PDF**：https://arxiv.org/pdf/2605.27394
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Human-AI Collaboration for Estimating Scientific Replicability”展开，属于「应用与基准」方向。作者核心问题是：. Determining whether published scientific findings can successfully be replicated is a long-standing challenge in the empirical sciences. Existing ap- proaches for replicability assessment typically rely either on human judgment, i.e., creative assembly of h…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Human-AI Collaboration for Estimating Scientific Replicability”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [248] Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models

- **评分**：4/10
- **作者/机构**：Jaehoon Kang, Yejin Lee, Yoonji Park, Kyuhong Shim
- **论文链接**：https://arxiv.org/abs/2605.27376
- **PDF**：https://arxiv.org/pdf/2605.27376
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models”展开，属于「应用与基准」方向。作者核心问题是：A. Inter-utterance Style Interpolation While prompt-based text-to-speech (TTS) mod- arXiv:2605.27376v1 [cs.CL] 9 Apr 2026 els enable natural language-driven speaking style control, they often provide limited fine- Source Style: Male voice Target Style: Female…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [249] Soro: A Lightweight Foundation Model and Chatbot for Tajik

- **评分**：4/10
- **作者/机构**：Stanislav Liashkov, Haitz Sáez de Ocáriz Borde, Azizjon Azimi, Khushbakht Shaymardonov, Shuhratjon Khalitbekov, Bonu Boboeva
- **论文链接**：https://arxiv.org/abs/2605.27379
- **PDF**：https://arxiv.org/pdf/2605.27379
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Soro: A Lightweight Foundation Model and Chatbot for Tajik”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Soro: A Lightweight Foundation Model and Chatbot for Tajik”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [250] Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions

- **评分**：4/10
- **作者/机构**：Antonia Karamolegkou, Nicolas Angleraud, Benoît Sagot, Thibault Clérice
- **论文链接**：https://arxiv.org/abs/2605.27750
- **PDF**：https://arxiv.org/pdf/2605.27750
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions”展开，属于「应用与基准」方向。作者核心问题是：often producing semantically plausible but visually unsupported output (Shu et al., 2025; Liang et al., arXiv:2605.27750v1 [cs.CL] 26 May 2026 Recent work has shown that Vision-Language 2026; He et al., 2025; Gong et al., 2026). While Models (VLMs) used for o…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Reading or Guessing? Visual Grounding Failures of Vision-Language Models for OCR in Ancient Greek Editions”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [251] Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts

- **评分**：4/10
- **作者/机构**：Yuyue Wang, Xihua Wang, Xin Cheng, Yijing Chen, Ruihua Song
- **论文链接**：https://arxiv.org/abs/2605.28063
- **PDF**：https://arxiv.org/pdf/2605.28063
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts”展开，属于「应用与基准」方向。作者核心问题是：Audio generation has made significant progress, yet synthesizing unified audio where speech and sounds are naturally composited remains a challenge. Current methods either rely on disjoint pipelines, which fail to capture fine-grained inter- actions, or requi…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Unified Synthesis of Compositional Speech and Sound from Free-Form Text Prompts”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [252] CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models

- **评分**：4/10
- **作者/机构**：Fengze Yang, Bo Yu, Xuewen Luo, Cathy Liu, Chenxi Liu
- **论文链接**：https://arxiv.org/abs/2605.28115
- **PDF**：https://arxiv.org/pdf/2605.28115
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“CIVIC: End-to-End Sequence Compactness for Efficient Vision-Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [253] FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales

- **评分**：4/10
- **作者/机构**：Jorge L. Rodriguez, Victor Angulo Morales, Areej Alwahas, Mariana Elias Lara, Fida Mohammad Thoker, Kasper Johansen, Bernard Ghanem, Fernando T. Maestre, Matthew F. McCabe
- **论文链接**：https://arxiv.org/abs/2605.28174
- **PDF**：https://arxiv.org/pdf/2605.28174
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [254] When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models

- **评分**：4/10
- **作者/机构**：Jungwon Park, Jimyeong Kim, Jungmin Ko, Nojun Kwak, Wonjong Rhee
- **论文链接**：https://arxiv.org/abs/2605.28181
- **PDF**：https://arxiv.org/pdf/2605.28181
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models”展开，属于「应用与基准」方向。作者核心问题是：Most training-free DLM decoding strategies use Diffusion language models decode text by it- model confidence as the position-selection sig- arXiv:2605.28181v1 [cs.CL] 27 May 2026 eratively denoising masked token sequences, nal. For example, top-probability de…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“When Confidence Misleads: Suffix Anchoring and Anchor-Proximity Confidence Modulation for Diffusion Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [255] Pruning and Distilling Mixture-of-Experts into Dense Language Models

- **评分**：4/10
- **作者/机构**：Junhyuck Kim, Jihun Yun, Haechan Kim, Gyeongman Kim, Joonghyun Bae, Jaewoong Cho
- **论文链接**：https://arxiv.org/abs/2605.28207
- **PDF**：https://arxiv.org/pdf/2605.28207
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Pruning and Distilling Mixture-of-Experts into Dense Language Models”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Pruning and Distilling Mixture-of-Experts into Dense Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [256] PrunePath: Towards Highly Structured Sparse Language Models

- **评分**：4/10
- **作者/机构**：Zhexuan Gu, Zixun Fu, Yancheng Yuan
- **论文链接**：https://arxiv.org/abs/2605.28283
- **PDF**：https://arxiv.org/pdf/2605.28283
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PrunePath: Towards Highly Structured Sparse Language Models”展开，属于「应用与基准」方向。作者核心问题是：… Transformer Backbone (N Layers) MoE Layer arXiv:2605.28283v1 [cs.CL] 27 May 2026 Feed-forward networks (FFNs) dominate the Input sequence (Token) Input sequence (Token) Input Token Embedding parameter count and computation of modern language models, yet exi…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“PrunePath: Towards Highly Structured Sparse Language Models”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [257] Entropy-aware Masking for Masked Language Modeling

- **评分**：4/10
- **作者/机构**：Gokul Srinivasagan, Kai Hartung, Munir Georges
- **论文链接**：https://arxiv.org/abs/2605.28526
- **PDF**：https://arxiv.org/pdf/2605.28526
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Entropy-aware Masking for Masked Language Modeling”展开，属于「应用与基准」方向。作者核心问题是：training the model to predict these masked tokens using the surrounding context. This enables the Masked language modeling has become a stan- arXiv:2605.28526v1 [cs.AI] 27 May 2026 model to learn both syntactic structure and seman- dard pretraining objective…

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Entropy-aware Masking for Masked Language Modeling”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [258] Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests

- **评分**：4/10
- **作者/机构**：Richard J. Young, Gregory D. Moody
- **论文链接**：https://arxiv.org/abs/2605.28734
- **PDF**：https://arxiv.org/pdf/2605.28734
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests”展开，属于「应用与基准」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
相关性够收录，但优先级不高：更适合作为资料索引，除非你正好关心这个具体应用或 benchmark。

**🔧 技术方案**  
- **模型架构**：以现有 LLM 能力为基础，面向具体应用任务做流程化建模和实验验证。  
- **核心创新**：主要新意在于把“Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests”这个问题形式化到「应用与基准」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「应用与基准」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
