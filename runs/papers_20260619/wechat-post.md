---
title: "Agent/LLM论文速递｜2026-06-19｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-06-19｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-06-19｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-06-19"
cover_subtitle: "Agent系统与工具使用 / LLM推理与规划"
---

# 📡 Agent/LLM论文速递｜2026-06-19｜精选版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **4** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**2** 篇
- LLM 推理 / 规划 / RAG：**2** 篇
- 评测 / 安全 / 对齐：**0** 篇

这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Benchmarking Agentic Review Systems | ⭐ 9/10 | Agent, benchmark, LLM |
| Agent系统与工具使用 | 2 | Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining | ⭐ 9/10 | Agent, benchmark, LLM |
| LLM推理与规划 | 1 | QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation | ⭐ 9/10 | 推理/规划, benchmark, reasoning |
| RAG与知识检索 | 1 | Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software | ⭐ 9/10 | RAG/知识检索, benchmark, LLM |

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

## 🧠 LLM 推理 / 规划 / RAG


### [3] QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation

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


### [4] Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software

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

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
