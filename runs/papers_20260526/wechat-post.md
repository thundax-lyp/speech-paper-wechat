---
title: "Agent/LLM论文速递｜2026-05-26｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-26｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、RAG与知识检索、应用与基准；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-26｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、RAG与知识检索、应用与基准；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-26"
cover_subtitle: "Agent系统与工具使用 / RAG与知识检索..."
---

# 📡 Agent/LLM论文速递｜2026-05-26｜精选版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **4** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**1** 篇
- LLM 推理 / 规划 / RAG：**1** 篇
- 评测 / 安全 / 对齐：**0** 篇

这篇只放按 ML / NLP 顶会审稿口径看，最值得大多数读者花时间看的 1–4 篇。优先标准不是热闹，而是问题是否真、系统是否能跑、实验是否能说明 Agent/LLM 的能力边界。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | VeriTrace: Evolving Mental Models for Deep Research Agents | ⭐ 8/10 | deep research agent, mental model, cognitive graph, feedback loops |
| RAG与知识检索 | 1 | Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG | ⭐ 8/10 | agentic RAG, continual correction, factual nugget, production |
| 应用与基准 | 1 | Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World | ⭐ 8/10 | personal assistant, long-horizon context, GUI+CLI, benchmark |
| 应用与基准 | 2 | MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research | ⭐ 8/10 | mobile GUI agent, simulation, online RL, benchmark |

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


### [1] VeriTrace: Evolving Mental Models for Deep Research Agents

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

## 🧠 LLM 推理 / 规划 / RAG


### [2] Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG

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

## 🧪 应用 / Benchmark


### [3] Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World

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


### [4] MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

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

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
