---
title: "Agent/LLM论文速递｜2026-06-02｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-06-02｜全量版：本期收录 80 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-06-02｜全量版：本期收录 80 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-06-02"
cover_subtitle: "Agent系统与工具使用 / RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-06-02｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **80** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**1** 篇
- LLM 推理 / 规划 / RAG：**35** 篇
- 评测 / 安全 / 对齐：**22** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | ASE-26: a curriculum for agentic software engineering as a discipline | ⭐ 9/10 | agent |
| RAG与知识检索 | 1 | Critic-R: Improving Agentic Search using Instruction-tuned Retrievers with Natural Language Introspective Feedback | ⭐ 9/10 | agent, RAG, retrieval, reasoning |
| RAG与知识检索 | 2 | MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation | ⭐ 9/10 | agent, multi-agent, RAG, retrieval |
| RAG与知识检索 | 3 | MemPro: Agentic Memory Systems as Evolvable Programs | ⭐ 9/10 | agent, retrieval, memory |
| RAG与知识检索 | 4 | ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment | ⭐ 9/10 | agent, RAG, benchmark |
| RAG与知识检索 | 5 | MOSAIC: Modular Orchestration for Structured Agentic Intelligence and Composition | ⭐ 9/10 | agent, retrieval, memory |
| RAG与知识检索 | 6 | Multi-Agent Conformal Prediction with Personalized Statistical Validity | ⭐ 9/10 | agent, multi-agent, RAG, privacy |
| RAG与知识检索 | 7 | Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults | ⭐ 9/10 | agent, retrieval, safety |
| RAG与知识检索 | 8 | SS-ZKR: Spatial-Semantic Zero-Knowledge Routing for Privacy-Preserving Multi-Agent Collaboration | ⭐ 9/10 | agent, multi-agent, RAG, privacy |
| RAG与知识检索 | 9 | ExpWeaver: LLM Agents Learn from Experience via Latent RAG | ⭐ 9/10 | agent, RAG, retrieval, reasoning |
| RAG与知识检索 | 10 | TravelEval: A Comprehensive Benchmarking Framework for Evaluating LLM-Powered Travel Planning Agents | ⭐ 9/10 | agent, RAG, benchmark, reasoning |
| RAG与知识检索 | 11 | SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision | ⭐ 9/10 | agent, benchmark, memory |
| RAG与知识检索 | 12 | ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment | ⭐ 9/10 | agent, RAG, tool use |
| RAG与知识检索 | 13 | SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories | ⭐ 9/10 | agent |
| RAG与知识检索 | 14 | Digital Twin-Assisted Adaptive Multi-Agent DRL for Intelligent Spectrum and Resource Management in Open-RAN UAV-Enabled 6G Networks | ⭐ 9/10 | agent, multi-agent, RAG |
| RAG与知识检索 | 15 | Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems | ⭐ 9/10 | agent, multi-agent, RAG, benchmark |
| RAG与知识检索 | 16 | Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory | ⭐ 9/10 | agent, multi-agent, RAG, reasoning |
| RAG与知识检索 | 17 | Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems | ⭐ 9/10 | agent, retrieval, tool use, benchmark |
| RAG与知识检索 | 18 | Dive into Ambiguity: A*-Inspired Multi-Agents Commonsense Obfuscation Attack on LLM Prompts | ⭐ 9/10 | agent, multi-agent, reasoning, safety |
| RAG与知识检索 | 19 | Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence | ⭐ 9/10 | agent, retrieval |
| RAG与知识检索 | 20 | TechGraphRAG: An Agentic Graph-Augmented RAG Framework for Technical Literature Reasoning | ⭐ 9/10 | agent, RAG, retrieval, reasoning |
| RAG与知识检索 | 21 | LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning for Agentic Language Models | ⭐ 9/10 | agent, tool use, reasoning, planning |
| RAG与知识检索 | 22 | RadioMaster: Multi-Agent System for Autonomous Radio Signal Generation | ⭐ 9/10 | agent, multi-agent, retrieval, benchmark |
| RAG与知识检索 | 23 | Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents | ⭐ 9/10 | agent, retrieval, tool use, benchmark |
| RAG与知识检索 | 24 | QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs | ⭐ 9/10 | agent, RAG, tool use, reasoning |
| RAG与知识检索 | 25 | AutoMedBench: Towards Medical AutoResearch with Agentic AI Models | ⭐ 9/10 | agent, RAG, benchmark |
| RAG与知识检索 | 26 | SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning | ⭐ 9/10 | agent, RAG, tool use, reasoning |
| RAG与知识检索 | 27 | BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning | ⭐ 9/10 | agent, RAG, tool use, benchmark |
| RAG与知识检索 | 28 | Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning | ⭐ 9/10 | agent, RAG, tool use, benchmark |
| RAG与知识检索 | 29 | POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems | ⭐ 9/10 | agent, multi-agent, RAG, benchmark |
| RAG与知识检索 | 30 | SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training | ⭐ 9/10 | agent, retrieval, memory |
| LLM推理与规划 | 1 | Iteris: Agentic Research Loops for Computational Mathematics | ⭐ 9/10 | agent |
| RAG与知识检索 | 31 | Bridging the Last Mile of Time Series Forecasting with LLM Agents | ⭐ 9/10 | agent, tool use, reasoning, memory |
| RAG与知识检索 | 32 | AgentxGCore: Agentic AI for Next-Generation Mobile Core Network | ⭐ 8/10 | agent, multi-agent, RAG, reasoning |
| RAG与知识检索 | 33 | Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution | ⭐ 8/10 | agent, RAG, retrieval, memory |
| RAG与知识检索 | 34 | AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents | ⭐ 8/10 | agent, retrieval, benchmark, reasoning |
| 多智能体与协作 | 1 | Deliberative Curation: A Protocol for Multi-Agent Knowledge Bases | ⭐ 9/10 | agent, multi-agent, tool use |
| 多智能体与协作 | 2 | How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 3 | Scaling Behavior of Single LLM-Driven Multi-Agent Systems | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 4 | FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search | ⭐ 9/10 | agent, multi-agent, tool use, benchmark |
| 多智能体与协作 | 5 | Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 6 | CAREAgent: Clinical Agent with Structured Reasoning and Tool-Integrated for Order Generation | ⭐ 9/10 | agent, multi-agent, tool use, benchmark |
| 多智能体与协作 | 7 | Can LLM Agents Sustain Long-Horizon Organizational Dynamics? | ⭐ 9/10 | agent, multi-agent, memory, planning |
| 多智能体与协作 | 8 | Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability | ⭐ 9/10 | agent, multi-agent, tool use |
| 多智能体与协作 | 9 | LLM Consortium for Software Design Refinement: A Controlled Experiment on Multi-Agent Collaboration Topologies | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 10 | Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation | ⭐ 9/10 | agent, tool use, benchmark, reasoning |
| 多智能体与协作 | 11 | Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams | ⭐ 9/10 | agent, multi-agent, tool use, benchmark |
| 多智能体与协作 | 12 | Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus | ⭐ 9/10 | agent, multi-agent, reasoning |
| 多智能体与协作 | 13 | SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes | ⭐ 9/10 | agent, benchmark, reasoning |
| 多智能体与协作 | 14 | Agentic-J: An AI Agent for Biological Microscopy Image Analysis | ⭐ 9/10 | agent, multi-agent, tool use |
| 多智能体与协作 | 15 | MOC: Multi-Order Communication in LLM-based Multi-Agent Systems | ⭐ 9/10 | agent, multi-agent |
| 多智能体与协作 | 16 | MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation | ⭐ 9/10 | agent, tool use, benchmark, MCP |
| 多智能体与协作 | 17 | Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents | ⭐ 8/10 | agent, reasoning |
| 多智能体与协作 | 18 | Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design | ⭐ 8/10 | agent, multi-agent, benchmark |
| 多智能体与协作 | 19 | Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate | ⭐ 8/10 | agent, multi-agent, reasoning |
| 多智能体与协作 | 20 | Agentic Clustering: Controllable Text Taxonomies via Multi-Agent Refinement | ⭐ 8/10 | agent, multi-agent, benchmark |
| 多智能体与协作 | 21 | Network Distributed Multi-Agent Reinforcement Learning for Consensus Control of Quadcopters | ⭐ 8/10 | agent, multi-agent, planning |
| 多智能体与协作 | 22 | Coordination Graphs for Constrained Multi-Agent Reinforcement Learning | ⭐ 8/10 | agent, multi-agent |
| LLM训练与对齐 | 1 | Skill or Skip? Learning Selective Skill Invocation in Agentic Tasks via Dual-Granularity Preference Learning | ⭐ 9/10 | agent |
| LLM训练与对齐 | 2 | Acting with AI: An Interaction-Based Framework for Agentic Tort Liability | ⭐ 9/10 | agent, tool use, planning |
| LLM训练与对齐 | 3 | Leyline: KV Cache Directives for Agentic Inference | ⭐ 9/10 | agent, tool use |
| 评测与安全 | 1 | On Effectiveness and Efficiency of Agentic Tool-calling and RL Training | ⭐ 9/10 | agent, tool use, reasoning |
| 评测与安全 | 2 | CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems | ⭐ 9/10 | agent, memory, planning |
| 评测与安全 | 3 | Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations | ⭐ 9/10 | agent, tool use, benchmark, reasoning |
| 评测与安全 | 4 | Benchmarking Security Risk Detection and Verification in Open Agentic Skill Ecosystems | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 5 | 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code | ⭐ 9/10 | agent, tool use, benchmark, reasoning |
| 评测与安全 | 6 | TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning | ⭐ 9/10 | agent, tool use, benchmark, reasoning |
| 评测与安全 | 7 | Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems | ⭐ 9/10 | agent, tool use, memory, safety |
| 评测与安全 | 8 | Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents | ⭐ 9/10 | agent, benchmark, reasoning |
| 评测与安全 | 9 | MobEvolve: An Agentic Self-Evolving Heuristic System for Interpretable Human Mobility Generation | ⭐ 9/10 | agent, benchmark, memory |
| 评测与安全 | 10 | OctoT2I: A Self-Evolving Agentic Text-to-Image Router | ⭐ 9/10 | agent, tool use, memory |
| 评测与安全 | 11 | AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations | ⭐ 9/10 | agent, tool use, benchmark |
| 评测与安全 | 12 | COMAP: Co-Evolving World Models and Agent Policies for LLM Agents | ⭐ 9/10 | agent, tool use, benchmark, planning |
| 评测与安全 | 13 | AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design | ⭐ 9/10 | agent, tool use, benchmark, reasoning |
| 评测与安全 | 14 | Policy and World Modeling Co-Training for Language Agents | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 15 | Food Noise & False Safety: A Systematic Evaluation of How LLMs Fail to Adapt to Eating Disorder Queries with Clinician Feedback | ⭐ 9/10 | safety |
| 评测与安全 | 16 | Monitoring Agentic Systems Before They're Reliable | ⭐ 9/10 | agent |
| 评测与安全 | 17 | Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs | ⭐ 8/10 | benchmark, safety |
| 评测与安全 | 18 | RoleCDE:Benchmarking and Mitigating Role-Alignment Trade-offs in Role-Playing Agents | ⭐ 8/10 | agent, benchmark, reasoning |
| 评测与安全 | 19 | ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL | ⭐ 8/10 | agent, memory |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] ASE-26: a curriculum for agentic software engineering as a discipline

- **评分**：9/10
- **作者/机构**：Mikael Gorsky；机构：Holon Institute of Technology
- **论文链接**：https://arxiv.org/abs/2606.01152
- **PDF**：https://arxiv.org/pdf/2606.01152v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《ASE-26: a curriculum for agentic software engineering as a discipline》展开。The work of a professional software engineer has begun to consist, increasingly, of directing agents rather than writing code, and the empirical evidence for the shift is now several years deep. Anthropic's Economic Index puts automation at 79 per cent of Claude Code interactions [2]; Handa and colleagues at Anthropic find AI exposure for Computer Programmer tasks at approximately 75 per cent of the role's distinct activities [3]; Brynjolfsson and colleagues at Stanford's Digital Economy Lab report a 13 per cent relative decline in employment for workers aged 22 to 25 in occupations most exposed to AI [4].

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [2] Critic-R: Improving Agentic Search using Instruction-tuned Retrievers with Natural Language Introspective Feedback

- **评分**：9/10
- **作者/机构**：Md Zarif Ul Alam, Alireza Salemi, Hamed Zamani；机构：Center for Intelligent Information Retrieval；University of Massachusetts Amherst；{zarifalam,asalemi,zamani}@cs.umass.edu
- **论文链接**：https://arxiv.org/abs/2606.00590
- **PDF**：https://arxiv.org/pdf/2606.00590v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Critic-R: Improving Agentic Search using Instruction-tuned Retrievers with Natural Language Introspective Feedback》展开。Agentic search systems iteratively interact with retrieval models to answer complex queries. Despite substantial progress, optimizing retrievers for agentic search remains challenging, often requiring heavy co-training or gold-standard annotations that limit real-world applicability.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [3] MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation

- **评分**：9/10
- **作者/机构**：Chuanjie Wu, Zhishang Xiang, Yunbo Tang, Zerui Chen, Qinggang Zhang, Jinsong Su；机构：wuchuanjie@stu.xmu.edu.cn；Xiamen University1, 2；xiangzhishang@stu.xmu.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.00610
- **PDF**：https://arxiv.org/pdf/2606.00610v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation》展开。Retrieval-Augmented Generation (RAG) has become an essential method for mitigating hallucinations in Large Language Models (LLMs) by leveraging external knowledge. Although effective for simple queries, traditional RAG struggles with large-scale, unstructured corpora where information is highly fragmented.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：20 pages。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [4] MemPro: Agentic Memory Systems as Evolvable Programs

- **评分**：9/10
- **作者/机构**：Qingshan Liu, Guoqing Wang, Wen Wu, Jingqi Huang, Xinqi Tao, Dejia Song, Jie Zhou, Liang He；机构：1East China Normal University；2Xiaohongshu Inc.；{51285901015,wgq}@stu.ecnu.edu.cn wwu@cs.ecnu.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.00619
- **PDF**：https://arxiv.org/pdf/2606.00619v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《MemPro: Agentic Memory Systems as Evolvable Programs》展开。Long-horizon autonomous agents require memory systems to retain historical information, track evolving states, and reuse relevant knowledge beyond finite context windows. Existing agentic memory systems typically follow a memory construction-retrieval (MCR) pipeline, but often adapt mainly the memory bank while keeping the surrounding pipeline fixed after deployment.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [5] ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment

- **评分**：9/10
- **作者/机构**：Qiuyu Tian, Zequn Liu, Yingce Xia, Haojie Yin, Youyong Kong；机构：ForeSci: Evaluating LLM Agents for Forward-Looking AI Research；1Southeast University, Nanjing, China；2Beijing Zhongguancun Academy, Beijing, China
- **论文链接**：https://arxiv.org/abs/2606.00644
- **PDF**：https://arxiv.org/pdf/2606.00644v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment》展开。AI research often requires decisions before future evidence exists: which bottleneck to attack, which direction to pursue, or where a project should be positioned. We introduce ForeSci, a temporally controlled benchmark for evaluating whether LLM agents can make such forward-looking research judgements from historical evidence.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：500 tasks；500 tasks；2026

Figure；500
tasks。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [6] MOSAIC: Modular Orchestration for Structured Agentic Intelligence and Composition

- **评分**：9/10
- **作者/机构**：Yifan Bao, Xinyu Xi, Xinyu Liu, Wen Ge, Lei Jiang, Kevin Zhang, Raad Khraishi, Yihao Ang 等；机构：1Department of Computer Science, National University of Singapore；2University College London；3University of Edinburgh
- **论文链接**：https://arxiv.org/abs/2606.00708
- **PDF**：https://arxiv.org/pdf/2606.00708v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《MOSAIC: Modular Orchestration for Structured Agentic Intelligence and Composition》展开。Automated data science is a structured model-selection problem. A solution must choose data transformations, feature representations, architecture, training procedure, evaluation protocol, and refinement strategy for a task.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [7] Multi-Agent Conformal Prediction with Personalized Statistical Validity

- **评分**：9/10
- **作者/机构**：Martin V. Vejling, Christophe A. N. Biscio, Adrien Mazoyer, Petar Popovski, Shashi Raj Pandey；机构：Department of Electronic Systems；Aalborg University, Aalborg, Denmark；mvv@es.aau.dk
- **论文链接**：https://arxiv.org/abs/2606.00717
- **PDF**：https://arxiv.org/pdf/2606.00717v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Multi-Agent Conformal Prediction with Personalized Statistical Validity》展开。Uncertainty quantification is essential in high-stakes machine learning tasks. However, one of the principled solutions, conformal prediction, faces challenges under limited local calibration data, privacy constraints, and data heterogeneity.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [8] Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults

- **评分**：9/10
- **作者/机构**：Rana Muhammad Usman；机构：1Independent Researcher；LLM agents increasingly act after consuming ranked external information streams such as；rollouts on four modern open instruct LLMs from three independent labs, we identify three
- **论文链接**：https://arxiv.org/abs/2606.00914
- **PDF**：https://arxiv.org/pdf/2606.00914v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Adversarial Feeds Steer LLM Agent Decisions Against Their Defaults》展开。LLM agents increasingly act after consuming ranked external information streams such as social feeds, search results, retrieval contexts, and email queues, yet safety evaluations almost always test the model or the user prompt in isolation, never the upstream ranker that decides what the agent reads just before it acts. We introduce a controlled protocol that holds the model, persona, topic, and final decision prompt fixed and varies only the composition and ordering of the posts an agent encounters during a preceding ten-turn "scrolling" phase, isolating the causal effect of feed curation on a downstream decision.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [9] SS-ZKR: Spatial-Semantic Zero-Knowledge Routing for Privacy-Preserving Multi-Agent Collaboration

- **评分**：9/10
- **作者/机构**：Hassan Touheed；机构：htouheed@hotmail.com；increase in multi -agent system (MAS) inquiries between Q1 2024 and Q2 2025 [3], and industry；parallel: Google’s Agent -to-Agent (A2A) protocol [5], now governed by the Linux Foundation with
- **论文链接**：https://arxiv.org/abs/2606.00962
- **PDF**：https://arxiv.org/pdf/2606.00962v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《SS-ZKR: Spatial-Semantic Zero-Knowledge Routing for Privacy-Preserving Multi-Agent Collaboration》展开。Foundational agent interoperability standards, notably the Agent-to-Agent (A2A) protocol and the Model Context Protocol (MCP), have advanced multi-agent system communication, and complementary identity frameworks leveraging W3C Decentralised Identifiers (DIDs) and Verifiable Credentials (VCs) provide cryptographic agent authentication. However, no existing protocol supports content-based semantic routing of agent payloads across organisational trust boundaries without requiring the routing intermediary to decrypt the payload, which is a hard constraint in compliance-sensitive environments governed by GDPR, HIPAA, and MiFID II.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [10] ExpWeaver: LLM Agents Learn from Experience via Latent RAG

- **评分**：9/10
- **作者/机构**：Tao Feng, Tianyang Luo, Jingjun Xu, Zhigang Hua, Yan Xie, Shuang Yang, Ge Liu, Jiaxuan You；机构：eration. To address these limitations, we pro-；1Department of Computer Science, University of Illinois；Urbana-Champaign, Urbana, IL, USA 2Meta Monetization AI,
- **论文链接**：https://arxiv.org/abs/2606.01041
- **PDF**：https://arxiv.org/pdf/2606.01041v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《ExpWeaver: LLM Agents Learn from Experience via Latent RAG》展开。Experience learning has achieved promising results in enhancing LLM agent planning and reasoning by integrating past interactions as reusable knowledge. However, existing methods remain confined to explicit text space, retrieving experiences via semantic similarity and concatenating them into the context window, leading to substantial token overhead and a decoupled architecture that separates retrieval from generation.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：13 tasks。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [11] TravelEval: A Comprehensive Benchmarking Framework for Evaluating LLM-Powered Travel Planning Agents

- **评分**：9/10
- **作者/机构**：Weiyi Chen, Shuaixiong Wang, Ziyun Gao, Kaichun Hu, Wangze Ni, Shimin Di, Chen Jason Zhang, Lei Chen；机构：Zhejiang University；only-chen@foxmail.com；Hong Kong Polytechnic University
- **论文链接**：https://arxiv.org/abs/2606.01046
- **PDF**：https://arxiv.org/pdf/2606.01046v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《TravelEval: A Comprehensive Benchmarking Framework for Evaluating LLM-Powered Travel Planning Agents》展开。The development of Large Language Models (LLMs) has significantly improved travel planning applications, yet evaluating such models is limited by existing benchmarks' limitations: 1) overemphasis on constraint compliance, neglecting multi-dimensional qualities like spatio-temporal cost; 2) datasets lacking real-world authenticity and coverage in key areas (e.g., lodging, transport); and 3) isolated daily plan assessments that miss critical details (e.g., the impact of daily accommodation and visit pacing) needed for entire plan's evaluation. To address this gap, we introduce TravelEval, a realistic and comprehensive benchmark.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：31 pages。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [12] SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision

- **评分**：9/10
- **作者/机构**：Yuxuan Liu, Zhaochen Su, Lingyun Xie, Yuhao Zhang, Qing Zong, Jiahe Guo, Zhongwei Xie, Yiyan Ji 等；机构：1The Hong Kong University of Science and Technology 2Harbin Institute of Technology；3Harbin Institute of Technology, Shenzhen 4Nanjing University 5The University of Hong Kong；*Corresponding author:hlibt@connect.ust.hk
- **论文链接**：https://arxiv.org/abs/2606.01139
- **PDF**：https://arxiv.org/pdf/2606.01139v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision》展开。Agent skills are procedural artifacts that enable LLM agents to execute workflows, verify constraints, and recover from failures. Existing self-evolving methods refine skills using accumulated trajectories.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [13] ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment

- **评分**：9/10
- **作者/机构**：Zhengyang Zhao, Shengjie Ye, Lu Ma, Hao Liang, Hengyi Feng, Wentao Zhang；机构：1 Peking University 2 Sichuan University, Chengdu；zhengyangzhao25@stu.pku.edu.cn,yeshengjie@stu.scu.edu.cn；wentao.zhang@pku.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.01279
- **PDF**：https://arxiv.org/pdf/2606.01279v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment》展开。AI agents are increasingly being tasked with automating AI research itself, particularly the critical post-training phase that transforms base LLMs into aligned assistants. However, recent evaluations reveal that even frontier agents struggle to perform this task.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [14] SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories

- **评分**：9/10
- **作者/机构**：Zhuoyun Yu, Xin Xie, Wuguannan Yao, Chenxi Wang, Lei Liang, Xiang Qi, Shumin Deng；机构：♠Zhejiang University, ♣Ant Digital Technologies, Ant Group,；♢Zhejiang University - Ant Group Joint Laboratory of Knowledge Graph；{3220104147, 231sm}@zju.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.01311
- **PDF**：https://arxiv.org/pdf/2606.01311v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories》展开。Large language model (LLM) agents increasingly rely on reusable external skills to solve long-horizon interactive tasks. Existing training-free skill adaptation pipelines usually update skills from full trajectories or session-level feedback, which makes failure attribution coarse and often produces unstable or overly broad revisions.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [15] Digital Twin-Assisted Adaptive Multi-Agent DRL for Intelligent Spectrum and Resource Management in Open-RAN UAV-Enabled 6G Networks

- **评分**：9/10
- **作者/机构**：Marwan Dhuheir, Thang X. Vu, Symeon Chatzinotas；机构：The Interdisciplinary Centre for Security, Reliability and Trust (SnT), University of Luxembourg, Luxembourg.；physical network elements, enabling predictive analytics and
- **论文链接**：https://arxiv.org/abs/2606.01324
- **PDF**：https://arxiv.org/pdf/2606.01324v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Digital Twin-Assisted Adaptive Multi-Agent DRL for Intelligent Spectrum and Resource Management in Open-RAN UAV-Enabled 6G Networks》展开。The evolution toward 6G wireless networks envisions a seamlessly intelligent, Open-RAN-enabled architecture where unmanned aerial vehicles (UAVs) play a pivotal role in extending coverage, enhancing resilience, and ensuring reliable connectivity for ground users deployment. However, efficiently managing spectrum and resources in such highly dynamic UAV-assisted environments remains a major challenge due to nonlinear system interactions, mobility-induced topology variations, and stringent latency and energy constraints.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [16] Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems

- **评分**：9/10
- **作者/机构**：Junze Zhu, Weihao Chen, Xuanwang Zhang, Zhen Wu, Xinyu Dai；机构：1National Key Laboratory for Novel Software Technology,；Nanjing University, China 2School of Artificial Intelligence,；Nanjing University, China. Correspondence to: Zhen Wu
- **论文链接**：https://arxiv.org/abs/2606.01351
- **PDF**：https://arxiv.org/pdf/2606.01351v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems》展开。The transition from single-turn models to Multi-Agent Systems (MAS) promises enhanced problem-solving capabilities, yet the centralized orchestration topology remains a critical point of fragility. To analyze this, we propose a Mean-Field Entropy Dynamics framework, modeling the orchestration process as a system governed by the competing forces of task resolution and cumulative context loading.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [17] Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory

- **评分**：9/10
- **作者/机构**：Ruiyin Li, Yiran Zhang, Xiyu Zhou, Yangxiao Cai, Peng Liang, Weisong Sun, Jifeng Xuan, Zhi Jin 等；机构：RUIYIN LI,School of Computer Science, Wuhan University, China；YIRAN ZHANG,Nanyang Technological University, Singapore；XIYU ZHOU,School of Computer Science, Wuhan University, China
- **论文链接**：https://arxiv.org/abs/2606.01385
- **PDF**：https://arxiv.org/pdf/2606.01385v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory》展开。Software architecture design is a critical yet inherently complex and knowledge-intensive phase that requires balancing competing quality attributes and adapting to evolving requirements. Traditionally, this process has been time-consuming, labor-intensive, and heavily reliant on architects, often resulting in limited exploration of alternative architectural decompositions and styles, especially under the pressures of agile development.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：10 case；39 pages。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [18] Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems

- **评分**：9/10
- **作者/机构**：Rahul Suresh Babu, Adarsh Agrawal；机构：Independent Researcher；rahulsb@bu.edu；adagrawal@cs.stonybrook.edu
- **论文链接**：https://arxiv.org/abs/2606.01416
- **PDF**：https://arxiv.org/pdf/2606.01416v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems》展开。Tool-augmented large language model (LLM) agents rely on orchestration layers that coordinate planning, retrieval, tool invocation, validation, memory, and recovery. In these systems, failures arise not only from model errors, but also from orchestration-level issues such as tool timeouts, malformed arguments, stale context, contradictory evidence, retry loops, and unverified intermediate outputs.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [19] Dive into Ambiguity: A*-Inspired Multi-Agents Commonsense Obfuscation Attack on LLM Prompts

- **评分**：9/10
- **作者/机构**：Boxuan Wang, Zhuoyun Li, Xiaowei Huang, Yi Dong；机构：University of Liverpool；boxuan.wang@liverpool.ac.uk；zhuoyun.li@liverpool.ac.uk
- **论文链接**：https://arxiv.org/abs/2606.01441
- **PDF**：https://arxiv.org/pdf/2606.01441v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Dive into Ambiguity: A*-Inspired Multi-Agents Commonsense Obfuscation Attack on LLM Prompts》展开。Large language models (LLMs) excel in reasoning and knowledge-intensive tasks but remain vulnerable to prompt-level adversarial attacks that preserve intent while triggering commonsense hallucinations. This vulnerability is urgent, as LLMs are rapidly integrated into safety-critical domains where factual reliability is non-negotiable.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [20] Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence

- **评分**：9/10
- **作者/机构**：Fiona Y. Wang, Markus J. Buehler；机构：Laboratory for Atomistic and Molecular Mechanics；Department of Biological Engineering；Massachusetts Institute of Technology
- **论文链接**：https://arxiv.org/abs/2606.01444
- **PDF**：https://arxiv.org/pdf/2606.01444v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence》展开。Scientific discovery is not only answer generation but revision of the representational regime in which evidence, artifacts, operations, and verifiers are typed. We develop a category-theoretic account of agentic discovery for materials science.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [21] TechGraphRAG: An Agentic Graph-Augmented RAG Framework for Technical Literature Reasoning

- **评分**：9/10
- **作者/机构**：Kanwar Bharat Singh；机构：for domain-specific technical reasoning support, instantiated over a curated corpus；Key contributions include a 100-point evidence sufficiency scoring framework；author validation with intra-corpus citation resolution; and a self-correcting gen-
- **论文链接**：https://arxiv.org/abs/2606.01613
- **PDF**：https://arxiv.org/pdf/2606.01613v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《TechGraphRAG: An Agentic Graph-Augmented RAG Framework for Technical Literature Reasoning》展开。This paper presents an agentic retrieval-augmented generation (RAG) framework for domain-specific technical reasoning support, instantiated over a curated corpus of approximately 2,100 academic papers in intelligent tires, vehicle dynamics, and vehicle control. Unlike conventional single-pass RAG systems, the proposed architecture employs a 13-step autonomous pipeline that classifies queries by intent, scores evidence sufficiency against a multi-dimensional rubric, performs agentic retry with drift-guarded query reformulation, searches external academic databases (Crossref, OpenAlex, Semantic Scholar) through iterative optimize--search--vet loops, traverses a Neo4j knowledge graph for relational context, verifies citation integrity, and applies post-generation quality checks with automatic regeneration.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [22] LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning for Agentic Language Models

- **评分**：9/10
- **作者/机构**：Prateek Kumar Sikdar；机构：prateek.k.sikdar@accenture.com；Agentic language model systems alternate between two structurally distinct step types: structuredtool calls(short,
- **论文链接**：https://arxiv.org/abs/2606.01838
- **PDF**：https://arxiv.org/pdf/2606.01838v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning for Agentic Language Models》展开。Agentic language model systems alternate between two structurally distinct step types: structured tool calls (short, deterministic, low perplexity) and open-ended planning/reasoning steps (long, complex, high perplexity). Despite this heterogeneity, current inference systems apply identical compute to every step.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [23] RadioMaster: Multi-Agent System for Autonomous Radio Signal Generation

- **评分**：9/10
- **作者/机构**：Jiazhen Lei, Tianze Cao, Yuxin Sha, Sihan Wang, Bingbing Wang, Fengyuan Zhu, Zeming Yang, Xiaohua Tian；机构：limitations and fail to accomplish this task when applied to radio
- **论文链接**：https://arxiv.org/abs/2606.01862
- **PDF**：https://arxiv.org/pdf/2606.01862v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《RadioMaster: Multi-Agent System for Autonomous Radio Signal Generation》展开。Translating user intents into physical radio signals represents the critical yet notoriously tedious final step in wireless prototyping, as it requires intricate knowledge of physical layer details and presents immense implementation challenges. Large Language Models (LLMs) and multi-agent systems have revolutionized conventional software engineering, raising the compelling question of whether they can resolve these formidable difficulties.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [24] Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents

- **评分**：9/10
- **作者/机构**：Ailiya Borjigin, Igor Stadnyk, Ben Bilski, Maksym Chikita, Dmytro Kyrylenko, Sofiia Pidturkina, Julia Stadnyk；机构：ailiya.borjigin@gmail.com；igor@true.trading；ben@true.trading
- **论文链接**：https://arxiv.org/abs/2606.01886
- **PDF**：https://arxiv.org/pdf/2606.01886v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents》展开。Financial AI agents often fail for a simple reason: they make users carry the complexity. A user must repeatedly restate goals, risk preferences, portfolio context, past judgments, and shifting market assumptions, while the agent answers, retrieves, acts, and forgets.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：58%。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [25] QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs

- **评分**：9/10
- **作者/机构**：Qizhe Li, Haolong Chen, Shan Dai, Zhuo Li, Zhiwei Hu, Xuan Li, Guangxu Zhu, Qingjiang Shi；机构：qizheli@link.cuhk.edu.cn；The Chinese University of Hong；Shenzhen Research Institute of Big
- **论文链接**：https://arxiv.org/abs/2606.01925
- **PDF**：https://arxiv.org/pdf/2606.01925v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs》展开。Diagnosing Quality-of-Experience (QoE) degradations in operational Radio Access Networks (RANs) is a critical but notoriously complex task, traditionally requiring labor-intensive expert analysis over high-dimensional, cross-layer telemetry. While Large Language Models (LLMs) offer unprecedented reasoning capabilities, they are fundamentally unsuited for raw RANs troubleshooting: they fail at numeric time-series analysis, hallucinate protocol-violating causal links, and lack the stateful rigor required for multi-step fault localization.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [26] AutoMedBench: Towards Medical AutoResearch with Agentic AI Models

- **评分**：9/10
- **作者/机构**：Junqi Liu, Salena Song, Yuhan Wang, Jiawei Mao, Hardy Chen, Xiaoke Huang, Tianhao Qi, Pengfei Guo 等；机构：TOWARDSMEDICALAUTORESEARCH WITHAGENTIC；1University of California, Santa Cruz 2NVIDIA；Autonomous agents are increasingly expected to support end-to-end medical-AI
- **论文链接**：https://arxiv.org/abs/2606.01961
- **PDF**：https://arxiv.org/pdf/2606.01961v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《AutoMedBench: Towards Medical AutoResearch with Agentic AI Models》展开。Autonomous agents are increasingly expected to support end-to-end medical-AI research workflows, moving beyond isolated prediction tasks or short-form clinical question answering. However, existing medical agent benchmarks primarily evaluate final outputs, providing limited visibility into agent behavior within the research process.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure；24 tasks。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [27] SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning

- **评分**：9/10
- **作者/机构**：Lichao Wang, Zhaoxing Ren, Tianzhuo Yang, Jiaming Ji, Chi Harold Liu, Yaodong Yang, Juntao Dai；机构：1Beijing Institute of Technology；2Beijing Academy of Artificial Intelligence；3Institute for Artificial Intelligence, Peking University
- **论文链接**：https://arxiv.org/abs/2606.01991
- **PDF**：https://arxiv.org/pdf/2606.01991v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning》展开。As Large Language Model (LLM) agents increasingly leverage the Model Context Protocol (MCP) to operate in complex environments, the expansion of their action spaces offers agents unsafe capabilities and underscores the risk of power-seeking. While broad action space and greater environment influence are essential for task fulfillment, they create a fragile risk surface where minor errors or hallucinations are magnified into catastrophic failures.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [28] BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning

- **评分**：9/10
- **作者/机构**：Shannon Serrao, Soumitra Chatterjee, Dorina Strori, Abhishek Sharma, Nathan Miller；机构：BADGER — Merkle；Shannon Serrao ∗ Soumitra Chatterjee ∗ Dorina Strori ∗；Merkle Analytics
- **论文链接**：https://arxiv.org/abs/2606.02109
- **PDF**：https://arxiv.org/pdf/2606.02109v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning》展开。Enterprise AI systems that translate natural language into SQL queries and orchestrate multi-step agentic reasoning pipelines require evaluation approaches fundamentally different from academic benchmarks. Spider and BIRD established execution-accuracy protocols; G-Eval and RAGAS advanced LLM-based assessment; and recent work such as Spider 2.0, BEAVER, and BIRD-Interact has begun to address enterprise and agentic dimensions.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [29] Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning

- **评分**：9/10
- **作者/机构**：Liuji Chen, Dianxing Tang, Xing Shi, Dingshuo Chen, Qiang Liu, Shu Wu, Liang Wang；机构：Learning When Not to Act: Mitigating Tool Abuse in Agentic；1NLPR, Institute of Automation, Chinese Academy of Sciences,；2ByteDance, 3Zhejiang University,
- **论文链接**：https://arxiv.org/abs/2606.02132
- **PDF**：https://arxiv.org/pdf/2606.02132v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning》展开。Agentic reinforcement learning can induce tool abuse, where models overuse external tools even for queries solvable by internal reasoning. Existing approaches mitigate this issue with uniform tool-use penalties or hard limits, which reduce tool frequency but may also suppress useful tool-assisted exploration.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [30] POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems

- **评分**：9/10
- **作者/机构**：Iñaki Dellibarda Varela, R. Sendra-Arranz, Pablo Romero-Sorozabal, J. M. Valverde-García, Annemarie F. Laudanski, Álvaro Gutiérrez, Eduardo Rocon, Manuel Cebrian；机构：1Center for Automation and Robotics, Spanish National Research；*Corresponding author(s). E-mail(s): i.dellibarda@csic.es; e.rocon@csic.es;；challenge is not only technical; it is increasingly regulatory. Under the EU AI Act
- **论文链接**：https://arxiv.org/abs/2606.02282
- **PDF**：https://arxiv.org/pdf/2606.02282v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems》展开。Orchestrating Large Language Models into Multi-Agent Systems (LLM-MAS) has unlocked remarkable reasoning capabilities, yet emergent failures and hallucinations that resist characterisation block their deployment in safety-critical domains -- a gap made legally untenable by emerging AI regulation. Existing evaluation paradigms share a common flaw: centralised judgment creates single points of failure and demands domain-specific expertise.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [31] SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training

- **评分**：9/10
- **作者/机构**：Zhongyu He, Yuanfan Li, Fei Huang, Tianyu Chen, Siyuan Chen, Xingyang Li, Meng Hsuan Yu, Xiangrong Liu 等；机构：1Xiamen University, 2Meituan, 3Macao Polytechnic University,；Correspondence:hezhongyu@stu.xmu.edu.cn；ence, increasing engineering complexity, con-
- **论文链接**：https://arxiv.org/abs/2606.02355
- **PDF**：https://arxiv.org/pdf/2606.02355v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training》展开。Long-horizon LLM agents can benefit from reusable skills, yet existing skill-based methods often rely on external skill generators during training or persistent skill retrieval at inference, increasing engineering complexity, context length, and deployment latency. We propose Self-Internalizing Reinforcement learning with Intrinsic skills (SIRI), a three-phase framework that enables agents to discover, validate, and internalize skills without external skill generators or inference-time skill banks.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：0
Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [32] Iteris: Agentic Research Loops for Computational Mathematics

- **评分**：9/10
- **作者/机构**：Leheng Chen, Zihao Liu, Wanyi He, Bin Dong；机构：Iteris: Agentic Research Loops for Computational；1School of Mathematical Sciences, Peking University；2Beijing International Center for Mathematical Research and the New Cornerstone Science
- **论文链接**：https://arxiv.org/abs/2606.02484
- **PDF**：https://arxiv.org/pdf/2606.02484v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Iteris: Agentic Research Loops for Computational Mathematics》展开。Recent advances in large language models and agentic AI systems have enabled significant progress in mathematical discovery, from solving competition problems to tackling research-level conjectures. However, open problems in computational mathematics have received comparatively less attention: research in this area often requires not only proofs but also numerical experimentation, adversarial constructions, and algorithm design.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [33] Bridging the Last Mile of Time Series Forecasting with LLM Agents

- **评分**：9/10
- **作者/机构**：Yuhua Liao, Zetian Wang, Qiangqiang Nie, Zhenhua Zhang；机构：Li et al., 2025). These advances have made it increasingly；Liao<yh liao@trip.com>.
- **论文链接**：https://arxiv.org/abs/2606.02497
- **PDF**：https://arxiv.org/pdf/2606.02497v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Bridging the Last Mile of Time Series Forecasting with LLM Agents》展开。Time series forecasting has advanced rapidly, especially with the emergence of foundation models that show strong zero-shot performance on numerical extrapolation. However, in real-world forecasting settings, a statistically plausible baseline is rarely the final forecast used in practice.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [34] AgentxGCore: Agentic AI for Next-Generation Mobile Core Network

- **评分**：8/10
- **作者/机构**：Maria Katarine Santana Barbosa, Kelvin L. Dias；机构：E-mail:{mksb, kld}@cin.ufpe.br；applications and the increasingly complex network management；as a first step toward integrating analytics, Artificial Intelligence
- **论文链接**：https://arxiv.org/abs/2606.00417
- **PDF**：https://arxiv.org/pdf/2606.00417v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《AgentxGCore: Agentic AI for Next-Generation Mobile Core Network》展开。To meet the stringent requirements of emerging applications and the increasingly complex network management and operation, the Next Generation Mobile Networks (NextG), or 6G, will adopt an AI-native architecture on the Core Network (CN). In this movement, the Third Generation Partnership Project (3GPP) has extended the cellular CN with new function as a first step toward integrating analytics, Artificial Intelligence (AI), and machine learning.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [35] Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution

- **评分**：8/10
- **作者/机构**：Vikas Reddy, Sumanth Challaram；机构：vikas.challaram@gmail.com；sumanth.reddy@iitkgp.ac.in；LLM-based memory systems are increasingly tasked with maintaining facts that evolve over time. A
- **论文链接**：https://arxiv.org/abs/2606.01435
- **PDF**：https://arxiv.org/pdf/2606.01435v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution》展开。LLM-based memory systems increasingly maintain facts that evolve over time, where a recurring failure is conflict resolution: when a fact has multiple contradictory values, which should the agent return? MemoryAgentBench (MAB; Hu et al., 2026) makes this explicit in its FactConsolidation task: facts are numbered, the counterfactual has the higher serial, and agents are told newer facts have larger serials.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是检索增强流程，结合证据筛选、图谱/记忆结构和生成后校验来提升可追溯性。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [36] AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents

- **评分**：8/10
- **作者/机构**：Yiheng Shu, Bernal Jiménez Gutiérrez, Saisri Padmaja Jonnalagedda, Yuguang Yao, Huan Sun, Yu Su；机构：1The Ohio State University 2Johns Hopkins University 3Intuit AI Research；{shu.251, sun.397, su.809}@osu.edu；benchmarks often rely on naive task streams with limited analysis of cross-task
- **论文链接**：https://arxiv.org/abs/2606.02461
- **PDF**：https://arxiv.org/pdf/2606.02461v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents》展开。Language agents spend substantial inference time solving individual tasks, yet the experience acquired in one episode is often underutilized in future episodes. Continual learning expects an agent to accumulate reusable experience across a stream of tasks, improve over time, and avoid interference from irrelevant experiences.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---

## 🤝 多智能体 / 协作


### [37] Deliberative Curation: A Protocol for Multi-Agent Knowledge Bases

- **评分**：9/10
- **作者/机构**：Steven Johnson；机构：and (3) graduated sanctions adapted for stateless agents, including a broken agent handling；integrates baseline defenses against Sybil attacks and sycophancy (commit-reveal voting,；seven behavioral archetypes under two adversity scenarios. The principal finding is that the
- **论文链接**：https://arxiv.org/abs/2606.00007
- **PDF**：https://arxiv.org/pdf/2606.00007v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Deliberative Curation: A Protocol for Multi-Agent Knowledge Bases》展开。As AI agents transition from isolated tools to collaborative participants in shared knowledge ecosystems, governing collective knowledge curation becomes a critical challenge. Human platform governance mechanisms do not transfer directly: agent statelessness undermines deterrence-based sanctions, model homogeneity violates independence assumptions underlying crowd wisdom, and sycophancy collapses deliberative consensus.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [38] How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval

- **评分**：9/10
- **作者/机构**：Nazmus Ashrafi；机构：Independent Researcher；nazmus.s.ashrafi@gmail.com；pass@1 advantage: the leanest architectures match or beat the
- **论文链接**：https://arxiv.org/abs/2606.00308
- **PDF**：https://arxiv.org/pdf/2606.00308v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval》展开。Large-language-model code generation has shifted from single-shot prompting to multi-agent orchestrations - analyst, coder, tester, and debugger pipelines - and is evaluated almost exclusively on functional correctness. Whether these architectures also affect the structural complexity of the code they produce, and which orchestration layers carry the cost, remains largely unexamined: prior work has documented prompt-level effects on code complexity, but the architecture-level question is open.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：130%；130%。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [39] Scaling Behavior of Single LLM-Driven Multi-Agent Systems

- **评分**：9/10
- **作者/机构**：Jialing Li, Zhouhong Gu, Yin Cai, Hongwei Feng；机构：Fudan University；jialingli22@m.fudan.edu.cn；zhgu22@m.fudan.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.00655
- **PDF**：https://arxiv.org/pdf/2606.00655v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Scaling Behavior of Single LLM-Driven Multi-Agent Systems》展开。The burgeoning field of LLM-based Multi-Agent Systems (MAS) promises to tackle complex tasks through collaborative intelligence, yet fundamental questions regarding their scaling behavior and intrinsic collective dynamics remain underexplored. This paper systematically investigates how the performance of a homogeneous MAS evolves as the number of agents increases, isolating the variable of collaboration from model or knowledge heterogeneity.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [40] FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search

- **评分**：9/10
- **作者/机构**：Md Nakhla Rafi, Md Ahasanuzzaman, Dong Jae Kim, Zhijie Wang, Tse-Hsun Chen；机构：Concordia University；mdnakhla.rafi@mail.concordia.ca；m_ahasa@live.concordia.ca
- **论文链接**：https://arxiv.org/abs/2606.00765
- **PDF**：https://arxiv.org/pdf/2606.00765v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search》展开。LLM-based agents increasingly solve complex tasks through long trajectories involving reasoning steps, tool calls, and inter-agent communication. However, when these agents fail, it is often unclear which agent caused the failure and which step introduced the decisive error.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [41] Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems

- **评分**：9/10
- **作者/机构**：Thanh Luong Tuan；机构：Golden Gate University, San Francisco；Enterprise multi-agent systems increasingly expose multiple coordination patterns, but deployments；sonnet, gemma_openrouter, and an auxiliary openai cloud-validation arm. All 1,440 generated outputs
- **论文链接**：https://arxiv.org/abs/2606.00804
- **PDF**：https://arxiv.org/pdf/2606.00804v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems》展开。Enterprise multi-agent systems increasingly expose multiple coordination patterns, but deployments often lack evidence for when to use consensus, debate, synthesis, or a simpler single-agent workflow. This paper evaluates whether coordination strategy should be selected dynamically by problem class rather than fixed globally.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [42] CAREAgent: Clinical Agent with Structured Reasoning and Tool-Integrated for Order Generation

- **评分**：9/10
- **作者/机构**：Ruihui Hou, Ziyue Huai, Chennuo Zhang, Ziyan Liu, Siran Zhao, Yao Yu, Jie Zhai, Tong Ruan；机构：♢East China University of Science and Technology, Shanghai, China,；♣Zhongshan Hospital, Fudan University, Shanghai, China.；including clinical diagnosis (Dou et al., 2024; Wu
- **论文链接**：https://arxiv.org/abs/2606.01094
- **PDF**：https://arxiv.org/pdf/2606.01094v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《CAREAgent: Clinical Agent with Structured Reasoning and Tool-Integrated for Order Generation》展开。Clinical order generation serves as a critical bridge between clinical decision-making and real-world practice, translating medical decisions into concrete and executable orders. Existing agents mainly focus on coarse-grained decisions and overlook the fine-grained, executable information required for clinical orders.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [43] Can LLM Agents Sustain Long-Horizon Organizational Dynamics?

- **评分**：9/10
- **作者/机构**：Xuancheng Zhu, Yang Yue, Shuaibing Wan, Zihan Dou, Xiaohan Zhang, Yongrui Liu, Guoshun Nan；机构：1Beijing University of Posts and Telecommunications, Beijing, China；Large language agents are increasingly used；centered coordination problem and introduce
- **论文链接**：https://arxiv.org/abs/2606.01199
- **PDF**：https://arxiv.org/pdf/2606.01199v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Can LLM Agents Sustain Long-Horizon Organizational Dynamics?》展开。Large language agents are increasingly used for social simulation, yet it remains unclear whether they can sustain coherent behavior in structured organizations, where goals must propagate through hierarchy, tasks depend on prior execution, and artifacts accumulate over long horizons. We formulate long-horizon organizational simulation as a memory-centered coordination problem and introduce TaskWeave, a hierarchical agentic framework that maintains planning states through a Formulate-Partition-Diagnose-Align cycle and grounds execution through dependency-aware trace memory.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [44] Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability

- **评分**：9/10
- **作者/机构**：Xianyou Li, Weiran Yan, Yichao Wu, Penghao Liang, Mengwei Yuan, Jianan Liu, Jing Yang；机构：New York University；xl4230@nyu.edu；Independent Researcher
- **论文链接**：https://arxiv.org/abs/2606.01365
- **PDF**：https://arxiv.org/pdf/2606.01365v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability》展开。Tool-using multi-agent large language model (LLM) systems spend computation through model tokens, tool calls, retries, and code execution before producing an answer. When a run fails, final-answer evaluation reveals the endpoint but usually not the point at which the trajectory stopped making recoverable progress.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：1 runs；2 runs；3 runs。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [45] LLM Consortium for Software Design Refinement: A Controlled Experiment on Multi-Agent Collaboration Topologies

- **评分**：9/10
- **作者/机构**：Nagarjuna Kanamarlapudi, Praveen K；机构：nagarjuna.kanamarlapudi@gmail.com；kpraveen0122@outlook.com
- **论文链接**：https://arxiv.org/abs/2606.01490
- **PDF**：https://arxiv.org/pdf/2606.01490v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《LLM Consortium for Software Design Refinement: A Controlled Experiment on Multi-Agent Collaboration Topologies》展开。We present a controlled experiment evaluating 12 multi-agent LLM collaboration topologies for software architecture design. Using a $2\times2\times2$ factorial design (Authority $\times$ Roles $\times$ Dynamics), we conducted 520 experimental runs across 8 design tasks of varying complexity, with 5 repetitions each.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：520 runs。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [46] Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation

- **评分**：9/10
- **作者/机构**：Donghwan Kim, Prakhar Singh, Younghoon Min, Jongryool Kim, Jongse Park, Kiwan Maeng；机构：1The Pennsylvania State University；*{djk6434,kvm6242}@psu.edu；prohibitive evaluation costs, and limited visibility into propri-
- **论文链接**：https://arxiv.org/abs/2606.01725
- **PDF**：https://arxiv.org/pdf/2606.01725v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation》展开。Agentic AI completes tasks through iterative planning, tool use, and reasoning based on observed outcomes. Despite its popularity, its system-level behavior remains poorly understood, particularly for complex datasets and agent architectures-owing to highly non-deterministic execution, prohibitive evaluation costs, and limited visibility into proprietary models.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [47] Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams

- **评分**：9/10
- **作者/机构**：Zewen Liu, Zhan Shi, Yisi Sang, Bing He, Minhua Lin, Tianxin Wei, Dakuo Wang, Benoit Dumoulin 等；机构：1Emory University 2Amazon 3The Pennsylvania State University 4UIUC 5Northeastern University；{zewen.liu,wei.jin}@emory.edu; luhanqin@amazon.com；GEPA, and Meta-Harness improve LLM agents
- **论文链接**：https://arxiv.org/abs/2606.01770
- **PDF**：https://arxiv.org/pdf/2606.01770v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams》展开。Auto-harness systems such as A-Evolve, GEPA, and Meta-Harness improve LLM agents by optimizing prompts, skills, tools, memories, and supporting infrastructure from execution feedback, but they are typically evaluated on fixed offline benchmarks. Real deployments instead present open-ended task streams: histories grow without a fixed endpoint, heterogeneous tasks require different harnesses, and problem distributions shift over time.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [48] Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus

- **评分**：9/10
- **作者/机构**：Wanshuang Gou, Zihan Liu；机构：1 Chengdu University；proaches include Multi-Agent Debate (MAD)(Du et al.；2023), and MetaGPT(Hong et al. 2024). These systems
- **论文链接**：https://arxiv.org/abs/2606.01828
- **PDF**：https://arxiv.org/pdf/2606.01828v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus》展开。Large language model-driven multi-agent systems enhance the reliability of complex reasoning tasks through multi-round deliberation, role specialization, and cross-validation. However, existing multi-agent debate and collaboration frameworks typically adopt fully connected communication, causing the number of messages, token costs, and end-to-end latency to grow approximately quadratically with the number of agents; although fixed sparse topologies reduce overhead, they cannot adapt communication relationships to different task instances or intermediate reasoning states, making them prone either to preserving low-value interactions or to losing critical error-correction information.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [49] SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes

- **评分**：9/10
- **作者/机构**：Kuan Li, Shuo Zhang, Huacan Wang, Fangzhou Yu, Zecheng Sheng, Yi Gu, Weipeng Ming, Lei Xue 等；机构：1Midea Group 2Beijing University of Posts and Telecommunications；3Donghua University 4The University of Sydney 5Peking University；⋄Work completed during an internship at Midea AI Research Center.
- **论文链接**：https://arxiv.org/abs/2606.01912
- **PDF**：https://arxiv.org/pdf/2606.01912v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes》展开。Smart homes are evolving toward complex state-dependent living environments, requiring Large Language Models (LLMs) to reason over user intent, preferences, and multi-device interactions. However, existing smart-home benchmarks often focus on static instruction-to-API mapping or limited simulations, failing to evaluate whether LLMs can reason, interact, and act reliably in realistic household scenarios.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：100 tasks。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [50] Agentic-J: An AI Agent for Biological Microscopy Image Analysis

- **评分**：9/10
- **作者/机构**：Lukas Johanns, Marilin Moor, Davide Panzeri, Yu Zhou, Xinyi Chen, Nora F. K. Pauly, Zixuan Pan, Matthias Gunzer 等；机构：2Institute of Computer Science, University of Tartu, Tartu, Estonia.；3Faculty of Computer Science, Ruhr University Bochum, Bochum, Germany.；4Informatics Institute, University of Amsterdam, Amsterdam, Netherlands.
- **论文链接**：https://arxiv.org/abs/2606.02080
- **PDF**：https://arxiv.org/pdf/2606.02080v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Agentic-J: An AI Agent for Biological Microscopy Image Analysis》展开。Biological image analysis increasingly demands integration across heterogeneous tools, programming environments, and domain knowledge that few researchers can command simultaneously. We present Agentic-J, a containerised, multi-agent AI assistant, primarily for ImageJ/Fiji that enables biologists to specify analysis tasks in natural language, from nuclei segmentation and cell tracking to multi-condition quantification.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [51] MOC: Multi-Order Communication in LLM-based Multi-Agent Systems

- **评分**：9/10
- **作者/机构**：Yao Guan, Lin Wang, Zhihu Lu, Ziyi Wang, Wenzhu Yan, Qiang Duan；机构：most research focuses on optimizing coordina-；equally critical problem:how to transmit and；these limitations, we propose the Multi-Order
- **论文链接**：https://arxiv.org/abs/2606.02359
- **PDF**：https://arxiv.org/pdf/2606.02359v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《MOC: Multi-Order Communication in LLM-based Multi-Agent Systems》展开。Despite the remarkable progress of Large Language Model (LLM) based Multi-Agent Systems, most research focuses on optimizing coordination topology while largely underexploring the equally critical problem: how to transmit and optimize messages among agents effectively? Current communication schemes typically rely on the direct concatenation of first-order neighbor responses, which induces a restricted evidence receptive field and leads to the dilution of crucial insights over multi-hop paths.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [52] MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation

- **评分**：9/10
- **作者/机构**：Wenhao Wang, Peizhi Niu, Gongyi Zou, Xiyuan Yang, Jingxing Wang, Haoting Shi, Yaxin Du, Jingyi Chai 等；机构：& Intelligence Crew (MAGIC), Shanghai Jiao Tong University,；Shanghai, China 2Department of Computer Science and Technol-；ogy, Zhejiang University, Hangzhou, China 3University of Illinois
- **论文链接**：https://arxiv.org/abs/2606.02470
- **PDF**：https://arxiv.org/pdf/2606.02470v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation》展开。The Model Context Protocol (MCP) has emerged as a transformative standard for connecting large language models (LLMs) with external data sources and tools, and has been rapidly adopted across personal applications and development platforms. However, existing benchmarks predominantly focus on generic information-seeking tools and fail to capture the practical challenges posed by personal social applications, where tools interact with individual accounts or local databases.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [53] Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents

- **评分**：8/10
- **作者/机构**：Yufeng Wang；机构：louiswang524@gmail.com；reliable: inconsistency is 0.0–1.8% across three model families, including；Using this setup, we decompose the “faithfulness gap” into two distinct steps and find
- **论文链接**：https://arxiv.org/abs/2606.00476
- **PDF**：https://arxiv.org/pdf/2606.00476v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents》展开。Do LLM agents act on the reasoning they state? This question of process fidelity is central to using LLMs in social simulation, yet it is hard to measure where no reference for correct behavior exists.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [54] Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design

- **评分**：8/10
- **作者/机构**：Zaifei Yang, Weiyu Chen, Yaqing Wang, James Kwok；机构：1The Hong Kong University of Science and Technology；2City University of Hong Kong；3 Beijing Institute of Mathematical Sciences and Applications
- **论文链接**：https://arxiv.org/abs/2606.00555
- **PDF**：https://arxiv.org/pdf/2606.00555v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design》展开。Structure-based drug design increasingly employs LLM agents to iteratively refine ligands against a target pocket, yet a viable ligand must satisfy two often-conflicting objectives -- binding affinity and druggability -- which single optimization steps rarely improve together. To quantify this difficulty, we introduce two diagnostic metrics: the first measures how often a single edit improves both objectives, and the second measures how often a gain on one objective comes with a loss on the other.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [55] Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate

- **评分**：8/10
- **作者/机构**：Xiqi Hao, Zengqing Wu, Yu-Xuan Qiu, Chuan Xiao, Ruiqi Xu, Shuyuan Zheng, Jianbin Qin；机构：Not All Flips Are Conformity:；1Beijing Institute of Technology, Zhuhai,2University of Osaka,3Shenzhen University；zengqing.wu@ist.osaka-u.ac.jp, qinjianbin@szu.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.00820
- **PDF**：https://arxiv.org/pdf/2606.00820v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate》展开。Multi-agent debate (MAD) is a promising strategy for improving LLM reasoning, but when agents converge on a shared answer, it is unclear whether that convergence reflects genuine deliberation or social compliance. We show that the conventional answer flip rate conflates three distinct mechanisms: spontaneous instability, stance-induced conformity, and reasoning-induced persuasion.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [56] Agentic Clustering: Controllable Text Taxonomies via Multi-Agent Refinement

- **评分**：8/10
- **作者/机构**：Simon Löwe, Emily Silcock；机构：1Burning Glass Institute, 2Harvard University；Correspondence:emilysilcock@fas.harvard.edu；from a corpus and then assign each text to it.
- **论文链接**：https://arxiv.org/abs/2606.01255
- **PDF**：https://arxiv.org/pdf/2606.01255v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Agentic Clustering: Controllable Text Taxonomies via Multi-Agent Refinement》展开。Recent text-clustering methods use large language models to propose a cluster taxonomy from a corpus and then assign each text to it. These pipelines are fundamentally programmatic: the sequence of LLM calls and the rules for stopping, merging, and splitting clusters are fixed in code in advance, so they generalise poorly across corpora of different structure and cannot easily incorporate user-supplied constraints such as a target cluster count or a clustering intent.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [57] Network Distributed Multi-Agent Reinforcement Learning for Consensus Control of Quadcopters

- **评分**：8/10
- **作者/机构**：Youssef Mahran, Zeyad Gamal, Aamir Ahmad, Ayman El-Badawy；机构：1Mechatronics Engineering Department, German University in Cairo (GUC), Egypt；2Institute of Flight Mechanics and Control (IFR), Head of Flight Robotics, University of Stuttgart, Germany；3Faculty of EMS, Head of Mechatronics Engineering Department, German University in Cairo (GUC), Egypt
- **论文链接**：https://arxiv.org/abs/2606.02107
- **PDF**：https://arxiv.org/pdf/2606.02107v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Network Distributed Multi-Agent Reinforcement Learning for Consensus Control of Quadcopters》展开。This paper proposes a Network Distributed Multi-Agent Reinforcement Learning (ND-MARL) framework for quadcopter consensus control. Compared to conventional multi-agent MARL formulations that rely on centralized planning or fully decentralized execution, ND-MARL incorporates the swarm communication graph into the decision process.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [58] Coordination Graphs for Constrained Multi-Agent Reinforcement Learning

- **评分**：8/10
- **作者/机构**：Santiago Amaya-Corredor, Miguel Calvo-Fullana, Anders Jonsson；机构：{santiagoesteban.amaya, miguel.calvo, anders.jonsson}@upf.edu；1Department of Engineering, Universitat Pompeu Fabra, Barcelona, Spain；reward. Collision avoidance, energy budgets, and bandwidth limits must be enforced. Constrained
- **论文链接**：https://arxiv.org/abs/2606.02337
- **PDF**：https://arxiv.org/pdf/2606.02337v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Coordination Graphs for Constrained Multi-Agent Reinforcement Learning》展开。Constrained Multi-agent reinforcement learning (CMARL) faces two intertwined challenges: the joint action space grows exponentially with the number of agents, and additional requirements couple agents in ways that reward structure alone does not capture. We introduce Coordination Graphs for Constrained Multi-Agent Reinforcement Learning (CG-CMARL), a framework that addresses both challenges by combining coordination graphs with Lagrangian duality.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是多智能体通信或协作拓扑，用交互结构影响推理、共识、分工或失败传播。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [59] Skill or Skip? Learning Selective Skill Invocation in Agentic Tasks via Dual-Granularity Preference Learning

- **评分**：9/10
- **作者/机构**：Chishui Chen, Jiaye Lin, Te Sun, Junxi Wang, Yi Yang, Cong Qin, Yangen Hu, Lu Pan 等；机构：1Meituan 2Fudan University 3Shanghai Jiao Tong University；4Nanjing University 5Peking University；{chenchishui, linjiaye}@meituan.com
- **论文链接**：https://arxiv.org/abs/2606.00510
- **PDF**：https://arxiv.org/pdf/2606.00510v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Skill or Skip? Learning Selective Skill Invocation in Agentic Tasks via Dual-Granularity Preference Learning》展开。Agent skills are callable procedural modules that provide reusable knowledge and execution policies for complex agentic tasks. However, existing methods mainly focus on selecting relevant skills or improving the skills themselves, while overlooking whether a relevant skill should actually be invoked at the current decision point.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [60] Acting with AI: An Interaction-Based Framework for Agentic Tort Liability

- **评分**：9/10
- **作者/机构**：Yiheng Yao；机构：Stanford University；should attach. We resolve four incident-anchored cases, situ-
- **论文链接**：https://arxiv.org/abs/2606.00518
- **PDF**：https://arxiv.org/pdf/2606.00518v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Acting with AI: An Interaction-Based Framework for Agentic Tort Liability》展开。Agentic AI systems can plan over multiple steps, use tools, and execute tasks over time. When such systems cause harm, tort law struggles to allocate responsibility because the harmful path may be neither fully chosen by the user nor specifically foreseen by the developer.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [61] Leyline: KV Cache Directives for Agentic Inference

- **评分**：9/10
- **作者/机构**：Bole Ma, Jan Eitzinger, Harald Koestler；机构：Erlangen National High Performance Computing Center；{bole.ma, jan.eitzinger, harald.koestler}@fau.de；dropped, trajectories pivoted. Two distinct
- **论文链接**：https://arxiv.org/abs/2606.01065
- **PDF**：https://arxiv.org/pdf/2606.01065v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Leyline: KV Cache Directives for Agentic Inference》展开。Modern KV cache management assumes the chatbot workload: prompts arrive once and the cache grows append-only, so prefix caching and forward-only eviction are correct by construction. Agentic LLMs break this assumption.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [62] On Effectiveness and Efficiency of Agentic Tool-calling and RL Training

- **评分**：9/10
- **作者/机构**：Tong Liu, Cheng Qian, Matej Cief, Yuan He, Daniele Dan, Nikolaos Aletras, Gabriella Kazai；机构：tation choices including the random seed, sys-；of recent progress in LLM agents (Openai, 2025; Anthropic,；2025b; Deepmind, 2025; xAI, 2025; Meta, 2025). By in-
- **论文链接**：https://arxiv.org/abs/2606.00135
- **PDF**：https://arxiv.org/pdf/2606.00135v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《On Effectiveness and Efficiency of Agentic Tool-calling and RL Training》展开。Tool-calling is a central component of modern large language model (LLM) agents, equipping them with skills beyond their parametric knowledge. This paper studies tool-calling along two complementary axes: effectiveness, i.e., how this capability is measured, and efficiency, i.e., how it is learned.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [63] CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems

- **评分**：9/10
- **作者/机构**：Yannan Wang, Longli Yang, Zhen Liu, Abhishek Kumar, Carsten Maple；机构：Beijing Jiaotong University；yannanwang@bjtu.edu.cn；longli_yang@163.com
- **论文链接**：https://arxiv.org/abs/2606.00756
- **PDF**：https://arxiv.org/pdf/2606.00756v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems》展开。Deploying lightweight Large Language Model (LLM) agents on edge servers can reduce latency and move agentic services closer to users, but resource-constrained edge models often struggle with long-horizon tasks that require persistent memory, subgoal tracking, and reflection. Fine-tuning edge models after deployment is costly and difficult to scale across heterogeneous nodes, while purely local memory leaves agents with isolated experience and growing prompt context.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2.1 Task。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [64] Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations

- **评分**：9/10
- **作者/机构**：Adril Putra Merin, David Anugraha, Ayu Purwarianti, Genta Indra Winata；机构：1Institut Teknologi Bandung 2Stanford University 3Capital One；adrilbless37@gmail.com, davidanu@stanford.edu,；ayu@informatika.org, genta.winata@capitalone.com
- **论文链接**：https://arxiv.org/abs/2606.00832
- **PDF**：https://arxiv.org/pdf/2606.00832v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations》展开。Recent advances in agentic AI have enabled agents to complete complex tasks through tool use, reasoning, and multi-step planning. Yet existing benchmarks evaluate agents within a single session, ignoring past actions, stated preferences, and prior decisions that agents must integrate to fulfill personalized user goals.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure；2.1 Tasks。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [65] Benchmarking Security Risk Detection and Verification in Open Agentic Skill Ecosystems

- **评分**：9/10
- **作者/机构**：Ismail Hossain, Sai Puppala, Zhuoran Lu, Sajedul Talukder, Nan Jiang；机构：1University of Texas at El Paso, TX, USA,2Southern Illinois University-Carbondale, IL, USA,3Purdue；University, IN, USA；malicious skills in the live OpenClaw ecosystem, including samples from the recentClawHavocsupply-
- **论文链接**：https://arxiv.org/abs/2606.00925
- **PDF**：https://arxiv.org/pdf/2606.00925v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Benchmarking Security Risk Detection and Verification in Open Agentic Skill Ecosystems》展开。Open agent platforms allow community contributors to publish reusable skills that agents can invoke at runtime. This extensibility also creates a supply-chain risk: malicious contributors can hide harmful behavior inside skills that appear benign under superficial inspection.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [66] 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code

- **评分**：9/10
- **作者/机构**：Yipeng Gao, Lei Shu, Genzhi Ye, Xi Xiong, Ameesh Makadia, Meiqi Guo, Laurent Itti, Jindong Chen；机构：1Google DeepMind,2Google Research,3University of Southern California；provides high-fidelity feedback for iterative refinement. We release 3DCodeBench, including the curated；Blender Foundation, 2026a; Esri, 2026; IDV, Inc., 2026; SideFX, 2026), driving immense commer-
- **论文链接**：https://arxiv.org/abs/2606.01057
- **PDF**：https://arxiv.org/pdf/2606.01057v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code》展开。Procedural 3D modeling through code is emerging as a versatile paradigm, offering deterministic, engine-ready, and precisely editable assets that neural 3D generators inherently lack. Authoring such procedural content, however, demands deep expertise in 3D software APIs, parametric design, and code-level geometric reasoning.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：4.7
Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [67] TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning

- **评分**：9/10
- **作者/机构**：Yaxuan Kong, Qingren Yao, Yuqi Nie, Yichen Li, Yilei Shao, Stefan Zohren, Anna Vettoruzzo, Joaquin Vanschoren 等；机构：1University of Oxford 2VulpiV ox Intelligence 3Eindhoven University of Technology；4Griffith University 5Squirrel Ai Learning 6East China Normal University；yaxuan.kong@eng.ox.ac.uk; q.yao@tue.nl
- **论文链接**：https://arxiv.org/abs/2606.01498
- **PDF**：https://arxiv.org/pdf/2606.01498v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning》展开。Time series data inform critical decisions across many real-world domains. While large language model (LLM) agents can analyze data through natural language and tools, it remains unclear whether they can conduct reliable time series analysis across multi-turn conversations.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：240 tasks。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [68] Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems

- **评分**：9/10
- **作者/机构**：Ankur Sharma, Deep Shah；机构：Independent Researcher；ankur.sharma@ocproject.net；deepshah146@gmail.com
- **论文链接**：https://arxiv.org/abs/2606.01508
- **PDF**：https://arxiv.org/pdf/2606.01508v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems》展开。Traditional operating systems were designed around deterministic programs, explicit control flow, and human initiated workflows. Their core abstractions processes, threads, system calls, files, and permissions assume bounded behavior and predictable interaction patterns.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [69] Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents

- **评分**：9/10
- **作者/机构**：Aitor Arronte Alvarez, Naiyi Xie Fincham；机构：Naiyi Xie Fincham1[0000−0002−4959−436X]；University of Hawaii at Manoa, Honolulu HI 96822, USA；{arronte,naiyixf}@hawaii.edu
- **论文链接**：https://arxiv.org/abs/2606.01584
- **PDF**：https://arxiv.org/pdf/2606.01584v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents》展开。Conversational tutoring agents have been shown to improve learning engagement and student outcomes, and large language models (LLMs) are increasingly used in these systems to provide scalable, personalized feedback. However, LLMs may perpetuate or amplify stereotypical social biases, posing particular risks in educational settings.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [70] MobEvolve: An Agentic Self-Evolving Heuristic System for Interpretable Human Mobility Generation

- **评分**：9/10
- **作者/机构**：Junlin He, Yihong Tang, Tong Nie, Ao Qu, Yuebing Liang, Hamzeh Alizadeh, Bang Liu, Wei Ma 等；机构：1The Hong Kong Polytechnic University, 2McGill University, 4MIT, 5Tsinghua University,；8Mila – Quebec AI Institute；junlinspeed.he@connect.polyu.hk yihong.tang@mail.mcgill.ca wei.w.ma@polyu.edu.hk lijun.sun@mcgill.ca
- **论文链接**：https://arxiv.org/abs/2606.01640
- **PDF**：https://arxiv.org/pdf/2606.01640v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《MobEvolve: An Agentic Self-Evolving Heuristic System for Interpretable Human Mobility Generation》展开。Human mobility generation aims to synthesize realistic trip chains for target populations based on individual features. Existing paradigms, including deep generative models, LLM-based methods, and traditional heuristics, struggle to satisfy the complex demands of this task while simultaneously maintaining interpretability, behavioral plausibility, population-level distributional alignment, and inference efficiency.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [71] OctoT2I: A Self-Evolving Agentic Text-to-Image Router

- **评分**：9/10
- **作者/机构**：Xu Jiang, Bin Chen, Gehui Li, Yule Duan, Ronggang Wang, Jian Zhang；机构：1School of Electronic and Computer Engineering, Peking University；2Guangdong Provincial Key Laboratory of Ultra High Definition Immersive Media Technology,；Shenzhen Graduate School, Peking University
- **论文链接**：https://arxiv.org/abs/2606.01803
- **PDF**：https://arxiv.org/pdf/2606.01803v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《OctoT2I: A Self-Evolving Agentic Text-to-Image Router》展开。The explosive growth of Text-to-Image (T2I) models, from large-scale versions to lightweight, real-time ones, now faces diminishing marginal returns from single-model scaling. Agentic T2I methods emerged to alleviate this bottleneck by using multiple models.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是工具调用与编排，把 LLM、外部工具、状态监控和反馈回路串成可执行系统。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：3%；6%。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [72] AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations

- **评分**：9/10
- **作者/机构**：Hiskias Dingeto, Will Leeney；机构：hiskias@stackone.com；will@stackone.com；model panel (Anthropic, OpenAI, Google), no-
- **论文链接**：https://arxiv.org/abs/2606.02240
- **PDF**：https://arxiv.org/pdf/2606.02240v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations》展开。Indirect prompt injection in tool-use agents is a concrete production threat: LLM agents read from integrations (third-party services such as Gmail, Salesforce, or Jira accessed through tool calls) whose response content the user neither writes nor controls. Existing benchmarks under-measure the threat: most cover only a handful of integrations with the same attack payload replayed across runs, and open-source guards are trained on chat-style data rather than tool-response content.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：2026

Figure。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [73] COMAP: Co-Evolving World Models and Agent Policies for LLM Agents

- **评分**：9/10
- **作者/机构**：Youwei Liu, Jian Wang, Hanlin Wang, Wenjie Li；机构：1 Central South University 2 College of Computer Science, Sichuan University；3 Department of Computing, The Hong Kong Polytechnic University；loyiv5477@gmail.com wangjian51@scu.edu.cn
- **论文链接**：https://arxiv.org/abs/2606.02372
- **PDF**：https://arxiv.org/pdf/2606.02372v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《COMAP: Co-Evolving World Models and Agent Policies for LLM Agents》展开。Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution. However, existing textual world models are typically fixed after training, preventing them from adapting to the on-policy state-action distributions induced by an evolving agent.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [74] AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design

- **评分**：9/10
- **作者/机构**：Sahil Rahman, Maxx Richard Rahman；机构：tive rather than merely imitating high-fitness se-；1Bedford College, London, United Kingdom 2Saarland Univer-；<srahman@bedford.ac.uk>.
- **论文链接**：https://arxiv.org/abs/2606.02386
- **PDF**：https://arxiv.org/pdf/2606.02386v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design》展开。Protein language models (PLMs) are passive oracles: they generate sequences in a single forward pass with no mechanism to consult external biophysical feedback or redirect generation when a candidate violates thermodynamic or structural constraints. We introduce AgentPLM, which addresses this by equipping a pre-trained PLM with i) Reasoning-Augmented Decoding (RAD), which interleaves autoregressive generation with tool calls (ESMFold, FoldX, AutoDock Vina), and ii) Contrastive Agent Policy Optimisation (CAPO), a trajectory-level extension of direct preference optimisation that trains the policy end-to-end to learn when oracle feedback is informative rather than merely imitating high-fitness sequences.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [75] Policy and World Modeling Co-Training for Language Agents

- **评分**：9/10
- **作者/机构**：Ning Lu, Baijiong Lin, Shengcai Liu, Jiahao Wu, Haoze Lv, Yanbin Wei, Lingting Zhu, Shengju Qian 等；机构：1Southern University of Science and Technology；2Hong Kong University of Science and Technology；3Hong Kong University of Science and Technology (Guangzhou)
- **论文链接**：https://arxiv.org/abs/2606.02388
- **PDF**：https://arxiv.org/pdf/2606.02388v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Policy and World Modeling Co-Training for Language Agents》展开。Reinforcement learning (RL) improves large language model (LLM) agents by teaching them which actions lead to high rewards, but provides little supervision on what those actions do to the environment. World modeling (WM) can fill this gap, yet existing approaches often require separate simulators, extra training stages, or additional inference-time computation.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [76] Food Noise & False Safety: A Systematic Evaluation of How LLMs Fail to Adapt to Eating Disorder Queries with Clinician Feedback

- **评分**：9/10
- **作者/机构**：Giulia Pucci, Emily Hemendinger, Ruizhe Li, Gavin Abercrombie, Tanvi Dinkar, Arabella Sinclair；机构：Gavin Abercrombie(†) Tanvi Dinkar(♭) Arabella Sinclair(♡♭)；(♡)University of Aberdeen(⋄)University of Colorado Anschutz；(†)Heriot-Watt University,(♭)University College London
- **论文链接**：https://arxiv.org/abs/2606.02444
- **PDF**：https://arxiv.org/pdf/2606.02444v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Food Noise & False Safety: A Systematic Evaluation of How LLMs Fail to Adapt to Eating Disorder Queries with Clinician Feedback》展开。Recent evidence shows that people with eating disorders (EDs) are increasingly seeking guidance, advice, and emotional support from Large Language Model (LLM)-based chat systems. Although these systems are not designed to provide clinical advice, their perceived expertise, neutrality and accessibility make them a frequent, albeit risky, source of support.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [77] Monitoring Agentic Systems Before They're Reliable

- **评分**：9/10
- **作者/机构**：Marisa Ferrara Boston, Glen Hanson, Effi Georgala, JD Hudgens, Heather Frase；机构：marisa@reinsai.com；glen@reinsai.com；effi@reinsai.com
- **论文链接**：https://arxiv.org/abs/2606.02494
- **PDF**：https://arxiv.org/pdf/2606.02494v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Monitoring Agentic Systems Before They're Reliable》展开。Agentic systems entering production typically operate as partially integrated assemblies where structural defects, not task-level errors, dominate the failure landscape. At this maturity level, task-level error detection may be infeasible: structural failure modes mask the signal that task-level monitors are designed to detect.We present a monitoring and triage methodology that decomposes agentic system evaluation into three dimensions (quality, suitability, efficiency) at three monitoring scopes (within-run, cross-run, structural), using variance as a characterization signal.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心在任务建模、推理流程和实验评估设计。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
PDF/摘要中可见的量化线索：220
runs。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [78] Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs

- **评分**：8/10
- **作者/机构**：Subhadip Mitra；机构：Subhadip Mitra∗；Research Lead, Rota Labs；subhadip@rotalabs.ai
- **论文链接**：https://arxiv.org/abs/2606.00813
- **PDF**：https://arxiv.org/pdf/2606.00813v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs》展开。Safety alignment in LLMs does not improve monotonically across model generations. Studying four generations of Google's Gemma family (7B-31B) with quality-diversity evolution (MAP-Elites) as an automated red-teaming probe, we find that Gemma 3 (12B) exhibits 68.7% +/- 5.7% attack success rate (ASR; mean +/- std, 3 seeds), significantly higher than its predecessor Gemma 2 (45.5% +/- 7.2%; p = 0.030, paired bootstrap) and its successor Gemma 4 (33.9% +/- 1.8%).

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [79] RoleCDE:Benchmarking and Mitigating Role-Alignment Trade-offs in Role-Playing Agents

- **评分**：8/10
- **作者/机构**：Huayi Lai, Shichao Song, Simin Niu, Hanyu Wang, Jiawei Yang, Zhouxing Wang, Zhiqiang Yin, Xun Liang；机构：RoleCDE: Benchmarking and Mitigating Role–Alignment Trade-offs；1School of Information, Renmin University of China, Beijing, China；offer limited insight into decision making under
- **论文链接**：https://arxiv.org/abs/2606.01552
- **PDF**：https://arxiv.org/pdf/2606.01552v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《RoleCDE:Benchmarking and Mitigating Role-Alignment Trade-offs in Role-Playing Agents》展开。Role-playing agents(RPAs) are widely used to steer large language models(LLMs) toward role-consistent behavior, yet existing benchmarks mainly evaluate surface-level fidelity and offer limited insight into decision making under role-alignment value conflicts. To address this gap, we introduce RoleCDE, the first benchmark designed to evaluate RPAs under structured conflicts between role-specific values and alignment-oriented constraints.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---


### [80] ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL

- **评分**：8/10
- **作者/机构**：Zelin He, Haotian Lin, Boran Han, Wei Zhu, Haoyang Fang, Bernie Wang, Xuan Zhu, Runze Li 等；机构：Inspired by Anthropic’s Skill Creator, we introduce RESKILL , an RL-in-the-loop skill；2026). A pioneering effort is Anthropic’s Skill Creator (Anthropic, 2026), which automates skill creation；(Zhang et al., 2026), principle distillation (Wu et al., 2025), and skill distillation (Xia et al., 2025). However,
- **论文链接**：https://arxiv.org/abs/2606.01619
- **PDF**：https://arxiv.org/pdf/2606.01619v1
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文围绕《ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL》展开。Agentic reinforcement learning (RL) enables LLM agents to improve continuously from environment rewards, yet the resulting policies do not systematically accumulate reusable strategies that generalize across tasks. Modular skills can provide such reusable strategies, yet existing skill-augmented RL methods decouple skill creation from policy optimization, risking adopting skills that conflict with the evolving policy.

**☠️ 毒舌点评**  
这篇更适合按系统论文/评测论文看：重点不是名字里有 Agent，而是任务定义、失败模式、基线和可复现性是否扎实。本次已抽取 PDF 首页/正文文本，评价依据比只看摘要更稳。

**🔧 技术方案**  
- **模型架构**：核心是评测环境/协议，把模型放进可重复的任务流程里，观察决策、工具调用或长程交互表现。  
- **核心创新**：主要价值在把 Agent/LLM 能力放到更具体的系统、评测或长程任务设定里；若缺少强基线和消融，仍应按增量工作处理。  
- **训练 / 推理策略**：多数条目是推理时编排、评测或系统流程；涉及 RL/偏好学习/训练的论文需重点核对奖励、数据和泛化实验。

**📊 实验结果**  
当前可见材料没有足够细的量化数字，需读完整实验章节确认强度。

**💡 为什么值得看**  
适合快速判断今天 Agent/LLM 方向的新系统、评测协议和失败模式；精选优先看可落地、可复现、能暴露能力边界的工作。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
