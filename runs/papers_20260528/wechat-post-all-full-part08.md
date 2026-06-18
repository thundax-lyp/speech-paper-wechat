---
title: "Agent/LLM论文速递｜2026-05-28｜全量版8/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版8/13：本期收录 20 篇，重点看 多智能体与协作；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版8/13：本期收录 20 篇，重点看 多智能体与协作；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "多智能体与协作"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版8/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**11** 篇

这是今天全量版第 8/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| 多智能体与协作 | 1 | Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 2 | Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 3 | LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning | ⭐ 8/10 | agent, multi-agent, RAG, retrieval |
| 多智能体与协作 | 4 | Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 5 | CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disputes Verdict | ⭐ 8/10 | agent, multi-agent |
| 多智能体与协作 | 6 | Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning | ⭐ 8/10 | agent, multi-agent, reasoning |
| 多智能体与协作 | 7 | GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection | ⭐ 8/10 | agent |
| 多智能体与协作 | 8 | SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks | ⭐ 8/10 | agent |
| 多智能体与协作 | 9 | Speed-Weighted Adaptive Flocking for Sailing Swarms under Dynamic Environmental Forcing | ⭐ 5/10 | multi-agent, collaboration |
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

</span>

## 🤝 多智能体 / 协作


### [1] Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems

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


### [2] Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification

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


### [3] LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning

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


### [4] Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems

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


### [5] CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disputes Verdict

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


### [6] Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning

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


### [7] GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection

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


### [8] SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks

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


### [9] Speed-Weighted Adaptive Flocking for Sailing Swarms under Dynamic Environmental Forcing

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


### [10] ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment

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


### [11] DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation

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


### [12] Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning

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


### [13] Zipping the Thought: When and How Compressed Reasoning Data Works in LLM Post-Training

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


### [14] ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains

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


### [15] PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting

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


### [16] Training Stratigraphy: Persistent Behavioral Artifacts in Large Language Models Observed Through Longitudinal AI-Human Interaction

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


### [17] CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models

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


### [18] Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning

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


### [19] AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates

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


### [20] From Learning Resources to Competencies: LLM-Based Tagging with Evidence and Graph Constraints

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

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
