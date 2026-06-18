---
title: "Agent/LLM论文速递｜2026-05-28｜全量版2/13"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-28｜全量版2/13：本期收录 20 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-28｜全量版2/13：本期收录 20 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-28"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-28｜全量版2/13

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **20** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**7** 篇
- LLM 推理 / 规划 / RAG：**13** 篇
- 评测 / 安全 / 对齐：**0** 篇

这是今天全量版第 2/13 篇，保留完整简介、点评、技术方案、实验结果和为什么值得看。为避开微信单篇正文大小限制，258 篇论文按顺序拆分发布。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings | ⭐ 8/10 | agent, workflow |
| Agent系统与工具使用 | 2 | Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 3 | Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation | ⭐ 8/10 | agent, workflow |
| Agent系统与工具使用 | 4 | Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 5 | Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 6 | MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 7 | Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents | ⭐ 8/10 | agent |
| LLM推理与规划 | 1 | OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis | ⭐ 10/10 | agent, reasoning, tool use |
| RAG与知识检索 | 1 | AI Research Agents Narrow Scientific Exploration | ⭐ 10/10 | agent, search |
| LLM推理与规划 | 2 | Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning | ⭐ 10/10 | agent, planning |
| RAG与知识检索 | 2 | A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks | ⭐ 10/10 | agent, RAG, benchmark |
| RAG与知识检索 | 3 | LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know? | ⭐ 10/10 | agent, search |
| RAG与知识检索 | 4 | Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval | ⭐ 10/10 | agent, retrieval |
| RAG与知识检索 | 5 | APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents | ⭐ 9/10 | agent |
| RAG与知识检索 | 6 | RAGe: A Retrieval-Augmented Generation Evaluation Framework | ⭐ 9/10 | RAG, retrieval, evaluation |
| RAG与知识检索 | 7 | DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents | ⭐ 9/10 | agent, benchmark |
| RAG与知识检索 | 8 | A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test | ⭐ 9/10 | RAG, evaluation |
| RAG与知识检索 | 9 | Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents? | ⭐ 9/10 | agent, retrieval, search |
| RAG与知识检索 | 10 | The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages | ⭐ 9/10 | RAG |
| RAG与知识检索 | 11 | Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations | ⭐ 9/10 | RAG, retrieval |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings

- **评分**：8/10
- **作者/机构**：Shadmehr Zaregarizi, Khashayar Yavari
- **论文链接**：https://arxiv.org/abs/2605.28168
- **PDF**：https://arxiv.org/pdf/2605.28168
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings”展开，属于「Agent系统与工具使用」方向。作者核心问题是：1 Introduction Large language models (LLMs) have demonstrated promising ca- The transition toward grid-interactive buildings increasingly relies pability in generating reward functions for deep reinforcement on deep reinforcement learning (DRL) agents that op…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [2] Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

- **评分**：8/10
- **作者/机构**：Jiapeng Zhu, Jianxiang Yu, Yibo Zhao, Chengcheng Han, Qi Gu, Xunliang Cai, Xiang Li, Weining Qian
- **论文链接**：https://arxiv.org/abs/2605.28424
- **PDF**：https://arxiv.org/pdf/2605.28424
- **代码链接**：https://github.com/JasonZhujp/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning”展开，属于「Agent系统与工具使用」方向。作者核心问题是：performance bottlenecks (Xu and Yan, 2026; Ling et al., 2026). A skill encapsulates procedural knowl- Equipping large language models with explicit arXiv:2605.28424v1 [cs.CL] 27 May 2026 skills has emerged as a promising paradigm edge into modular, reusable t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [3] Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation

- **评分**：8/10
- **作者/机构**：Melih Catal, Alex Wolf, Tiago Ferreiro Matos, Pooja Rani, Harald Gall
- **论文链接**：https://arxiv.org/abs/2605.28515
- **PDF**：https://arxiv.org/pdf/2605.28515
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation”展开，属于「Agent系统与工具使用」方向。作者核心问题是：are affiliated with providers that offer such ser- vices, these choices may be skewed toward the arXiv:2605.28515v1 [cs.SE] 27 May 2026 Large Language Models (LLMs) have become provider’s own ecosystem. We define this behavior an integral part of software dev…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [4] Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem

- **评分**：8/10
- **作者/机构**：Luca Beurer-Kellner, Aleksei Kudrinskii, Marco Milanta, Kristian Bonde Nielsen, Hemang Sarkar, Liran Tal
- **论文链接**：https://arxiv.org/abs/2605.28588
- **PDF**：https://arxiv.org/pdf/2605.28588
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem”展开，属于「Agent系统与工具使用」方向。作者核心问题是：We analyzed 3,984 AI agent skills from major marketplaces and found 76 confirmed malicious payloads, including credential theft, backdoor installation, and data exfil- tration. 13.4% of all skills contain at least one critical-level security issue and at leas…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Technical Report: Exploring the Emerging Threats of the Agent Skill Ecosystem”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [5] Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents

- **评分**：8/10
- **作者/机构**：Zheng Wu, Pengzhou Cheng, Zongru Wu, Yuan Guo, Tianjie Ju, Aston Zhang, Gongshen Liu, Zhuosheng Zhang
- **论文链接**：https://arxiv.org/abs/2605.28629
- **PDF**：https://arxiv.org/pdf/2605.28629
- **代码链接**：https://github.com/Wuzheng02/Mobile-Aptus

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Recent advancements in multimodal large language models (MLLMs) have shown exceptional potential in enabling mobile-using agents to autonomously execute human instructions. However, fully automated agents often try to execute tasks even when they are unable t…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [6] MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution

- **评分**：8/10
- **作者/机构**：Yanqiu Zhao, Dongying Zheng, Kaibo Huang, Yukun Wei, Zhongliang Yang, Linna Zhou
- **论文链接**：https://arxiv.org/abs/2605.28646
- **PDF**：https://arxiv.org/pdf/2605.28646
- **代码链接**：https://github.com/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution”展开，属于「Agent系统与工具使用」方向。作者核心问题是：6 Lin Yue ••• Reply in chat ALLOW arXiv:2605.28646v1 [cs.CR] 27 May 2026 GUI agents rely on screenshots to infer in- Is the report available now? tent and operate across applications, but these Forward screenshots often contain private messages, Yes. You can…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [7] Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

- **评分**：8/10
- **作者/机构**：Suji Kim, Kangsan Kim, Sung Ju Hwang
- **论文链接**：https://arxiv.org/abs/2605.28775
- **PDF**：https://arxiv.org/pdf/2605.28775
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents”展开，属于「Agent系统与工具使用」方向。作者核心问题是：Computer-use agents (CUAs) have recently made substantial progress, but deploy- ing a separate large expert for each software domain remains expensive. Small open CUAs are more practical specialization targets, but they remain substantially weaker and exhibit…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「Agent系统与工具使用」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 为决策/控制核心，外接工具、浏览、规划或工作流模块，形成面向任务执行的 agent pipeline。  
- **核心创新**：主要新意在于把“Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents”这个问题形式化到「Agent系统与工具使用」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「Agent系统与工具使用」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [8] OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis

- **评分**：10/10
- **作者/机构**：Jing Hao, Siyuan Dai, Yongxin Zhang, Yuci Liang, Jiamin Wu, Jiahao Bao, Yuxuan Fan, Zanting Ye, Yanpeng Sun, Xinyu Zhang, Ming Hu, Liang Zhan 等
- **论文链接**：https://arxiv.org/abs/2605.27378
- **PDF**：https://arxiv.org/pdf/2605.27378
- **代码链接**：https://github.com/isjinghao/OralAgent

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis”展开，属于「LLM推理与规划」方向。作者核心问题是：Dental image analysis plays a pivotal role in Instruction arXiv:2605.27378v1 [cs.CL] 9 Apr 2026 Observation supporting accurate diagnosis and treatment planning in 𝑂! oral healthcare. Although recent advances have produced Response: dental AI models for speci…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“OralAgent: Integrating Reasoning, Tools, and Knowledge for Interactive Dental Image Analysis”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [9] AI Research Agents Narrow Scientific Exploration

- **评分**：10/10
- **作者/机构**：Yixuan Tang, Yi Yang
- **论文链接**：https://arxiv.org/abs/2605.27905
- **PDF**：https://arxiv.org/pdf/2605.27905
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“AI Research Agents Narrow Scientific Exploration”展开，属于「RAG与知识检索」方向。作者核心问题是：AI research agents can now generate research ideas, design experiments, run code, and draft papers, raising the possibility of large-scale AI-assisted scientific discovery. Many current agent frameworks explicitly encourage the generation of novel and high-im…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“AI Research Agents Narrow Scientific Exploration”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [10] Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning

- **评分**：10/10
- **作者/机构**：Zhenyu Cui, Xiangzhong Luo
- **论文链接**：https://arxiv.org/abs/2605.27935
- **PDF**：https://arxiv.org/pdf/2605.27935
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning”展开，属于「LLM推理与规划」方向。作者核心问题是：. Recent mechanistic studies suggest that large language mod- els (LLMs) may utilize their depth inefficiently in standard single-turn tasks. Whether this still holds in autonomous agent settings, where mod- els must perform multi-turn planning, tool use, and…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「LLM推理与规划」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：以 LLM 推理链、规划、搜索、求解器或中间状态建模为核心，关注复杂任务求解能力。  
- **核心创新**：主要新意在于把“Do Agents Think Deeper? A Mechanistic Investigation of Layer-Wise Dynamics in Sequential Planning”这个问题形式化到「LLM推理与规划」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「LLM推理与规划」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [11] A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks

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


### [12] LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

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


### [13] Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval

- **评分**：10/10
- **作者/机构**：Shiyu Chen, Tarfah Alrashed, Alon Halevy, Natasha Noy
- **论文链接**：https://arxiv.org/abs/2605.28787
- **PDF**：https://arxiv.org/pdf/2605.28787
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval”展开，属于「RAG与知识检索」方向。作者核心问题是：. In the era of autonomous agents, machine-actionable data is critical for data-driven workflows. For more than a decade, semantic metadata like schema.org has anchored the FAIR principles (Findable, Accessible, Interoperable, and Reusable) for machine-action…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [14] APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents

- **评分**：9/10
- **作者/机构**：Quan Zheng, Yan Gao, Shaobin He, Haoxiang Guan, Yuanhe Tian, Jie Feng, Ming Wang, Shuxin Zheng, Zhen Liu
- **论文链接**：https://arxiv.org/abs/2605.27419
- **PDF**：https://arxiv.org/pdf/2605.27419
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：LLM-agent simulation offers a flexible computational tool for studying population response trajectories that depend on scenario events, memory, demographics, and evolving social context. However, full multi-round simulation scales linearly with both populatio…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [15] RAGe: A Retrieval-Augmented Generation Evaluation Framework

- **评分**：9/10
- **作者/机构**：Larissa Guder, João Pedro de Moura, Arthur Accorsi, Gustavo Losch do Amaral, Maurício Cecílio Magnaguagno, Felipe Meneguzzi, Marcio Sorraglia Pinho, Dalvan Griebler
- **论文链接**：https://arxiv.org/abs/2605.27445
- **PDF**：https://arxiv.org/pdf/2605.27445
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“RAGe: A Retrieval-Augmented Generation Evaluation Framework”展开，属于「RAG与知识检索」方向。作者核心问题是：Deploying Large Language Model (LLM) applications, particularly those rely- ing on Retrieval-Augmented Generation (RAG), remains challenging due to high computational demands, outdated knowledge bases, and the need to man- ually select optimal pipeline compon…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“RAGe: A Retrieval-Augmented Generation Evaluation Framework”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [16] DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents

- **评分**：9/10
- **作者/机构**：Shijie Cao, Yuan Yuan, Jing Liu
- **论文链接**：https://arxiv.org/abs/2605.27566
- **PDF**：https://arxiv.org/pdf/2605.27566
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents”展开，属于「RAG与知识检索」方向。作者核心问题是：agents fail to consistently surpass strong dispatch- ing baselines—behaving more like robust heuris- Progress in neural combinatorial optimization for tic approximators than superior optimizers. arXiv:2605.27566v1 [cs.AI] 26 May 2026 Dynamic Flexible Job Shop…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [17] A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test

- **评分**：9/10
- **作者/机构**：Camilo Chacón Sartori, José H. García
- **论文链接**：https://arxiv.org/abs/2605.27789
- **PDF**：https://arxiv.org/pdf/2605.27789
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test”展开，属于「RAG与知识检索」方向。作者核心问题是：because it is simple and cheap to scale. It also hides important choices. A method can look bet- Retrieval-augmented generation (RAG) sys- ter because it selected better evidence, because it tems are often compared by asking a large lan- induced longer answer…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [18] Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?

- **评分**：9/10
- **作者/机构**：Yibo Zhao, Zichen Ding, Jiayi Wu, Zun Wang, Xiang Li
- **论文链接**：https://arxiv.org/abs/2605.27881
- **PDF**：https://arxiv.org/pdf/2605.27881
- **代码链接**：https://github.com/YiboZhao624/

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?”展开，属于「RAG与知识检索」方向。作者核心问题是：to computer-using agents (OpenAI, 2025; Liu et al., 2026; Yang et al., 2026), coding agents (Ma et al., arXiv:2605.27881v1 [cs.CL] 27 May 2026 Search agents powered by large language mod- 2026; Team et al., 2026; Zhang et al., 2026), and els can autonomously…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [19] The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages

- **评分**：9/10
- **作者/机构**：Eric Onyame, Runtao Zhou, Kowshik Thopalli, Bhavya Kailkhura, Chirag Agarwal
- **论文链接**：https://arxiv.org/abs/2605.27901
- **PDF**：https://arxiv.org/pdf/2605.27901
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages”展开，属于「RAG与知识检索」方向。作者核心问题是：Chain-of-thought (CoT) monitoring has been proposed as a promising safety mech- anism for detecting misaligned behavior in large language models. However, its reliability remains largely unexplored beyond English and across diverse model families. We present…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---


### [20] Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations

- **评分**：9/10
- **作者/机构**：Sachin Kumar
- **论文链接**：https://arxiv.org/abs/2605.27958
- **PDF**：https://arxiv.org/pdf/2605.27958
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇论文围绕“Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations”展开，属于「RAG与知识检索」方向。作者核心问题是：distributed sub-threshold features. These find- ings demonstrate that probe fragility under stan- arXiv:2605.27958v1 [cs.CL] 27 May 2026 Linear probes trained on internal activations of dard training reflects distributional narrowness Large Language Models (L…

**☠️ 毒舌点评**  
今天少数值得优先精读的稿子：问题切在「RAG与知识检索」主线上，标题里给出的任务/系统边界比较清楚。真正要看的是实验是否覆盖失败案例，而不只是把 LLM/Agent 包装成一个漂亮流程图。

**🔧 技术方案**  
- **模型架构**：围绕检索、记忆、知识库或长上下文组织 LLM 输入，重点在证据获取与上下文利用。  
- **核心创新**：主要新意在于把“Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations”这个问题形式化到「RAG与知识检索」框架下，并给出对应的数据、系统流程或评测口径。  
- **训练 / 推理策略**：通常依赖提示、工具调用、检索增强、搜索/规划或多轮交互推理；若有微调，应重点看消融和迁移表现。

**📊 实验结果**  
从摘要/首页信息看，论文声称给出系统性实验或基准验证；精读时应优先核查对比基线、消融、失败案例和统计显著性。

**💡 为什么值得看**  
它触及「RAG与知识检索」里较核心的问题，适合作为今天优先精读或后续跟踪的入口。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
