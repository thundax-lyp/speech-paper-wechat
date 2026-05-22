---
title: "Agent/LLM论文速递｜2026-05-22｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-22｜全量版：本期收录 36 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-22｜全量版：本期收录 36 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-22"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-22｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **36** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**8** 篇
- LLM 推理 / 规划 / RAG：**9** 篇
- 评测 / 安全 / 对齐：**13** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems | ⭐ 9/10 | self-evolving agents, source rewriting, production failures, agent systems |
| Agent系统与工具使用 | 2 | Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost | ⭐ 8/10 | workflow compilation, small LLM, orchestration, cost |
| Agent系统与工具使用 | 3 | Trace2Skill: Verifier-Guided Skill Evolution for Long-Context EDA Agents | ⭐ 7/10 | EDA agents, skill evolution, verifier, long context |
| Agent系统与工具使用 | 4 | The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems | ⭐ 7/10 | event sourcing, auditable agents, reactive graphs |
| Agent系统与工具使用 | 5 | Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents | ⭐ 7/10 | self-evolving agents, hygiene, evaluation |
| Agent系统与工具使用 | 6 | Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents | ⭐ 7/10 | runtime harness, deterministic agents, interface adaptation |
| Agent系统与工具使用 | 7 | PocketAgents: A Manifest-Driven Library of Autonomous Defense Agents | ⭐ 6/10 | defense agents, manifest, library |
| Agent系统与工具使用 | 8 | Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents | ⭐ 6/10 | enterprise agents, skills, governance |
| LLM推理与规划 | 1 | Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents | ⭐ 8/10 | agent memory, credit assignment, long-horizon RL, GRPO |
| RAG与知识检索 | 1 | SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval | ⭐ 8/10 | search agents, state-gated retrieval, benchmark, RAG |
| RAG与知识检索 | 2 | SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents | ⭐ 7/10 | multi-hop retrieval, speculation, retrieval agents |
| LLM推理与规划 | 2 | Efficient Agentic Reasoning Through Self-Regulated Simulative Planning | ⭐ 7/10 | simulative planning, agentic reasoning, self-regulation |
| LLM推理与规划 | 3 | IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents | ⭐ 7/10 | speculative planning, idle time, LLM agents |
| LLM推理与规划 | 4 | Planning in the LLM Era: Building for Reliability and Efficiency | ⭐ 6/10 | planning, LLM reliability, survey |
| LLM推理与规划 | 5 | ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning | ⭐ 6/10 | KV cache, tree reasoning, scaling |
| LLM推理与规划 | 6 | Steins;Gate Drive: Semantic Safety Arbitration over Structured Futures for Latency-Decoupled LLM Planning | ⭐ 6/10 | safety arbitration, structured futures, planning |
| LLM推理与规划 | 7 | Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents | ⭐ 5/10 | theory of mind, persuasive agents, reasoning |
| 多智能体与协作 | 1 | Self-Evolving Multi-Agent Systems via Decentralized Memory | ⭐ 7/10 | multi-agent, decentralized memory, self-evolution |
| 多智能体与协作 | 2 | Cross-domain benchmarks reveal when coordinated AI agents improve scientific inference from partial evidence | ⭐ 6/10 | scientific agents, coordination, benchmark |
| 多智能体与协作 | 3 | Claw AI Lab: An Autonomous Multi-Agent Research Team | ⭐ 6/10 | autonomous research team, multi-agent, research agents |
| LLM训练与对齐 | 1 | Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning | ⭐ 7/10 | spreadsheet agents, reinforcement learning, realistic tasks |
| LLM训练与对齐 | 2 | ACC: Compiling Agent Trajectories for Long-Context Training | ⭐ 6/10 | agent trajectories, long-context training, compilation |
| LLM训练与对齐 | 3 | Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts | ⭐ 6/10 | alignment failure, conflict contexts, deployment |
| 评测与安全 | 1 | Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents | ⭐ 8/10 | agent evaluation, trace diagnostics, observability, LLM agents |
| 评测与安全 | 2 | Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety | ⭐ 8/10 | agentic safety, multi-turn benchmark, deception, risk escalation |
| 评测与安全 | 3 | Autonomous LLM Agents & CTFs: A Second Look | ⭐ 7/10 | CTF, autonomous agents, cybersecurity |
| 评测与安全 | 4 | From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents | ⭐ 7/10 | software agents, trajectory supervision, privileged process |
| 评测与安全 | 5 | Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems | ⭐ 7/10 | prompt injection, multi-agent LLM, domain camouflage |
| 评测与安全 | 6 | Benchmarking Autonomous Agents against Temporal, Spatial, and Semantic Evasions | ⭐ 7/10 | autonomous agents, evasion, benchmark |
| 评测与安全 | 7 | SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations | ⭐ 7/10 | tool-calling, synthetic data, agent evaluation |
| 评测与安全 | 8 | Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard | ⭐ 7/10 | security benchmark, agents, measurement |
| 评测与安全 | 9 | LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems | ⭐ 7/10 | multi-agent, KV sharing, latent communication, safety |
| 评测与安全 | 10 | Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs | ⭐ 6/10 | alignment failure, OOD monitors, LLM safety |
| 应用与基准 | 1 | TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks | ⭐ 8/10 | terminal agents, benchmark, real-world tasks, CLI |
| 应用与基准 | 2 | WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance | ⭐ 7/10 | spreadsheet agents, finance, benchmark |
| 应用与基准 | 3 | Evaluating Large Language Models as Live Strategic Agents: Provider Performance, Hybrid Decomposition, and Operational Gaps in Timed Risk Play | ⭐ 5/10 | strategic agents, timed risk, provider comparison |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

- **评分**：9/10
- **作者/机构**：Qianshu Cai；Yonggang Zhang；Xianzhang Jia；Wei Xue；Jun Song；Xinmei Tian；Yike Guo
- **论文链接**：https://arxiv.org/abs/2605.22794
- **PDF**：https://arxiv.org/pdf/2605.22794
- **代码链接**：https://github.com/dav-joy-thon/MOSS

<span style="font-size: 14px;">

**📌 简介**  
MOSS 把自进化 Agent 的可变范围从 prompt、skill、memory 扩到源代码层：从线上失败样本自动构造批次，让外部 coding agent 修改 agent harness，再用回放验证、容器热切换和健康检查做受控发布。

**☠️ 毒舌点评**  
今天最值得看的系统稿。它不是又写一个“会反思的 prompt”，而是承认真实 Agent 的很多 bug 在路由、hook 顺序、状态不变量和 dispatch 代码里。风险也很明显：自改代码的安全边界、评测覆盖和用户授权机制必须非常硬。

**🔧 技术方案**  
- **模型架构**：生产 Agent 系统外包一层演化控制器，包含失败证据聚合、候选补丁生成、临时 worker 回放验证、用户同意门控和容器级回滚。  
- **核心创新**：把 agent evolution 的操作对象提升到 source-level rewriting，覆盖 text artifact 无法触及的结构性失败。  
- **训练 / 推理策略**：不训练基座模型；用外部 coding-agent CLI 生成代码修改，系统侧负责阶段编排、验证和发布判定。

**📊 实验结果**  
在 OpenClaw 上，一个演化周期把四任务平均 grader score 从 0.25 提到 0.61，并给出可回放验证链路。

**💡 为什么值得看**  
如果你关心 Agent 从 demo 走向长期运行，MOSS 提的问题非常核心：系统怎么从真实失败里改自己的代码，而不是只改提示词。

</span>

---


### [2] Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost

- **评分**：8/10
- **作者/机构**：Simon Dennis；Rivaan Patil；Kevin Shabahang；Hao Guo
- **论文链接**：https://arxiv.org/abs/2605.22502
- **PDF**：https://arxiv.org/pdf/2605.22502
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文主张把稳定的 agentic workflow 从外部 orchestrator 编译进小模型权重里，形成“地下 Agent”：流程知识进权重，临时状态留在 prompt，从而减少上下文、成本和第三方暴露。

**☠️ 毒舌点评**  
这个观点很有争议，也很值得吵。它挑战了 LangGraph/CrewAI 这类外部编排默认范式：如果流程长期稳定，为什么每轮都把流程塞进上下文？证据来自少数流程域，外推到开放 Agent 还需要谨慎。

**🔧 技术方案**  
- **模型架构**：将 travel booking、Zoom support、insurance claims 等流程数据转成微调任务，比较小模型 compiled workflow、frontier in-context 和 LangGraph orchestrator。  
- **核心创新**：把 agent workflow 持久结构视为模型权重中的 procedural knowledge，而非每轮外部调度。  
- **训练 / 推理策略**：对 3B/8B 小模型进行流程微调；重编译周期被定位为 CI/CD 级别的部署动作。

**📊 实验结果**  
报告 8B compiled model 达到 frontier in-context 质量的 87-98%，每轮成本降低 128-462 倍，部分任务失败率低于 orchestrator。

**💡 为什么值得看**  
如果你的 Agent 是稳定业务流程，而不是开放探索，这篇会迫使你重新计算“编排框架 vs 微调模型”的账。

</span>

---


### [3] Trace2Skill: Verifier-Guided Skill Evolution for Long-Context EDA Agents

- **评分**：7/10
- **作者/机构**：Zijian Du；Nathaniel Pinckney
- **论文链接**：https://arxiv.org/abs/2605.21810
- **PDF**：https://arxiv.org/pdf/2605.21810
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Trace2Skill 面向 EDA Agent，从执行 trace 中抽取可复用 skill，并用 verifier 引导技能演化。

**☠️ 毒舌点评**  
垂直领域很窄，但“从 trace 到 skill”的路线很有 Agent 工程价值。问题在于 EDA 外的泛化还不确定。

**🔧 技术方案**  
- **模型架构**：读取长上下文执行轨迹，归纳技能并用验证器筛选。  
- **核心创新**：把成功/失败 trace 转成可复用 skill library。  
- **训练 / 推理策略**：以 verifier-guided skill evolution 为主。

**📊 实验结果**  
在 EDA 任务上展示技能演化带来的改进。

**💡 为什么值得看**  
如果你在做企业/垂直 Agent，trace 复盘到技能沉淀是刚需。

</span>

---


### [4] The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems

- **评分**：7/10
- **作者/机构**：Yohei Nakajima
- **论文链接**：https://arxiv.org/abs/2605.21997
- **PDF**：https://arxiv.org/pdf/2605.21997
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
The Log is the Agent 把 Agent 建模为事件溯源的 reactive graph，强调可审计、可 fork 和可回放。

**☠️ 毒舌点评**  
这更像系统设计宣言，但击中了 Agent 工程痛点：没有日志结构，就没有可靠复盘。实验可能不重，思想有启发。

**🔧 技术方案**  
- **模型架构**：用事件日志驱动 Agent 状态和反应图。  
- **核心创新**：把 log 从附属记录提升为 Agent 的核心状态。  
- **训练 / 推理策略**：系统架构设计。

**📊 实验结果**  
主要通过系统论证和案例展示。

**💡 为什么值得看**  
如果你做可观测、可回放 Agent，这篇值得扫。

</span>

---


### [5] Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents

- **评分**：7/10
- **作者/机构**：Xing Zhang；Yanwei Cui；Guanghui Wang；Ziyuan Li；Wei Qiu；Bing Zhu；Peiyang He
- **论文链接**：https://arxiv.org/abs/2605.22148
- **PDF**：https://arxiv.org/pdf/2605.22148
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Ratchet 给自演化 LLM Agent 提出最小 hygiene recipe，强调演化过程中的评测、版本和失败控制。

**☠️ 毒舌点评**  
这类论文不一定炫，但很实用。自演化 Agent 如果没有 hygiene，很快就会把自己改坏。

**🔧 技术方案**  
- **模型架构**：围绕自演化循环设计最小工程规范。  
- **核心创新**：把 hygiene 作为 self-evolution 的核心条件。  
- **训练 / 推理策略**：工程流程与评测约束为主。

**📊 实验结果**  
论文展示 recipe 对演化稳定性的帮助。

**💡 为什么值得看**  
做自改、自学习 Agent 的团队可以拿来当检查清单。

</span>

---


### [6] Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents

- **评分**：7/10
- **作者/机构**：Tianshi Xu；Huifeng Wen；Meng Li
- **论文链接**：https://arxiv.org/abs/2605.22166
- **PDF**：https://arxiv.org/pdf/2605.22166
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文主张“适配接口而不是改模型”，通过 runtime harness adaptation 提高 LLM Agent 的确定性。

**☠️ 毒舌点评**  
这是很工程派的观点：很多不稳定来自接口契约和环境包装，而不一定要微调模型。新意不爆炸，但实用。

**🔧 技术方案**  
- **模型架构**：在运行时调整 harness、接口和约束，使 Agent 行为更确定。  
- **核心创新**：把可靠性问题下沉到接口适配层。  
- **训练 / 推理策略**：推理/运行时机制，不训练模型。

**📊 实验结果**  
展示 harness adaptation 对确定性和成功率的改善。

**💡 为什么值得看**  
做生产 Agent 时，接口层往往比模型层更可控。

</span>

---


### [7] PocketAgents: A Manifest-Driven Library of Autonomous Defense Agents

- **评分**：6/10
- **作者/机构**：Sidnei Barbieri；Ágney Lopes Roth Ferraz；Lourenço Alves Pereira Júnior
- **论文链接**：https://arxiv.org/abs/2605.21694
- **PDF**：https://arxiv.org/pdf/2605.21694
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
PocketAgents 是一个 manifest-driven 的自主防御 Agent 库。

**☠️ 毒舌点评**  
偏工具库/系统介绍，实用性可能高，研究新意有限。

**🔧 技术方案**  
- **模型架构**：用 manifest 描述防御 Agent 能力和调用方式。  
- **核心创新**：通过 manifest 组织可复用 defense agents。  
- **训练 / 推理策略**：系统库。

**📊 实验结果**  
展示防御任务中的 Agent 组合。

**💡 为什么值得看**  
安全运维 Agent 方向可以参考。

</span>

---


### [8] Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents

- **评分**：6/10
- **作者/机构**：Ting Liu
- **论文链接**：https://arxiv.org/abs/2605.22634
- **PDF**：https://arxiv.org/pdf/2605.22634
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Contractual Skills 提出 GovernSpec 设计框架，用契约化技能治理企业 AI Agent。

**☠️ 毒舌点评**  
偏框架/治理设计，工程落地感强于算法新意。适合企业 Agent，但不是普适研究强稿。

**🔧 技术方案**  
- **模型架构**：用契约描述技能边界、权限和验收。  
- **核心创新**：把 enterprise agent skills 纳入规格化治理。  
- **训练 / 推理策略**：设计框架。

**📊 实验结果**  
以案例和框架论证为主。

**💡 为什么值得看**  
企业 Agent 真要上线，技能契约比炫技更重要。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [9] Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents

- **评分**：8/10
- **作者/机构**：Sikuan Yan；Ahmed Bahloul；Ercong Nie；Susanna Schwarzmann；Riccardo Trivisonno；Volker Tresp；Yunpu Ma
- **论文链接**：https://arxiv.org/abs/2605.21768
- **PDF**：https://arxiv.org/pdf/2605.21768
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Memory-R2 处理长程记忆 Agent 的 RL 信用分配问题：记忆写入会改变后续环境，导致普通 group-relative 比较不公平。论文提出 LoGo-GRPO，用局部 rerollout 和全局轨迹奖励结合来训练记忆形成与演化。

**☠️ 毒舌点评**  
记忆 Agent 的瓶颈不是“加个向量库”这么轻松，而是写错、删错、过期信息都会污染未来。论文抓住了长程记忆训练里很容易被忽略的因果/信用问题，是偏训练方法的硬稿。

**🔧 技术方案**  
- **模型架构**：共享 LLM backbone 扮演 fact extractor 和 memory manager，通过角色提示形成记忆构建与维护模块。  
- **核心创新**：局部同状态 rerollout 比较不同记忆操作结果，缓解不同 rollout 记忆状态不一致带来的不公平奖励。  
- **训练 / 推理策略**：LoGo-GRPO 同时优化全局长程轨迹奖励和局部记忆操作奖励，并用 8/16/32 session 递增 curriculum 稳定训练。

**📊 实验结果**  
论文报告该训练框架能在多 session 记忆环境中更稳定地学习 memory formation 与 memory evolution。

**💡 为什么值得看**  
长程 Agent 迟早要面对持久记忆，Memory-R2 对“怎么训练会写记忆的 Agent”给了比 prompt 工程更正经的答案。

</span>

---


### [10] SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval

- **评分**：8/10
- **作者/机构**：Ningyuan Li；Haiyang Shen；Mugeng Liu；Yudong Han；Zhuofan Shi；Sixiong Xie；Yun Ma
- **论文链接**：https://arxiv.org/abs/2605.22219
- **PDF**：https://arxiv.org/pdf/2605.22219
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
SGR-Bench 评测 search agents 在 state-gated retrieval 场景下的能力：信息不是一次检索就能拿到，而是需要随着状态变化逐步解锁、判断和继续搜索。

**☠️ 毒舌点评**  
这比普通 RAG QA 更像真实研究任务：不是“搜一下回答”，而是要在状态约束下决定下一步搜什么。好的地方是任务设定贴近 Agent；风险是 benchmark 复杂后容易混入环境设计偏差。

**🔧 技术方案**  
- **模型架构**：构造带状态门控的信息检索任务，要求 Agent 在多步搜索中维护状态、识别解锁条件并完成回答。  
- **核心创新**：把 retrieval 从静态文档匹配推进到状态依赖的 search-agent 评测。  
- **训练 / 推理策略**：评测基准为主，不涉及训练。

**📊 实验结果**  
论文比较不同模型/agent 在 state-gated retrieval 下的成功率和搜索行为。

**💡 为什么值得看**  
对 RAG 读者来说，这篇提醒我们：Agentic RAG 的难点常常在搜索策略，而不是 embedding 模型本身。

</span>

---


### [11] SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents

- **评分**：7/10
- **作者/机构**：Mehrdad Saberi；Keivan Rezaei；Soheil Feizi
- **论文链接**：https://arxiv.org/abs/2605.21965
- **PDF**：https://arxiv.org/pdf/2605.21965
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
SpecHop 用连续 speculation 加速 multi-hop retrieval agents，让检索 Agent 提前展开可能路径。

**☠️ 毒舌点评**  
多跳检索的瓶颈是串行等待和路径不确定。speculation 是自然解法，关键是别把无效分支成本放大。

**🔧 技术方案**  
- **模型架构**：对多跳检索路径进行预测和提前执行。  
- **核心创新**：把 speculative execution 引入 retrieval-agent pipeline。  
- **训练 / 推理策略**：推理时加速策略。

**📊 实验结果**  
报告多跳检索任务的延迟/效果收益。

**💡 为什么值得看**  
对 Agentic RAG 系统优化有参考价值。

</span>

---


### [12] Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

- **评分**：7/10
- **作者/机构**：Mingkai Deng；Jinyu Hou；Lara Sá Neves；Varad Pimpalkhute；Taylor W. Killian；Zhengzhong Liu；Eric P. Xing
- **论文链接**：https://arxiv.org/abs/2605.22138
- **PDF**：https://arxiv.org/pdf/2605.22138
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文提出 self-regulated simulative planning，让 Agent 在推理中自我调节模拟规划的深度和成本。

**☠️ 毒舌点评**  
Agent planning 常见问题是要么想太少，要么无限思考。自调节规划预算是对的方向，但要看是否真的跨任务稳健。

**🔧 技术方案**  
- **模型架构**：在推理时生成模拟路径，并自适应控制规划。  
- **核心创新**：用 self-regulation 平衡规划质量和计算成本。  
- **训练 / 推理策略**：推理策略优化。

**📊 实验结果**  
报告在 agentic reasoning 任务中提升效率/表现。

**💡 为什么值得看**  
适合关注 test-time scaling 和规划预算的人。

</span>

---


### [13] IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents

- **评分**：7/10
- **作者/机构**：Daewon Choi；Kyunghyun Park；Woomin Song；Saket Dingliwal；Sai Muralidhar Jayanthi；Jinwoo Shin；Aram Galstyan
- **论文链接**：https://arxiv.org/abs/2605.22154
- **PDF**：https://arxiv.org/pdf/2605.22154
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
IdleSpec 利用 Agent 执行中的空闲时间做 speculative planning，提前准备可能的后续动作。

**☠️ 毒舌点评**  
思路工程味很足：很多 Agent 慢不是模型不会想，而是等待工具和环境时没有并行规划。问题是 speculation 错了会不会引入额外成本和错误。

**🔧 技术方案**  
- **模型架构**：在 agent loop 中识别 idle window，并生成候选后续计划。  
- **核心创新**：把空闲等待转化为计划预算。  
- **训练 / 推理策略**：推理时优化，不训练新模型。

**📊 实验结果**  
论文报告可降低端到端等待并改善部分任务效率。

**💡 为什么值得看**  
适合关注 Agent latency 和执行效率的人。

</span>

---


### [14] Planning in the LLM Era: Building for Reliability and Efficiency

- **评分**：6/10
- **作者/机构**：Michael Katz；Harsha Kokel；Kavitha Srinivas；Shirin Sohrabi
- **论文链接**：https://arxiv.org/abs/2605.21902
- **PDF**：https://arxiv.org/pdf/2605.21902
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Planning in the LLM Era 讨论 LLM 时代规划系统的可靠性和效率。

**☠️ 毒舌点评**  
偏综述/观点，适合补背景，不是今天最硬的实验论文。

**🔧 技术方案**  
- **模型架构**：梳理规划方法、LLM 接入方式和可靠性问题。  
- **核心创新**：把经典规划与 LLM 工作流放在同一可靠性框架下讨论。  
- **训练 / 推理策略**：无训练。

**📊 实验结果**  
以分析和设计建议为主。

**💡 为什么值得看**  
适合想把 LLM planning 做稳的人快速对齐问题空间。

</span>

---


### [15] ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning

- **评分**：6/10
- **作者/机构**：Yeqiu Chen；Ziyan Liu；Zhenxin Huang；Runquan Gui；Hong Wang；Lei Liu
- **论文链接**：https://arxiv.org/abs/2605.22106
- **PDF**：https://arxiv.org/pdf/2605.22106
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
ArborKV 面向树状 LLM reasoning 的结构感知 KV cache 管理。

**☠️ 毒舌点评**  
这不是 Agent 系统论文，但对树搜索、分支推理和 test-time scaling 有工程价值。

**🔧 技术方案**  
- **模型架构**：利用推理树结构管理 KV cache。  
- **核心创新**：让 KV 缓存复用匹配树状推理结构。  
- **训练 / 推理策略**：推理系统优化。

**📊 实验结果**  
报告缓存效率和推理扩展收益。

**💡 为什么值得看**  
如果你的 Agent 做树搜索规划，底层 KV 管理会影响成本。

</span>

---


### [16] Steins;Gate Drive: Semantic Safety Arbitration over Structured Futures for Latency-Decoupled LLM Planning

- **评分**：6/10
- **作者/机构**：Anjie Qiu；Hans D. Schotten
- **论文链接**：https://arxiv.org/abs/2605.22456
- **PDF**：https://arxiv.org/pdf/2605.22456
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Steins;Gate Drive 用 structured futures 做语义安全仲裁，面向低延迟 LLM planning。

**☠️ 毒舌点评**  
名字很酷，问题也有趣，但从摘要看更偏特定系统设定，通用性还需观察。

**🔧 技术方案**  
- **模型架构**：生成多个结构化未来并做安全仲裁。  
- **核心创新**：用 futures arbitration 分离规划延迟和安全判断。  
- **训练 / 推理策略**：推理时安全机制。

**📊 实验结果**  
展示在延迟受限规划中的安全收益。

**💡 为什么值得看**  
适合关注实时规划和安全仲裁的读者。

</span>

---


### [17] Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents

- **评分**：5/10
- **作者/机构**：Minghui Ma；Bin Guo；Runze Yang；Mengqi Chen；Yan Liu；Jingqi Liu；Yahan Pei；Xuehao Ma；Qiuyun Zhang；Zhiwen Yu
- **论文链接**：https://arxiv.org/abs/2605.22602
- **PDF**：https://arxiv.org/pdf/2605.22602
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文用双知识增强 ToM 推理提升 persuasive agents。

**☠️ 毒舌点评**  
ToM 和 persuasion 有研究价值，但和本号核心 Agent 系统/评测主线距离较远，低分收录。

**🔧 技术方案**  
- **模型架构**：结合两类知识增强说服场景下的 ToM 推理。  
- **核心创新**：面向 persuasive agents 的 ToM reasoning。  
- **训练 / 推理策略**：推理增强。

**📊 实验结果**  
报告说服任务上的效果。

**💡 为什么值得看**  
对社交/说服 Agent 感兴趣可看。

</span>

---

## 🤝 多智能体 / 协作


### [18] Self-Evolving Multi-Agent Systems via Decentralized Memory

- **评分**：7/10
- **作者/机构**：Guangya Hao；Yunbo Long；Zhuokai Zhao
- **论文链接**：https://arxiv.org/abs/2605.22721
- **PDF**：https://arxiv.org/pdf/2605.22721
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文研究通过去中心化记忆让多智能体系统自我演化，重点在不同 agent 如何保留、传播和利用经验。

**☠️ 毒舌点评**  
方向重要，但多智能体自演化很容易写成漂亮概念。入选全量是因为 memory + MAS 的组合值得关注，精选还要看实验是否足够硬。

**🔧 技术方案**  
- **模型架构**：多 agent 各自维护记忆并通过交互更新系统行为。  
- **核心创新**：用 decentralized memory 支撑系统级演化，而非单一中央记忆。  
- **训练 / 推理策略**：以系统机制和实验评测为主。

**📊 实验结果**  
展示自演化过程中的协作改进趋势。

**💡 为什么值得看**  
多智能体系统要长期运行，记忆组织方式会直接影响协作质量。

</span>

---


### [19] Cross-domain benchmarks reveal when coordinated AI agents improve scientific inference from partial evidence

- **评分**：6/10
- **作者/机构**：Fiona Y. Wong；Markus J. Buehler
- **论文链接**：https://arxiv.org/abs/2605.22300
- **PDF**：https://arxiv.org/pdf/2605.22300
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文用跨域科学任务评估协调式 AI agents 何时比简单 workflow 更有价值。

**☠️ 毒舌点评**  
MIT 科学 Agent 题材吸引人，但结论很克制：协调不是总赢，有时只是提升 provenance。这个克制反而是优点。

**🔧 技术方案**  
- **模型架构**：四类科学任务，设置冻结面板、基线、消融和 provenance 记录。  
- **核心创新**：明确区分性能提升、可解释/溯源提升和表征转换。  
- **训练 / 推理策略**：评测框架。

**📊 实验结果**  
部分分布式证据任务有收益，强 combined-summary baseline 下未必提升 top-line。

**💡 为什么值得看**  
对科学发现 Agent 的评估很有参考意义。

</span>

---


### [20] Claw AI Lab: An Autonomous Multi-Agent Research Team

- **评分**：6/10
- **作者/机构**：Fan Wu；Cheng Chen；Zhenshan Tan；Taiyu Zhang；Xinzhen Xu；Yanyu Qian；Dingcheng Gao；Lanyun Zhu；Qi Zhu；Yi Tan；Deyi Ji；Guosheng Lin；Tianrun Chen；Deheng Ye；Fayao Liu
- **论文链接**：https://arxiv.org/abs/2605.22662
- **PDF**：https://arxiv.org/pdf/2605.22662
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Claw AI Lab 描述一个自主多智能体研究团队。

**☠️ 毒舌点评**  
这类“AI Lab”系统很容易 demo 化，值得看架构和失败模式，不宜默认高分。

**🔧 技术方案**  
- **模型架构**：多 Agent 分工承担研究流程。  
- **核心创新**：把研究团队流程映射到自主 Agent 协作。  
- **训练 / 推理策略**：系统实现。

**📊 实验结果**  
展示端到端研究自动化案例。

**💡 为什么值得看**  
适合关注 AI researcher/多 Agent 组织形态的人。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [21] Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning

- **评分**：7/10
- **作者/机构**：Banghao Chi；Yining Xie；Mingyuan Wu；Jingcheng Yang；Jize Jiang；Zhaoheng Li；Shengyi Qian；Minjia Zhang；Klara Nahrstedt；Rui Hou；Xiangjun Fan；Hanchao Yu
- **论文链接**：https://arxiv.org/abs/2605.22642
- **PDF**：https://arxiv.org/pdf/2605.22642
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Spreadsheet-RL 用强化学习提升大语言模型 Agent 在真实电子表格任务上的能力。

**☠️ 毒舌点评**  
和 WorkstreamBench 互补：一个偏评测，一个偏训练。价值在于把 RL 放到更真实的办公任务，而不是玩具环境。

**🔧 技术方案**  
- **模型架构**：围绕 spreadsheet 操作构造 RL 环境和奖励。  
- **核心创新**：将 realistic spreadsheet tasks 纳入 Agent RL 训练。  
- **训练 / 推理策略**：用强化学习优化表格任务执行策略。

**📊 实验结果**  
论文报告 RL 后在表格任务上有提升。

**💡 为什么值得看**  
对办公 Agent 和企业自动化读者有直接参考。

</span>

---


### [22] ACC: Compiling Agent Trajectories for Long-Context Training

- **评分**：6/10
- **作者/机构**：Qisheng Su；Zhen Fang；Shiting Huang；Yu Zeng；Yiming Zhao；Kou Shi；Ziao Zhang；Lin Chen；Zehui Chen；Lijun Wu；Feng Zhao
- **论文链接**：https://arxiv.org/abs/2605.21850
- **PDF**：https://arxiv.org/pdf/2605.21850
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
ACC 将 Agent trajectories 编译成 long-context training 数据。

**☠️ 毒舌点评**  
方向合理，但目前更像数据/训练管线小步推进，影响力取决于是否能跨任务泛化。

**🔧 技术方案**  
- **模型架构**：把 agent 执行轨迹整理为长上下文训练样本。  
- **核心创新**：利用真实/生成轨迹增强长上下文 Agent 能力。  
- **训练 / 推理策略**：长上下文训练。

**📊 实验结果**  
报告训练后在相关任务上改进。

**💡 为什么值得看**  
适合关注 agent data flywheel 的读者。

</span>

---


### [23] Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts

- **评分**：6/10
- **作者/机构**：Andrii Kryshtal
- **论文链接**：https://arxiv.org/abs/2605.22720
- **PDF**：https://arxiv.org/pdf/2605.22720
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文讨论 LLM 在冲突语境部署中可能放大冲突的对齐失败。

**☠️ 毒舌点评**  
主题高风险但从技术 Agent 角度稍远。值得安全读者扫，但不放精选。

**🔧 技术方案**  
- **模型架构**：分析冲突场景下的模型行为和部署风险。  
- **核心创新**：把 alignment failure 放到现实冲突语境中考察。  
- **训练 / 推理策略**：评测/分析。

**📊 实验结果**  
展示特定冲突语境中的失败案例。

**💡 为什么值得看**  
提醒我们 Agent/LLM 部署风险不只在越狱，也在社会语境。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [24] Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

- **评分**：8/10
- **作者/机构**：Asaf Yehudai；Lilach Eden；Michal Shmueli-Scheuer
- **论文链接**：https://arxiv.org/abs/2605.22608
- **PDF**：https://arxiv.org/pdf/2605.22608
- **代码链接**：https://ibm.biz/ACLEAR-Code

<span style="font-size: 14px;">

**📌 简介**  
Agentic CLEAR 是 LLM Agent 的多层级自动评测框架，面向 system、trace、node 三个粒度生成行为诊断，目标是补足 observability 工具只记录日志、缺少可行动错误分析的问题。

**☠️ 毒舌点评**  
Agent 评测最缺的不是又一个总分，而是能告诉开发者“哪里坏、为什么坏、反复怎么坏”。这篇的价值在于把 trace-level 诊断产品化，缺点是 LLM-as-judge 诊断本身仍要防漂移。

**🔧 技术方案**  
- **模型架构**：位于现有 observability 层之上，读取执行 trace，生成节点级、轨迹级、系统级文本反馈，并提供 UI 做错误聚合和下钻。  
- **核心创新**：动态生成任务相关错误洞察，而不是依赖静态手写 taxonomy；同时覆盖多粒度诊断。  
- **训练 / 推理策略**：主要是评测框架和 LLM judge pipeline，不涉及训练新模型。

**📊 实验结果**  
在四个 benchmark、七类 agentic setting 和大量 LLM calls 上，与人工错误标注有较强一致性，并能预测任务成功率。

**💡 为什么值得看**  
做 Agent 平台的人会很需要这类工具：最终答案对了不代表过程安全，最终答案错了也需要知道系统性失败在哪。

</span>

---


### [25] Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety

- **评分**：8/10
- **作者/机构**：Piercosma Bisconti；Matteo Prandi；Federico Pierucci；Federico Sartore；Enrico Panai；Laura Caroli；Yue Zhu；Adam Leon Smith；Luca Nannini；Marcello Galisai；Susanna Cifani；Francesco Giarrusso；Marcantonio Bracale Syrnikov；Daniele Nardi
- **论文链接**：https://arxiv.org/abs/2605.22643
- **PDF**：https://arxiv.org/pdf/2605.22643
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Boiling the Frog 提出多轮 Agentic Safety benchmark，关注风险如何在连续交互中逐步升级，而不是单轮安全分类。

**☠️ 毒舌点评**  
安全评测如果只测单轮拒答，很容易漏掉“温水煮”式诱导。Agent 的危险也常在长期目标、工具调用和上下文迁移里慢慢长出来，这个设定很对。

**🔧 技术方案**  
- **模型架构**：构建多轮交互安全场景，考察模型/Agent 在渐进式诱导下是否保持边界。  
- **核心创新**：把 agentic safety 从单轮 prompt safety 扩展到多轮状态迁移和渐进风险。  
- **训练 / 推理策略**：基准评测，不训练模型。

**📊 实验结果**  
论文报告不同系统在多轮风险升级场景中的失败差异。

**💡 为什么值得看**  
做 Agent 安全不能只看一次回复，这篇适合用来校准多轮红队思路。

</span>

---


### [26] Autonomous LLM Agents & CTFs: A Second Look

- **评分**：7/10
- **作者/机构**：Youness Bouchari；Matteo Boffa；Marco Mellia；Idilio Drago；Thanh Minh Bui；Dario Rossi
- **论文链接**：https://arxiv.org/abs/2605.21497
- **PDF**：https://arxiv.org/pdf/2605.21497
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文重新审视 Autonomous LLM Agents 在 CTF 任务中的能力。

**☠️ 毒舌点评**  
CTF 很适合测试长程工具使用，但也容易被 benchmark-specific tricks 污染。这篇价值在于给安全 Agent 能力泼冷水或重新校准。

**🔧 技术方案**  
- **模型架构**：让 LLM Agent 在 CTF 环境中进行自主探索和解题。  
- **核心创新**：复查现有 CTF 结论，关注真实可复现能力。  
- **训练 / 推理策略**：评测为主。

**📊 实验结果**  
报告不同 Agent 在 CTF 上的表现与局限。

**💡 为什么值得看**  
安全 Agent 很热，但能力边界需要这种二次审视。

</span>

---


### [27] From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents

- **评分**：7/10
- **作者/机构**：Murong Ma；Tianyu Chen；Yun Lin；Shuai Lu；Qinglin Zhu；Yeyun Gong；Zhiyong Huang；Peng Cheng；Yan Lu；Jin Song Dong
- **论文链接**：https://arxiv.org/abs/2605.21996
- **PDF**：https://arxiv.org/pdf/2605.21996
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文从 patch-level 监督推进到 trajectory-level privileged process supervision，用于软件工程 Agent。

**☠️ 毒舌点评**  
只看最终 patch 容易奖励碰巧修好，trajectory supervision 更能约束过程。问题是 privileged signal 的成本和可获得性。

**🔧 技术方案**  
- **模型架构**：记录软件工程 Agent 的中间轨迹并进行过程监督。  
- **核心创新**：把监督粒度从补丁结果提升到执行轨迹。  
- **训练 / 推理策略**：训练/评测信号设计。

**📊 实验结果**  
展示过程监督对软件工程 Agent 的帮助。

**💡 为什么值得看**  
做 coding agent 的人会关心如何评价和训练“过程”。

</span>

---


### [28] Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems

- **评分**：7/10
- **作者/机构**：Aaditya Pai
- **论文链接**：https://arxiv.org/abs/2605.22001
- **PDF**：https://arxiv.org/pdf/2605.22001
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文研究 domain-camouflaged injection 如何绕过多 Agent LLM 系统的 guard。

**☠️ 毒舌点评**  
多 Agent 系统里安全边界会被角色和领域包装稀释，这篇关注的就是这种盲区。威胁模型值得看。

**🔧 技术方案**  
- **模型架构**：构造伪装成领域内容的注入攻击，测试 guard 检测能力。  
- **核心创新**：强调多 Agent 场景下 domain camouflage 对安全检测的破坏。  
- **训练 / 推理策略**：攻击评测为主。

**📊 实验结果**  
展示现有 guard 在伪装注入下的漏检。

**💡 为什么值得看**  
做工具调用和多 Agent 安全的人需要这类负面样本。

</span>

---


### [29] Benchmarking Autonomous Agents against Temporal, Spatial, and Semantic Evasions

- **评分**：7/10
- **作者/机构**：Jianan Ma；Xiaohu Du；Ruixiao Lin；Yaoxiang Bian；Jialuo Chen；Jingyi Wang；Xiaofang Yang；Shiwen Cui；Changhua Meng；Xinhao Deng；Zhen Wang
- **论文链接**：https://arxiv.org/abs/2605.22321
- **PDF**：https://arxiv.org/pdf/2605.22321
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文评测 Autonomous Agents 面对时间、空间和语义规避策略时的鲁棒性。

**☠️ 毒舌点评**  
Agent 在真实环境里会遇到会变形的任务和对抗性提示，evasion 评测比静态题库更接近现实。

**🔧 技术方案**  
- **模型架构**：构造 temporal/spatial/semantic evasion 场景测试 Agent。  
- **核心创新**：把规避维度系统化拆分到 Agent benchmark 中。  
- **训练 / 推理策略**：评测为主。

**📊 实验结果**  
报告不同 Agent 对三类规避的脆弱性。

**💡 为什么值得看**  
适合做可靠性和红队评测。

</span>

---


### [30] SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations

- **评分**：7/10
- **作者/机构**：Shuaiqi Wang；Aadyaa Maddi；Zinan Lin；Giulia Fanti
- **论文链接**：https://arxiv.org/abs/2605.22564
- **PDF**：https://arxiv.org/pdf/2605.22564
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
SynAE 评估用于 tool-calling Agent 评测的合成数据质量。

**☠️ 毒舌点评**  
Agent 评测越来越依赖合成任务，但合成数据烂了，排行榜就没有意义。这个问题朴素但重要。

**🔧 技术方案**  
- **模型架构**：构建评估框架衡量合成样本对 tool-calling evaluation 的质量。  
- **核心创新**：把 synthetic data quality 作为 Agent eval 的一等问题。  
- **训练 / 推理策略**：评测框架为主。

**📊 实验结果**  
展示不同合成数据对评测可靠性的影响。

**💡 为什么值得看**  
适合维护 Agent benchmark 或自动造题流水线的人。

</span>

---


### [31] Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard

- **评分**：7/10
- **作者/机构**：Sahar Abdelnabi；Chris Hicks；Konrad Rieck；Ahmad-Reza Sadeghi
- **论文链接**：https://arxiv.org/abs/2605.22568
- **PDF**：https://arxiv.org/pdf/2605.22568
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文讨论为什么 Agent 安全 benchmark 很难测准，强调不要被指标骗。

**☠️ 毒舌点评**  
这类 meta-benchmark 论文可能不提供新系统，但对当前 Agent 安全热潮很必要：测量本身经常是最薄弱的一环。

**🔧 技术方案**  
- **模型架构**：分析 Agent security benchmarking 的构造、泄漏、可重复性和指标问题。  
- **核心创新**：把 benchmark validity 放在安全评测中心。  
- **训练 / 推理策略**：方法论/分析为主。

**📊 实验结果**  
给出安全评测容易自欺的案例和建议。

**💡 为什么值得看**  
如果你引用安全榜单，这篇能帮你更谨慎。

</span>

---


### [32] LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

- **评分**：7/10
- **作者/机构**：Sadia Asif；Mohammad Mohammadi Amiri；Momin Abbas；Prasanna Sattigeri；Karthikeyan Natesan Ramamurthy
- **论文链接**：https://arxiv.org/abs/2605.22786
- **PDF**：https://arxiv.org/pdf/2605.22786
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
LCGuard 关注多 Agent 共享 KV/cache 时潜在通信带来的安全问题，试图给共享机制加防护。

**☠️ 毒舌点评**  
KV 共享能省成本也能泄漏信息，这个问题会随着多 Agent 系统工程化变得更现实。论文偏机制安全，受众稍窄。

**🔧 技术方案**  
- **模型架构**：在多 Agent KV sharing 通道上加入 latent communication guard。  
- **核心创新**：把安全边界推进到缓存/隐式通信层。  
- **训练 / 推理策略**：系统机制与评测为主。

**📊 实验结果**  
展示 guard 对不安全潜在通信的抑制效果。

**💡 为什么值得看**  
未来 Agent 系统会共享越来越多中间状态，安全不只在最终文本。

</span>

---


### [33] Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs

- **评分**：6/10
- **作者/机构**：Dylan Feng；Pragya Srivastava；Cassidy Laidlaw
- **论文链接**：https://arxiv.org/abs/2605.21602
- **PDF**：https://arxiv.org/pdf/2605.21602
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文评测并改进 LLM OOD alignment failure monitors。

**☠️ 毒舌点评**  
不是 Agent 专项，但 alignment monitor 对高自治 Agent 很关键。放全量，供安全读者参考。

**🔧 技术方案**  
- **模型架构**：构建 OOD alignment failure 监控评测。  
- **核心创新**：关注分布外对齐失败检测。  
- **训练 / 推理策略**：评测和监控方法。

**📊 实验结果**  
报告 monitor 改进效果。

**💡 为什么值得看**  
Agent 权限越高，越需要提前发现对齐失效。

</span>

---

## 🧪 应用 / Benchmark


### [34] TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks

- **评分**：8/10
- **作者/机构**：Zhaoyang Chu；Jiarui Hu；Xingyu Jiang；Pengyu Zou；Han Li；Chao Peng；Peter O'Hearn；Earl T. Barr；Mark Harman；Federica Sarro；He Ye
- **论文链接**：https://arxiv.org/abs/2605.22535
- **PDF**：https://arxiv.org/pdf/2605.22535
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
TerminalWorld 面向真实终端任务评测 Agent，不再只看浏览器或代码补丁，而是把命令行环境里的多步操作、文件状态和工具调用纳入 benchmark。

**☠️ 毒舌点评**  
终端是 coding/research Agent 真正高频的工作界面，这类 benchmark 比“网页点按钮”更接近工程现实。关键要看任务覆盖、沙箱隔离和评分是否足够抗投机。

**🔧 技术方案**  
- **模型架构**：构建终端环境任务集，要求 Agent 在 shell、文件系统和工具输出之间连续决策。  
- **核心创新**：把真实 CLI 工作流系统化评测，补足现有 web/coding benchmark 的界面盲区。  
- **训练 / 推理策略**：评测基准为主，不训练模型。

**📊 实验结果**  
论文给出多模型/多 agent 在真实终端任务上的表现差异和失败模式。

**💡 为什么值得看**  
任何想做工程 Agent 的团队都该看终端任务，因为大量真实工作根本不发生在漂亮 UI 里。

</span>

---


### [35] WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

- **评分**：7/10
- **作者/机构**：Thomson Yen；Julian Poeltl；Harshith Srinivas Gear；Yilin Meng；Joshua Fan；Adam Shen；Yili Liu；Ali Bauyrzhan；Siri Du；Haoyang Liu；Daniel Guetta；Hongseok Namkoong
- **论文链接**：https://arxiv.org/abs/2605.22664
- **PDF**：https://arxiv.org/pdf/2605.22664
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
WorkstreamBench 评测 LLM Agent 在金融电子表格端到端任务中的表现。

**☠️ 毒舌点评**  
电子表格是企业 Agent 的真实战场，比聊天 QA 难得多。应用域偏金融，但任务形态有普适性。

**🔧 技术方案**  
- **模型架构**：构建 spreadsheet workstream，从理解、编辑到校验完整链路。  
- **核心创新**：把 Agent 评测从单步表格问答推进到端到端工作流。  
- **训练 / 推理策略**：基准评测。

**📊 实验结果**  
报告主流 Agent 在电子表格工作流上的能力缺口。

**💡 为什么值得看**  
企业 Agent 落地绕不开表格，这篇有现实参考价值。

</span>

---


### [36] Evaluating Large Language Models as Live Strategic Agents: Provider Performance, Hybrid Decomposition, and Operational Gaps in Timed Risk Play

- **评分**：5/10
- **作者/机构**：H. C. Ekne
- **论文链接**：https://arxiv.org/abs/2605.22238
- **PDF**：https://arxiv.org/pdf/2605.22238
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文把大语言模型当作实时战略 Agent，在 timed Risk play 中比较 provider 表现和混合分解策略。

**☠️ 毒舌点评**  
有趣但偏游戏/战略应用，和通用 Agent 工程联系有限。低分保留为边缘参考。

**🔧 技术方案**  
- **模型架构**：构建 timed Risk play 环境测试 LLM strategic agents。  
- **核心创新**：分析 provider performance 和 decomposition gap。  
- **训练 / 推理策略**：评测为主。

**📊 实验结果**  
报告不同 provider 的策略表现差异。

**💡 为什么值得看**  
适合关注博弈型 Agent 的读者。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
