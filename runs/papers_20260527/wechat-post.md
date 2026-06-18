---
title: "Agent/LLM论文速递｜2026-05-27｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-27｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-27｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-27"
cover_subtitle: "Agent系统与工具使用 / 评测与安全"
---

# 📡 Agent/LLM论文速递｜2026-05-27｜精选版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **4** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**1** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**2** 篇

这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation | ⭐ 8/10 | agent, memory, evaluation |
| 评测与安全 | 1 | PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions | ⭐ 9/10 | benchmark, evaluation |
| 评测与安全 | 2 | MemFail: Stress-Testing Failure Modes of LLM Memory Systems | ⭐ 8/10 | memory |
| 应用与基准 | 1 | VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions | ⭐ 8/10 | agent, proactive assistant |

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


### [1] MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

- **评分**：8/10
- **作者/机构**：作者：Huawei Lin、Peng Li、Jie Song、Fuxin Jiang、Tieying Zhang
- **论文链接**：https://arxiv.org/abs/2605.27366
- **PDF**：https://arxiv.org/pdf/2605.27366
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Large language model (LLM) agents rely on reusable skills to solve complex tasks. However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability, reliability, and long-term improvement.

**☠️ 毒舌点评**  
MUSE-Autoskill 把 skill creation、skill memory、unit-test evaluation 和 refinement 放进同一个 agent 生命周期，是今天最像“可演化 Agent 基础设施”的系统稿。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合做 agent skills、长期记忆和工具型 agent 平台的人优先精读。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [2] PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions

- **评分**：9/10
- **作者/机构**：作者：Ruhallah Niazi、Faeze Ghorbanpour、Alexander Fraser
- **论文链接**：https://arxiv.org/abs/2605.27015
- **PDF**：https://arxiv.org/pdf/2605.27015
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions”展开，核心落点是评测、安全、可靠性与攻击面。 摘要显示，作者主要处理的问题是：Persian is spoken by over 110 million people and has a literary tradition spanning more than a Despite impressive multilingual capabilities, millennium, yet LLM competence in Persian liter- We introduce PersLitEval, a bench- mark of 4,514 Persian literature multiple- tional humanities, and domain-specific NLP tasks choice questions across eight fine-grained cate- (Kalhor and Yaghoobzadeh, 2026; Moosavi Mon- gories spanning spelling, literary devices, gram- azzah et al., 2025), understanding their capabili- mar, voc

**☠️ 毒舌点评**  
价值在于把 Agent/LLM 的可靠性问题落到可测攻击面、失败模式或 benchmark 上；短板通常是防御和泛化验证还要继续看。

**🔧 技术方案**  
- **模型架构**：围绕评测、安全、可靠性与攻击面构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“PersLitEval: Fine-grained Benchmark and Evaluation of LLMs on Persian Literature Questions”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注评测、安全、可靠性与攻击面的读者快速扫读；若你正在做相关系统，建议优先看问题定义、评测协议和失败案例。

</span>

---


### [3] MemFail: Stress-Testing Failure Modes of LLM Memory Systems

- **评分**：8/10
- **作者/机构**：作者：Ishir Garg、Neel Kolhe、Dawn Song、Xuandong Zhao
- **论文链接**：https://arxiv.org/abs/2605.26667
- **PDF**：https://arxiv.org/pdf/2605.26667
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“MemFail: Stress-Testing Failure Modes of LLM Memory Systems”展开，核心落点是Agent 系统、工具调用与工作流落地。 摘要显示，作者主要处理的问题是：A growing body of work on LLM memory sys- tems has emerged in response, augmenting agents Large language model (LLM) agents increas- with external stores they can read, write, and update ingly rely on external memory systems to re- over a lifetime, enabling consistent and personal- main consistent across long-horizon interac- ized responses (Chhikara et al., 2025; Xu et al., tions, but little empirical work has been done 2025; Liu et al., 2026; Xu et al., 2026; Rasmussen to understand the specific failure modes and

**☠️ 毒舌点评**  
MemFail 专门压力测试 LLM memory system 的失败模式，切中长期 agent 最容易被忽视的可靠性问题。

**🔧 技术方案**  
- **模型架构**：围绕Agent 系统、工具调用与工作流落地构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“MemFail: Stress-Testing Failure Modes of LLM Memory Systems”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
适合关注 agent memory、可靠性评测和上线风险的人重点看。

</span>

---

## 🧪 应用 / Benchmark


### [4] VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions

- **评分**：8/10
- **作者/机构**：作者：Yuxin Chen、Yi Zhang、Zhengzhou Cai、Yaorui Shi、Zhiyuan Yao、Chenhang Cui、Jingnan Zheng、Yaqi Huo、Xi Su、Qi Gu、Xunliang Cai、Xiang Wang、An Zhang、Tat-Seng Chua
- **论文链接**：https://arxiv.org/abs/2605.27141
- **PDF**：https://arxiv.org/pdf/2605.27141
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕“VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions”展开，核心落点是多智能体协作、博弈与社会智能。 摘要显示，作者主要处理的问题是：Large language models (LLMs) have evolved into interactive agents that collaborate with users in real-world tasks. Effective collaboration in such settings increasingly depends on understanding the user beyond what is explicitly stated, as user intent is often reflected in fragmented daily interactions and requires both personalized modeling and proactive interaction.

**☠️ 毒舌点评**  
VitaBench 2.0 把 personalized / proactive assistant 放进长期用户交互序列，重点评估偏好抽取、偏好更新和主动补问，而不是只看单轮工具调用。

**🔧 技术方案**  
- **模型架构**：围绕多智能体协作、博弈与社会智能构建方法或评测框架；具体模块以论文中的系统图、任务环境、数据构造和评测协议为准。  
- **核心创新**：把“VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions”对应的问题显式化，并尝试用框架、benchmark、指标或训练/推理流程给出可复用解法。  
- **训练 / 推理策略**：主要从论文摘要和正文首页判断：可能包含现有 LLM/agent 的推理流程、数据构造、SFT/RL、检索增强或评测协议；精读时应重点看实验设置与 ablation。

**📊 实验结果**  
摘要/首页显示作者给出了实验或系统分析；公众号稿按审稿口径关注其是否有对比、消融、真实任务和失败模式，而不是只看单点指标。

**💡 为什么值得看**  
如果你在做个人助理、长期记忆或 proactive agent，这篇 benchmark 很值得跟。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
