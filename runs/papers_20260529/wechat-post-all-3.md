---
title: "Agent/LLM论文速递｜2026-05-29｜全量版（3/4）"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-29｜全量版（3/4）：本期收录 16 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-29｜全量版（3/4）：本期收录 16 篇，重点看 Agent系统与工具使用、RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-29"
cover_subtitle: "Agent系统与工具使用 / RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-29｜全量版（3/4）

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **16** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**1** 篇
- LLM 推理 / 规划 / RAG：**8** 篇
- 评测 / 安全 / 对齐：**4** 篇

这是本期全量收录第 3/4 篇分稿，每篇最多 16 篇，方便在公众号多图文里阅读和转发。全量版保留更多相关论文，但仍建议优先看评分和关键词。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | Modularizing Educational LLM-Agency for Fostering Responsible Learning Assistance | ⭐ 4/10 | agent, tool use, workflow |
| RAG与知识检索 | 1 | AgentSchool: An LLM-Powered Multi-Agent Simulation for Education | ⭐ 4/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 2 | From GPS Points to Travel Patterns: Flexible and Semantic Trajectory Generation with LLMs | ⭐ 4/10 | RAG, retrieval, knowledge |
| LLM推理与规划 | 1 | Projectional Decoding: Towards Semantic-Aware LLM Generation | ⭐ 4/10 | reasoning, planning, LLM |
| LLM推理与规划 | 2 | Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies | ⭐ 4/10 | reasoning, planning, LLM |
| RAG与知识检索 | 3 | Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms | ⭐ 4/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 4 | On Language Generation in the Limit with Bounded Memory | ⭐ 4/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 5 | Unlocking the Working Memory of Large Language Models for Latent Reasoning | ⭐ 3/10 | RAG, retrieval, knowledge |
| LLM推理与规划 | 3 | Beyond 3D VQAs: Injecting 3D Spatial Priors into Vision-Language Models for Enhanced Geometric Reasoning | ⭐ 3/10 | reasoning, planning, LLM |
| 多智能体与协作 | 1 | Teaching Values to Machines: Simulating Human-Like Behavior in LLMs | ⭐ 4/10 | multi-agent, collaboration |
| LLM训练与对齐 | 1 | Recovering Diversity Without Losing Alignment: A DPO Recipe for Post-Trained LLMs | ⭐ 4/10 | alignment, training |
| LLM训练与对齐 | 2 | How's it going? Reinforcement learning in language models recruits a functional welfare axis | ⭐ 4/10 | alignment, training |
| 评测与安全 | 1 | Double-Edged Sword or Sharp Tool? Designing and Evaluating Triadic LLM-Teacher Collaboration for K-12 Writing at Scale | ⭐ 3/10 | evaluation, safety, reliability |
| 评测与安全 | 2 | GRUFF: LLM Pronoun Fidelity, Reasoning, and Biases in German | ⭐ 3/10 | evaluation, safety, reliability |
| 应用与基准 | 1 | Anchorless Diversification for Parallel LLM Ideation | ⭐ 3/10 | Agent, LLM |
| 应用与基准 | 2 | LLUMI: Improving LLM Writing Assistance for Mental Health Support with Online Community Feedback | ⭐ 3/10 | Agent, LLM |

</span>

## 🧭 Agent 系统 / 工具使用


### [1] Modularizing Educational LLM-Agency for Fostering Responsible Learning Assistance

- **评分**：4/10
- **作者/机构**：作者：Julius Gabelmann, Felix Jahn, Kevin Baum, Sophie van Rossum, Emely Wuenscher, Timo P. Gros, Verena Wolf
- **论文链接**：https://arxiv.org/abs/2605.30187
- **PDF**：https://arxiv.org/pdf/2605.30187
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文讨论“Modularizing Educational LLM-Agency for Fostering Responsible Learning Assistance”中的智能体机制，重点在任务分解、记忆/工具/协作或运行时决策如何影响 LLM Agent 的可靠性。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以 LLM Agent 的观察、计划、行动、记忆或人类监督闭环为主要结构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🧠 LLM 推理 / 规划 / RAG


### [2] AgentSchool: An LLM-Powered Multi-Agent Simulation for Education

- **评分**：4/10
- **作者/机构**：作者：Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang
- **论文链接**：https://arxiv.org/abs/2605.30144
- **PDF**：https://arxiv.org/pdf/2605.30144
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文讨论“AgentSchool: An LLM-Powered Multi-Agent Simulation for Education”中的智能体机制，重点在任务分解、记忆/工具/协作或运行时决策如何影响 LLM Agent 的可靠性。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以多个 LLM/专业组件之间的通信、路由或协作为核心结构。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [3] From GPS Points to Travel Patterns: Flexible and Semantic Trajectory Generation with LLMs

- **评分**：4/10
- **作者/机构**：作者：Silin Zhou, Chenhao Wang, Yuntao Wen, Shuo Shang, Lisi Chen, Panos Kalnis
- **论文链接**：https://arxiv.org/abs/2605.30014
- **PDF**：https://arxiv.org/pdf/2605.30014
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文从训练、微调或数据组织角度切入，试图解释或改进“From GPS Points to Travel Patterns: Flexible and Semantic Trajectory Generation with LLMs”所对应的 LLM 能力形成过程。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [4] Projectional Decoding: Towards Semantic-Aware LLM Generation

- **评分**：4/10
- **作者/机构**：作者：Boqi Chen, José Antonio Hernández López, Aren A. Babikian
- **论文链接**：https://arxiv.org/abs/2605.30054
- **PDF**：https://arxiv.org/pdf/2605.30054
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文聚焦“Projectional Decoding: Towards Semantic-Aware LLM Generation”，从 LLM推理与规划 角度研究大模型能力、应用或风险边界。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [5] Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies

- **评分**：4/10
- **作者/机构**：作者：Kajetan Schweighofer, Conor F. Hayes, Roberto Dailey, Risto Miikkulainen, Xin Qiu
- **论文链接**：https://arxiv.org/abs/2605.30148
- **PDF**：https://arxiv.org/pdf/2605.30148
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文从训练、微调或数据组织角度切入，试图解释或改进“Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies”所对应的 LLM 能力形成过程。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕数据、微调目标或参数高效训练机制组织方法。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [6] Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms

- **评分**：4/10
- **作者/机构**：作者：Botao Amber Hu, Helena Rong, Max Van Kleek
- **论文链接**：https://arxiv.org/abs/2605.30169
- **PDF**：https://arxiv.org/pdf/2605.30169
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文讨论“Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms”中的智能体机制，重点在任务分解、记忆/工具/协作或运行时决策如何影响 LLM Agent 的可靠性。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以多个 LLM/专业组件之间的通信、路由或协作为核心结构。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [7] On Language Generation in the Limit with Bounded Memory

- **评分**：4/10
- **作者/机构**：作者：Jon Kleinberg, Anay Mehrotra, Amin Saberi, Grigoris Velegkas
- **论文链接**：https://arxiv.org/abs/2605.30324
- **PDF**：https://arxiv.org/pdf/2605.30324
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文从训练、微调或数据组织角度切入，试图解释或改进“On Language Generation in the Limit with Bounded Memory”所对应的 LLM 能力形成过程。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [8] Unlocking the Working Memory of Large Language Models for Latent Reasoning

- **评分**：3/10
- **作者/机构**：作者：Lukas Aichberger, Sepp Hochreiter
- **论文链接**：https://arxiv.org/abs/2605.30343
- **PDF**：https://arxiv.org/pdf/2605.30343
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“Unlocking the Working Memory of Large Language Models for Latent Reasoning”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [9] Beyond 3D VQAs: Injecting 3D Spatial Priors into Vision-Language Models for Enhanced Geometric Reasoning

- **评分**：3/10
- **作者/机构**：作者：Chun-Hsiao Yeh, Shengyi Qian, Manchen Wang, Yi Ma, Joseph Tighe, Fanyi Xiao
- **论文链接**：https://arxiv.org/abs/2605.30231
- **PDF**：https://arxiv.org/pdf/2605.30231
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“Beyond 3D VQAs: Injecting 3D Spatial Priors into Vision-Language Models for Enhanced Geometric Reasoning”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🤝 多智能体 / 协作


### [10] Teaching Values to Machines: Simulating Human-Like Behavior in LLMs

- **评分**：4/10
- **作者/机构**：作者：Asaf Yehudai, Naama Rozen, Ariel Gera
- **论文链接**：https://arxiv.org/abs/2605.30036
- **PDF**：https://arxiv.org/pdf/2605.30036
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Teaching Values to Machines: Simulating Human-Like Behavior in LLMs”提出评测/诊断框架，关注 多智能体与协作 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [11] Recovering Diversity Without Losing Alignment: A DPO Recipe for Post-Trained LLMs

- **评分**：4/10
- **作者/机构**：作者：Vinay Samuel, Yapei Chang, Mohit Iyyer
- **论文链接**：https://arxiv.org/abs/2605.30021
- **PDF**：https://arxiv.org/pdf/2605.30021
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文从训练、微调或数据组织角度切入，试图解释或改进“Recovering Diversity Without Losing Alignment: A DPO Recipe for Post-Trained LLMs”所对应的 LLM 能力形成过程。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕数据、微调目标或参数高效训练机制组织方法。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [12] How's it going? Reinforcement learning in language models recruits a functional welfare axis

- **评分**：4/10
- **作者/机构**：作者：Andy Q Han, David J. Chalmers, Pavel Izmailov
- **论文链接**：https://arxiv.org/abs/2605.30232
- **PDF**：https://arxiv.org/pdf/2605.30232
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“How's it going? Reinforcement learning in language models recruits a functional welfare axis”提出评测/诊断框架，关注 LLM训练与对齐 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [13] Double-Edged Sword or Sharp Tool? Designing and Evaluating Triadic LLM-Teacher Collaboration for K-12 Writing at Scale

- **评分**：3/10
- **作者/机构**：作者：Canran Wang, Yuwen Yang, Zhen Wang, Ming Ma, Ding Yu, Chentai Wang, Keman Huang, Xiaoyong Du
- **论文链接**：https://arxiv.org/abs/2605.30200
- **PDF**：https://arxiv.org/pdf/2605.30200
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“Double-Edged Sword or Sharp Tool? Designing and Evaluating Triadic LLM-Teacher Collaboration for K-12 Writing at Scale”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [14] GRUFF: LLM Pronoun Fidelity, Reasoning, and Biases in German

- **评分**：3/10
- **作者/机构**：作者：Fabian Mewes, Anne Lauscher, Vagrant Gautam
- **论文链接**：https://arxiv.org/abs/2605.30214
- **PDF**：https://arxiv.org/pdf/2605.30214
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“GRUFF: LLM Pronoun Fidelity, Reasoning, and Biases in German”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🧪 应用 / Benchmark


### [15] Anchorless Diversification for Parallel LLM Ideation

- **评分**：3/10
- **作者/机构**：作者：Fares Nabil Ibrahim, Nafis Saami Azad, Raiyan Abdul Baten
- **论文链接**：https://arxiv.org/abs/2605.30150
- **PDF**：https://arxiv.org/pdf/2605.30150
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“Anchorless Diversification for Parallel LLM Ideation”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [16] LLUMI: Improving LLM Writing Assistance for Mental Health Support with Online Community Feedback

- **评分**：3/10
- **作者/机构**：作者：Jiwon Kim, Maya Ajit, Sherry Gong, Soorya Ram Shimgekar, Dong Whi Yoo, Eshwar Chandrasekharan, Koustuv Saha
- **论文链接**：https://arxiv.org/abs/2605.30273
- **PDF**：https://arxiv.org/pdf/2605.30273
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
该论文题目指向“LLUMI: Improving LLM Writing Assistance for Mental Health Support with Online Community Feedback”相关问题；本轮网络未能稳定取得摘要/全文，因此这里只做保守纳入，主要供读者按标题快速定位。

**☠️ 毒舌点评**  
信息不足，保守降权：标题相关但缺少可稳定读取的摘要/全文证据，建议读者点进 arXiv 后再判断是否深读。

**🔧 技术方案**  
- **模型架构**：以 LLM 能力分析、应用流程或方法改造为主线。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
当前仅有标题级信息，结果强度未核验。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
