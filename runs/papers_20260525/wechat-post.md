---
title: "Agent/LLM论文速递｜2026-05-25｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-25｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-25｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-25"
cover_subtitle: "Agent系统与工具使用 / RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-25｜精选版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **4** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**2** 篇
- LLM 推理 / 规划 / RAG：**1** 篇
- 评测 / 安全 / 对齐：**1** 篇

这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | SkillOpt: Executive Strategy for Self-Evolving Agent Skills | ⭐ 9/10 | agent |
| Agent系统与工具使用 | 2 | Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents | ⭐ 8/10 | agent |
| RAG与知识检索 | 1 | Parallel Context Compaction for Long-Horizon LLM Agent Serving | ⭐ 8/10 | agent, LLM |
| 评测与安全 | 1 | MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection | ⭐ 8/10 | agent, memory |

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


### [1] SkillOpt: Executive Strategy for Self-Evolving Agent Skills

- **评分**：9/10
- **作者/机构**：Yifan Yang；Ziyang Gong；Weiquan Huang；Qihao Yang；Ziwei Zhou；Zisu Huang；Yan Li；Xuemei Gao；Qi Dai；Bei Liu；Kai Qiu；Yuqing Yang；Dongdong Chen；Xue Yang；Chong Luo
- **论文链接**：https://arxiv.org/abs/2605.23904
- **PDF**：https://arxiv.org/pdf/2605.23904
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「SkillOpt: Executive Strategy for Self-Evolving Agent Skills」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
SkillOpt 把 Agent skill 的进化从经验记录推进到可执行策略选择，适合放在今天第一篇看。

**🔧 技术方案**  
- **模型架构**：围绕推理、规划或策略生成构建方法，通常把任务分解、反馈或验证接入 LLM 推理过程。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 LLM推理与规划 的读者快速判断是否加入精读列表。

</span>

---


### [2] Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

- **评分**：8/10
- **作者/机构**：Jiazheng Kang；Bowen Zhang；Zixin Song；Jiangwang Chen；Xiao Yang；Da Zhu；Guanjun Jiang
- **论文链接**：https://arxiv.org/abs/2605.23590
- **PDF**：https://arxiv.org/pdf/2605.23590
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
把 rubric 放进 ReAct 步级协作里，试图让 Agent 的行动-观察循环有更细粒度的过程反馈，方向清楚。

**🔧 技术方案**  
- **模型架构**：以 LLM/Agent 执行环为核心，围绕工具调用、技能/工作流、状态管理或任务执行链路组织系统。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 Agent系统与工具使用 的读者快速判断是否加入精读列表。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [3] Parallel Context Compaction for Long-Horizon LLM Agent Serving

- **评分**：8/10
- **作者/机构**：Musa Cim；Burak Topcu；Chita Das；Mahmut Taylan Kandemir
- **论文链接**：https://arxiv.org/abs/2605.23296
- **PDF**：https://arxiv.org/pdf/2605.23296
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Parallel Context Compaction for Long-Horizon LLM Agent Serving」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
长程 Agent 服务最头疼的是上下文膨胀，这篇做 parallel context compaction，问题非常工程核心。

**🔧 技术方案**  
- **模型架构**：把外部记忆、检索或上下文压缩接入模型调用链路，重点处理长程信息选择与可用性。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 RAG与知识检索 的读者快速判断是否加入精读列表。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [4] MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

- **评分**：8/10
- **作者/机构**：Zhewen Tan；Yilun Yao；Huiyan Jin；Wenhan Yu；Guoan Wang；Mengyuan Fan；liang lu；Feng Liu；Xiangzheng Zhang；Duohe Ma；Tong Yang；Lin Sun
- **论文链接**：https://arxiv.org/abs/2605.23723
- **PDF**：https://arxiv.org/pdf/2605.23723
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
记忆投毒会直接影响长期 Agent 的可信度，这篇把 post-hoc 审计落到因果归因与结构异常检测上，是很贴近实战的问题。

**🔧 技术方案**  
- **模型架构**：面向 Agent/LLM 的行为诊断、风险审计、鲁棒性或可靠性评测。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 评测与安全 的读者快速判断是否加入精读列表。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
