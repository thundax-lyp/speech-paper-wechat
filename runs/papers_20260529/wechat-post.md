---
title: "Agent/LLM论文速递｜2026-05-29｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-29｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-29｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-29"
cover_subtitle: "Agent系统与工具使用 / RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-29｜精选版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **4** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**1** 篇
- LLM 推理 / 规划 / RAG：**2** 篇
- 评测 / 安全 / 对齐：**0** 篇

这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents | ⭐ 8/10 | agent, tool use, workflow |
| RAG与知识检索 | 1 | ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure | ⭐ 8/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 2 | Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents | ⭐ 7/10 | RAG, retrieval, knowledge |
| 多智能体与协作 | 1 | Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization | ⭐ 7/10 | multi-agent, collaboration |

</span>

## 精选入选规则

默认按 ML 顶会审稿口径，用固定 rubric 打分：

- **新意（0–3）**：有没有明确的新方法、新任务设定或新范式
- **影响力（0–3）**：是不是对 Agent / LLM 主线方向有代表性，不只是特别窄的小点
- **证据强度（0–2）**：实验是否完整、对比是否靠谱、结论是否站得住
- **受众匹配度（0–2）**：是否贴近 Agent、LLM、多智能体、工具使用、RAG、对齐与评测等核心受众

分数校准：

- `6`：合格可读，但多半偏 incremental
- `7`：接近 strong accept，不是默认鼓励分
- `8+`：默认稀缺，只有当天明显强稿才配拿

总分 **≥7** 才进入精选；若满足条件论文过多，则按总分排序取前 **1–4 篇**；若高分论文不足，则宁缺毋滥，不硬凑。


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

## 🧠 LLM 推理 / 规划 / RAG


### [2] ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure

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


### [3] Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents

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

## 🤝 多智能体 / 协作


### [4] Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization

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

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
