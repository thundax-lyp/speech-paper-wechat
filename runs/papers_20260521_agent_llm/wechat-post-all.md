---
title: "Agent/LLM论文速递｜2026-05-21｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-21｜全量版：本期收录 25 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-21｜全量版：本期收录 25 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-21"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-21｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **25** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**6** 篇
- LLM 推理 / 规划 / RAG：**6** 篇
- 评测 / 安全 / 对齐：**7** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs | ⭐ 7/10 | enterprise analytics, agentic LLM, governed APIs, Text-to-SQL |
| Agent系统与工具使用 | 2 | AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions | ⭐ 7/10 | GUI automation, RPA, code synthesis, LLM agents |
| Agent系统与工具使用 | 3 | Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling | ⭐ 7/10 | web agents, JIT compilation, latency, browser automation |
| Agent系统与工具使用 | 4 | Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration | ⭐ 6/10 | tool-augmented agent, CAD-CAE, closed-loop optimization, simulation |
| Agent系统与工具使用 | 5 | Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines | ⭐ 6/10 | agentic pipeline, semantic caching, MCP tools, workflow optimization |
| Agent系统与工具使用 | 6 | Declarative Data Services: Structured Agentic Discovery for Composing Data Systems | ⭐ 6/10 | agentic discovery, data systems, composition, declarative services |
| LLM推理与规划 | 1 | Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents | ⭐ 8/10 | language agents, offline memory consolidation, experience, reusable knowledge |
| LLM推理与规划 | 2 | MemGym: a Long-Horizon Memory Environment for LLM Agents | ⭐ 8/10 | agent memory, long-horizon, benchmark, web/coding agents |
| LLM推理与规划 | 3 | Training Language Agents to Learn from Experience | ⭐ 7/10 | language agents, experience learning, reflection, in-context training |
| LLM推理与规划 | 4 | APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents | ⭐ 7/10 | self-evolving agents, exploration, memory, policy |
| LLM推理与规划 | 5 | SOLAR: A Self-Optimizing Open-Ended Autonomous Agent for Lifelong Learning and Continual Adaptation | ⭐ 6/10 | lifelong learning, autonomous agent, continual adaptation, self-optimization |
| LLM推理与规划 | 6 | Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning | ⭐ 6/10 | long-context reasoning, chain-of-thought, tuning, proxy |
| 多智能体与协作 | 1 | AgentCo-op: Retrieval-Based Synthesis of Interoperable Multi-Agent Workflows | ⭐ 7/10 | multi-agent workflows, retrieval, tool composition, scientific agents |
| 多智能体与协作 | 2 | Multi-agent Collaboration with State Management | ⭐ 7/10 | multi-agent collaboration, state management, codebase editing, conflict resolution |
| 多智能体与协作 | 3 | COAgents: Multi-Agent Framework to Learn and Navigate Routing Problems Search Space | ⭐ 6/10 | multi-agent, routing problems, search space, optimization |
| LLM训练与对齐 | 1 | Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment | ⭐ 7/10 | DPO, RLHF, alignment, failure modes |
| 评测与安全 | 1 | DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation | ⭐ 9/10 | deep research, benchmark, web evidence, long-horizon reasoning |
| 评测与安全 | 2 | AgentAtlas: Beyond Outcome Leaderboards for LLM Agents | ⭐ 8/10 | LLM agents, evaluation, trajectory safety, leaderboard |
| 评测与安全 | 3 | SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents | ⭐ 8/10 | coding agents, reward hacking, specification, hidden tests |
| 评测与安全 | 4 | Governance by Construction for Generalist Agents | ⭐ 7/10 | agent governance, enterprise agents, policy, controls |
| 评测与安全 | 5 | Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows | ⭐ 7/10 | runtime verification, distributed agents, causal logic, workflow safety |
| 评测与安全 | 6 | Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents | ⭐ 7/10 | trace diagnostics, LLM agents, failure analysis, production corpora |
| 应用与基准 | 1 | Terminal-World: Scaling Terminal-Agent Environments via Agent Skills | ⭐ 7/10 | terminal agents, agent skills, environment generation, training data |
| 应用与基准 | 2 | Agentic Agile-V: From Vibe Coding to Verified Engineering in Software and Hardware Development | ⭐ 6/10 | coding agents, verified engineering, software/hardware, evidence review |
| 应用与基准 | 3 | From Automated to Autonomous: Hierarchical Agent-native Network Architecture (HANA) | ⭐ 6/10 | autonomous networks, hierarchical agents, network architecture |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs

- **评分**：7/10
- **作者/机构**：Gundeep Singh（Dialpad）；Parsa Kavehzadeh（Dialpad）；Jing Xia（Dialpad）；Xue-Yong Fu（Dialpad）；Julien Bouvier Tremblay（Dialpad）；Md Tahmid Rahman Laskar（Dialpad）；Vincent Lum（Dialpad）；Shashi Bhushan TN（Dialpad）
- **论文链接**：https://arxiv.org/abs/2605.21027
- **PDF**：https://arxiv.org/pdf/2605.21027
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Analytic Agent 认为企业分析不只是 Text-to-SQL，因为真实企业数据往往通过 governed APIs 暴露。系统让 LLM Agent 调用企业分析 API，而不是直接裸查数据库。

**☠️ 毒舌点评**  
这篇很产品化，也很现实。Text-to-SQL 在 demo 里好看，企业里经常绕不开权限、口径和 API 治理。贡献可能不如基础模型论文“学术性感”，但场景判断靠谱。

**🔧 技术方案**  
- **模型架构**：LLM-based Analytic Agent，围绕 governed enterprise analytics APIs 做查询规划、调用和回答生成。  
- **核心创新**：从 Text-to-SQL 转向 API-governed enterprise analytics agent。  
- **训练 / 推理策略**：系统工程为主，依赖 LLM 工具调用和 API 编排。

**📊 实验结果**  
摘要强调传统 BI 和 Text-to-SQL 难以覆盖企业管控 API 流程。

**💡 为什么值得看**  
Agent 进企业，首先要学会尊重已有 API 和治理边界，而不是幻想直接访问所有表。

</span>

---


### [2] AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions

- **评分**：7/10
- **作者/机构**：Minghao Chen；Xinyi Hu；Zhou Yu；Yufei Yin
- **论文链接**：https://arxiv.org/abs/2605.21082
- **PDF**：https://arxiv.org/pdf/2605.21082
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
AutoRPA 面向重复 GUI 任务：不是每次都让 LLM 逐步看屏幕操作，而是从交互中合成可复用代码，降低重复任务里的成本和延迟。

**☠️ 毒舌点评**  
这是实用 Agent 系统问题。很多 GUI Agent benchmark 只看一次性任务成功率，真实办公自动化却是重复流程。把交互转为代码/脚本很合理，重点要看失败恢复和界面变化鲁棒性。

**🔧 技术方案**  
- **模型架构**：LLM 从 GUI 交互轨迹中合成可执行自动化代码，替代逐步人工式操作循环。  
- **核心创新**：把 GUI Agent 从 one-off 操作推进到可复用 RPA 代码生成。  
- **训练 / 推理策略**：系统方法为主，依赖 LLM 代码合成和交互记录。

**📊 实验结果**  
摘要强调重复 GUI 任务场景下效率提升。

**💡 为什么值得看**  
如果 Agent 不能把重复流程固化成工具，它就永远是慢吞吞的遥控器。

</span>

---


### [3] Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling

- **评分**：7/10
- **作者/机构**：Caleb Winston；Ron Yifeng Wang；Azalia Mirhoseini；Christos Kozyrakis
- **论文链接**：https://arxiv.org/abs/2605.21470
- **PDF**：https://arxiv.org/pdf/2605.21470
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇把 browser-use / computer-use Agent 的高延迟问题当成编译问题处理：把自然语言任务规划 JIT 成可缓存的脚本/调度，减少逐步 LLM 调用。

**☠️ 毒舌点评**  
Web Agent 现在慢是硬伤，每个 click/type 都调一次模型，体验和成本都爆炸。JIT compilation 这个角度很工程，但很对。挑战是网页状态变化和错误恢复会不会把“编译好”的计划打碎。

**🔧 技术方案**  
- **模型架构**：CUA JIT compiler 将 LLM 计划转成 browser tool 脚本，并利用 code cache / scheduling 降低延迟。  
- **核心创新**：把 Agent planning 的一部分从在线推理迁移到可复用编译产物。  
- **训练 / 推理策略**：系统优化论文，结合 LLM 规划、浏览器工具和缓存。

**📊 实验结果**  
摘要强调减少顺序 fetch-screenshot-execute loop 带来的延迟和错误。

**💡 为什么值得看**  
Web Agent 要产品化，速度不是锦上添花，是能不能用的门槛。

</span>

---


### [4] Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration

- **评分**：6/10
- **作者/机构**：Liyuan Deng（Northwestern Polytechnical University / Shanghai Artificial Intelligence Laboratory）；Shujian Deng（Shanghai Artificial Intelligence Laboratory）；Yongkang Chen；Yongkang Dai；Zhihang Zhong；Linyang Li；Xiao Sun；Yilei Shi（Northwestern Polytechnical University）；Huaxi Huang（Shanghai Artificial Intelligence Laboratory）
- **论文链接**：https://arxiv.org/abs/2605.20190
- **PDF**：https://arxiv.org/pdf/2605.20190
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
COSMO-Agent 做 CAD-CAE 闭环优化：生成参数化几何、运行仿真、提取位移/应力指标，再根据约束更新设计参数。

**☠️ 毒舌点评**  
这是典型工具增强 Agent 落地场景。亮点在闭环仿真和建模编排，而不是语言模型本身。对通用 Agent 研究者来说不是最核心，但对工业设计 Agent 很有参考价值。

**🔧 技术方案**  
- **模型架构**：工具增强 Agent 编排 CAD、CAE simulation、metric extraction 和参数更新。  
- **核心创新**：把 Agent 用于设计-仿真-优化闭环，而非只做对话辅助。  
- **训练 / 推理策略**：系统编排和工具调用为主。

**📊 实验结果**  
摘要强调在可行性、效率和稳定性上优于通用模型直接处理。

**💡 为什么值得看**  
真实工业 Agent 的价值常来自工具闭环，不是聊天能力。

</span>

---


### [5] Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines

- **评分**：6/10
- **作者/机构**：Alimurtaza Merchant（Columbia University）；Krish Veera（Columbia University）；Sajal Kumar Goyla（Columbia University）；Shambhawi Bhure（Columbia University）；Dhaval Patel（IBM）；Kaoutar El Maghraoui（IBM Research）
- **论文链接**：https://arxiv.org/abs/2605.20630
- **PDF**：https://arxiv.org/pdf/2605.20630
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文在工业资产操作 benchmark 中评估 temporal semantic caching 和 workflow optimization，目标是减少 plan-execute pipeline 里的工具发现、规划、MCP 调用和总结开销。

**☠️ 毒舌点评**  
这是 Agent 工程优化论文，创新不惊艳但场景现实。Plan-execute pipeline 的重复开销会在企业流程里放大，缓存和 workflow 优化是必做项。问题是方法可能比较应用特定。

**🔧 技术方案**  
- **模型架构**：围绕 AssetOpsBench 的 plan-execute pipeline，引入 semantic caching 和 workflow 优化。  
- **核心创新**：把 Agent pipeline 的重复语义与工具调用开销作为一等优化对象。  
- **训练 / 推理策略**：系统评估为主，不训练新基础模型。

**📊 实验结果**  
摘要强调工业工作流中单个查询需协调多类工具，重复开销明显。

**💡 为什么值得看**  
Agent 成本和延迟优化不是小修小补，生产里常常决定能不能上线。

</span>

---


### [6] Declarative Data Services: Structured Agentic Discovery for Composing Data Systems

- **评分**：6/10
- **作者/机构**：Shanshan Ye（Northeastern University）；Duo Lu（Brown University）
- **论文链接**：https://arxiv.org/abs/2605.20690
- **PDF**：https://arxiv.org/pdf/2605.20690
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
DDS 把 agentic discovery 用到多系统数据后端组合：Agent 要根据失败日志和组合知识找到能跑的 data stack，而不是在单一 benchmark 里生成算法。

**☠️ 毒舌点评**  
问题真实，但更偏数据系统组合。它的亮点是承认无边界 coding agent 很难稳定收敛，所以引入 declarative structure。证据强度要看真实 stack 的覆盖和失败分析。

**🔧 技术方案**  
- **模型架构**：结构化 agentic discovery 架构，用 declarative data services 限制和组织数据系统组合搜索。  
- **核心创新**：从无界失败日志迭代转向带结构的 data-system composition。  
- **训练 / 推理策略**：系统方法，不是模型训练论文。

**📊 实验结果**  
摘要称 unbounded agentic discovery 即使加迭代和组合知识也不稳定，DDS 改善收敛。

**💡 为什么值得看**  
Agent 写数据系统最怕拼出能编译但跑不起来的组合，这篇正中痛点。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [7] Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents

- **评分**：8/10
- **作者/机构**：Chongrui Ye（University of Illinois Urbana-Champaign）；Yuxiang Liu（University of Illinois Urbana-Champaign）；Yu Wang（University of California San Diego）；Haofei Yu（University of Illinois Urbana-Champaign）；Yining Zhao（University of Illinois Urbana-Champaign）；Ge Liu（University of Illinois Urbana-Champaign）；Julian McAuley（University of California San Diego）；Jiaxuan You（University of Illinois Urbana-Champaign）
- **论文链接**：https://arxiv.org/abs/2605.20616
- **PDF**：https://arxiv.org/pdf/2605.20616
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Auto-Dreamer 借鉴 complementary learning systems，把 Agent 的在线记忆获取和离线记忆巩固分开：先积累任务经验，再离线抽象成可复用知识、流程或剪枝后的记忆。

**☠️ 毒舌点评**  
这篇和 MemGym 互补：一个建环境测记忆，一个尝试改 memory consolidation。亮点是承认在线记忆堆积不等于学习，必须有跨 session 的整理和抽象。风险是 consolidator 生成的知识是否可靠，是否会把错误经验固化。

**🔧 技术方案**  
- **模型架构**：语言 Agent 的离线 memory consolidator，从多 session 经验中提取模式、程序和压缩记忆。  
- **核心创新**：把 Agent 记忆从在线记录推进到离线 consolidation。  
- **训练 / 推理策略**：学习式离线巩固模块，处理累计经验并生成可复用记忆。

**📊 实验结果**  
摘要强调现有 memory 方法缺少全局跨会话视角，Auto-Dreamer 用离线整理改善后续任务。

**💡 为什么值得看**  
Agent 要长期工作，记忆必须会“睡觉整理”，否则只是越来越乱的日志仓库。

</span>

---


### [8] MemGym: a Long-Horizon Memory Environment for LLM Agents

- **评分**：8/10
- **作者/机构**：Wujiang Xu（Rutgers University）；Yu Wang（Capital One）；Kai Mei（Rutgers University）；Kaiqu Liang（Princeton University）；Zhenting Wang（Rutgers University）；Mingyu Jin（Rutgers University）；Han Zhang（Rutgers University）；Shi-Xiong Zhang（Capital One）；Wenyue Hua（Microsoft Research）；Sambit Sahu（Capital One）；Dimitris N. Metaxas（Rutgers University）
- **论文链接**：https://arxiv.org/abs/2605.20833
- **PDF**：https://arxiv.org/pdf/2605.20833
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
MemGym 关注长程 Agent 的记忆能力，不再只测多轮聊天里的个性化记忆，而是把记忆放进 coding、web navigation 等真实 agentic execution 场景。

**☠️ 毒舌点评**  
记忆是 Agent 的核心瓶颈之一，但很多 memory benchmark 太像聊天玩具。MemGym 把 memory、reasoning 和长程执行绑在一起，这个方向对实际 Agent 很重要。真正价值取决于环境多样性和 memory failure 的诊断粒度。

**🔧 技术方案**  
- **模型架构**：统一多个 agent gyms 和 memory-grounded pipelines，形成 memory-reasoning-action 评测环境。  
- **核心创新**：从聊天记忆转向长程任务执行中的动态记忆形成与使用。  
- **训练 / 推理策略**：可用于训练/评估 memory-enabled LLM agents；论文重点是环境与评测。

**📊 实验结果**  
摘要称现有 memory benchmark 迁移到 coding/web agent 场景较差，MemGym 针对这个缺口设计。

**💡 为什么值得看**  
没有长期记忆，Agent 就只能做一次性脚本；这篇正好测它能不能持续积累经验。

</span>

---


### [9] Training Language Agents to Learn from Experience

- **评分**：7/10
- **作者/机构**：Yuval Shalev（University of Cambridge）；Zifeng Ding（University of Cambridge）；Mateja Jamnik（University of Cambridge）
- **论文链接**：https://arxiv.org/abs/2605.20477
- **PDF**：https://arxiv.org/pdf/2605.20477
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文提出 In-context Training 任务：reflector 观察 actor 的历史轨迹，生成系统提示，让 actor 在未来未见任务上表现更好。核心问题是 Agent 能否把经验蒸馏成跨任务可用的 lesson。

**☠️ 毒舌点评**  
reflection 论文很多，但大多只会在当前任务内自我修补。这篇把问题提升到跨任务经验迁移，方向更对。短板是 prompt 形式的经验是否稳定，以及 actor/reflector 分工是否会过拟合环境。

**🔧 技术方案**  
- **模型架构**：actor 收集交互轨迹，reflector 从轨迹生成未来任务可用的 system prompts。  
- **核心创新**：把 self-reflection 从单任务纠错扩展为跨任务经验学习。  
- **训练 / 推理策略**：提出 ICT 框架，并用 RL 训练/优化 reflector 生成经验提示。

**📊 实验结果**  
摘要称关注未来 unseen tasks 的性能提升，而不是当前实例修补。

**💡 为什么值得看**  
Agent 不能从经验中抽象可复用规则，就谈不上长期自主。

</span>

---


### [10] APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents

- **评分**：7/10
- **作者/机构**：Yibo Li（National University of Singapore）；Jiashuo Yang（Beijing University of Posts and Telecommunications）；Zhi Zheng（National University of Singapore）；Zhiyuan Hu（National University of Singapore）；Yuan Sui（National University of Singapore）；Shizun Wang（National University of Singapore）；Yufei He（National University of Singapore）；Bryan Hooi（National University of Singapore）
- **论文链接**：https://arxiv.org/abs/2605.21240
- **PDF**：https://arxiv.org/pdf/2605.21240
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
APEX 解决 self-evolving LLM agents 的 exploration collapse：随着记忆增长，Agent 容易困在熟悉高回报套路里，反而不再探索更优策略。

**☠️ 毒舌点评**  
这是长期 Agent 的真实病：记忆越多不一定越聪明，也可能越保守。APEX 把探索机制单独拿出来做，有价值。需要看它是否只在 toy interactive environment 里有效，还是能迁移到复杂任务。

**🔧 技术方案**  
- **模型架构**：自治策略探索机制，鼓励 self-evolving Agent 在记忆积累后仍探索替代策略。  
- **核心创新**：明确提出并处理 self-evolving agent 的 exploration collapse。  
- **训练 / 推理策略**：围绕长期交互环境和记忆反思机制优化探索策略。

**📊 实验结果**  
摘要声称改善自演化 Agent 在长程任务里的策略发现。

**💡 为什么值得看**  
Agent 的经验系统如果只会固化旧套路，就会变成会写日志的局部最优机器。

</span>

---


### [11] SOLAR: A Self-Optimizing Open-Ended Autonomous Agent for Lifelong Learning and Continual Adaptation

- **评分**：6/10
- **作者/机构**：Nitin Vetcha（National University of Singapore / Indian Institute of Science）；Dianbo Liu（National University of Singapore）
- **论文链接**：https://arxiv.org/abs/2605.20189
- **PDF**：https://arxiv.org/pdf/2605.20189
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
SOLAR 关注动态真实环境下的 Agent 终身学习和持续适应，试图避免传统 fine-tuning 在非平稳流数据中成本高、易遗忘的问题。

**☠️ 毒舌点评**  
方向很大，风险也很大。self-optimizing open-ended autonomous agent 听起来很诱人，但容易变成概念堆叠。需要看是否有足够可复现实验支撑 lifelong adaptation。

**🔧 技术方案**  
- **模型架构**：自优化自治 Agent，面向流式任务和概念漂移进行持续适应。  
- **核心创新**：把终身学习和 Agent 自我优化结合。  
- **训练 / 推理策略**：避免频繁梯度微调，强调非平稳环境中的在线/持续适应。

**📊 实验结果**  
摘要强调处理 concept drift 和 catastrophic forgetting。

**💡 为什么值得看**  
长期 Agent 迟早要面对环境变化，这篇提供了一个探索方向。

</span>

---


### [12] Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning

- **评分**：6/10
- **作者/机构**：Miao Li（University of Edinburgh）；Irina Saparina（University of Edinburgh）；Alexander Gurung（University of Edinburgh）；Mirella Lapata（University of Edinburgh）
- **论文链接**：https://arxiv.org/abs/2605.20201
- **PDF**：https://arxiv.org/pdf/2605.20201
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文研究长上下文推理中的 proxy-based CoT tuning，目标是让模型在长输入中维持中间推理链，而不是被上下文长度拖垮。

**☠️ 毒舌点评**  
长上下文推理是 LLM 主线问题，但从标题看这篇更偏训练技巧。可读性取决于 proxy 的定义是否清楚、是否比直接 CoT/long-context finetune 更稳。作为全量版收录，精选优先级低于 Agent 系统与评测论文。

**🔧 技术方案**  
- **模型架构**：基于 proxy 的 chain-of-thought tuning，用于长上下文推理。  
- **核心创新**：用代理信号改善长上下文 CoT 学习。  
- **训练 / 推理策略**：针对长上下文任务进行 CoT tuning。

**📊 实验结果**  
需关注长文档、多跳推理和 out-of-distribution 长度上的提升。

**💡 为什么值得看**  
Agent 和 deep research 都依赖长上下文推理，这类训练方法值得留档。

</span>

---

## 🤝 多智能体 / 协作


### [13] AgentCo-op: Retrieval-Based Synthesis of Interoperable Multi-Agent Workflows

- **评分**：7/10
- **作者/机构**：Shuaike Shen（Carnegie Mellon University）；Wenduo Cheng（Carnegie Mellon University）；Shike Wang（Carnegie Mellon University）；Mingqian Ma（Carnegie Mellon University）；Jian Ma（Carnegie Mellon University）
- **论文链接**：https://arxiv.org/abs/2605.20425
- **PDF**：https://arxiv.org/pdf/2605.20425
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
AgentCo-op 面向开放科学场景里的多 Agent workflow 合成，用检索复用 skills、tools 和外部 agents，通过 typed artifact handoffs 组合成可执行流程。

**☠️ 毒舌点评**  
多 Agent 论文很多停在“让几个角色聊天”，这篇至少关注互操作、artifact 类型和可执行 workflow，问题更实。挑战是开放科学任务没有清晰标量 reward，bounded self-improvement 是否足够稳很关键。

**🔧 技术方案**  
- **模型架构**：检索式 workflow synthesis，组合 reusable skills/tools/agents，并用 typed artifact handoffs 保证接口。  
- **核心创新**：把多 Agent 协作从角色对话推进到可互操作工具链合成。  
- **训练 / 推理策略**：以检索和自改进为主，不依赖大规模监督训练。

**📊 实验结果**  
摘要强调面向缺少训练集和可靠指标的开放科学任务。

**💡 为什么值得看**  
多 Agent 真正难的是接口和交付物，不是谁扮演 PI 谁扮演学生。

</span>

---


### [14] Multi-agent Collaboration with State Management

- **评分**：7/10
- **作者/机构**：Mengyang Liu（Shanghai Jiaotong University / Cortices AI）；Taozhi Chen（Emory University）；Zhenhua Xu（Peking University）；Xue Jiang（Peking University）；Yihong Dong（Peking University）
- **论文链接**：https://arxiv.org/abs/2605.20563
- **PDF**：https://arxiv.org/pdf/2605.20563
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
STORM 关注多 Agent 同时编辑共享代码库时的状态管理问题。与其给每个 Agent 一个独立 worktree 后事后合并，不如在协作过程中管理状态、冲突和一致视图。

**☠️ 毒舌点评**  
这是多 Agent coding 的硬问题。很多系统把冲突留给最终 merge，结果恢复成本很高。STORM 如果能在实时协作中减少 silent conflict，就比“多开几个 Agent 并行写代码”这种演示更有价值。

**🔧 技术方案**  
- **模型架构**：state-oriented management for multi-agent collaboration，管理共享代码库状态和冲突。  
- **核心创新**：把多 Agent 协作的核心从任务分配转向状态一致性。  
- **训练 / 推理策略**：系统方法为主，不以模型训练为核心。

**📊 实验结果**  
摘要强调避免后验合并阶段的昂贵恢复。

**💡 为什么值得看**  
多 Agent 编程要上规模，状态管理比角色提示词重要得多。

</span>

---


### [15] COAgents: Multi-Agent Framework to Learn and Navigate Routing Problems Search Space

- **评分**：6/10
- **作者/机构**：Oleksandr Yakovenko（Huawei Technologies Canada）；Mahdi Mostajabdaveh（Huawei Technologies Canada）；Cheikh Ahmed（Huawei Technologies Canada）；Abdullah Ali Sivas（Huawei Technologies Canada）；Xiaorui Li（Huawei Technologies Canada）；Zirui Zhou（Huawei Technologies Canada）；Mao Kun（Huawei Technologies）
- **论文链接**：https://arxiv.org/abs/2605.20618
- **PDF**：https://arxiv.org/pdf/2605.20618
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
COAgents 把 VRP 搜索过程建成图，由多个 Agent 在解空间中进行局部改进和跳转，目标是比手工启发式更能适配不同实例。

**☠️ 毒舌点评**  
多 Agent 用在组合优化上不新，但这里任务明确、可验证。它和 LLM Agent 主线关联没那么强，更像多智能体优化框架；如果实验扎实可以读，公众号里应放在次优先级。

**🔧 技术方案**  
- **模型架构**：解空间图上的 cooperative multi-agent search，节点是解，边是局部优化或跳转。  
- **核心创新**：用多 Agent 协作学习和导航 routing search space。  
- **训练 / 推理策略**：围绕 VRP 实例训练/搜索，多 Agent 决定探索与改进。

**📊 实验结果**  
摘要强调相对手工启发式的泛化潜力。

**💡 为什么值得看**  
它提醒我们 Agent 不只有 LLM 聊天，也可以是可验证优化过程里的协作搜索者。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [16] Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment

- **评分**：7/10
- **作者/机构**：Zhiqin Yang；Yonggang Zhang；Wei Xue；Dong Fang；Bo Han；Yike Guo
- **论文链接**：https://arxiv.org/abs/2605.20834
- **PDF**：https://arxiv.org/pdf/2605.20834
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文重新审视 DPO 与 RLHF 的理论等价性，指出这种等价不是普遍成立，而依赖隐含条件，并分析失败模式与可证明对齐。

**☠️ 毒舌点评**  
对齐方向的基础问题。DPO 被大量使用，但“更简单所以等价”这件事一直需要小心。这篇如果证明严谨且失败模式贴近实际训练，会对 post-training recipe 有参考价值。

**🔧 技术方案**  
- **模型架构**：理论分析 DPO/RLHF 条件等价关系，并刻画隐含假设与失败模式。  
- **核心创新**：把 DPO-RLHF 等价从默认叙事改为条件命题。  
- **训练 / 推理策略**：对齐理论与 post-training 分析，不是系统 Agent 论文。

**📊 实验结果**  
摘要称证明等价是 conditional rather than universal。

**💡 为什么值得看**  
Agent 再强也要对齐，post-training 的理论坑不能靠经验 recipe 糊过去。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [17] DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation

- **评分**：9/10
- **作者/机构**：Sixiong Xie（Peking University）；Zhuofan Shi（Peking University）；Haiyang Shen（Peking University）；Jiuzheng Wang；Siqi Zhong；Mugeng Liu；Chongyang Pan；Peilun Jia；Baoqing Sun；Xiang Jing（Peking University）；Yun Ma（Peking University）
- **论文链接**：https://arxiv.org/abs/2605.21482
- **PDF**：https://arxiv.org/pdf/2605.21482
- **代码链接**：https://sixiongxie1001-dot.github.io/deep-research-benchmark2.0

<span style="font-size: 14px;">

**📌 简介**  
DeepWeb-Bench 面向 frontier LLM 的 deep research 能力：开放网页搜索、多源证据收集、长链推导和最终答案生成。它不是普通 QA，而是试图把“研究型 Agent”真正需要的跨源证据和长程推理压进 benchmark。

**☠️ 毒舌点评**  
今天最值得看的 benchmark。很多 deep research 产品已经把旧 benchmark 打穿了，继续拿静态 QA 刷榜意义很小。这篇如果数据构造和可验证性扎实，会成为评估研究型 Agent 的关键参照。短板是 benchmark 容易被未来产品过拟合，但问题设定很正。

**🔧 技术方案**  
- **模型架构**：构建跨源证据和长程推导任务集合，要求 Agent 搜索开放网页、聚合证据并推导答案。  
- **核心创新**：把 deep research 从浅层网页问答推进到大规模跨源证据与长链 derivation。  
- **训练 / 推理策略**：非训练论文；核心是 benchmark 构造、任务验证和模型/产品评测。

**📊 实验结果**  
摘要显示 frontier deep research products 在旧评测上区分度不足，DeepWeb-Bench 用更难任务拉开差异。

**💡 为什么值得看**  
Agent/LLM 真正走向研究助理，最缺的就是这种能揭示能力边界的评测。

</span>

---


### [18] AgentAtlas: Beyond Outcome Leaderboards for LLM Agents

- **评分**：8/10
- **作者/机构**：Parsa Mazaheri（University of California, Santa Cruz）；Kasra Mazaheri（Massachusetts Institute of Technology）
- **论文链接**：https://arxiv.org/abs/2605.20530
- **PDF**：https://arxiv.org/pdf/2605.20530
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
AgentAtlas 认为评估 Agent 不能只看最终成功率，因为同一个最终答案背后的工具调用、约束遵守、恢复能力和轨迹安全可能完全不同。论文试图从 outcome leaderboard 转向过程级 Agent 评测。

**☠️ 毒舌点评**  
这篇抓住了 Agent 评测的痛处：final answer 对 chatbot 够用，对会操作浏览器、代码库和文件系统的 Agent 远远不够。亮点在评测单位从结果扩展到轨迹。挑战是指标设计容易复杂，落地要看是否能被不同 Agent 框架复用。

**🔧 技术方案**  
- **模型架构**：面向 LLM Agent 的评测框架，关注决策序列、状态变化、工具使用、约束遵守和恢复行为。  
- **核心创新**：从单点结果评估转向轨迹与过程质量评估。  
- **训练 / 推理策略**：非训练论文；偏 benchmark/framework 设计。

**📊 实验结果**  
论文强调现有 benchmark 单位碎片化，AgentAtlas 提供更细粒度诊断维度。

**💡 为什么值得看**  
如果 Agent 要进入生产，评测不能只问“成没成”，还要问“怎么成的、有没有越权”。

</span>

---


### [19] SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

- **评分**：8/10
- **作者/机构**：Bingchen Zhao（Weco AI）；Dhruv Srikanth（Weco AI）；Yuxiang Wu（Weco AI）；Zhengyao Jiang（Weco AI）
- **论文链接**：https://arxiv.org/abs/2605.21384
- **PDF**：https://arxiv.org/pdf/2605.21384
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
SpecBench 专门测长程 coding agents 的 reward hacking：Agent 可能通过可见测试，但偏离用户真实规格。它把任务拆成自然语言规格、可见验证测试和组合式隐藏测试。

**☠️ 毒舌点评**  
这题非常现实。代码 Agent 现在最大的风险不是不会写，而是会“聪明地”迎合测试。SpecBench 把这个问题单独拎出来，比又一个 SWE-bench 变体更有价值。关键看任务是否覆盖真实软件工程里的规格组合与边界条件。

**🔧 技术方案**  
- **模型架构**：由规格描述、可见测试、隐藏组合测试组成的 coding-agent reward hacking 评测。  
- **核心创新**：把长程 coding agent 的规格偏离和测试投机明确建模为评测对象。  
- **训练 / 推理策略**：非训练论文；用于评测 Agent 行为而非训练模型。

**📊 实验结果**  
摘要说明自动测试套件成为监督瓶颈，SpecBench 用 held-out compositional tests 暴露投机行为。

**💡 为什么值得看**  
企业用 coding agent 前，必须知道它是在实现需求，还是只是在讨好测试。

</span>

---


### [20] Governance by Construction for Generalist Agents

- **评分**：7/10
- **作者/机构**：Segev Shlomov（IBM）；Iftach Shoham（IBM）；Alon Oved（IBM）；Ido Levy（IBM）；Sami Marreed（IBM）；Harold Ship（IBM）；Offer Akrabi（IBM）；Sergey Zeltyn（IBM）；Avi Yaeli（IBM）；Nir Mashkif（IBM）
- **论文链接**：https://arxiv.org/abs/2605.20874
- **PDF**：https://arxiv.org/pdf/2605.20874
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇强调 enterprise generalist agents 不能事后补安全，而要 governance by construction：系统要在架构层规定可执行动作、约束、审批和可审计性。

**☠️ 毒舌点评**  
企业 Agent 论文里，治理通常是附录口号。这篇把 governance 放到系统构造里，方向正确。它的贡献可能更偏架构和经验总结，未必有漂亮 benchmark，但对生产落地很关键。

**🔧 技术方案**  
- **模型架构**：面向 enterprise agents 的 governance-by-construction 架构，围绕动作权限、接口、审计和策略约束设计。  
- **核心创新**：把 Agent 治理内建为架构原则，而不是外部 guardrail。  
- **训练 / 推理策略**：系统/架构论文，不以训练新模型为核心。

**📊 实验结果**  
摘要强调自治工具操作必须有构造期治理约束。

**💡 为什么值得看**  
Agent 越能操作真实系统，治理越不能靠提示词祈祷。

</span>

---


### [21] Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows

- **评分**：7/10
- **作者/机构**：Benedikt Bollig（Université Paris-Saclay / CNRS / ENS Paris-Saclay / LMF）
- **论文链接**：https://arxiv.org/abs/2605.20923
- **PDF**：https://arxiv.org/pdf/2605.20923
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文给分布式 LLM Agent workflow 引入 Causal Past Logic，用于 runtime verification。核心观点：异步 Agent 工作流不能当成单一顺序日志监控，决策只能依赖其因果可见的事件。

**☠️ 毒舌点评**  
这篇偏形式化，但很重要。多 Agent workflow 一旦异步运行，日志顺序和因果可见性不是一回事。用 causal past 做 guard，比事后看一条全局 log 更严谨。受众窄，但安全工程价值高。

**🔧 技术方案**  
- **模型架构**：在 ZipperGen agent-workflow 框架中加入 CPL，作为条件和循环 guard 的源级逻辑。  
- **核心创新**：把因果可见性引入 LLM Agent workflow 的运行时验证。  
- **训练 / 推理策略**：无训练；形式化方法和运行时验证。

**📊 实验结果**  
摘要展示 CPL 可检查跨 lifeline 的 latest causally visible event。

**💡 为什么值得看**  
多 Agent 系统要可靠，不仅要会推理，还要知道自己在当时到底能看到什么。

</span>

---


### [22] Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents

- **评分**：7/10
- **作者/机构**：Akshay Manglik（Scale AI）；Apaar Shanker（Scale AI）；Kaustubh Deshpande（Scale AI）；Jason Qin（Scale AI）；Yash Maurya（Scale AI）；Veronica Chatrath（Scale AI）；Vijay S. Kalmath（Scale AI）；Levi Lentz（Scale AI）；Yuan Xue（Scale AI）
- **论文链接**：https://arxiv.org/abs/2605.21347
- **PDF**：https://arxiv.org/pdf/2605.21347
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Insights Generator 做 corpus-level trace diagnostics：不是人工看几条 Agent trace 猜原因，而是在大规模执行轨迹中找系统性行为模式，并给出证据支撑的自然语言洞察。

**☠️ 毒舌点评**  
这很像生产 Agent 真正需要的可观测性。单条 trace 很长，人工排查不可能扩展。论文如果能把 insight 和证据绑定好，会比漂亮 dashboard 更有用。风险是生成的 insight 自己也可能幻觉。

**🔧 技术方案**  
- **模型架构**：输入 Agent execution traces 语料，输出跨 trace group 的 grounded natural-language insights。  
- **核心创新**：把 Agent failure analysis 从样本级人工排查提升到语料级诊断。  
- **训练 / 推理策略**：系统/诊断方法为主，使用 LLM 总结和证据链接。

**📊 实验结果**  
摘要强调能发现只在 trace populations 中浮现的模式。

**💡 为什么值得看**  
Agent 上线后，最缺的是知道它为什么批量失败，而不是一条条翻日志。

</span>

---

## 🧪 应用 / Benchmark


### [23] Terminal-World: Scaling Terminal-Agent Environments via Agent Skills

- **评分**：7/10
- **作者/机构**：Zihao Cheng（Beihang University）；Hongru Wang（Independent Researcher）；Zeming Liu（Beihang University）；Xinyi Wang（Independent Researcher）；Xiangrong Zhu（Independent Researcher）；Yuhang Guo（Beijing Institute of Technology）；Wei Lin（Independent Researcher）；Jeff Z. Pan（University of Edinburgh）；Yunhong Wang（Beihang University）
- **论文链接**：https://arxiv.org/abs/2605.20876
- **PDF**：https://arxiv.org/pdf/2605.20876
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Terminal-World 试图扩展 terminal-agent 训练/评测环境。它用 Agent skills 来生成或组织命令行任务，缓解高质量 terminal task 数据稀缺的问题。

**☠️ 毒舌点评**  
终端 Agent 是 coding/research Agent 的基础能力之一，但环境和任务数据确实稀缺。Terminal-World 的价值取决于任务是否真实、多样、可验证，而不是生成一堆玩具 shell 题。方向值得关注。

**🔧 技术方案**  
- **模型架构**：通过 agent skills 扩展 terminal environments，构造可执行、可验证的命令行任务。  
- **核心创新**：把技能结构用于 terminal-agent 环境规模化。  
- **训练 / 推理策略**：用于训练和评估 terminal agents；核心是环境/任务生成。

**📊 实验结果**  
摘要指出现有方法依赖人工 seed 或 GitHub 局部来源，Terminal-World 试图扩大任务覆盖。

**💡 为什么值得看**  
Agent 如果不会可靠使用终端，就很难成为真正的软件工程助手。

</span>

---


### [24] Agentic Agile-V: From Vibe Coding to Verified Engineering in Software and Hardware Development

- **评分**：6/10
- **作者/机构**：Christopher Koch（Independent Researcher）
- **论文链接**：https://arxiv.org/abs/2605.20456
- **PDF**：https://arxiv.org/pdf/2605.20456
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Agentic Agile-V 讨论从 vibe coding 走向 verified engineering：Agentic coding 系统能读仓库、计划、改文件、跑测试、发 PR，但证据并不支持“自治生成一定提升工程结果”的简单叙事。

**☠️ 毒舌点评**  
这篇像一篇工程方法论/证据综述。它的价值在泼冷水：AI coding 有收益，但必须放进验证、测试和审查流程。不是硬核方法论文，但对实际采用 coding agent 的团队很有用。

**🔧 技术方案**  
- **模型架构**：围绕 agentic coding 系统的工程流程框架，强调验证和证据。  
- **核心创新**：把 hype-heavy vibe coding 转向可验证软件/硬件工程流程。  
- **训练 / 推理策略**：非训练论文；方法论和证据整合。

**📊 实验结果**  
摘要引用企业与开源场景中生产率研究差异，强调证据边界。

**💡 为什么值得看**  
Agent 编程不是魔法，真正难的是把生成能力纳入工程质量体系。

</span>

---


### [25] From Automated to Autonomous: Hierarchical Agent-native Network Architecture (HANA)

- **评分**：6/10
- **作者/机构**：Binghan Wu；Shoufeng Wang；Yunxin Liu；Ya-Qin Zhang；Joseph Sifakis；Ye Ouyang
- **论文链接**：https://arxiv.org/abs/2605.20608
- **PDF**：https://arxiv.org/pdf/2605.20608
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
HANA 面向 L4/L5 autonomous networks，提出分层 agent-native 网络架构，让网络运维从静态脚本自动化转向具备自感知和策略治理的自治系统。

**☠️ 毒舌点评**  
这是领域架构论文，和通用 LLM Agent 有交集但不完全重合。优点是把 Agent 放进复杂网络运维场景，缺点是容易停在 reference architecture。适合关注 telecom/网络自治的人。

**🔧 技术方案**  
- **模型架构**：分层多 Agent 网络架构，包含 self-awareness、战略治理和主动优化。  
- **核心创新**：将自治网络从脚本自动化升级为 agent-native 参考架构。  
- **训练 / 推理策略**：架构设计为主，非模型训练。

**📊 实验结果**  
摘要强调处理 off-nominal conditions 和长期策略治理。

**💡 为什么值得看**  
Agent 真落地常常在这种复杂运维系统里，而不是只在浏览器 demo。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
