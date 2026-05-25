---
title: "Agent/LLM论文速递｜2026-05-25｜全量版"
author: "Thundax"
summary: "Agent/LLM论文速递｜2026-05-25｜全量版：本期收录 45 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
description: "Agent/LLM论文速递｜2026-05-25｜全量版：本期收录 45 篇，重点看 Agent系统与工具使用；优先关注真系统、真评测、真能力边界，不看纯花活。"
cover_text: "Agent/LLM论文速递｜2026-05-25"
cover_subtitle: "Agent系统与工具使用"
---

# 📡 Agent/LLM论文速递｜2026-05-25｜全量版

> 数据源：arXiv `cs.AI` / `cs.CL` / `cs.MA` 当日新投稿  
> 过滤：只保留 Agent / LLM / 多智能体相关论文  
> 视角：按 NeurIPS / ICML / ICLR / ACL 审稿口径做毒舌评审

## 📋 总览

- 共收录 **45** 篇 Agent / LLM 相关论文
- Agent 系统 / 工具使用：**12** 篇
- LLM 推理 / 规划 / RAG：**10** 篇
- 评测 / 安全 / 对齐：**10** 篇

这篇是过滤后的完整收录版。只要属于当天 Agent / LLM 覆盖范围，就都列进来，方便重度读者系统扫稿和后续检索。

### 总览表

<span style="font-size: 13px;">

| 方向 | 序号 | 论文 | 评分 | 关键词 |
|---|---:|---|---|---|
| Agent系统与工具使用 | 1 | SkillOpt: Executive Strategy for Self-Evolving Agent Skills | ⭐ 9/10 | agent |
| Agent系统与工具使用 | 2 | EVE-Agent: Evidence-Verifiable Self-Evolving Agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 3 | DART: Semantic Recoverability for Structured Tool Agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 4 | Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 5 | Agentic Proving for Program Verification | ⭐ 8/10 | agent |
| Agent系统与工具使用 | 6 | Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 7 | From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills | ⭐ 7/10 | agent |
| Agent系统与工具使用 | 8 | 6G Communication Networks Enabling Embodied Agents: Architecture and Prototype | ⭐ 6/10 | agent |
| Agent系统与工具使用 | 9 | Goal-Conditioned Agents that Learn Everything All at Once | ⭐ 6/10 | agent |
| Agent系统与工具使用 | 10 | Structure-Guided Entity Resolution: Fine-Tuning LLMs for Robust Name Matching in Complex Linguistic Contexts | ⭐ 6/10 | LLM |
| Agent系统与工具使用 | 11 | One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents | ⭐ 6/10 | agent |
| Agent系统与工具使用 | 12 | PhotoFlow: Agentic 3D Virtual Photography Missions | ⭐ 6/10 | agent |
| LLM推理与规划 | 1 | RMA: an Agentic System for Research-Level Mathematical Problems | ⭐ 8/10 | agent |
| LLM推理与规划 | 2 | GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models | ⭐ 8/10 | reasoning |
| RAG与知识检索 | 1 | Parallel Context Compaction for Long-Horizon LLM Agent Serving | ⭐ 8/10 | agent, LLM |
| RAG与知识检索 | 2 | A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification | ⭐ 6/10 | agent |
| RAG与知识检索 | 3 | What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA | ⭐ 6/10 | agent, memory |
| RAG与知识检索 | 4 | When Is Next-Token Prediction Useful? Marginalization, Ergodicity, Mixture Identifiability, Local Sufficiency, RAG, Tools, and Programming | ⭐ 6/10 | RAG |
| LLM推理与规划 | 3 | Convergence Without Understanding: When Language Models Agree on Representations but Disagree on Reasoning | ⭐ 6/10 | reasoning |
| RAG与知识检索 | 5 | Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals | ⭐ 6/10 | LLM, reasoning |
| RAG与知识检索 | 6 | PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide Image VQA | ⭐ 6/10 | agent, memory |
| RAG与知识检索 | 7 | Leveraging Foundation Models for Causal Generative Modeling | ⭐ 6/10 | RAG |
| 多智能体与协作 | 1 | Foundation Protocol: A Coordination Layer for Agentic Society | ⭐ 8/10 | agent |
| 多智能体与协作 | 2 | How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning | ⭐ 7/10 | agent, LLM, multi-agent, planning |
| 多智能体与协作 | 3 | Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning | ⭐ 7/10 | agent, multi-agent |
| 多智能体与协作 | 4 | SVR-MAD: A Bayesian-Inspired Framework for Posterior-Guided Multi-Agent Debate | ⭐ 6/10 | agent, multi-agent |
| 多智能体与协作 | 5 | CultivAgents: Cultivating Relationship-Centered Multi-Agent Systems for Personalized Gardening | ⭐ 6/10 | agent, multi-agent |
| 多智能体与协作 | 6 | Self-Refining Topology Optimization via an LLM-Based Multi-Agent Framework | ⭐ 6/10 | agent, LLM, multi-agent |
| 多智能体与协作 | 7 | When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems | ⭐ 6/10 | agent, LLM, multi-agent, planning |
| 多智能体与协作 | 8 | ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning | ⭐ 6/10 | agent, multi-agent |
| 多智能体与协作 | 9 | CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces | ⭐ 6/10 | agent, multi-agent |
| 评测与安全 | 1 | PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs | ⭐ 8/10 | LLM, benchmark |
| 评测与安全 | 2 | Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks | ⭐ 8/10 | LLM, reasoning, benchmark |
| 评测与安全 | 3 | Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks | ⭐ 8/10 | LLM, benchmark |
| 评测与安全 | 4 | Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems | ⭐ 8/10 | RAG, benchmark |
| 评测与安全 | 5 | ChartFI: Benchmarking Faithfulness and Insightfulness of Chart Descriptions from Multimodal Large Language Models | ⭐ 8/10 | benchmark |
| 评测与安全 | 6 | MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection | ⭐ 8/10 | agent, memory |
| 评测与安全 | 7 | How Human-Like Are Large Language Models? A Register-Aware Linguistic Evaluation Framework | ⭐ 7/10 | evaluation |
| 评测与安全 | 8 | It's the humans, not the data: Geopolitical bias in LLMs originates in post-training, amplified by the language of the prompt | ⭐ 7/10 | LLM |
| 评测与安全 | 9 | Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystems | ⭐ 6/10 | agent |
| 评测与安全 | 10 | OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents | ⭐ 6/10 | agent, LLM |
| 应用与基准 | 1 | The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management | ⭐ 7/10 | LLM |
| 应用与基准 | 2 | Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection | ⭐ 7/10 | LLM |
| 应用与基准 | 3 | Can AI Guess What You Know? Performance Comparison of Large Language Models for Human Domain Knowledge Estimation From Communication Logs | ⭐ 6/10 | RAG与知识检索 |
| 应用与基准 | 4 | Human Decision-Making with Persuasive and Narrative LLM Explanations | ⭐ 6/10 | LLM |

</span>

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


### [2] EVE-Agent: Evidence-Verifiable Self-Evolving Agents

- **评分**：8/10
- **作者/机构**：Yamato Arai；Yuma Ichikawa
- **论文链接**：https://arxiv.org/abs/2605.22905
- **PDF**：https://arxiv.org/pdf/2605.22905
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「EVE-Agent: Evidence-Verifiable Self-Evolving Agents」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 Agent系统与工具使用 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [3] DART: Semantic Recoverability for Structured Tool Agents

- **评分**：8/10
- **作者/机构**：Ke Yang；Panpan Li；Zonghan Wu；Kejin Xu；Huaxi Huang；Xiaoshui Huang
- **论文链接**：https://arxiv.org/abs/2605.23311
- **PDF**：https://arxiv.org/pdf/2605.23311
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「DART: Semantic Recoverability for Structured Tool Agents」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 Agent系统与工具使用 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [4] Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

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


### [5] Agentic Proving for Program Verification

- **评分**：8/10
- **作者/机构**：Alessandro Sosso；Akhil Arora；Bas Spitters
- **论文链接**：https://arxiv.org/abs/2605.23772
- **PDF**：https://arxiv.org/pdf/2605.23772
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Agentic Proving for Program Verification」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 Agent系统与工具使用 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [6] Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness

- **评分**：7/10
- **作者/机构**：Manish Aryal；Faiyaz Azam；Agnivo Banerjee；Sai Sidhanth Manoharan Jayanthi；Allegra Laro；Clément Legentilhomme；Andrew Lin；Florian Lorkowski；Radman Rakhshandehroo；Patric Rommel；Emanuel Ruzak；Nathan Theng；Paul Yushin Rapoport
- **论文链接**：https://arxiv.org/abs/2605.23146
- **PDF**：https://arxiv.org/pdf/2605.23146
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

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


### [7] From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

- **评分**：7/10
- **作者/机构**：Zisu Huang；Jingwen Xu；Yifan Yang；Ziyang Gong；Qihao Yang；Muzhao Tian；Xiaohua Wang；Changze Lv；Xuemei Gao；Qi Dai；Bei Liu；Kai Qiu；Xue Yang；Dongdong Chen；Xiaoqing Zheng；Chong Luo
- **论文链接**：https://arxiv.org/abs/2605.23899
- **PDF**：https://arxiv.org/pdf/2605.23899
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

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


### [8] 6G Communication Networks Enabling Embodied Agents: Architecture and Prototype

- **评分**：6/10
- **作者/机构**：Lipeng Dai；Luping Xiang；Kun Yang
- **论文链接**：https://arxiv.org/abs/2605.23263
- **PDF**：https://arxiv.org/pdf/2605.23263
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「6G Communication Networks Enabling Embodied Agents: Architecture and Prototype」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 Agent系统与工具使用 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [9] Goal-Conditioned Agents that Learn Everything All at Once

- **评分**：6/10
- **作者/机构**：Michael Matthews；Matthew Jackson；Michael Beukman；Thomas Foster；Alistair Letcher；Scott Fujimoto；Cédric Colas；Jakob Foerster
- **论文链接**：https://arxiv.org/abs/2605.23551
- **PDF**：https://arxiv.org/pdf/2605.23551
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Goal-Conditioned Agents that Learn Everything All at Once」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 Agent系统与工具使用 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [10] Structure-Guided Entity Resolution: Fine-Tuning LLMs for Robust Name Matching in Complex Linguistic Contexts

- **评分**：6/10
- **作者/机构**：Shivam Chourasia；Hitesh Kapoor；Nilesh Patil
- **论文链接**：https://arxiv.org/abs/2605.23597
- **PDF**：https://arxiv.org/pdf/2605.23597
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Structure-Guided Entity Resolution: Fine-Tuning LLMs for Robust Name Matching in Complex Linguistic Contexts」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 Agent系统与工具使用 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [11] One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents

- **评分**：6/10
- **作者/机构**：Yoosung Hong
- **论文链接**：https://arxiv.org/abs/2605.23652
- **PDF**：https://arxiv.org/pdf/2605.23652
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 Agent系统与工具使用 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [12] PhotoFlow: Agentic 3D Virtual Photography Missions

- **评分**：6/10
- **作者/机构**：Jiarui Guo；Haojia Wei；Yiming Zhang；Yifei Liu；Yuning Gong；Hongjie Zhang；Xue Yang；Zhihang Zhong
- **论文链接**：https://arxiv.org/abs/2605.23771
- **PDF**：https://arxiv.org/pdf/2605.23771
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「PhotoFlow: Agentic 3D Virtual Photography Missions」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 Agent系统与工具使用 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [13] RMA: an Agentic System for Research-Level Mathematical Problems

- **评分**：8/10
- **作者/机构**：Zelin Zhao；Bo Yuan；Jaemoo Choi；Yongxin Chen
- **论文链接**：https://arxiv.org/abs/2605.22875
- **PDF**：https://arxiv.org/pdf/2605.22875
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「RMA: an Agentic System for Research-Level Mathematical Problems」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 LLM推理与规划 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [14] GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models

- **评分**：8/10
- **作者/机构**：Vartan Shadarevian；Kia Ghods；Alex Kenich；Anany Kotawala
- **论文链接**：https://arxiv.org/abs/2605.23238
- **PDF**：https://arxiv.org/pdf/2605.23238
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 LLM推理与规划 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [15] Parallel Context Compaction for Long-Horizon LLM Agent Serving

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


### [16] A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification

- **评分**：6/10
- **作者/机构**：Joshua Odmark；Gideon Rubin；Deon van der Vyver
- **论文链接**：https://arxiv.org/abs/2605.23058
- **PDF**：https://arxiv.org/pdf/2605.23058
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 RAG与知识检索 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [17] What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA

- **评分**：6/10
- **作者/机构**：Xinjie He；Zhiyuan Lin；Su Liu；Jialun Wu；Qiyang Xie；Weikai Zhou；Shuai Xiao
- **论文链接**：https://arxiv.org/abs/2605.23067
- **PDF**：https://arxiv.org/pdf/2605.23067
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 RAG与知识检索 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [18] When Is Next-Token Prediction Useful? Marginalization, Ergodicity, Mixture Identifiability, Local Sufficiency, RAG, Tools, and Programming

- **评分**：6/10
- **作者/机构**：Francesco Corielli
- **论文链接**：https://arxiv.org/abs/2605.23278
- **PDF**：https://arxiv.org/pdf/2605.23278
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「When Is Next-Token Prediction Useful? Marginalization, Ergodicity, Mixture Identifiability, Local Sufficiency, RAG, Tools, and Programming」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 RAG与知识检索 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [19] Convergence Without Understanding: When Language Models Agree on Representations but Disagree on Reasoning

- **评分**：6/10
- **作者/机构**：Muhammad Usama；Dong Eui Chang
- **论文链接**：https://arxiv.org/abs/2605.23315
- **PDF**：https://arxiv.org/pdf/2605.23315
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Convergence Without Understanding: When Language Models Agree on Representations but Disagree on Reasoning」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 LLM推理与规划 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [20] Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals

- **评分**：6/10
- **作者/机构**：Sirui Chen；Lei Xu；Yuying Zhao；Yutian Chen；Yu Wang；Beier Zhu；Hanwang Zhang；Shengjie Zhao；Chaochao Lu
- **论文链接**：https://arxiv.org/abs/2605.23384
- **PDF**：https://arxiv.org/pdf/2605.23384
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 RAG与知识检索 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [21] PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide Image VQA

- **评分**：6/10
- **作者/机构**：Chunze Yang；Qidong Liu；Wenjie Zhao；Yue Tang；Jiusong Ge；Di Zhang；Jiashuai Liu；Lei Wu；Junbo Lu；Ni Zhang；Xian Wu；Zeyu Gao；Chen Li
- **论文链接**：https://arxiv.org/abs/2605.23559
- **PDF**：https://arxiv.org/pdf/2605.23559
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide Image VQA」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 RAG与知识检索 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [22] Leveraging Foundation Models for Causal Generative Modeling

- **评分**：6/10
- **作者/机构**：Aneesh Komanduri；Xintao Wu
- **论文链接**：https://arxiv.org/abs/2605.23861
- **PDF**：https://arxiv.org/pdf/2605.23861
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Leveraging Foundation Models for Causal Generative Modeling」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 RAG与知识检索 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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

## 🤝 多智能体 / 协作


### [23] Foundation Protocol: A Coordination Layer for Agentic Society

- **评分**：8/10
- **作者/机构**：Bang Liu；Yongfeng Gu；Jiayi Zhang；Zhaoyang Yu；Sirui Hong；Maojia Song；Xiaoqiang Wang；Mingyi Deng；Zijie Zhuang；Ronghao Wang；Mingzhe Cao；Yutong Zhu；Xingjian Li；Yifan Wu；Jianhao Ruan；Yiran Peng；Shuangrui Chen；Jinlin Wang；Yizhang Lin；Dongjie Zhang；Dekun Wu；Chen Ma；Lizi Liao；Han Yu；Jian Pei；Heng Ji；Qiang Yang；Yuyu Luo；Chenglin Wu
- **论文链接**：https://arxiv.org/abs/2605.23218
- **PDF**：https://arxiv.org/pdf/2605.23218
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Foundation Protocol: A Coordination Layer for Agentic Society」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 多智能体与协作 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [24] How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning

- **评分**：7/10
- **作者/机构**：Zeyu He；Hannah Kim；Dan Zhang；Estevam Hruschka
- **论文链接**：https://arxiv.org/abs/2605.23023
- **PDF**：https://arxiv.org/pdf/2605.23023
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [25] Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning

- **评分**：7/10
- **作者/机构**：Sijia Li；Xiaoyu Tan；Qixing Wang；Weiyi Zhao；Chen Zhan；Teqi Hao；Xuemin Wang；Lei Gu；Roland Eils；Xihe Qiu
- **论文链接**：https://arxiv.org/abs/2605.23320
- **PDF**：https://arxiv.org/pdf/2605.23320
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [26] SVR-MAD: A Bayesian-Inspired Framework for Posterior-Guided Multi-Agent Debate

- **评分**：6/10
- **作者/机构**：Weifan Jiang；Rana Shahout；Minghao Li；Zhenting Qi；Yilun Du；Michael Mitzenmacher；Minlan Yu
- **论文链接**：https://arxiv.org/abs/2605.23099
- **PDF**：https://arxiv.org/pdf/2605.23099
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「SVR-MAD: A Bayesian-Inspired Framework for Posterior-Guided Multi-Agent Debate」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 多智能体与协作 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [27] CultivAgents: Cultivating Relationship-Centered Multi-Agent Systems for Personalized Gardening

- **评分**：6/10
- **作者/机构**：Yiyang Wang；Moeiini Reilly；Britney Johnson；Kefei Yan；Alex Cabral；Josiah Hester
- **论文链接**：https://arxiv.org/abs/2605.23193
- **PDF**：https://arxiv.org/pdf/2605.23193
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「CultivAgents: Cultivating Relationship-Centered Multi-Agent Systems for Personalized Gardening」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 多智能体与协作 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [28] Self-Refining Topology Optimization via an LLM-Based Multi-Agent Framework

- **评分**：6/10
- **作者/机构**：Hyunjee Park；Hayoung Chung
- **论文链接**：https://arxiv.org/abs/2605.23273
- **PDF**：https://arxiv.org/pdf/2605.23273
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Self-Refining Topology Optimization via an LLM-Based Multi-Agent Framework」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 多智能体与协作 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [29] When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems

- **评分**：6/10
- **作者/机构**：Zehao Wang；Shilong Jin；Zhao Cao；Lanjun Wang
- **论文链接**：https://arxiv.org/abs/2605.23414
- **PDF**：https://arxiv.org/pdf/2605.23414
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 多智能体与协作 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [30] ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning

- **评分**：6/10
- **作者/机构**：Elie Abboud；Oren Gal
- **论文链接**：https://arxiv.org/abs/2605.23562
- **PDF**：https://arxiv.org/pdf/2605.23562
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 多智能体与协作 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---


### [31] CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces

- **评分**：6/10
- **作者/机构**：Joydeep Chandra
- **论文链接**：https://arxiv.org/abs/2605.23887
- **PDF**：https://arxiv.org/pdf/2605.23887
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 多智能体与协作 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：由多个 Agent/角色/策略共同完成任务，核心在协调机制、通信协议或群体行为评估。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 多智能体与协作 的读者快速判断是否加入精读列表。

</span>

---

## 🛡️ 评测 / 安全 / 可靠性


### [32] PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs

- **评分**：8/10
- **作者/机构**：Luze Sun；Anshuman Suri；Harsh Chaudhari；Cristina Nita-Rotaru；Alina Oprea
- **论文链接**：https://arxiv.org/abs/2605.23168
- **PDF**：https://arxiv.org/pdf/2605.23168
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 评测与安全 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [33] Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks

- **评分**：8/10
- **作者/机构**：Chuyifei Zhang；Hongyu Cui；Xiaowen Huang；Jitao Sang
- **论文链接**：https://arxiv.org/abs/2605.23170
- **PDF**：https://arxiv.org/pdf/2605.23170
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 评测与安全 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [34] Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks

- **评分**：8/10
- **作者/机构**：Vivek Dahiya；Sunny Nehra；Vipul Dholariya；Bhavik Shangari；Chandra Khatri
- **论文链接**：https://arxiv.org/abs/2605.23243
- **PDF**：https://arxiv.org/pdf/2605.23243
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 评测与安全 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [35] Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems

- **评分**：8/10
- **作者/机构**：Stefano Cirillo；Domenico Desiato；Giuseppe Polese；Giandomenico Solimando
- **论文链接**：https://arxiv.org/abs/2605.23618
- **PDF**：https://arxiv.org/pdf/2605.23618
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 评测与安全 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [36] ChartFI: Benchmarking Faithfulness and Insightfulness of Chart Descriptions from Multimodal Large Language Models

- **评分**：8/10
- **作者/机构**：Fen Wang；Zekai Shao；Qiman Kang；Chunran Hu；Zhixuan Zhang；Lexu Xie；Chao Liu；Siming Chen
- **论文链接**：https://arxiv.org/abs/2605.23694
- **PDF**：https://arxiv.org/pdf/2605.23694
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「ChartFI: Benchmarking Faithfulness and Insightfulness of Chart Descriptions from Multimodal Large Language Models」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
值得优先扫读。它抓住了 评测与安全 里比较硬的问题，标题和摘要都显示有明确系统设定或评测目标；真正要追的是实验是否覆盖真实失败模式，而不是只展示顺滑 demo。

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


### [37] MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

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


### [38] How Human-Like Are Large Language Models? A Register-Aware Linguistic Evaluation Framework

- **评分**：7/10
- **作者/机构**：Björn Nieth；Marianna Gracheva；Michaela Mahlberg；Bjoern Eskofier；Emmanuelle Salin
- **论文链接**：https://arxiv.org/abs/2605.23651
- **PDF**：https://arxiv.org/pdf/2605.23651
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「How Human-Like Are Large Language Models? A Register-Aware Linguistic Evaluation Framework」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

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


### [39] It's the humans, not the data: Geopolitical bias in LLMs originates in post-training, amplified by the language of the prompt

- **评分**：7/10
- **作者/机构**：Stuart Bladon；Brinnae Bent
- **论文链接**：https://arxiv.org/abs/2605.23825
- **PDF**：https://arxiv.org/pdf/2605.23825
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「It's the humans, not the data: Geopolitical bias in LLMs originates in post-training, amplified by the language of the prompt」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

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


### [40] Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystems

- **评分**：6/10
- **作者/机构**：Muhammad Zia Hydari；Farooq Muzaffar
- **论文链接**：https://arxiv.org/abs/2605.23179
- **PDF**：https://arxiv.org/pdf/2605.23179
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystems」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 评测与安全 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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


### [41] OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents

- **评分**：6/10
- **作者/机构**：Jiahao Ying；Boxian Ai；Wei Tang；Siyuan Liu；Yixin Cao
- **论文链接**：https://arxiv.org/abs/2605.23657
- **PDF**：https://arxiv.org/pdf/2605.23657
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 评测与安全 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

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

## 🧪 应用 / Benchmark


### [42] The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management

- **评分**：7/10
- **作者/机构**：Binqi Shen；Lier Jin；Hanyu Cai；Lan Hu；Yuting Xin
- **论文链接**：https://arxiv.org/abs/2605.23071
- **PDF**：https://arxiv.org/pdf/2605.23071
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

**🔧 技术方案**  
- **模型架构**：面向具体应用或基准任务组织 LLM 能力，重点看任务定义和评估是否扎实。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 应用与基准 的读者快速判断是否加入精读列表。

</span>

---


### [43] Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection

- **评分**：7/10
- **作者/机构**：Kieu Dang；Phung Lai；NhatHai Phan；Yelong Shen；Ruoming Jin
- **论文链接**：https://arxiv.org/abs/2605.23175
- **PDF**：https://arxiv.org/pdf/2605.23175
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
可以进精选候选。方向贴近 Agent/LLM 主线，问题意识清楚；但还需要看全文里的基线、消融和错误分析，判断是不是能从概念稿走到可复现结论。

**🔧 技术方案**  
- **模型架构**：面向具体应用或基准任务组织 LLM 能力，重点看任务定义和评估是否扎实。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 应用与基准 的读者快速判断是否加入精读列表。

</span>

---


### [44] Can AI Guess What You Know? Performance Comparison of Large Language Models for Human Domain Knowledge Estimation From Communication Logs

- **评分**：6/10
- **作者/机构**：Ko Watanabe；Shoya Ishimaru
- **论文链接**：https://arxiv.org/abs/2605.22971
- **PDF**：https://arxiv.org/pdf/2605.22971
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Can AI Guess What You Know? Performance Comparison of Large Language Models for Human Domain Knowledge Estimation From Communication Logs」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
偏 LLM 应用评估，和 Agent 主线有距离，适合全量收录但不进精选。

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


### [45] Human Decision-Making with Persuasive and Narrative LLM Explanations

- **评分**：6/10
- **作者/机构**：Laura R. Marusich；Mary Grace Kozuch Dhooghe；Jonathan Z. Bakdash；Murat Kantarcioglu
- **论文链接**：https://arxiv.org/abs/2605.23867
- **PDF**：https://arxiv.org/pdf/2605.23867
- **代码链接**：暂无

<span style="font-size: 14px;">

**📌 简介**  
这篇围绕「Human Decision-Making with Persuasive and Narrative LLM Explanations」展开，核心问题是把 Agent/LLM 能力从单次生成推进到更可控的系统、评测或任务流程；从摘要看，论文重点在方法设计与实验验证，而不是单纯应用包装。英文摘要要点：

**☠️ 毒舌点评**  
相关但不必第一时间精读。它对 应用与基准 读者有检索价值，不过从元数据看更像局部改进或应用型工作，建议按具体需求再深入。

**🔧 技术方案**  
- **模型架构**：面向具体应用或基准任务组织 LLM 能力，重点看任务定义和评估是否扎实。  
- **核心创新**：主要新意来自问题设定、系统编排或评测视角；需要结合全文实验确认贡献边界。  
- **训练 / 推理策略**：从元数据看不一定训练新基座模型；多数工作更偏系统、推理流程、评测或任务适配。

**📊 实验结果**  
摘要显示包含实验或案例验证；具体数值、基线和消融建议阅读 PDF 后再做最终判断。

**💡 为什么值得看**  
适合关注 应用与基准 的读者快速判断是否加入精读列表。

</span>

---

## 结语

今天这批论文里，真正值得继续追的是两类：

- **能落地的 Agent 系统**：有真实任务、真实工具链、真实失败分析
- **能解释 LLM 能力边界的工作**：不是只在熟 benchmark 上刷一点数字

按 ML / NLP 顶会标尺，真正能拿高分的稿子本来就不会很多。如果只想选一篇精读，优先看今天评分最高那篇。
