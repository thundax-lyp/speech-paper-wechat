---
title: "Agent/LLM论文速递｜2026-05-28｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜精选版：本期收录 4 篇，重点看 RAG与知识检索、评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜精选版：本期收录 4 篇，重点看 RAG与知识检索、评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "RAG与知识检索 / 评测与安全"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜精选版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **4** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**2** 篇
- 评测 / 安全 / 对齐：**2** 篇

这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks | ⭐ 10/10 | agent, RAG, benchmark |
| RAG与知识检索 | 2 | LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know? | ⭐ 10/10 | agent, search |
| 评测与安全 | 1 | Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs | ⭐ 10/10 | evaluation, reliability |
| 评测与安全 | 2 | VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora | ⭐ 10/10 | agent, planning, benchmark, web |

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


## 🧠 LLM 推理 / 规划 / RAG


### [1] A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks

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


### [2] LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

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

## 🛡️ 评测 / 安全 / 可靠性


### [3] Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs

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


### [4] VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora

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

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
