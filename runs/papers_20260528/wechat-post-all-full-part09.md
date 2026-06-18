---
title: "Agent/LLM论文速递｜2026-05-28｜全量版9/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版9/13：本期收录 20 篇，重点看 LLM训练与对齐；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版9/13：本期收录 20 篇，重点看 LLM训练与对齐；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "LLM训练与对齐"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版9/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**20** 篇

这是今天全量版第 9/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| LLM训练与对齐 | 1 | Skill-Conditioned Gated Self-Distillation for LLM Reasoning | ⭐ 7/10 | reasoning |
| LLM训练与对齐 | 2 | Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization | ⭐ 7/10 | alignment, training |
| LLM训练与对齐 | 3 | Self-Improving Language Models with Bidirectional Evolutionary Search | ⭐ 7/10 | search |
| LLM训练与对齐 | 4 | Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models | ⭐ 6/10 | alignment |
| LLM训练与对齐 | 5 | Learning to Translate from Soft to Hard LLM Prompts | ⭐ 6/10 | alignment, training |
| LLM训练与对齐 | 6 | Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction | ⭐ 6/10 | alignment, training |
| 评测与安全 | 1 | EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents | ⭐ 10/10 | agent, benchmark, tool use |
| 评测与安全 | 2 | A Unified Framework for the Evaluation of LLM Agentic Capabilities | ⭐ 10/10 | agent, evaluation |
| 评测与安全 | 3 | Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows | ⭐ 10/10 | agent |
| 评测与安全 | 4 | DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints | ⭐ 10/10 | planning, benchmark, tool use |
| 评测与安全 | 5 | Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs | ⭐ 10/10 | evaluation, reliability |
| 评测与安全 | 6 | VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora | ⭐ 10/10 | agent, planning, benchmark, web |
| 评测与安全 | 7 | Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities | ⭐ 9/10 | alignment |
| 评测与安全 | 8 | When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 9 | AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications | ⭐ 9/10 | benchmark |
| 评测与安全 | 10 | Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 11 | Disentangling Language Roles in Multilingual LLM Task Execution | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 12 | TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling | ⭐ 9/10 | agent, safety |
| 评测与安全 | 13 | Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 14 | PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management | ⭐ 9/10 | benchmark |

</span>

## ⚙️ LLM 训练 / 对齐


### [1] Skill-Conditioned Gated Self-Distillation for LLM Reasoning

- **评分**：7/10
- **作者/机构**：Jiazhen Huang, Xiao Chen, Xiao Luo, Yong Dai, Senkang Hu, Yuzhi Zhao
- **论文链接**：https://arxiv.org/abs/2605.28791
- **PDF**：https://arxiv.org/pdf/2605.28791
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Skill-Conditioned Gated Self-Distillation for LLM Reasoning”展开，属于「LLM训练与对齐」方向。作者核心问题是：is equally well known: the reward signal is sparse, delayed, and nearly uniform across the entire tra- arXiv:2605.28791v1 [cs.CL] 27 May 2026 On-policy self-distillation (SD) improves LLM reasoning by using teacher-side privileged in- jectory. On-policy disti…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Skill-Conditioned Gated Self-Distillation for LLM Reasoning”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization

- **评分**：7/10
- **作者/机构**：Beiduo Chen, Pingjun Hong, Ziyun Zhang, Benjamin Roth, Anna Korhonen, Barbara Plank
- **论文链接**：https://arxiv.org/abs/2605.28802
- **PDF**：https://arxiv.org/pdf/2605.28802
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization”展开，属于「LLM训练与对齐」方向。作者核心问题是：provide only a partial view of annotator behav- ior: they indicate what annotators choose, but not Free-text explanations extend human label vari- arXiv:2605.28802v1 [cs.CL] 27 May 2026 ation (HLV) beyond label disagreement by re- why. Free-text explanations…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] Self-Improving Language Models with Bidirectional Evolutionary Search

- **评分**：7/10
- **作者/机构**：Guowei Xu, Zhenting Qi, Huangyuan Su, Weirui Ye, Himabindu Lakkaraju, Sham M. Kakade, Yilun Du
- **论文链接**：https://arxiv.org/abs/2605.28814
- **PDF**：https://arxiv.org/pdf/2605.28814
- **代码链接**：https://github.com/Embodied-Minds-Lab/BES

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Self-Improving Language Models with Bidirectional Evolutionary Search”展开，属于「LLM训练与对齐」方向。作者核心问题是：Search has been proposed as an effective method for self-improving language mod- els and agentic systems, both for post-training sample generation and for inference. However, widely used methods such as best-of-N sampling and tree search face two fundamental…

**☠️ 毒舌点评**  
可进精选候选：方向贴近「LLM训练与对齐」读者，问题也相对明确。毒舌一点说，亮点能否成立取决于对比基线和真实场景复杂度，别只看标题里的 Agent/LLM 光环。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Self-Improving Language Models with Bidirectional Evolutionary Search”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM训练与对齐」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models

- **评分**：6/10
- **作者/机构**：Yizhong Geng, Yanliang Li, Jinghan Yang, Tianhan Jiang, Boxun An, Ya Li, Xiaoyu Shen
- **论文链接**：https://arxiv.org/abs/2605.27383
- **PDF**：https://arxiv.org/pdf/2605.27383
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models”展开，属于「LLM训练与对齐」方向。作者核心问题是：ical rules and irregular scripts (Ren et al., 2021; Shen et al., 2018). Spoken Language Models (SLMs) have emerged Spoken Language Models (SLMs) have emerged as a powerful alternative by modeling discretized neural to- arXiv:2605.27383v1 [cs.CL] 10 Apr 2026 a…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM训练与对齐」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [5] Learning to Translate from Soft to Hard LLM Prompts

- **评分**：6/10
- **作者/机构**：Pitipat Kongsomjit, Suryansh Goyal, Jacob Whitehill
- **论文链接**：https://arxiv.org/abs/2605.27642
- **PDF**：https://arxiv.org/pdf/2605.27642
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learning to Translate from Soft to Hard LLM Prompts”展开，属于「LLM训练与对齐」方向。作者核心问题是：In contrast to LLM parameters or adapters, soft prompts share the same embedding space as natural arXiv:2605.27642v1 [cs.CL] 26 May 2026 Soft prompt tuning is a parameter-efficient language tokens, and it is thus tempting to hope that method for adapting LLMs…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Learning to Translate from Soft to Hard LLM Prompts”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM训练与对齐」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---


### [6] Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction

- **评分**：6/10
- **作者/机构**：Zehan Li, Yutong Zhu, Siyang Wu, Honglin Bao, James A. Evans
- **论文链接**：https://arxiv.org/abs/2605.27878
- **PDF**：https://arxiv.org/pdf/2605.27878
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction”展开，属于「LLM训练与对齐」方向。作者核心问题是：Human story domains 30 23 New Yorker arXiv:2605.27878v1 [cs.CL] 27 May 2026 Pr ofessional fiction Large language models produce fluent fiction, Full TMAS Story Common fiction 10 0 Story Star yet their creative output is widely seen as flat. Story We ask where…

**☠️ 毒舌点评**  
合格可扫：主题相关，但大概率更像增量系统、应用验证或局部评测。适合快速了解方法设定，不建议默认当成范式级突破。

**🔧 技术方案**  
- **模型架构**：围绕 LLM 训练、偏好优化、对齐、安全拒答或后训练信号设计展开。  
- **核心创新**：主要新意在于把“Narrative Flattening: How Post-Training Compresses Thematic, Affective, and Stylistic Variation in LLM Fiction”这个问题形式化到「LLM训练与对齐」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：重点关注偏好信号、奖励/拒答信号、微调或后训练策略，以及这些信号是否真的改善泛化。

**📊 实验结果**  
目前按首页信息只能判断其给出一定实验或案例验证；证据强度需要进一步读完整实验表和附录后确认。

**💡 为什么值得看**  
它可以补齐今天「LLM训练与对齐」方向的版图，方便后续检索同类系统、任务或评测设定。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [7] EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents

- **评分**：10/10
- **作者/机构**：Yunqi Liu, Tong Niu, Zitong Wang, Zhenlong Dai, Yuqi Qing, Weiqiang Wang, Jian Liu
- **论文链接**：https://arxiv.org/abs/2605.27820
- **PDF**：https://arxiv.org/pdf/2605.27820
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents”展开，属于「评测与安全」方向。作者核心问题是：As AI agents increasingly operate in open, real-world environments, they require a deep synergy of multimodal perception, tool invocation with multi-hop reason- ing, and dynamic interaction with users. However, existing benchmarks fail to jointly evaluate the…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] A Unified Framework for the Evaluation of LLM Agentic Capabilities

- **评分**：10/10
- **作者/机构**：Pengyu Zhu, Lijun Li, Yaxing Lyu, Qianxin Luo, Jingyi Yang, Yi Liu, Tingfeng Hui, Xinyu Yuan, Li Sun, Sen Su, Jing Shao
- **论文链接**：https://arxiv.org/abs/2605.27898
- **PDF**：https://arxiv.org/pdf/2605.27898
- **代码链接**：https://huggingface.co/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Unified Framework for the Evaluation of LLM Agentic Capabilities”展开，属于「评测与安全」方向。作者核心问题是：1 Introduction arXiv:2605.27898v1 [cs.AI] 27 May 2026 Large language models (LLMs) are increasingly As LLMs are increasingly deployed as agents, evaluated not only as text generators, but as agents reliable assessment of their agentic capabilities that plan…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“A Unified Framework for the Evaluation of LLM Agentic Capabilities”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

- **评分**：10/10
- **作者/机构**：Yilun Yao, Xinyu Tan, Chao-Hsuan Liu, Yaoming Li, Zhengyang Wang, Wenhan Yu, Zhewen Tan, Yuxuan Tian, Guangxiang Zhao, Lin Sun, Xiangzheng Zhang, Tong Yang
- **论文链接**：https://arxiv.org/abs/2605.27922
- **PDF**：https://arxiv.org/pdf/2605.27922
- **代码链接**：https://github.com/Qihoo360/harness-bench

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows”展开，属于「评测与安全」方向。作者核心问题是：LLM agents are increasingly deployed as executable systems that use tools, mod- ify workspaces, and produce concrete artifacts. In such workflows, performance depends not only on the base model, but also on the harness: the system layer that manages context…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints

- **评分**：10/10
- **作者/机构**：Zhitong Chen, Kai Yin, Weifeng Zhang, Zhiyuan Wang, Xiangjue Dong, Chengkai Liu, Zhewei Liu, Yiming Xiao, Ali Mostafavi, James Caverlee
- **论文链接**：https://arxiv.org/abs/2605.27957
- **PDF**：https://arxiv.org/pdf/2605.27957
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints”展开，属于「评测与安全」方向。作者核心问题是：analysts must rapidly orchestrate specialized tools for tasks such as satellite image analysis, precip- arXiv:2605.27957v1 [cs.CL] 27 May 2026 Disasters cause severe societal impacts, de- itation nowcasting, flood modeling, and damage manding rapid coordinati…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs

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


### [12] VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora

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


### [13] Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities

- **评分**：9/10
- **作者/机构**：Nuan Wen, Xuezhe Ma
- **论文链接**：https://arxiv.org/abs/2605.27388
- **PDF**：https://arxiv.org/pdf/2605.27388
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities”展开，属于「评测与安全」方向。作者核心问题是：Large language models (LLMs) are increasingly utilized as proxies for computational social analysis; yet, their ability to faithfully represent the ”thick descriptions” (Geertz, 1973) of human communities remains a critical challenge. Current evaluations ofte…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Modeling Community Attitude through Reaction Tone: A Human-AI Collaborative Framework for Evaluating LLM Alignment with Linguistic Behaviors in Online Communities”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference

- **评分**：9/10
- **作者/机构**：Pu Li, Jiawen Qi, Qinyu Chen
- **论文链接**：https://arxiv.org/abs/2605.27435
- **PDF**：https://arxiv.org/pdf/2605.27435
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference”展开，属于「评测与安全」方向。作者核心问题是：Deploying large language models (LLMs) on mobile TABLE I devices increasingly relies on heterogeneous execution, yet no C OMPARISON WITH PRIOR MOBILE LLM BENCHMARKING STUDIES . SA: prior study has systematically characterized NPU effectiveness at STAGE - AWAR…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications

- **评分**：9/10
- **作者/机构**：Yuchao Wu, Wenji Fang, Jing Wang, Wenkai Li, Ziyan Guo, Zhiyao Xie
- **论文链接**：https://arxiv.org/abs/2605.27472
- **PDF**：https://arxiv.org/pdf/2605.27472
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications”展开，属于「评测与安全」方向。作者核心问题是：Assertion-based verification (ABV) is a cornerstone of modern hardware design, yet manually translating design intent into formal SystemVerilog Assertions (SVAs) remains labor-intensive and error- prone. While Large Language Models (LLMs) show promise for au-…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“AssertLLM2: A Comprehensive LLM Benchmark for Assertion Generation from Design Specifications”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems

- **评分**：9/10
- **作者/机构**：Yipeng Ouyang, Xin Huang, Bingjie Liu, Zhongchun Zheng, Yuhao Gu, Xianwei Zhang
- **论文链接**：https://arxiv.org/abs/2605.27492
- **PDF**：https://arxiv.org/pdf/2605.27492
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems”展开，属于「评测与安全」方向。作者核心问题是：execution behavior under partial workflow failure. The framework Large language model (LLM) agents are rapidly evolving from cod- further incorporates utility-oriented multi-dimensional metrics that ing assistants into autonomous software engineering systems.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] Disentangling Language Roles in Multilingual LLM Task Execution

- **评分**：9/10
- **作者/机构**：Qishi Zhan, Minxuan Hu, Seoyeon Jang, Lei Zhao, Ziheng Chen, Man Liang, Xinyue Xiang, Jiaxin Liu, Guansu Wang, Liang He
- **论文链接**：https://arxiv.org/abs/2605.27649
- **PDF**：https://arxiv.org/pdf/2605.27649
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Disentangling Language Roles in Multilingual LLM Task Execution”展开，属于「评测与安全」方向。作者核心问题是：with colleagues in China. Such cases make mul- tilingual task execution a triplet-structured prob- Multilingual LLMs are increasingly used arXiv:2605.27649v1 [cs.CL] 26 May 2026 when instruction, source content, and re- lem: the instruction language, content…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Disentangling Language Roles in Multilingual LLM Task Execution”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling

- **评分**：9/10
- **作者/机构**：Jiaqian Li, Yanshu Li, Boxuan Zhang, Ruixiang Tang, Kuan-Hao Huang
- **论文链接**：https://arxiv.org/abs/2605.27690
- **PDF**：https://arxiv.org/pdf/2605.27690
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling”展开，属于「评测与安全」方向。作者核心问题是：arXiv:2605.27690v1 [cs.CL] 26 May 2026 LLM agents increasingly operate through multi- turn tool use and environment interaction, where safety risks often emerge from interme- diate steps long before they surface in the final outcome. Reactive auditing is ther…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness

- **评分**：9/10
- **作者/机构**：Jaechang Kim, Sunung Mun, Seungjoon Lee, Jaewoong Cho, Jungseul Ok
- **论文链接**：https://arxiv.org/abs/2605.27879
- **PDF**：https://arxiv.org/pdf/2605.27879
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness”展开，属于「评测与安全」方向。作者核心问题是：XAI Method Category Feature Counter- Feature Surrogate Importance factual Influence Model Explainable AI (XAI) helps users interpret model behavior and identify potential faults. Why User Question Type arXiv:2605.27879v1 [cs.AI] 27 May 2026 Agentic XAI system…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management

- **评分**：9/10
- **作者/机构**：Yuxuan Zhao, Sijia Chen, Ningxin Su
- **论文链接**：https://arxiv.org/abs/2605.27887
- **PDF**：https://arxiv.org/pdf/2605.27887
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management”展开，属于「评测与安全」方向。作者核心问题是：however, remains inadequately evaluated. PM re- quires constructing multi-asset portfolios that bal- arXiv:2605.27887v1 [cs.AI] 27 May 2026 LLMs have shown strong performance across ance return objectives against explicit risk con- diverse financial tasks, ye…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
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
