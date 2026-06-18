---
title: "Agent/LLM论文速递｜2026-05-28｜全量版11/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版11/13：本期收录 20 篇，重点看 评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版11/13：本期收录 20 篇，重点看 评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "评测与安全"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版11/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**20** 篇

这是今天全量版第 11/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| 评测与安全 | 1 | Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections | ⭐ 8/10 | safety |
| 评测与安全 | 2 | From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies | ⭐ 8/10 | agent |
| 评测与安全 | 3 | Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning | ⭐ 8/10 | reasoning |
| 评测与安全 | 4 | Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems | ⭐ 8/10 | agent |
| 评测与安全 | 5 | Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 6 | Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 7 | ChildEval: When large language models meet children's personalities | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 8 | Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 9 | When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models | ⭐ 8/10 | safety |
| 评测与安全 | 10 | Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization | ⭐ 8/10 | reasoning |
| 评测与安全 | 11 | Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 12 | Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents | ⭐ 8/10 | agent |
| 评测与安全 | 13 | Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 14 | Entropy Distribution as a Fingerprint for Hallucinations in Generative Models | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 15 | Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation | ⭐ 8/10 | reasoning |
| 评测与安全 | 16 | SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models | ⭐ 8/10 | safety, alignment |
| 评测与安全 | 17 | SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving | ⭐ 8/10 | safety |
| 评测与安全 | 18 | Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study | ⭐ 8/10 | evaluation, reliability |
| 评测与安全 | 19 | Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis | ⭐ 7/10 | evaluation, reliability |
| 评测与安全 | 20 | Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks | ⭐ 7/10 | evaluation, reliability |

</span>

## 🛡️ 评测 / 安全 / 可靠性


### [1] Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections

- **评分**：8/10
- **作者/机构**：Wenzhe Song, Hao Zhang
- **论文链接**：https://arxiv.org/abs/2605.27418
- **PDF**：https://arxiv.org/pdf/2605.27418
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections”展开，属于「评测与安全」方向。作者核心问题是：The imminent integration of autonomous vehicles introduction of a network of robot transit paths that intersect and mobile robots in urban settings presents a critical safety with vehicular lanes creates a dense web of conflict points, challenge for future in…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies

- **评分**：8/10
- **作者/机构**：Vassilis Vassiliades
- **论文链接**：https://arxiv.org/abs/2605.27547
- **PDF**：https://arxiv.org/pdf/2605.27547
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies”展开，属于「评测与安全」方向。作者核心问题是：. As humans, robots, and software agents increasingly share safety-critical environments, coordination must move from static task al- location to managing uncertain commitments. Existing frameworks fall short: they either assume rigid, static teams or learn o…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning

- **评分**：8/10
- **作者/机构**：Saptarshi Sengupta, Suhang Wang
- **论文链接**：https://arxiv.org/abs/2605.27596
- **PDF**：https://arxiv.org/pdf/2605.27596
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning”展开，属于「评测与安全」方向。作者核心问题是：large models such as GPT-5 (OpenAI, 2025) and Recently, there has been increased interest in K2 (Team et al., 2025). Developing such models is arXiv:2605.27596v1 [cs.CL] 26 May 2026 Small Language Models (SLMs), which are non-trivial, making their wider adopt…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Can Hallucinations Be Useful? Solving Multi-Hop Questions With SLMs By Chaining System-I/II Reasoning”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems

- **评分**：8/10
- **作者/机构**：Srini Ramaswamy
- **论文链接**：https://arxiv.org/abs/2605.27628
- **PDF**：https://arxiv.org/pdf/2605.27628
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems”展开，属于「评测与安全」方向。作者核心问题是：As autonomous and agentic AI systems scale in robotic and human-machine environments, managing hallucination and persistent but unjustified action remains an open challenge. Rather than attributing these failures solely to model or alignment limitations, this…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction

- **评分**：8/10
- **作者/机构**：Joan Vendrell Gallart, Solmaz Kia, Russell Bent, Michael Grosskopf
- **论文链接**：https://arxiv.org/abs/2605.27706
- **PDF**：https://arxiv.org/pdf/2605.27706
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction”展开，属于「评测与安全」方向。作者核心问题是：We introduce CAROL (Chain-based Adaptive Reconfiguration Over Lattices), a probabilistic framework for test-time hallucination reduction in large language models. Rather than relying on token-level uncertainty, CAROL defines a semantic uncertainty measure bas…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Chain-based Adaptive Reconfiguration Over Lattices for Hallucination Reduction”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration

- **评分**：8/10
- **作者/机构**：Hankyeol Kim, Pilsung Kang
- **论文链接**：https://arxiv.org/abs/2605.27752
- **PDF**：https://arxiv.org/pdf/2605.27752
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration”展开，属于「评测与安全」方向。作者核心问题是：medical question answering to coding agents. Re- cent work therefore evaluates not only whether arXiv:2605.27752v1 [cs.AI] 26 May 2026 LLM confidence calibration is often evaluated a model answers correctly, but also whether its by comparing two signals: toke…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Asking Is Not Enough: Protocol Sensitivity in LLM Confidence Calibration”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] ChildEval: When large language models meet children's personalities

- **评分**：8/10
- **作者/机构**：Yanyan Luo, Xue Han, Chunxu Zhao, Ruiqiao Bai, Yaxing Zhang, Qian Hu, Lijun Mei, Junlan Feng
- **论文链接**：https://arxiv.org/abs/2605.27805
- **PDF**：https://arxiv.org/pdf/2605.27805
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“ChildEval: When large language models meet children's personalities”展开，属于「评测与安全」方向。作者核心问题是：(e.g., healthcare (Xu et al., 2024; Han et al., 2023), finance (Easin et al., 2024) and other domains (Bai arXiv:2605.27805v1 [cs.CL] 27 May 2026 While LLMs enable personalized chatbots, et al., 2025; Wang et al., 2025)) to deliver personal- their effectivene…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“ChildEval: When large language models meet children's personalities”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security

- **评分**：8/10
- **作者/机构**：Xiang Fang, Wanlong Fang
- **论文链接**：https://arxiv.org/abs/2605.27823
- **PDF**：https://arxiv.org/pdf/2605.27823
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security”展开，属于「评测与安全」方向。作者核心问题是：2025; Wang et al. 2026c; Cai et al. 2025; Fang and Fang 2026; Wang et al. 2026a; Fang, Fang, and Ji 2026; Wang Large Language Models (LLMs) are increasingly vulnera- et al. 2026d, 2025e; Fang 2026; Fang, Fang, and Wang ble to adversarial prompts that exploit…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models

- **评分**：8/10
- **作者/机构**：Dasol Choi, Alex Kwon
- **论文链接**：https://arxiv.org/abs/2605.27851
- **PDF**：https://arxiv.org/pdf/2605.27851
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models”展开，属于「评测与安全」方向。作者核心问题是：through static benchmarks, where models are eval- uated on their ability to choose the safe or ethical arXiv:2605.27851v1 [cs.AI] 27 May 2026 Safety benchmark scores provide incomplete action under standard assumptions (Herrador, 2025; evidence of deployment…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“When Context Flips, Safety Breaks: Diagnosing Brittle Safety in Aligned Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization

- **评分**：8/10
- **作者/机构**：Jiawei Kong, Hao Fang, Shunxiang Liao, Jinyu Li, Bin Chen, Hao Wu, Shu-Tao Xia, Min Zhang
- **论文链接**：https://arxiv.org/abs/2605.27906
- **PDF**：https://arxiv.org/pdf/2605.27906
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization”展开，属于「评测与安全」方向。作者核心问题是：Multimodal Large Reasoning Models intro- arXiv:2605.27906v1 [cs.AI] 27 May 2026 Is there a dining duce the reasoning paradigm, demonstrating table in the image? strong capabilities on complex vision-language tasks. However, they still suffer from severe hallu…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Reasoning Matters: Mitigate Hallucination in Multimodal Large Reasoning Models via Reasoning-Conditioned Preference Optimization”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values

- **评分**：8/10
- **作者/机构**：Seongjun Lee, Suwan Yoon, Changhee Lee
- **论文链接**：https://arxiv.org/abs/2605.28170
- **PDF**：https://arxiv.org/pdf/2605.28170
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values”展开，属于「评测与安全」方向。作者核心问题是：As large language models (LLMs) are increasingly integrated into high-stakes decision-making, the ability to reliably quantify uncertainty has become a critical requirement for safety and trust. However, current uncertainty arXiv:2605.28170v1 [cs.AI] 27 May 2…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Localizing Input Uncertainty Quantification for Large Language Models via Shapley Values”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents

- **评分**：8/10
- **作者/机构**：Yongxiang Li, Moxin Li, Zhixin Ma, Fengbin Zhu, Dongrui Liu, Wenjie Wang, Fuli Feng
- **论文链接**：https://arxiv.org/abs/2605.28201
- **PDF**：https://arxiv.org/pdf/2605.28201
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents”展开，属于「评测与安全」方向。作者核心问题是：transactions (Mou et al., 2026) and privacy leak- age (El Yagoubi et al., 2026). Large Language Model (LLM) agents remain arXiv:2605.28201v1 [cs.AI] 27 May 2026 vulnerable to safety threats from the external Safety threats to LLM agents can be broadly environ…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers

- **评分**：8/10
- **作者/机构**：Carmen Quiles-Ramírez, Leticia L. Rodríguez, Nicolás Martorell, Natalia Díaz-Rodríguez
- **论文链接**：https://arxiv.org/abs/2605.28215
- **PDF**：https://arxiv.org/pdf/2605.28215
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers”展开，属于「评测与安全」方向。作者核心问题是：window (Dong et al., 2024). Despite impressive few-shot accuracy, the reasoning process underlying these predictions In-context learning (ICL) enables multimodal remains a black box: models produce answers without any arXiv:2605.28215v1 [cs.AI] 27 May 2026 la…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] Entropy Distribution as a Fingerprint for Hallucinations in Generative Models

- **评分**：8/10
- **作者/机构**：Mattia J. Villani, Pranav Deshpande, Akshay Seshadri, Romina Yalovetzky, Niraj Kumar
- **论文链接**：https://arxiv.org/abs/2605.28264
- **PDF**：https://arxiv.org/pdf/2605.28264
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Entropy Distribution as a Fingerprint for Hallucinations in Generative Models”展开，属于「评测与安全」方向。作者核心问题是：Large Language Models (LLMs) often generate factually incorrect outputs, com- monly termed hallucinations, that undermine trust and limit deployment in high- stakes settings. Existing hallucination detection methods typically require multiple forward passes…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Entropy Distribution as a Fingerprint for Hallucinations in Generative Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation

- **评分**：8/10
- **作者/机构**：Zhaoyang Jiang, Xuanqi Peng, Fei Teng, Zhizhong Fu, Yunsoo Kim, Jiacong Mi, Zicheng Li, Honghan Wu
- **论文链接**：https://arxiv.org/abs/2605.28301
- **PDF**：https://arxiv.org/pdf/2605.28301
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation”展开，属于「评测与安全」方向。作者核心问题是：1 Introduction The modern recipe for making a compact reason- Chain-of-thought (CoT) distillation trains a ing model is simple: ask a stronger teacher to smaller model to imitate a teacher’s reason- write chain-of-thought solutions, then train the ing trace…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Better Accuracies, Worse Reasoning: A Step-Level Audit of Medical Chain-of-Thought Distillation”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models

- **评分**：8/10
- **作者/机构**：Chao Ding, Mouxiao Bian, Tianbin Li, Minjia Yuan, Yidong Jiang, Yankai Jiang, Jinru Ding, Jiayuan Chen, Zhuangzhi Gao, Pengcheng Chen, Zhao He, Rongzhao Zhang 等
- **论文链接**：https://arxiv.org/abs/2605.28338
- **PDF**：https://arxiv.org/pdf/2605.28338
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models”展开，属于「评测与安全」方向。作者核心问题是：Large language models(LLMs) increasingly match expert performance on licensing examinations, yet routine clinical use remains limited because governance requires auditable reasoning, safety and ethics alignment, and resilience to adversarial misuse. Here we p…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“SafeMed-R1: Clinician-Audited Safety and Ethics Alignment for Medical Large Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving

- **评分**：8/10
- **作者/机构**：Kangyu Wu, Peng Cui, Guoxi Chen, Ya Zhang
- **论文链接**：https://arxiv.org/abs/2605.28583
- **PDF**：https://arxiv.org/pdf/2605.28583
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving”展开，属于「评测与安全」方向。作者核心问题是：Ensuring both safety and efficiency in decision- making of autonomous driving systems remains a fundamen- tal challenge. Traditional Deep Reinforcement Learning (DRL) suffers from unsafe random exploration and slow convergence, while Large Language Models (LL…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study

- **评分**：8/10
- **作者/机构**：Irune Zubiaga, Aitor Soroa, Rodrigo Agerri
- **论文链接**：https://arxiv.org/abs/2605.28710
- **PDF**：https://arxiv.org/pdf/2605.28710
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study”展开，属于「评测与安全」方向。作者核心问题是：In this work, we study how to design effective training and evaluation strategies that enable ro- arXiv:2605.28710v1 [cs.CL] 27 May 2026 Large language models (LLMs) are increas- bust multilingual performance across languages ingly used for the automatic eval…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis

- **评分**：7/10
- **作者/机构**：Taylor Anderson, Sara Von Hoene, Orhan Yagizer Cinar, Emma Von Hoene, Amira Roess, Andrew Crooks, Hamdi Kavak
- **论文链接**：https://arxiv.org/abs/2605.27401
- **PDF**：https://arxiv.org/pdf/2605.27401
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis”展开，属于「评测与安全」方向。作者核心问题是：There is a growing interest in utilizing synthetic populations for a diverse range of applications. At the same time, we are witnessing a tremendous growth in artificial intelligence in all walks of life. This paper evaluates whether zero-shot large language…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Using Zero-Shot LLM-Generated Survey Data for Geographically Explicit Population Synthesis”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks

- **评分**：7/10
- **作者/机构**：Partho Ghose, Al Bashir, Prem Raj, Azlan Zahid
- **论文链接**：https://arxiv.org/abs/2605.27595
- **PDF**：https://arxiv.org/pdf/2605.27595
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks”展开，属于「评测与安全」方向。作者核心问题是：Large Language Models (LLMs) are being rapidly adopted in agricultural imaging applications, rang- ing from crop interpretation to synthetic field image generation. However, these models frequently exhibit hallucinations—outputs that appear confident yet devi…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「评测与安全」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Hallucination Behavior in Multimodal LLMs Across Agricultural Image Interpretation and Generation Tasks”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
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
