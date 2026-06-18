---
title: "Agent/LLM论文速递｜2026-05-29｜全量版（1/4）"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-29｜全量版（1/4）：本期收录 16 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-29｜全量版（1/4）：本期收录 16 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-29"
cover_subtitle: "Agent系统与工具使用 / RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-29｜全量版（1/4）

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **16** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**2** 篇
- LLM 推理 / 规划 / RAG：**7** 篇
- 评测 / 安全 / 对齐：**4** 篇

这是本期全量收录第 1/4 篇分稿，每篇最多 16 篇，方便在公众号多图文里阅读和转发。全量版保留更多相关论文，但仍建议优先看评分和关键词。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents | ⭐ 8/10 | agent, tool use, workflow |
| Agent系统与工具使用 | 2 | Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor? | ⭐ 7/10 | agent, tool use, workflow |
| RAG与知识检索 | 1 | ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure | ⭐ 8/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 2 | RAISE: RAG Design as an Architecture Search Problem | ⭐ 7/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 3 | Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents | ⭐ 7/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 4 | Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive Context Selection | ⭐ 6/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 5 | KairosAgent: Agentic Time Series Forecasting with Fused Semantic Reasoning | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 6 | How Reliable Are AI Attackers Against a Fixed Vulnerable Target? A 400-Run Empirical Study of LLM Penetration Testing Consistency | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 7 | Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software | ⭐ 5/10 | RAG, retrieval, knowledge |
| 多智能体与协作 | 1 | When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems | ⭐ 7/10 | multi-agent, collaboration |
| 多智能体与协作 | 2 | Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization | ⭐ 7/10 | multi-agent, collaboration |
| 多智能体与协作 | 3 | Enhancing Multi-Agent Communication through Attention Steering with Context Relevance | ⭐ 5/10 | multi-agent, collaboration |
| LLM训练与对齐 | 1 | Audio Jailbreaks in Large Audio-Language Models: Taxonomy, Attack-Defense Analysis, and Cost-Aware Evaluation | ⭐ 5/10 | alignment, training |
| 评测与安全 | 1 | HEART-Bench: Do LLM Agents Exhibit Human-like Psychology? | ⭐ 7/10 | evaluation, safety, reliability |
| 评测与安全 | 2 | Resolution Diagnostics for Paired LLM Evaluation | ⭐ 5/10 | evaluation, safety, reliability |
| 评测与安全 | 3 | LLMSurgeon: Diagnosing Data Mixture of Large Language Models | ⭐ 5/10 | evaluation, safety, reliability |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents

- **评分**：8/10
- **作者/机构**：作者：Anany Kotawala
- **论文链接**：https://arxiv.org/abs/2605.30335
- **PDF**：https://arxiv.org/pdf/2605.30335
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以 LLM Agent 的观察、计划、行动、记忆或人类监督闭环为主要结构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [2] Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?

- **评分**：7/10
- **作者/机构**：作者：Xiaoze Liu, Ruowang Zhang, Amir H. Abdi, Michel Galley, Zhikai Chen, Siheng Xiong, Xiaoqian Wang, Jing Gao
- **论文链接**：https://arxiv.org/abs/2605.30152
- **PDF**：https://arxiv.org/pdf/2605.30152
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文讨论“Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?”中的智能体机制，重点在任务分解、记忆/工具/协作或运行时决策如何影响 LLM Agent 的可靠性。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：以 LLM Agent 的观察、计划、行动、记忆或人类监督闭环为主要结构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [3] ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure

- **评分**：8/10
- **作者/机构**：作者：A. J. Lew, Y. Cao, M. J. Buehler
- **论文链接**：https://arxiv.org/abs/2605.30284
- **PDF**：https://arxiv.org/pdf/2605.30284
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [4] RAISE: RAG Design as an Architecture Search Problem

- **评分**：7/10
- **作者/机构**：作者：Zhen Chen, Yibing Liu, Weihao Xie, Yu Liang, Peilin Chen, Shiqi Wang
- **论文链接**：https://arxiv.org/abs/2605.30029
- **PDF**：https://arxiv.org/pdf/2605.30029
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“RAISE: RAG Design as an Architecture Search Problem”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [5] Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents

- **评分**：7/10
- **作者/机构**：作者：Ziyan Liu, Zhezheng Hao, Yeqiu Chen, Hong Wang, Jingren Hou, Ruiyi Ding, Yongkang Yang, Wence Ji, Wei Xia, Feng Liu
- **论文链接**：https://arxiv.org/abs/2605.30159
- **PDF**：https://arxiv.org/pdf/2605.30159
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文讨论“Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents”中的智能体机制，重点在任务分解、记忆/工具/协作或运行时决策如何影响 LLM Agent 的可靠性。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：以 LLM Agent 的观察、计划、行动、记忆或人类监督闭环为主要结构。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [6] Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive Context Selection

- **评分**：6/10
- **作者/机构**：作者：Yutong Wang, Xuebo Liu, Derek F. Wong, Zhilin Li, Rongqing Jiang, Min Zhang, Shimin Tao, Daimeng Wei, Min Zhang
- **论文链接**：https://arxiv.org/abs/2605.30274
- **PDF**：https://arxiv.org/pdf/2605.30274
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive Context Selection”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：贴近 Agent/LLM 主线，适合公众号读者快速追踪。

</span>

---


### [7] KairosAgent: Agentic Time Series Forecasting with Fused Semantic Reasoning

- **评分**：5/10
- **作者/机构**：作者：Kun Feng, Ziwei Shan, Yuchen Fang, Yiyang Tan, Sihan Lu, Shuqi Gu, Lintao Ma, Xingyu Lu, Kan Ren
- **论文链接**：https://arxiv.org/abs/2605.30002
- **PDF**：https://arxiv.org/pdf/2605.30002
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文讨论“KairosAgent: Agentic Time Series Forecasting with Fused Semantic Reasoning”中的智能体机制，重点在任务分解、记忆/工具/协作或运行时决策如何影响 LLM Agent 的可靠性。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：尝试拆解多步/多智能体系统里的贡献归因问题。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：贴近 Agent/LLM 主线，适合公众号读者快速追踪。

</span>

---


### [8] How Reliable Are AI Attackers Against a Fixed Vulnerable Target? A 400-Run Empirical Study of LLM Penetration Testing Consistency

- **评分**：5/10
- **作者/机构**：作者：Galip Tolga Erdem
- **论文链接**：https://arxiv.org/abs/2605.30096
- **PDF**：https://arxiv.org/pdf/2605.30096
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文聚焦“How Reliable Are AI Attackers Against a Fixed Vulnerable Target? A 400-Run Empirical Study of LLM Penetration Testing Consistency”，从 RAG与知识检索 角度研究大模型能力、应用或风险边界。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：贴近 Agent/LLM 主线，适合公众号读者快速追踪。

</span>

---


### [9] Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software

- **评分**：5/10
- **作者/机构**：作者：Nhat-Minh Nguyen
- **论文链接**：https://arxiv.org/abs/2605.30353
- **PDF**：https://arxiv.org/pdf/2605.30353
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：把真实开发/应用过程量化为可复盘案例，强调监督协议和失败模式。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🤝 多智能体 / 协作


### [10] When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems

- **评分**：7/10
- **作者/机构**：作者：Corrado Rainone, Davide Belli, Bence Major, Arash Behboodi
- **论文链接**：https://arxiv.org/abs/2605.30102
- **PDF**：https://arxiv.org/pdf/2605.30102
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以多个 LLM/专业组件之间的通信、路由或协作为核心结构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [11] Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization

- **评分**：7/10
- **作者/机构**：作者：Wenwu Li, Yuran Song, Mingze Zhao, Bo Jin, Wenhao Li
- **论文链接**：https://arxiv.org/abs/2605.30227
- **PDF**：https://arxiv.org/pdf/2605.30227
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以多个 LLM/专业组件之间的通信、路由或协作为核心结构。  
- **核心创新**：尝试拆解多步/多智能体系统里的贡献归因问题。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [12] Enhancing Multi-Agent Communication through Attention Steering with Context Relevance

- **评分**：5/10
- **作者/机构**：作者：Hongxiang Zhang, Yuan Tian, Tianyi Zhang
- **论文链接**：https://arxiv.org/abs/2605.30136
- **PDF**：https://arxiv.org/pdf/2605.30136
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Enhancing Multi-Agent Communication through Attention Steering with Context Relevance”提出评测/诊断框架，关注 多智能体与协作 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以多个 LLM/专业组件之间的通信、路由或协作为核心结构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [13] Audio Jailbreaks in Large Audio-Language Models: Taxonomy, Attack-Defense Analysis, and Cost-Aware Evaluation

- **评分**：5/10
- **作者/机构**：作者：Bo-Han Feng, Yu-Hsuan Li Liang, Chien-Feng Liu, You-Hsuan Chang, Yun-Nung Chen
- **论文链接**：https://arxiv.org/abs/2605.30031
- **PDF**：https://arxiv.org/pdf/2605.30031
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Audio Jailbreaks in Large Audio-Language Models: Taxonomy, Attack-Defense Analysis, and Cost-Aware Evaluation”提出评测/诊断框架，关注 LLM训练与对齐 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [14] HEART-Bench: Do LLM Agents Exhibit Human-like Psychology?

- **评分**：7/10
- **作者/机构**：作者：Weihan Peng, Chenxu Zhang, Qianao Wang, Yuling Shi, Heng Lian, Qihong Mao, Jiahao Pang, Chunliang Feng, Bowen Li, Xiaodong Gu
- **论文链接**：https://arxiv.org/abs/2605.30058
- **PDF**：https://arxiv.org/pdf/2605.30058
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“HEART-Bench: Do LLM Agents Exhibit Human-like Psychology?”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
值得放进精选：问题与 Agent/LLM 主线贴合，且相比普通应用稿更像是在补一个可复用的方法、评测或系统缺口。阅读时建议重点看任务定义、实验设置和失败案例是否支撑作者结论。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
精选候选：问题贴近 Agent/LLM 主线，且提供了评测、系统机制或能力边界方面的可读增量。

</span>

---


### [15] Resolution Diagnostics for Paired LLM Evaluation

- **评分**：5/10
- **作者/机构**：作者：Anany Kotawala
- **论文链接**：https://arxiv.org/abs/2605.30315
- **PDF**：https://arxiv.org/pdf/2605.30315
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Resolution Diagnostics for Paired LLM Evaluation”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [16] LLMSurgeon: Diagnosing Data Mixture of Large Language Models

- **评分**：5/10
- **作者/机构**：作者：Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
- **论文链接**：https://arxiv.org/abs/2605.30348
- **PDF**：https://arxiv.org/pdf/2605.30348
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“LLMSurgeon: Diagnosing Data Mixture of Large Language Models”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
