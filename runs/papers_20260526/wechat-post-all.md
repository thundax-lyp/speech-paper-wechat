---
title: "Agent/LLM论文速递｜2026-05-26｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-26｜全量版：本期收录 21 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-26｜全量版：本期收录 21 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-26"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-26｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **21** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**6** 篇
- LLM 推理 / 规划 / RAG：**4** 篇
- 评测 / 安全 / 对齐：**6** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks | ⭐ 8/10 | deep research agent, synthetic tasks, open models, RL |
| Agent系统与工具使用 | 2 | VeriTrace: Evolving Mental Models for Deep Research Agents | ⭐ 8/10 | deep research agent, mental model, cognitive graph, feedback loops |
| Agent系统与工具使用 | 3 | Toward Reliable Design of LLM-Enabled Agentic Workflows: Optimizing Latency-Reliability-Cost Tradeoffs | ⭐ 7/10 | agentic workflow, latency, reliability, cost |
| Agent系统与工具使用 | 4 | How Many Tools Should an LLM Agent See? A Chance-Corrected Answer | ⭐ 7/10 | tool retrieval, shortlist depth, Bits-over-Random, RL |
| Agent系统与工具使用 | 5 | Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams | ⭐ 6/10 | tool-call dependency, mechanistic analysis, residual stream, linear probe |
| Agent系统与工具使用 | 6 | Neural Router: Semantic Content Matching for Agentic AI | ⭐ 6/10 | semantic routing, pub/sub, edge-cloud, LLM matching |
| RAG与知识检索 | 1 | Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG | ⭐ 8/10 | agentic RAG, continual correction, factual nugget, production |
| RAG与知识检索 | 2 | Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search through Reinforcement Learning | ⭐ 7/10 | legal search, temporal consistency, RL, RAG |
| RAG与知识检索 | 3 | Spectral Retrieval: Multi-Scale Sinc Convolution over Token Embeddings for Localized Retrieval in LLM Multi-Agent Systems | ⭐ 6/10 | localized retrieval, multi-agent RAG, token embeddings, sinc convolution |
| RAG与知识检索 | 4 | Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki | ⭐ 6/10 | agent-native retrieval, LLM-Wiki, reasoning, RAG |
| 多智能体与协作 | 1 | A Multi-Agent LLM Framework for Rating the Quality of Surgical Feedback | ⭐ 6/10 | multi-agent LLM, surgical feedback, rubric rating, application |
| LLM训练与对齐 | 1 | A Sober Look at Agentic Misalignment in Automated Workflows | ⭐ 7/10 | agentic misalignment, multi-agent, evidence attribution, oversight |
| 评测与安全 | 1 | Stop Comparing LLM Agents Without Disclosing the Harness | ⭐ 7/10 | agent harness, evaluation, variance attribution, position paper |
| 评测与安全 | 2 | When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents | ⭐ 7/10 | MCP poisoning, tool security, LLM agents, benchmark |
| 评测与安全 | 3 | Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows | ⭐ 7/10 | trajectory hallucination, multi-agent workflow, industrial, audit |
| 评测与安全 | 4 | Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS | ⭐ 7/10 | tool attacks, LLM-MAS, memory, RL attacker |
| 评测与安全 | 5 | Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security | ⭐ 6/10 | trustworthy agentic AI, survey, security, evaluation |
| 应用与基准 | 1 | Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World | ⭐ 8/10 | personal assistant, long-horizon context, GUI+CLI, benchmark |
| 应用与基准 | 2 | MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research | ⭐ 8/10 | mobile GUI agent, simulation, online RL, benchmark |
| 应用与基准 | 3 | GroupTravelBench: Benchmarking LLM Agents on Multi-Person Travel Planning | ⭐ 6/10 | travel planning, LLM agents, multi-person, benchmark |
| 应用与基准 | 4 | PolyGnosis 2.0: Enhancing LLM Reasoning via Agentic Harness Engineering for Polymarket and OSINT Insight Extraction | ⭐ 6/10 | financial agents, OSINT, reflection, tool calling |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks

- **评分**：8/10
- **作者/机构**：作者：Jian Xie、Tianhe Lin、Zilu Wang、Yuting Ning、Yuekun Yao、Tianci Xue、Zhehao Zhang、Zhongyang Li、Kai Zhang、Yufan Wu、Shijie Chen、Boyu Gou
- **论文链接**：https://arxiv.org/abs/2605.24218
- **PDF**：https://arxiv.org/pdf/2605.24218
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
QUEST 发布一族开放 deep research agent 模型，目标覆盖长程搜索、事实查找、引用 grounding 和报告合成。

**☠️ 毒舌点评**  
这是大工程路线：合成任务、中训练、SFT、RL 串起来训练研究型 agent。亮点是开放模型和任务流水线；风险是论文 PDF 很长，细节多，真正复现成本不会低。

**🔧 技术方案**  
- **模型架构**：2B 到 35B 的开放 deep research agent 家族，围绕搜索、证据引用和报告写作能力设计。  
- **核心创新**：用统一合成任务流水线支撑多阶段训练，试图补上 proprietary deep research agent 不可复现的问题。  
- **训练 / 推理策略**：组合 mid-training、SFT 和 reinforcement learning，围绕 session-level 搜索与报告任务优化。

**📊 实验结果**  
论文主张 QUEST 在多类 long-horizon search 任务上具备较强泛化，并释放 demo、数据、权重和代码入口。

**💡 为什么值得看**  
适合关注 open deep research agent 和 agent 训练 recipe 的读者重点追踪。

</span>

---


### [2] VeriTrace: Evolving Mental Models for Deep Research Agents

- **评分**：8/10
- **作者/机构**：作者：Haolang Zhao、Yunbo Long、Lukas Beckenbauer、Alexandra Brintrup
- **论文链接**：https://arxiv.org/abs/2605.26081
- **PDF**：https://arxiv.org/pdf/2605.26081
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
VeriTrace 为深度研究 agent 加了显式“心智模型”层，用解释更新、偏差反馈和 schema 修订三类循环来约束研究过程。

**☠️ 毒舌点评**  
相比“让 LLM 自己反思”，这篇更像把反思变成可维护的数据结构。实验说小 backbone 也能追上更强 baseline，这是亮点；但 cognitive graph 的构造成本和泛化仍要继续看。

**🔧 技术方案**  
- **模型架构**：以认知图维护中间表示，把任务理解、证据依赖和 schema 变化显式化。  
- **核心创新**：把 deep research 的中间状态从隐式 chain-of-thought 转成可调控、可反馈修订的 cognitive graph。  
- **训练 / 推理策略**：在研究循环中持续做 interpretive update、deviation feedback、schema revision，用反馈而非单纯扩大上下文来修正模型。

**📊 实验结果**  
在 DeepResearch Bench 上，相同 Qwen3.5-27B backbone 下较最强 matched baseline 提升 4.22pp Insight，并报告 ablation 支持三类 loop 的作用。

**💡 为什么值得看**  
适合做 deep research agent、长程信息综合和 agent memory 的人看。

</span>

---


### [3] Toward Reliable Design of LLM-Enabled Agentic Workflows: Optimizing Latency-Reliability-Cost Tradeoffs

- **评分**：7/10
- **作者/机构**：作者：Ya-Ting Yang、Quanyan Zhu
- **论文链接**：https://arxiv.org/abs/2605.23929
- **PDF**：https://arxiv.org/pdf/2605.23929
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇从可靠性、延迟和成本三者权衡出发，为 LLM-enabled agentic workflow 建模，并推导 token/resource allocation 策略。

**☠️ 毒舌点评**  
它不是酷炫 demo，而是偏系统优化的基础工作。优点是问题真实，缺点是模型假设会限制直接落地。

**🔧 技术方案**  
- **模型架构**：将 workflow 表示成 agent 节点和信息流边组成的有向计算图，分别建模 LLM 与非 LLM agent。  
- **核心创新**：把 agent workflow 设计从经验调参转为 latency-reliability-cost constrained optimization。  
- **训练 / 推理策略**：推导顺序 workflow 下的闭式最优 token allocation，类似 water-filling 的边际收益均衡。

**📊 实验结果**  
理论分析给出在约束下最大化可靠性的唯一最优分配规则，并讨论 shadow price。

**💡 为什么值得看**  
适合关心 agent 系统成本、SLA 和编排优化的人。

</span>

---


### [4] How Many Tools Should an LLM Agent See? A Chance-Corrected Answer

- **评分**：7/10
- **作者/机构**：作者：Vyzantinos Repantis、Ameya Gawde、Harshvardhan Singh、Joey Blackwell II
- **论文链接**：https://arxiv.org/abs/2605.24660
- **PDF**：https://arxiv.org/pdf/2605.24660
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇问了一个很具体但常被忽略的问题：LLM agent 到底该看到多少个候选工具？作者用 chance-corrected 的 BoR 指标评价工具 shortlist 深度。

**☠️ 毒舌点评**  
问题小但实用，尤其适合工具注册表越来越大的 agent 系统。贡献更像 evaluation metric 和 probing policy，不是完整 agent 方案，所以分数克制。

**🔧 技术方案**  
- **模型架构**：将工具选择看成 retrieval depth 决策，在 BFCL、ToolBench、MetaTool 等 registry 上比较固定 K、F1 baseline 和 BoR reward。  
- **核心创新**：用 Bits-over-Random 抵消“工具越多随机命中越高”的假象，把 shortlist 长度本身变成可评价对象。  
- **训练 / 推理策略**：训练一个简单 RL policy 按 query 选择候选工具数，主要用于检验 BoR 奖励。

**📊 实验结果**  
在多种 scorer 和 registry 下，BoR policy 往往用更低平均深度达到接近固定 K 的 found rate；不同 scorer 会自然学出不同 K。

**💡 为什么值得看**  
如果你的 agent 平台在做 tool routing，这篇能帮你少一点拍脑袋调 K。

</span>

---


### [5] Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams

- **评分**：6/10
- **作者/机构**：作者：Tianda Sun、Dimitar Kazakov
- **论文链接**：https://arxiv.org/abs/2605.25310
- **PDF**：https://arxiv.org/pdf/2605.25310
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇问 LLM agent 的 residual stream 中是否线性编码了 tool-call dependency structure。

**☠️ 毒舌点评**  
很有机制解释味道，问题细而尖。它对实用 agent 平台的直接影响有限，但能帮助理解工具调用能力如何在模型内部呈现。

**🔧 技术方案**  
- **模型架构**：对执行工具调用任务的 LLM hidden states / residual streams 做线性解码。  
- **核心创新**：把工具依赖结构作为可探测表征，而不是只看最终调用成功率。  
- **训练 / 推理策略**：训练线性 probe 检测 tool-call dependency 信息。

**📊 实验结果**  
论文报告依赖结构可被线性解码，说明模型内部存在可读的工具规划信号。

**💡 为什么值得看**  
适合关注 mechanistic interpretability 和 tool-use representation 的读者。

</span>

---


### [6] Neural Router: Semantic Content Matching for Agentic AI

- **评分**：6/10
- **作者/机构**：作者：Lauri Lovén、Abhishek Kumar、Alexander Engelhardt、Alaa Saleh、Roberto Morabito、Xiaoli Liu、Naser Hossein Motlagh、Sasu Tarkoma
- **论文链接**：https://arxiv.org/abs/2605.25701
- **PDF**：https://arxiv.org/pdf/2605.25701
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Neural Router 把 LLM 用作 agentic AI 的语义内容匹配引擎，用在 edge-cloud 之间的 publish/subscribe 路由。

**☠️ 毒舌点评**  
它更偏分布式系统和语义路由，agent 味道没有前几篇浓，但对多 agent 消息分发、事件过滤有参考价值。

**🔧 技术方案**  
- **模型架构**：内容型 pub/sub broker，用 LLM 做多标签语义匹配，处理社媒、法律和智能家居传感数据。  
- **核心创新**：提出两处 crossover cost model，分析什么时候该压缩、合并或直接让长上下文模型处理候选。  
- **训练 / 推理策略**：离线 multi-label retrieval 设置，比较六个 LLM 与七个 baseline。

**📊 实验结果**  
实验显示后端模型选择常比 pipeline 配置更关键；在小上下文或长候选集场景，压缩策略才更有价值。

**💡 为什么值得看**  
适合做边缘 agent、事件路由和 agent 通信基础设施的人扫读。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [7] Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG

- **评分**：8/10
- **作者/机构**：作者：Moshe Hazoom、Gal Patel、Alon Talmor、Tom Hope
- **论文链接**：https://arxiv.org/abs/2605.25641
- **PDF**：https://arxiv.org/pdf/2605.25641
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
INO 把用户的事实纠错转成可检索 factual nuggets，并用生产 RAG agent 自己作为测试 harness 迭代改写，直到新知识能被找回。

**☠️ 毒舌点评**  
这是今天最接地气的 RAG 论文之一：问题来自 B2B 生产系统，评价也围绕 discoverability 和 usefulness。它不像新架构炫技，但对真实知识库维护很有启发。

**🔧 技术方案**  
- **模型架构**：在索引阶段生成 factual nugget，再用触发 query 与改写 query 调用原 RAG 流水线，分析失败轨迹并修订 nugget。  
- **核心创新**：把“用户纠错如何进入知识库”定义成 agentic RAG 的闭环优化问题，而不是简单追加 FAQ。  
- **训练 / 推理策略**：不改生产 agent 配置；使用检索-回答-反思-修订循环优化 nugget 表达。

**📊 实验结果**  
在两个生产 B2B agent、七个客户部署上，INO 在 support ticket 评测中达到约 78.2% discoverability / 70.4% usefulness，明显高于直接写入和 synthetic anchor baseline。

**💡 为什么值得看**  
对企业 RAG、客服知识库和持续学习系统很有参考价值。

</span>

---


### [8] Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search through Reinforcement Learning

- **评分**：7/10
- **作者/机构**：作者：Wei Fan、Yining Zhou、Mufan Zhang、Yanbing Weng、Yiran HU、Tianshi Zheng、Baixuan Xu、Chunyang Li、Jianhui Yang、Haoran Li、Yangqiu Song
- **论文链接**：https://arxiv.org/abs/2605.25920
- **PDF**：https://arxiv.org/pdf/2605.25920
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
LegalSearch-R1 解决法律 agentic search 的时间一致性问题：搜索到的法律条文必须匹配案件发生时点。

**☠️ 毒舌点评**  
问题定义很漂亮，尤其是法律场景里“最新信息”反而可能是错的。领域专用性较强，但对 temporal RAG 很有推广意义。

**🔧 技术方案**  
- **模型架构**：结合本地 statute RAG、web/search agent 和时间约束推理，避免把后续修法错误套到旧案。  
- **核心创新**：把 temporal consistency 明确作为 legal agentic search 的优化目标。  
- **训练 / 推理策略**：使用端到端强化学习训练搜索/推理策略，使 query 和证据选择包含时间条件。

**📊 实验结果**  
论文展示普通搜索 agent 会受训练截止或当前网页偏置影响，LegalSearch-R1 能更好匹配适用法版本。

**💡 为什么值得看**  
对法律 RAG、时序知识库和可审计检索很值得看。

</span>

---


### [9] Spectral Retrieval: Multi-Scale Sinc Convolution over Token Embeddings for Localized Retrieval in LLM Multi-Agent Systems

- **评分**：6/10
- **作者/机构**：作者：Andrea Morandi
- **论文链接**：https://arxiv.org/abs/2605.24764
- **PDF**：https://arxiv.org/pdf/2605.24764
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Spectral Retrieval 针对多 Agent RAG 中的局部相关片段检索，用多尺度 sinc convolution 处理 token embeddings。

**☠️ 毒舌点评**  
方法有信号处理味道，切中了 mean pooling 会稀释局部证据的问题。但论文规模较小，更像一个 retrieval primitive。

**🔧 技术方案**  
- **模型架构**：在 token embedding 序列上做多尺度卷积，保留局部 relevance spike。  
- **核心创新**：用频谱/多尺度滤波替代单向量 mean pooling，改善短 span 相关性的召回。  
- **训练 / 推理策略**：主要是检索阶段算法，不涉及 agent 训练。

**📊 实验结果**  
合成实验中 mean-pool 在单点相关场景接近随机，谱检索能恢复局部信号；并在 LIMIT-small 上做真实 encoder 测试。

**💡 为什么值得看**  
如果你的 multi-agent 系统依赖堆叠检索，这篇提醒你底层 retrieval ceiling 很关键。

</span>

---


### [10] Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki

- **评分**：6/10
- **作者/机构**：作者：Haoliang Ming、Feifei Li、Xiaoqing Wu、Wenhui Que
- **论文链接**：https://arxiv.org/abs/2605.25480
- **PDF**：https://arxiv.org/pdf/2605.25480
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
LLM-Wiki 主张 retrieval 应该像 reasoning：搜索、阅读、跳转、判断证据是否足够，而不是一次性取 chunk。

**☠️ 毒舌点评**  
方向对，但从当前文本看更像概念型 agent-native retrieval 框架，评测强度不如 INO。可作为 RAG 组织形式的想法来源。

**🔧 技术方案**  
- **模型架构**：把知识组织成更适合 agent traversal 的页面/链接结构，而不是平铺 chunk。  
- **核心创新**：将 retrieval-as-lookup 改写成 retrieval-as-reasoning，强调知识暴露方式本身影响 agent 能力。  
- **训练 / 推理策略**：让 agent 在 ReAct 式循环中沿显式指针搜索、阅读和组合证据。

**📊 实验结果**  
论文用多跳电影/人物类例子说明平铺 RAG 的局限，并提出自演化知识组织。

**💡 为什么值得看**  
适合关注结构化知识库、agentic RAG 和检索界面设计的人。

</span>

---

## 🤝 多智能体 / 协作


### [11] A Multi-Agent LLM Framework for Rating the Quality of Surgical Feedback

- **评分**：6/10
- **作者/机构**：作者：Rafal Kocielnik、J. Everett Knudsen、Steven Y. Cen、Jasmine Lin、Cherine H. Yang、Atharva Deo、Ujjwal Pasupulety、Peter Wager、Anima Anandkumar、Andrew J. Hung
- **论文链接**：https://arxiv.org/abs/2605.25440
- **PDF**：https://arxiv.org/pdf/2605.25440
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇用多 Agent LLM 框架评估外科反馈质量，是医疗教育里的 LLM 应用。

**☠️ 毒舌点评**  
应用价值明确，但方法创新主要在工作流组合和专家 rubric 映射，Agent/LLM 主线贡献相对窄。

**🔧 技术方案**  
- **模型架构**：多个 LLM agent 分别从不同评价维度审阅 surgical feedback，再汇总为质量评分。  
- **核心创新**：把复杂主观反馈评价拆给多角色 agent，降低单模型评分偏差。  
- **训练 / 推理策略**：通过 rubric-guided prompting 和 agent aggregation 完成推理。

**📊 实验结果**  
论文报告多 agent 评分与人工标准更一致，能辅助反馈质量控制。

**💡 为什么值得看**  
医疗教育读者可看；通用 agent 系统读者扫读即可。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [12] A Sober Look at Agentic Misalignment in Automated Workflows

- **评分**：7/10
- **作者/机构**：作者：Wenqian Ye、Bo Yuan、Zhichao Xu、Yijun Tian、Yawei Wang、Henry Kautz、Aidong Zhang
- **论文链接**：https://arxiv.org/abs/2605.24197
- **PDF**：https://arxiv.org/pdf/2605.24197
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇把自动化工作流里的 agentic misalignment 形式化为 agent 后验坍缩到通用 proxy utility 的问题，并提出 Agentic Evidence Attribution。

**☠️ 毒舌点评**  
优点是把“多 agent 会跑偏”讲成了更可分析的证据归因问题。缺点是概念和形式化偏重，落到复杂真实系统还需要更多外部验证。

**🔧 技术方案**  
- **模型架构**：在 Bayesian 框架下描述 multi-agent workflow 中 latent role 和 proxy utility 的错配。  
- **核心创新**：提出 AEA，用结构化、角色相关证据修正 agent 行为，而不是只靠更多 test-time scaling。  
- **训练 / 推理策略**：比较 self-reflection 和 weak-to-strong generalization 两类证据来源，用小 evidence model 为强 agent 提供纠偏信号。

**📊 实验结果**  
实验显示 evidence-conditioned alignment 能提升多智能体工作流可靠性，且小模型证据信号能带来有效监督。

**💡 为什么值得看**  
对做 agent 安全、workflow oversight 和 scalable supervision 的读者有启发。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [13] Stop Comparing LLM Agents Without Disclosing the Harness

- **评分**：7/10
- **作者/机构**：作者：Yunbei Zhang、Janet Wang、Yingqiang Ge、Weijie Xu、Jihun Hamm、Chandan K. Reddy
- **论文链接**：https://arxiv.org/abs/2605.23950
- **PDF**：https://arxiv.org/pdf/2605.23950
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇 position paper 直说：长程 agent 评测里，harness 配置往往比底层模型更决定结果。

**☠️ 毒舌点评**  
观点很对，也很适合社区降温。证据包含形式化和案例，但毕竟不是大规模新 benchmark；价值在于提醒评测报告必须披露 harness。

**🔧 技术方案**  
- **模型架构**：把 agent harness 视作闭环系统控制器，包含上下文构造、工具交互、编排和验证。  
- **核心创新**：提出 Binding Constraint Thesis：同级前沿模型比较中，性能方差常由 harness 主导。  
- **训练 / 推理策略**：用控制论形式化、文献/部署案例和方差分解论证 attribution 问题。

**📊 实验结果**  
论文指出 harness-induced variance 可超过 model-induced variance，导致跨论文模型比较和复现都不可靠。

**💡 为什么值得看**  
适合写 agent benchmark、做模型排行榜或复现实验前先读。

</span>

---


### [14] When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents

- **评分**：7/10
- **作者/机构**：作者：Shi Liu、Xuehai Tang、Xikang Yang、Liang Lin、Biyu Zhou、Wenjie Xiao、Wantao Liu
- **论文链接**：https://arxiv.org/abs/2605.24069
- **PDF**：https://arxiv.org/pdf/2605.24069
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
论文关注 MCP 等工具协议下的“说明书投毒”：工具文档或 manual 被操纵后，agent 的规划层会被误导。

**☠️ 毒舌点评**  
题目非常贴近当下 agent 基础设施安全。贡献主要是 realistic benchmark 和攻击面梳理；防御方案如果能更系统会更强。

**🔧 技术方案**  
- **模型架构**：围绕 MCP 工具调用流程建模攻击，从用户请求、工具描述、规划选择到执行链路分析风险。  
- **核心创新**：把攻击目标放在 agent 的 cognitive planning layer，而不是传统输入 prompt 注入。  
- **训练 / 推理策略**：构造 benchmark 评估被污染 tool manual 对 LLM agent 工具选择与执行的影响。

**📊 实验结果**  
论文系统展示 manual poisoning 可诱导错误工具选择和危险执行，强调协议互操作带来的隐蔽攻击面。

**💡 为什么值得看**  
MCP 生态正在变热，这篇适合所有做 tool-use agent 的人做安全清单。

</span>

---


### [15] Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows

- **评分**：7/10
- **作者/机构**：作者：Harshada Badave、Santosh Borse、Andrea Gomez、Harshitha Narahari、Sara Carter、Vishwa Bhatt、Aishani Rachakonda、Shuxin Lin、Dhaval Patel
- **论文链接**：https://arxiv.org/abs/2605.24219
- **PDF**：https://arxiv.org/pdf/2605.24219
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Trajel 关注多 Agent 工业流程中的轨迹级 hallucination，而不是只评最终答案。

**☠️ 毒舌点评**  
这是很实用的评测视角：很多 agent 失败藏在 Thought-Action-Observation 轨迹中。数据来自工业 workflow 是加分项，但检测模型仍会混淆细粒度类型。

**🔧 技术方案**  
- **模型架构**：基于 AssetOpsBench 的专家标注 agent traces，定义 factual、referential、logical、procedural、scope 五类幻觉。  
- **核心创新**：把 hallucination 审计从 final answer 拉到 trajectory/subtask/long-context 层。  
- **训练 / 推理策略**：比较 subtask classifier、trajectory-level NLI 和 Longformer long-context modeling。

**📊 实验结果**  
结果显示近半 hallucinated trajectories 涉及多类型错误，trajectory-aware detection 优于 post-hoc verification。

**💡 为什么值得看**  
做 agent 可靠性、日志审计和工业部署的人值得看。

</span>

---


### [16] Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS

- **评分**：7/10
- **作者/机构**：作者：Bingyu Yan、Xiaoming Zhang、Jinyu Hou、Chaozhuo Li、Ziyi Zhou、Yiming Hei、Litian Zhang
- **论文链接**：https://arxiv.org/abs/2605.25389
- **PDF**：https://arxiv.org/pdf/2605.25389
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Evo-Attacker 研究多智能体 LLM 系统中的长程工具攻击，用 memory-augmented RL 学习攻击策略。

**☠️ 毒舌点评**  
agent 安全方向的题目扎实，尤其贴近工具调用和长程交互。需要重点看威胁模型是否覆盖真实部署。

**🔧 技术方案**  
- **模型架构**：攻击者在 LLM-MAS 中跨多轮观察、记忆状态并选择工具攻击动作。  
- **核心创新**：把工具攻击从单轮 prompt exploit 扩展到长程、多 agent、带记忆的 RL 攻击。  
- **训练 / 推理策略**：使用强化学习优化攻击策略，并引入 memory 处理长期依赖。

**📊 实验结果**  
论文声称相比静态或短程攻击，Evo-Attacker 在长 horizon 工具攻击上更有效。

**💡 为什么值得看**  
适合做 agent security、red teaming 和 tool-use 防御的人。

</span>

---


### [17] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security

- **评分**：6/10
- **作者/机构**：作者：Jinhu Qi、Muzhi Li、Jiahong Liu、Yuqin Shu、Dianzhi Yu、Shicheng Ma、Wenqian Cui、Yiyang Zhao、Yiyi Chen、Ruoxi Jiang、Irwin King、Zenglin Xu
- **论文链接**：https://arxiv.org/abs/2605.23989
- **PDF**：https://arxiv.org/pdf/2605.23989
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这是一篇可信 agentic AI 综述，围绕安全鲁棒、隐私和系统安全整理风险、缓解策略和评测指标。

**☠️ 毒舌点评**  
综述的价值在于把风险映射到 Perceive-Plan-Act-Reflect-Learn 工作流。新意有限，但适合做资料入口。

**🔧 技术方案**  
- **模型架构**：以 agent workflow 为主线组织风险与防御，不强行限定具体 agent 架构。  
- **核心创新**：提供 metrics-and-benchmarks hub，并给出场景到 release-gating 指标的映射。  
- **训练 / 推理策略**：综述论文，无训练策略。

**📊 实验结果**  
覆盖 safety/robustness、privacy/system security、评价信号和发布门禁等主题。

**💡 为什么值得看**  
适合做 agent 安全综述、风险清单和项目立项背景材料。

</span>

---

## 🧪 应用 / Benchmark


### [18] Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World

- **评分**：8/10
- **作者/机构**：作者：Yusong Lin、Xinyuan Liang、Haiyang Wang、Qipeng Gu、Siqi Cheng、Jiangui Chen、Shuzhe Wu、Feiyang Pan、Lue Fan、Sanyuan Zhao、Dandan Tu
- **论文链接**：https://arxiv.org/abs/2605.26086
- **PDF**：https://arxiv.org/pdf/2605.26086
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
Claw-Anything 试图把个人助理 agent 放进更完整的数字世界：长期活动历史、多后端服务、多设备 GUI/CLI 交互和主动建议。

**☠️ 毒舌点评**  
这篇的好处是把“always-on assistant”从口号落到了可测环境。GPT-5.5 pass@1 只有 34.5% 说明任务确实难；但仿真世界和真实个人数据之间仍有距离。

**🔧 技术方案**  
- **模型架构**：通过多轮事件注入构造数月用户活动和互相关联的服务状态，agent 需要跨设备、跨服务完成查询、操作和主动辅助。  
- **核心创新**：把个人助理的上下文宽度、噪声、冲突信号和 proactive 需求同时纳入 benchmark。  
- **训练 / 推理策略**：主要是评测与数据生成流水线；agent 使用现有前沿模型进行交互和推理。

**📊 实验结果**  
实验显示上下文范围扩大后性能明显下降，proactive 场景尤其困难；GPT-5.5 pass@1 为 34.5%。

**💡 为什么值得看**  
如果你在做个人助理或桌面/移动 agent，这篇能提醒你真实困难不在单步工具调用，而在长期世界状态。

</span>

---


### [19] MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

- **评分**：8/10
- **作者/机构**：作者：Dingbang Wu、Rui Hao、Haiyang Wang、Shuzhe Wu、Han Xiao、Zhenghong Li、Bojiang Zhou、Zheng Ju、Zichen Liu、Lue Fan、Zhaoxiang Zhang
- **论文链接**：https://arxiv.org/abs/2605.26114
- **PDF**：https://arxiv.org/pdf/2605.26114
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
把日常手机 GUI 做成可验证、可并行、可重置的仿真环境，核心价值是让移动端 agent 不再只能靠真实设备慢慢试错。

**☠️ 毒舌点评**  
强项是工程问题选得准：状态 JSON 化、确定性判分和并行 rollout 都直击 GUI agent 训练瓶颈。短板是生态和任务覆盖还要看后续社区扩展，benchmark 论文常见的“环境即贡献”风险仍在。

**🔧 技术方案**  
- **模型架构**：浏览器托管的移动端仿真平台，包含可配置系统状态、app 状态、控件、通知、键盘和边缘手势，并以结构化 JSON 表示环境。  
- **核心创新**：将移动 GUI agent 的交互环境做成可 fork、可比对、可确定验证的低成本沙盒，支持几百个并行实例。  
- **训练 / 推理策略**：用环境支持在线 RL 和离线评测；重点不是新模型，而是可控状态、任务定义和 outcome judging。

**📊 实验结果**  
论文报告单实例约 400MB、冷启动约 3 秒；在 MobileGym-Bench 上训练后策略能迁移到真实设备，稳定失败任务也能暴露模型边界。

**💡 为什么值得看**  
适合关注 GUI agent、RL 环境和可验证评测的读者精读。

</span>

---


### [20] GroupTravelBench: Benchmarking LLM Agents on Multi-Person Travel Planning

- **评分**：6/10
- **作者/机构**：作者：Xiang Cheng、Yulan Hu、Lulu Zheng、Zheng Pan、Xin Li、Yong Liu
- **论文链接**：https://arxiv.org/abs/2605.25200
- **PDF**：https://arxiv.org/pdf/2605.25200
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
GroupTravelBench 评测 LLM agents 在多人旅行规划中的表现，重点是多用户偏好、约束冲突和计划协商。

**☠️ 毒舌点评**  
任务很生活化，适合测 agent 的约束满足和交互规划；但 benchmark 类论文能否成为主流，还要看数据规模和复用度。

**🔧 技术方案**  
- **模型架构**：构造多人旅行计划任务，包含用户偏好、冲突约束和规划输出。  
- **核心创新**：把单用户旅行规划扩展到多用户协商，强调偏好冲突处理。  
- **训练 / 推理策略**：评测现有 LLM agent 的计划生成和约束满足能力。

**📊 实验结果**  
论文显示当前 agent 在复杂多人偏好和冲突处理上仍不稳定。

**💡 为什么值得看**  
对个人助理、旅行规划 agent 和多方偏好建模有参考。

</span>

---


### [21] PolyGnosis 2.0: Enhancing LLM Reasoning via Agentic Harness Engineering for Polymarket and OSINT Insight Extraction

- **评分**：6/10
- **作者/机构**：作者：Daren Wang、Hong Xu、Jiawen Xian
- **论文链接**：https://arxiv.org/abs/2605.25958
- **PDF**：https://arxiv.org/pdf/2605.25958
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
PolyGnosis 2.0 用多 agent 架构把 Polymarket 异常信号和 GDELT OSINT 叙事流结合，提取预测情报。

**☠️ 毒舌点评**  
应用场景有意思，且认真比较 reflection、tool-calling、D&C、CoT 等 harness 技术。但金融 alpha 场景噪声太大，结论更适合作为工程经验而非通用 agent 定律。

**🔧 技术方案**  
- **模型架构**：多 agent pipeline 处理市场情绪、媒体叙事和异常信号，寻找 perspective mismatch。  
- **核心创新**：把 agent harness 组件在高噪声金融/OSINT 场景下逐项量化，而不是只宣称 multi-agent 更强。  
- **训练 / 推理策略**：比较反思循环、工具调用、divide-and-conquer、CoT 等组合，并观察 consensus bias。

**📊 实验结果**  
发现 D&C 对多维对齐必要，无约束 terminal reflection 会导致 logical drift，tool-calling 需要严格触发和过滤。

**💡 为什么值得看**  
适合看 agent harness 在真实高噪声领域如何翻车。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
