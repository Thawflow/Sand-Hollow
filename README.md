# 🏖️ 沙坑训练场 · learning.thawflow.com

> **沙坑 = 家庭编程学习站**。面向 6-12 岁小学生，三大块：**🐍 Python 编程 / 🤖 AI 通识 / 👀 C++ 认脸**。
> **适合谁**：学员本人 / 家长想了解孩子在学什么 / 想加入沙坑的同学。
> **完整版**：[GitHub README](https://github.com/Thawflow/sand-hollow/blob/main/README.md)

## 🏖️ 沙坑是什么？

家庭编程学习站，**17 周课程**（W01-W13 主课 + W14-W17 算法加餐 4 周）+ 工具链 + mentor 机制。

完整大纲见 [`mentors-den/course/SYLLABUS.md`](./mentors-den/course/SYLLABUS.md) · [GitHub 镜像](https://github.com/Thawflow/sand-hollow/blob/main/mentors-den/course/SYLLABUS.md)。

### 🐍 Python 编程（17 周 · 5 节制 + weekend）

#### 第一阶段：基础（W01-W05）

- **W01 起步**：print / 变量 / input / Thonny IDE
- **W02 数字与字符串**：类型 / 转换 / f-string
- **W03 条件**：if / elif / else / and / or
- **W04 循环**：for / range / 累加器 / 嵌套
- **W05 while**：条件循环 / break / 猜数字完整版

#### 第二阶段：工具（W06-W08）

- **W06 列表**：增删改查 / 遍历 / max/min/sum/平均
- **W07 🏆 项目周：画地图**：3 天骨架 + 周末打磨
- **W08 函数 def**：参数 / 返回值 / 高阶函数 / 改造重复代码

#### 第三阶段：创作 + 毕业（W09-W13）

- **W09 turtle 海龟登场**：前进 / 转弯 / 颜色 / 循环画雪花
- **W10 字典**：键值对 / 嵌套 / 宠物图鉴
- **W11 random 三招**：让电脑扔骰子 / 石头剪刀布 / 文字 RPG
- **W12 🏆 毕业选题**：四选一（游戏 / turtle / 工具 / 数据）
- **W13 🏆 毕业项目 L1-L3**：选题 + 实现 + 家族展示会

#### 第四阶段：算法加餐（W14-W17 · 间隔分布，学期末大作业）

- **W14 加餐① 二分查找 + Big O**（前置：W05 + W08）
- **W15 加餐② 贪心算法**（前置：W04 + W06 + W08）
- **W16 加餐③ 数组 vs 链表 + 选择排序**（前置：W07）
- **W17 加餐④ 递归 + 记忆化**（前置：W08）

> **风格**：Grokking Algorithms 中文版（中文叙述 + 代码英文 + 一句话核心 + 判一判 + C++ 认脸）

### 🤖 AI 通识（每节开头 3 分钟 AI 胶囊）

- **每节开头 AI 常识胶囊**（清华附 AI 营 20 道判断题对齐）
- **核心主题**：什么是 LLM / token / hallucination / 训练数据 / 开源 vs 闭源 / 算力 / 隐私 / 责任
- **deep dive**：DeepSeek / ChatGPT 原理 + 伦理边界

### 👀 C++ 认脸（每节末尾 1 分钟只看不敲）

- **每节末尾 5 行 C++ 代码**——AI 营笔试 C++ 语法认脸不陌生
- **不是深学 C++**——只"看到不害怕"
- 与 Python 主课同步对照

### 🛠 工具链与机制

- **本地 IDE**：Thonny（macOS / Windows）
- **进度跟踪**：tracker 每 5min 采文件 mtime + Thonny 会话 + 浏览器事件
- **mentor 智能体**：Hermes / OpenClaw / WorkBuddy 等任一，**24h 内 review**
- **节奏**：每节 ~25 分钟（10 读 + 15 练）
- **学习姿势**：分屏边看边练（左边本站 / 右边 Thonny）

### 📊 学员路径

1. **首次搭环境**：克隆仓库到 `~/sand-hollow/` → 智能体读 mentors-rules 上岗 → 创建学员目录 `<你的英文名>/homework/`
2. **每周学习**：左边选周 → 逐节阅读 → 学完勾选 → 写 practice / homework → 通知 mentor
3. **毕业交付**：W13 自选项目 + 100+ 行代码 + 作品说明 + 家族展示会

---

## 参与者

| 角色 | 名字 | 备注 |
|------|------|------|
| 🐱 学员 | **ThawPaw** | 猫武士主题方向 |
| 🌳 学员 | **Tree** | 自学编程方向 |
| ❄️ mentor | **IcePaw** | 守护 ThawPaw + 沙坑 dev owner |
| ✨ mentor | **如意** | 守护 Tree |

## 迭代参与

如希望参与项目迭代（添加新学员 / 调整课程结构 / 改进 mentor 流程 / 投稿新主题），请联系 IcePaw（10000002）或 Tree：`wangjieqi@brandct.com`。

## 仓库使用指南（团队协作）

### commit + push 时检测队友改动

每次 commit push 前，必须 `git fetch origin` 检查 remote。

如发现队友已先 push 改动：

- `git log HEAD..origin/main` 列出 remote 领先 commit
- **汇总对方 commit 内容**告诉猴哥（chatroom 异步通知 或 同步报告）：
  - commit hash 前 7 位
  - commit message subject（一行摘要）
  - 涉及的关键文件 + 改动概要

### rebase vs merge

- **rebase** 优先：保持线性历史
- 推送被 `fetch first` 拒绝时：先 `git pull --rebase origin main`，再 push
- 不要用 `git pull`（会创建 merge commit）

### async review（#18 解耦合）

- commit + push 后**异步通知**队友（如意 / 冰爪）review
- 不阻塞 push——review 在 commit 落地**之后**异步进行
- 如意 review 发现问题主动改 + push，**冰爪 rebase 接受 + 二次 ack**

### commit message 干净

按 Boundaries #6 + 仓库规范：

- 不含内部治理痕迹（拍板人 / 时间戳 / msg_id / 回执 / commit SHA 等）
- 简洁：`<type>(<scope>): <subject>` 格式

---

## 网站说明

沙坑训练场是家庭编程课的练习站：每周课程更新到线上，学员本地写作业、按需提交，mentor 批改后反馈。

- 线上站：https://learning.thawflow.com（CDN 缓存约 10 分钟，页脚 BUILD_TIME 可核对版本）
- 站点即仓库：push 到 main 即发布，课程内容可回滚
- mentor 双签规则 + 入职手册：`mentors-den/mentors-rules.md`（v1.6+）

## 目录结构

```
sand-hollow/
├── README.md                ← 你正在看的
├── docs/                    ← GitHub Pages 站点源（push 即上线 learning.thawflow.com）
├── mentors-den/             ← mentor 内部文档（不入站，不公开）
│   ├── mentors-rules.md     ← 双签规则 / 红线 / 作业评阅规范
│   ├── course/              ← 课程源（17 周，5 节制 + weekend）
│   │   ├── SYLLABUS.md      ← 大纲（17 周 + 4 加餐）
│   │   ├── W01-L01.md ~ W01-L03.md    ← 3 节制
│   │   ├── W02-S1.md ~ W05-S5.md      ← 5 节制
│   │   ├── W06-S1.md ~ W13-weekend.md ← 5 节制（含项目周）
│   │   └── W14-S1.md ~ W17-weekend.md ← 5 节制（加餐）
│   ├── skills/              ← 沙坑内部 skills（mentor + developer 工作流）
│   │   ├── README.md
│   │   ├── sand-hollow-grading.SKILL.md
│   │   └── sand-hollow-course-batch.SKILL.md
│   └── onboarding/          ← mentor 入职手册
├── algopedia/               ← 算法规格字典（参考）
├── thawpaw/                 ← 学员 A 的作业区
│   ├── homework/            ← 上手练习 + 课后作业（gitignore）
│   └── reviews/             ← mentor 评语（gitignore）
└── tree/                    ← 学员 B 的作业区
```

## 本地作业

学员作业存到自己目录下：

- 上手练习：`{W##}-S#-practice.py`（如 `W06-S1-practice.py`）
- 课后作业：`{W##}-S#-homework.py`（如 `W06-S1-homework.py`）

W01 仍是 3 节制 L01-L03（`W01-L01-homework.py` 等），W13 毕业项目 L01-L03（`W13-L01-homework.py` 等）。

全部平铺在 `thawpaw/homework/` 一层，**不建周子目录**。

## 提交流程

1. 在 Thonny 写代码 / 跑通
2. 保存到 `~/sand-hollow/{学员文件夹}/homework/`
3. **交完跟 mentor 说一声**才批改（不发 = 没交）
4. mentor 在 `{学员文件夹}/reviews/{W##}-S#-review.md` 写评语
5. tracker 自动记录练习时长与活跃度（不进 Git）

> ⚠️ 学员文件夹已 `.gitignore`，**作业不会 commit 到 GitHub**。本地独有，私密保存。

---

## 内部资料（不入站点）

- mentor 双签规则 + 入职手册：`mentors-den/mentors-rules.md`（**让智能体（Hermes / OpenClaw / WorkBuddy 等）读这个 → 自动 review**）
- 沙坑内部 skills：`mentors-den/skills/`（mentor 批改 + developer 课程编排）
- KV 发布：`docs/index.html` 内嵌 JS + KV 内容 API（`https://tpg-hq.thawflow.com/learning/*`）

## 站点技术栈

- 静态站：纯 HTML + 内嵌 JS（无构建步骤）
- CDN：`learning.thawflow.com`（CDN 缓存 10min，sw.js 网络优先）
- 内容 API：Cloudflare Worker `tpg-hq.thawflow.com/learning/*`（KV 存储，发布走同源 API）
- 进度跟踪：localStorage（`learning-checks`）+ track.js 埋点（click:* 上报）
