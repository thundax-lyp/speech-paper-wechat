---
title: "Agent/LLM论文速递｜2026-05-22｜精选版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-22｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-22｜精选版：本期收录 4 篇，重点看 Agent系统与工具使用、LLM推理与规划；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-22"
cover_subtitle: "Agent系统与工具使用 / LLM推理与规划"
---

# 📡 Agent/LLM论文速递｜2026-05-22｜精选版

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
| Agent系统与工具使用 | 1 | MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems | ⭐ 9/10 | self-evolving agents, source rewriting, production failures, agent systems |
| Agent系统与工具使用 | 2 | Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost | ⭐ 8/10 | workflow compilation, small LLM, orchestration, cost |
| LLM推理与规划 | 1 | Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents | ⭐ 8/10 | agent memory, credit assignment, long-horizon RL, GRPO |
| 评测与安全 | 1 | Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents | ⭐ 8/10 | agent evaluation, trace diagnostics, observability, LLM agents |

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

## 🧠 LLM 推理 / 规划 / RAG


### [3] Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents

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

## 🛡️ 评测 / 安全 / 可靠性


### [4] Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

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

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
