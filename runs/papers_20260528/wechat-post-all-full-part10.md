---
title: "Agent/LLM论文速递｜2026-05-28｜全量版10/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版10/13：本期收录 20 篇，重点看 评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版10/13：本期收录 20 篇，重点看 评测与安全；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "评测与安全"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版10/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**0** 篇
- 评测 / 安全 / 对齐：**20** 篇

这是今天全量版第 10/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| 评测与安全 | 1 | FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations | ⭐ 9/10 | reasoning, benchmark |
| 评测与安全 | 2 | Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking | ⭐ 9/10 | benchmark |
| 评测与安全 | 3 | KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 4 | AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios | ⭐ 9/10 | tool use |
| 评测与安全 | 5 | PetroBench: A Benchmark for Large Language Models in Petroleum Engineering | ⭐ 9/10 | benchmark |
| 评测与安全 | 6 | Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 7 | OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 8 | DEPART: DEcomposing PARiTy across Multilingual LLMs | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 9 | BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law | ⭐ 9/10 | reasoning, benchmark |
| 评测与安全 | 10 | Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning | ⭐ 9/10 | agent, reasoning |
| 评测与安全 | 11 | HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment | ⭐ 9/10 | benchmark, alignment |
| 评测与安全 | 12 | From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence | ⭐ 9/10 | agent, benchmark |
| 评测与安全 | 13 | HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs | ⭐ 9/10 | reasoning, benchmark |
| 评测与安全 | 14 | Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents | ⭐ 9/10 | agent, tool use |
| 评测与安全 | 15 | Cultural Binding Heads in Language Models | ⭐ 9/10 | evaluation, reliability |
| 评测与安全 | 16 | Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs | ⭐ 9/10 | search |
| 评测与安全 | 17 | Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News | ⭐ 9/10 | agent |
| 评测与安全 | 18 | Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability | ⭐ 9/10 | reasoning, evaluation |
| 评测与安全 | 19 | VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading | ⭐ 9/10 | alignment |
| 评测与安全 | 20 | Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named | ⭐ 8/10 | agent |

</span>

## 🛡️ 评测 / 安全 / 可靠性


### [1] FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations

- **评分**：9/10
- **作者/机构**：Xuesi Hu, Peng Wang, Jinpeng Miao, Xilin Tao, Caiwei Li, Yue Ma, Jie He, Qiancheng Zhang, Yuntao Zou, Dagang Li
- **论文链接**：https://arxiv.org/abs/2605.27896
- **PDF**：https://arxiv.org/pdf/2605.27896
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations”展开，属于「评测与安全」方向。作者核心问题是：et al., 2025). Notable examples include PIXIU (Xie et al., 2023), FinBen (Xie et al., 2024), and Fin- arXiv:2605.27896v1 [cs.CL] 27 May 2026 Recently, large language models (LLMs) have Master (Jiang et al., 2025). These benchmarks achieved superior performanc…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking

- **评分**：9/10
- **作者/机构**：Yuming, Huang, Yao Liu, Lei Wang, Junchen Wan
- **论文链接**：https://arxiv.org/abs/2605.27914
- **PDF**：https://arxiv.org/pdf/2605.27914
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking”展开，属于「评测与安全」方向。作者核心问题是：Subjective evaluation of LLM behavior — empathy, restraint, calibrated emotional tone — is hard. Human inter-rater agreement on such qualities saturates near ρ ≈ 0.45 across multiple domains; an LLM-as-judge proxy alone risks circularity, since a judge sharin…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Let the Results Speak: A Replication-First Paradigm for LLM Behavioral Benchmarking”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs

- **评分**：9/10
- **作者/机构**：Haechan Kim, Seungjun Chung, Inkyu Park, Jihoo Lee, Jonghyun Lee
- **论文链接**：https://arxiv.org/abs/2605.27984
- **PDF**：https://arxiv.org/pdf/2605.27984
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs”展开，属于「评测与安全」方向。作者核心问题是：et al., 2025; KimiTeam et al., 2025). As these mod- els move from transcription-oriented systems to- Speech language models (SpeechLMs) have achieved substantial progress by extending ward voice assistants and audio-interactive agents, large language models (…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios

- **评分**：9/10
- **作者/机构**：Kou Shi, Ziao Zhang, Shiting Huang, Avery Nie, Zhen Fang, Qiuchen Wang, Lin Chen, Huaian Chen, Zehui Chen, Feng Zhao
- **论文链接**：https://arxiv.org/abs/2605.27995
- **PDF**：https://arxiv.org/pdf/2605.27995
- **代码链接**：https://github.com/StoKou/repo-asynctool

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios”展开，属于「评测与安全」方向。作者核心问题是：increasingly capable LLM-based agents for tool use(OpenAI, 2025b; Comanici et al., 2025; An- arXiv:2605.27995v1 [cs.AI] 27 May 2026 Large language model (LLM)-based agents thropic, 2025; Yang et al., 2025; Team et al., 2025; have demonstrated strong capabilit…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] PetroBench: A Benchmark for Large Language Models in Petroleum Engineering

- **评分**：9/10
- **作者/机构**：Xiang Wang, Tingting Zhang, Sen Wang, Ying Wu, Heng Meng, Peng Zhou, Peng Li
- **论文链接**：https://arxiv.org/abs/2605.28032
- **PDF**：https://arxiv.org/pdf/2605.28032
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“PetroBench: A Benchmark for Large Language Models in Petroleum Engineering”展开，属于「评测与安全」方向。作者核心问题是：Large Language Models (LLMs) are experiencing rapid growth, accompanied by increasing applications in the petroleum industry. Given the diversity of available models and the complexity of engineering scenarios, the industry urgently requires a scientific eval…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“PetroBench: A Benchmark for Large Language Models in Petroleum Engineering”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents

- **评分**：9/10
- **作者/机构**：Bin Wu, Guanyun Zou, Bingbing Wang, Huan Zhao, Chuan Shi
- **论文链接**：https://arxiv.org/abs/2605.28108
- **PDF**：https://arxiv.org/pdf/2605.28108
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents”展开，属于「评测与安全」方向。作者核心问题是：No acquisition Acquired by asking arXiv:2605.28108v1 [cs.CL] 27 May 2026 Remind me before my art workshop Remind me before my art workshop A long-lived LLM agent, such as OpenClaw, earns its value by acting on a user’s preferences Reminder set. Reminder set.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents

- **评分**：9/10
- **作者/机构**：Chenyu Zhou, Xinyun Lu, Jiangyue Zhao, Jianghao Lin, Dongdong Ge, Yinyu Ye
- **论文链接**：https://arxiv.org/abs/2605.28158
- **PDF**：https://arxiv.org/pdf/2605.28158
- **代码链接**：https://github.com/0xzhouchenyu/OR-Space

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents”展开，属于「评测与安全」方向。作者核心问题是：Large language model (LLM) agents are increasingly used to assist with operations research (OR) arXiv:2605.28158v1 [cs.AI] 27 May 2026 modeling, yet existing OR-oriented benchmarks often reduce evaluation to one-shot translation from a self-contained textual…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [8] DEPART: DEcomposing PARiTy across Multilingual LLMs

- **评分**：9/10
- **作者/机构**：Manan Uppadhyay, Prashant Kodali, Pranjal Chitale, Reshma Ramaprasad, Himanshu Beniwal, Sunayana Sitaram
- **论文链接**：https://arxiv.org/abs/2605.28163
- **PDF**：https://arxiv.org/pdf/2605.28163
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DEPART: DEcomposing PARiTy across Multilingual LLMs”展开，属于「评测与安全」方向。作者核心问题是：explain it. Rather than just measuring the size of the cross-language gap, this work addresses a deeper arXiv:2605.28163v1 [cs.CL] 27 May 2026 Multilingual Large Language Models question: how much of the gap can be predicted (mLLMs) leaderboards report per-la…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“DEPART: DEcomposing PARiTy across Multilingual LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law

- **评分**：9/10
- **作者/机构**：Sebastian Nagl, Ann-Kristin Mayrhofer, Martin Heidebach, Aleyna Koçak, Anne Zettelmeier, Elly Breu, Angelina Greiner, Sofija Milijas, Matthias Grabmair
- **论文链接**：https://arxiv.org/abs/2605.28183
- **PDF**：https://arxiv.org/pdf/2605.28183
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law”展开，属于「评测与安全」方向。作者核心问题是：interpretive nature of doctrinal legal analysis. This poses a challenge for recent work on large arXiv:2605.28183v1 [cs.CL] 27 May 2026 We introduce the BenGER (Benchmark language models (LLMs): if human evaluation for German Law) dataset for evaluat- ing LLM…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“BenGER: Benchmarking LLM Systems on Subsumption-Based Legal Reasoning in German Law”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning

- **评分**：9/10
- **作者/机构**：Ke Xu, Yuhao Wang, Ziyang Cheng, Hongcheng Liu, Yanfeng Wang, Yu Wang
- **论文链接**：https://arxiv.org/abs/2605.28192
- **PDF**：https://arxiv.org/pdf/2605.28192
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning”展开，属于「评测与安全」方向。作者核心问题是：requires cross-modal multi-hop reasoning over evi- dence appearing at different temporal locations. Multi-hop audio-visual reasoning remains chal- arXiv:2605.28192v1 [cs.AI] 27 May 2026 lenging for Omni-LLMs, as relevant evidence is often sparse, temporally d…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Agentic Active Omni-Modal Perception for Multi-Hop Audio-Visual Reasoning”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment

- **评分**：9/10
- **作者/机构**：Yoonjin Jang, Junwoo Kim, Youngjoong Ko
- **论文链接**：https://arxiv.org/abs/2605.28308
- **PDF**：https://arxiv.org/pdf/2605.28308
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment”展开，属于「评测与安全」方向。作者核心问题是：Most standard EA benchmarks were designed to evaluate whether models can recover positive align- arXiv:2605.28308v1 [cs.CL] 27 May 2026 Entity Alignment (EA) is essential for knowl- ments across different KGs. Benchmarks such as edge graph (KG) fusion, but ex…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“HELEA: Hard-Negative Benchmark and LLM-based Reranking for Robust Entity Alignment”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [12] From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence

- **评分**：9/10
- **作者/机构**：Raffael Theiler, Ludovico Comito, David Leko, Leandro Von Krannichfeldt, Lev Telyatnikov, Olga Fink
- **论文链接**：https://arxiv.org/abs/2605.28371
- **PDF**：https://arxiv.org/pdf/2605.28371
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence”展开，属于「评测与安全」方向。作者核心问题是：Industrial Prognostics and Health Management (PHM) provides a representative case study for a broader challenge in applied machine learning: translating pub- lished papers into executable, benchmark-ready implementations. Reproducing under-specified methods i…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [13] HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs

- **评分**：9/10
- **作者/机构**：Yansong Ning, Mianpeng Liu, Jingwen Ye, Weidong Zhang, Hao Liu
- **论文链接**：https://arxiv.org/abs/2605.28398
- **PDF**：https://arxiv.org/pdf/2605.28398
- **代码链接**：https://github.com/usail-hkust/HRBench

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs”展开，属于「评测与安全」方向。作者核心问题是：et al., 2025), are achieving remarkable success on Hybrid-reasoning large language models complex tasks through extended chain-of-thought arXiv:2605.28398v1 [cs.AI] 27 May 2026 (LLMs) expose explicit controls over reason- (CoT) reasoning (Wei et al., 2022), b…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents

- **评分**：9/10
- **作者/机构**：Liang Cheng, Mingsheng Cai, Jiuming Jiang, Luo Mai
- **论文链接**：https://arxiv.org/abs/2605.28532
- **PDF**：https://arxiv.org/pdf/2605.28532
- **代码链接**：https://github.com/LeonChengg/FeasiGen

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents”展开，属于「评测与安全」方向。作者核心问题是："Book a plane ticket from Required Tools Edinburgh to London and pay with my credit card." Search_API Book_API Payment_API Tool-using agents often incur substantial com- arXiv:2605.28532v1 [cs.AI] 27 May 2026 (unavailable) putational cost due to long reasonin…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] Cultural Binding Heads in Language Models

- **评分**：9/10
- **作者/机构**：Avrile Floro, Luca Benedetto
- **论文链接**：https://arxiv.org/abs/2605.28543
- **PDF**：https://arxiv.org/pdf/2605.28543
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Cultural Binding Heads in Language Models”展开，属于「评测与安全」方向。作者核心问题是：as difference awareness: models should differentiate be- tween cultural groups when context justifies it, and equalize LLMs often default to equal treatment across cul- when it does not. They show that most fairness benchmarks tural groups, even though contex…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Cultural Binding Heads in Language Models”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs

- **评分**：9/10
- **作者/机构**：Yongsik Seo, Wooseok Jeong, Eunyoung Kim, Hyeonseo Jang, Dongha Lee
- **论文链接**：https://arxiv.org/abs/2605.28565
- **PDF**：https://arxiv.org/pdf/2605.28565
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs”展开，属于「评测与安全」方向。作者核心问题是：Users of search-augmented LLMs rely on citations as evidence that responses are grounded in real sources, and rarely verify the cited pages themselves. Millions of queries per day now pass through these systems, making citation quality a silent determinant of…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News

- **评分**：9/10
- **作者/机构**：Alejandro Buitrago López, Alberto Ortega Pastor, Javier Pastor-Galindo, José A. Ruipérez-Valiente
- **论文链接**：https://arxiv.org/abs/2605.28598
- **PDF**：https://arxiv.org/pdf/2605.28598
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News”展开，属于「评测与安全」方向。作者核心问题是：LLM-powered social agents are increasingly used emergent interaction patterns, rather than through direct arXiv:2605.28598v1 [cs.CL] 27 May 2026 to simulate online social behavior, yet their realism remains comparison with large-scale empirical audience data.…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability

- **评分**：9/10
- **作者/机构**：Leizhen Zhang, Shuhan Chen, Sheng Chen
- **论文链接**：https://arxiv.org/abs/2605.28602
- **PDF**：https://arxiv.org/pdf/2605.28602
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability”展开，属于「评测与安全」方向；从标题和首页信息看，重点是把 Agent/LLM 方法放到更具体的任务、评测或系统场景中检验。

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading

- **评分**：9/10
- **作者/机构**：Jinzhou Wu, Zhengwu Ma, Jixing Li, Baoping Tang, Zitong Lu
- **论文链接**：https://arxiv.org/abs/2605.28818
- **PDF**：https://arxiv.org/pdf/2605.28818
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading”展开，属于「评测与安全」方向。作者核心问题是：as an increasingly important benchmark for eval- Large language models (LLMs) have become uating whether language models capture human- arXiv:2605.28818v1 [cs.CL] 27 May 2026 increasingly useful computational models of like language processing (Caucheteux and…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：更偏评测/应用流程，训练细节不是主线；重点应看任务构造、评价指标和模型调用设置。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「评测与安全」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named

- **评分**：8/10
- **作者/机构**：Rohith Nama
- **论文链接**：https://arxiv.org/abs/2605.27396
- **PDF**：https://arxiv.org/pdf/2605.27396
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named”展开，属于「评测与安全」方向。作者核心问题是：Autonomous AI agents now plan, decide, and act on behalf of users across healthcare, financial services, and workplace contexts, often without step-by-step human approval. Existing AI literacy frameworks were built for a world in which humans evaluate AI outp…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「评测与安全」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 benchmark、诊断集或安全/可靠性评测框架为主，模型架构通常不是贡献核心。  
- **核心创新**：主要新意在于把“Agentic Literacy Debt: A Structural Problem the AI Literacy Field Has Not Yet Named”这个问题形式化到「评测与安全」框架下，并给出对应的数据、系统流程或评测口径。  
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
