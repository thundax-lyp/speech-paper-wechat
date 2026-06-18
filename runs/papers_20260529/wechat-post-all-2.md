---
title: "Agent/LLM论文速递｜2026-05-29｜全量版（2/4）"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-29｜全量版（2/4）：本期收录 16 篇，重点看 RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-29｜全量版（2/4）：本期收录 16 篇，重点看 RAG与知识检索；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-29"
cover_subtitle: "RAG与知识检索"
---

# 📡 Agent/LLM论文速递｜2026-05-29｜全量版（2/4）

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **16** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**0** 篇
- LLM 推理 / 规划 / RAG：**10** 篇
- 评测 / 安全 / 对齐：**5** 篇

这是本期全量收录第 2/4 篇分稿，每篇最多 16 篇，方便在公众号多图文里阅读和转发。全量版保留更多相关论文，但仍建议优先看评分和关键词。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| RAG与知识检索 | 1 | Latent Performance Profiling of Large Language Models | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 2 | Token Inflation: How Dishonest Providers Can Overcharge for Large Language Model Usage | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 3 | Learning to Choose: An Empowerment-Guided Multi-Agent System with semantic communication for Adaptive Method Selection | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 4 | Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 5 | DirectorBench: Diagnosing Long-Form Video Generation with Personalized Multi-Agent Evaluation | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 6 | SEAL: Can Saturated Benchmarks Be Revived by LLM-as-a-Meta-Judge? | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 7 | Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial Chat: A Prominence-Stratified Cross-Provider Audit | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 8 | When Should Models Change Their Minds? Contextual Belief Management in Large Language Models | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 9 | Do Language Models Track Entities Across State Changes? | ⭐ 5/10 | RAG, retrieval, knowledge |
| RAG与知识检索 | 10 | How LoRA Remembers? A Parametric Memory Law for LLM Finetuning | ⭐ 5/10 | RAG, retrieval, knowledge |
| 多智能体与协作 | 1 | Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas | ⭐ 5/10 | multi-agent, collaboration |
| LLM训练与对齐 | 1 | Demystifying Data Organization for Enhanced LLM Training | ⭐ 5/10 | alignment, training |
| 评测与安全 | 1 | Temporal Stability and Few-Shot Prompting in Math Task Assessment | ⭐ 5/10 | evaluation, safety, reliability |
| 评测与安全 | 2 | A Dual-Path Architecture for Scaling Compute and Capacity in LLMs | ⭐ 5/10 | evaluation, safety, reliability |
| 评测与安全 | 3 | Knowing What to Solve Before How: Preplan Empowered LLM Mathematical Reasoning | ⭐ 5/10 | evaluation, safety, reliability |
| 评测与安全 | 4 | VideoFDB: Evaluating Full-Duplex Vision-Speech Capabilities in Conversational Agents | ⭐ 5/10 | evaluation, safety, reliability |

</span>

## 🧠 LLM 推理 / 规划 / RAG


### [1] Latent Performance Profiling of Large Language Models

- **评分**：5/10
- **作者/机构**：作者：Tanmoy Chakraborty, Ayan Sengupta, Suparna Bhattacharya, Partha Pratim Chakrabarti, Amlan Chakrabarti, Supratik Chakraborty, Partha Pratim Das, Lipika Dey, Richa Singh, Mayank Vatsa
- **论文链接**：https://arxiv.org/abs/2605.30018
- **PDF**：https://arxiv.org/pdf/2605.30018
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Latent Performance Profiling of Large Language Models”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [2] Token Inflation: How Dishonest Providers Can Overcharge for Large Language Model Usage

- **评分**：5/10
- **作者/机构**：作者：Shahinul Hoque, Jinghuai Zhang, Jinyuan Sun, Fnu Suya
- **论文链接**：https://arxiv.org/abs/2605.30040
- **PDF**：https://arxiv.org/pdf/2605.30040
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文聚焦“Token Inflation: How Dishonest Providers Can Overcharge for Large Language Model Usage”，从 RAG与知识检索 角度研究大模型能力、应用或风险边界。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [3] Learning to Choose: An Empowerment-Guided Multi-Agent System with semantic communication for Adaptive Method Selection

- **评分**：5/10
- **作者/机构**：作者：Geremy Loachamín-Suntaxi, Robert Lazar, Dimitrios G. Giovanis, Ioannis G. Kevrekidis, Eleni D. Koronaki
- **论文链接**：https://arxiv.org/abs/2605.30042
- **PDF**：https://arxiv.org/pdf/2605.30042
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Learning to Choose: An Empowerment-Guided Multi-Agent System with semantic communication for Adaptive Method Selection”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [4] Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison

- **评分**：5/10
- **作者/机构**：作者：Tiancheng Yang, Matthias Schonlau, Ilia Sucholutsky
- **论文链接**：https://arxiv.org/abs/2605.30087
- **PDF**：https://arxiv.org/pdf/2605.30087
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [5] DirectorBench: Diagnosing Long-Form Video Generation with Personalized Multi-Agent Evaluation

- **评分**：5/10
- **作者/机构**：作者：Jiamin Chen, Qianben Chen, Jiawen Zhang, Yidi Wu, Yuchen Li, Xiaokun Zhang, Wangchunshu Zhou, Chen Ma
- **论文链接**：https://arxiv.org/abs/2605.30090
- **PDF**：https://arxiv.org/pdf/2605.30090
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“DirectorBench: Diagnosing Long-Form Video Generation with Personalized Multi-Agent Evaluation”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [6] SEAL: Can Saturated Benchmarks Be Revived by LLM-as-a-Meta-Judge?

- **评分**：5/10
- **作者/机构**：作者：Jiamin Chen, Yidi Wu, Qiexiang Wang, Qianben Chen, Yuchen Li, Yansen Zhang, Xiaokun Zhang, Wangchunshu Zhou, Chen Ma
- **论文链接**：https://arxiv.org/abs/2605.30104
- **PDF**：https://arxiv.org/pdf/2605.30104
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“SEAL: Can Saturated Benchmarks Be Revived by LLM-as-a-Meta-Judge?”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [7] Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial Chat: A Prominence-Stratified Cross-Provider Audit

- **评分**：5/10
- **作者/机构**：作者：Will Jack, Noah Lehman, Keller Maloney, Sarah Xu
- **论文链接**：https://arxiv.org/abs/2605.30207
- **PDF**：https://arxiv.org/pdf/2605.30207
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文从训练、微调或数据组织角度切入，试图解释或改进“Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial Chat: A Prominence-Stratified Cross-Provider Audit”所对应的 LLM 能力形成过程。

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


### [8] When Should Models Change Their Minds? Contextual Belief Management in Large Language Models

- **评分**：5/10
- **作者/机构**：作者：Haoming Xu, Weihong Xu, Zongrui Li, Mengru Wang, Yunzhi Yao, Chiyu Wu, Jin Shang, Yu Gong, Shumin Deng
- **论文链接**：https://arxiv.org/abs/2605.30219
- **PDF**：https://arxiv.org/pdf/2605.30219
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“When Should Models Change Their Minds? Contextual Belief Management in Large Language Models”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [9] Do Language Models Track Entities Across State Changes?

- **评分**：5/10
- **作者/机构**：作者：Zilu Tang, Qiao Zhao, Gabriel Franco, Derry Wijaya, Aaron Mueller, Sebastian Schuster, Najoung Kim
- **论文链接**：https://arxiv.org/abs/2605.30233
- **PDF**：https://arxiv.org/pdf/2605.30233
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Do Language Models Track Entities Across State Changes?”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：围绕检索、上下文组装和答案生成链路设计，关注知识源选择与冲突处理。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [10] How LoRA Remembers? A Parametric Memory Law for LLM Finetuning

- **评分**：5/10
- **作者/机构**：作者：Ziwen Xu, Haiwen Hong, Linsong Yu, Benglei Cui, Longtao Huang, Hui Xue, Ningyu Zhang
- **论文链接**：https://arxiv.org/abs/2605.30260
- **PDF**：https://arxiv.org/pdf/2605.30260
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“How LoRA Remembers? A Parametric Memory Law for LLM Finetuning”提出评测/诊断框架，关注 RAG与知识检索 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：围绕记忆表示、选择或更新策略提出机制化分析。  
- **训练 / 推理策略**：涉及训练、微调、偏好优化或强化学习设置。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 🤝 多智能体 / 协作


### [11] Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas

- **评分**：5/10
- **作者/机构**：作者：Víctor Gallego
- **论文链接**：https://arxiv.org/abs/2605.30003
- **PDF**：https://arxiv.org/pdf/2605.30003
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Discovering Cooperative Pipelines: Autoresearch for Sequential Social Dilemmas”提出评测/诊断框架，关注 多智能体与协作 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以多个 LLM/专业组件之间的通信、路由或协作为核心结构。  
- **核心创新**：主要新意来自问题设定、系统化分析或面向特定场景的方法组合。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## ⚙️ LLM 训练 / 对齐


### [12] Demystifying Data Organization for Enhanced LLM Training

- **评分**：5/10
- **作者/机构**：作者：Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang, Wenshan Wu, Qihao Zhao, Hao Li, Yuanyuan Gao, Kim-Hui Yap, Scarlett Li
- **论文链接**：https://arxiv.org/abs/2605.30334
- **PDF**：https://arxiv.org/pdf/2605.30334
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
论文从训练、微调或数据组织角度切入，试图解释或改进“Demystifying Data Organization for Enhanced LLM Training”所对应的 LLM 能力形成过程。

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

## 🛡️ 评测 / 安全 / 可靠性


### [13] Temporal Stability and Few-Shot Prompting in Math Task Assessment

- **评分**：5/10
- **作者/机构**：作者：Danielle S. Fox, Brenda L. Robles, Elizabeth DiPietro Brovey, Christian D. Schunn
- **论文链接**：https://arxiv.org/abs/2605.30151
- **PDF**：https://arxiv.org/pdf/2605.30151
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Temporal Stability and Few-Shot Prompting in Math Task Assessment”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [14] A Dual-Path Architecture for Scaling Compute and Capacity in LLMs

- **评分**：5/10
- **作者/机构**：作者：Markus Frey, Behzad Shomali, Joachim Koehler, Mehdi Ali
- **论文链接**：https://arxiv.org/abs/2605.30202
- **PDF**：https://arxiv.org/pdf/2605.30202
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“A Dual-Path Architecture for Scaling Compute and Capacity in LLMs”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

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


### [15] Knowing What to Solve Before How: Preplan Empowered LLM Mathematical Reasoning

- **评分**：5/10
- **作者/机构**：作者：Shaojie Wang, Liang Zhang
- **论文链接**：https://arxiv.org/abs/2605.30245
- **PDF**：https://arxiv.org/pdf/2605.30245
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“Knowing What to Solve Before How: Preplan Empowered LLM Mathematical Reasoning”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---


### [16] VideoFDB: Evaluating Full-Duplex Vision-Speech Capabilities in Conversational Agents

- **评分**：5/10
- **作者/机构**：作者：Amrita Mazumdar, Seonwook Park, Rajarshi Roy, Nikhil Srihari, Shengze Wang, Yuhao Zhou, Julia Wang, Koki Nagano, Shalini De Mello
- **论文链接**：https://arxiv.org/abs/2605.30256
- **PDF**：https://arxiv.org/pdf/2605.30256
- **代码链接**：

<span style="font-size: 14px;">

**📌 简介**  
这篇工作围绕“VideoFDB: Evaluating Full-Duplex Vision-Speech Capabilities in Conversational Agents”提出评测/诊断框架，关注 评测与安全 场景下模型能力、稳定性或偏差如何被更细粒度地暴露。

**☠️ 毒舌点评**  
相关性明确但优先级中等：适合作为本方向补充阅读，重点价值在场景、指标或工程经验，是否能迁移到通用 Agent/LLM 系统还需要看正文实验细节。

**🔧 技术方案**  
- **模型架构**：以任务集、指标、模型对比和诊断维度构成评测架构。  
- **核心创新**：提出新的诊断基准或评测切片，用来暴露现有指标看不到的能力差异。  
- **训练 / 推理策略**：未从当前可读信息看到大规模训练细节，更多是系统、评测或应用层研究。

**📊 实验结果**  
作者报告了相应实验、案例或评测结果；具体数值和消融建议读正文核对。

**💡 为什么值得看**  
全量收录：相关但优先级低于精选候选。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
