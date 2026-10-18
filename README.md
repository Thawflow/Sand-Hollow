# 🏖️ 沙坑训练场 · learning.thawflow.com

> **沙坑 = 家庭编程学习站**。面向 6-12 岁小学生，三大块：**🐍 Python 编程 / 🤖 AI 通识 / 👀 C++ 认脸**。
> **适合谁**：学员本人 / 家长想了解孩子在学什么 / 想加入沙坑的同学。
> **完整版**：[GitHub README](https://github.com/Thawflow/Sand-Hollow/blob/main/README.md)（含详细参与者、目录结构、本地作业、提交流程、cron 模板、技术栈）

## 🏖️ 沙坑是什么？

家庭编程学习站，三大块内容 + 工具链 + mentor 机制。完整大纲见 [`mentors-den/course/SYLLABUS.md`](./mentors-den/course/SYLLABUS.md) · [GitHub 镜像](https://github.com/Thawflow/Sand-Hollow/blob/main/mentors-den/course/SYLLABUS.md)。

### 🐍 Python 编程（W01 - W13 · 13 周主课）

- **W01 起步**：print / 变量 / input / Thonny IDE
- **W02 数字与字符串**：类型 / 转换 / f-string
- **W03 条件**：if / elif / else / and / or
- **W04 循环**：for / range / 累加器 / 嵌套
- **W05 while**：条件循环 / break / 猜数字完整版
- **W06 列表**：增删改查 / 遍历 / max/min/sum/平均
- **W07 🏆 项目周「猫咪冒险岛」**：用上 W01-W06 全部功夫搭 3 天游戏
- **W08 函数**：def / 参数 / 返回值 / 改造重复代码
- **W09 二分（算法加餐①）**：每次砍一半 / 词典寻宝赛
- **W10 turtle 画画**：前进/转弯/颜色/循环画雪花
- **W11 字典**：键值对 / 嵌套 / 宠物图鉴
- **W12 随机与游戏**：random / 石头剪刀布 / 文字 RPG
- **W13 🎓 毕业项目**：自选主题，100+ 行代码 + 作品说明 + 家族展示会

**算法加餐**（穿插）：二分 / 递归 / 数组 vs 链表 + 选择排序 / 贪心（猫武士场景）

### 🤖 AI 通识（贯穿 + 独立胶囊）

- **每课尾 3 分钟 AI 常识胶囊**（清华附 AI 营 20 道判断题对齐）
- **核心主题**：什么是 LLM / token / hallucination / 训练数据 / 开源 vs 闭源 / 算力 / 隐私 / 责任
- **W09 实战**：调用 OpenAI / 本地 LLM
- **deep dive**：DeepSeek / ChatGPT 原理 + 伦理边界

### 👀 C++ 认脸（同步孪生边栏）

- **每课 5 行只读 C++ 代码**——目的：AI 营笔试 C++ 语法认脸不陌生
- **不是深学 C++**——只"看到不害怕"
- 与 Python 主课同步对照，标"对比锚"

### 🛠 工具链与机制

- **本地 IDE**：Thonny（macOS / Windows）
- **进度跟踪**：tracker 每 5min 采文件 mtime + Thonny 会话 + 浏览器事件 → 融合统计
- **mentor 智能体**：Hermes / OpenClaw / WorkBuddy 等任一，**24h 内 review** 学员作业
- **节奏**：每课 30-45 分钟；两位学员各一份进度表，13 周主课 + 算法加餐
- **学习姿势**：分屏边看边练（左边本站 / 右边 Thonny）

### 📊 学员路径

1. **首次搭环境**：克隆仓库到 `~/Sand-Hollow/` → 智能体读 mentors-rules 上岗 → 创建学员目录 `<你的英文名>/homework/`
2. **每周学习**：左边选周 → 逐课阅读 → 学完勾选 → 写 practice / homework → 通知 mentor
3. **毕业交付**：W13 自选项目 + 100+ 行代码 + 作品说明 + 家族展示会

---

## 参与者

| 角色 | 名字 | 备注 |
|------|------|------|
| 🐱 学员 | **ThawPaw** | 猫武士主题方向 |
| 🌳 学员 | **Tree** | 自学编程方向 |
| ❄️ mentor | **IcePaw** | 守护 ThawPaw |
| ✨ mentor | **如意** | 守护 Tree |

---

## 迭代参与

如希望参与项目迭代（添加新学员 / 调整课程结构 / 改进 mentor 流程 / 投稿新主题），请联系 Tree：`wangjieqi@brandct.com`。

---

## 网站说明

沙坑训练场是家庭编程课的练习站：每周课程更新到线上，学员本地写作业、按需提交，mentor 批改后反馈。

- 线上站：https://learning.thawflow.com（CDN 缓存约 10 分钟，页脚 BUILD_TIME 可核对版本）
- 站点即仓库：push 到 main 即发布，课程内容可回滚
- mentor 双签规则 + 入职手册：`mentors-den/mentors-rules.md`（v1.6，2026-09-04 Tree 修订）

## 学习路径

课程按周推进（W01 起），每周拆成 L01/L02… 小课，配作业与批改：

1. 基础（W01 起）：input / 变量 / f-string，第一个小项目是 calculator 和 quiz bot
2. 工具链（W07）：git clone 本地克隆法接入，学会自己拉课程
3. 实战（W12）：OpenClaw 案例课，把前面学的串成真工具
4. 卡住时：annex 兜底资料随时查，sandbox 允许无限重练

进度因人而异，重练不算落后。

## 目录结构

```
Sand-Hollow/
├── README.md              ← 你正在看的
├── docs/                  ← GitHub Pages 站点源（push 即上线 learning.thawflow.com）
├── mentors-den/           ← mentor 内部文档（不入站，不公开）
│   ├── mentors-rules.md   ← 双签规则 / 红线 / 作业评阅规范（v1.6 含 Thonny 监测 + 14:00 节奏）
│   └── onboarding/        ← mentor 入职手册
├── thawpaw/               ← 学员 A 的作业区
│   ├── homework/          ← 上手练习 + 课后作业（gitignore）
│   └── reviews/           ← mentor 评语（gitignore）
└── tree/                  ← 学员 B 的作业区
```

每位学员一个文件夹，命名约定见 `mentors-den/mentors-rules.md`。

## 本地作业

学员作业存到自己目录下：

- 上手练习：`{W##}-L##-practice.py`（如 `W01-L01-practice.py`）
- 课后作业：`{W##}-L##-homework.py`（如 `W01-L02-homework.py`）

全部平铺在 `thawpaw/homework/` 一层，**不建周子目录**。旧命名保留兼容，新课按新约定。

## 提交流程

1. 在 Thonny 写代码 / 跑通
2. 保存到 `~/Sand-Hollow/{学员文件夹}/homework/`
3. **交完跟 mentor 说一声**才批改（不发 = 没交）
4. mentor 在 `{学员文件夹}/reviews/{W##}-L##-review.md` 写评语
5. tracker 自动记录练习时长与活跃度（不进 Git）

> ⚠️ 学员文件夹已 `.gitignore`，**作业不会 commit 到 GitHub**。本地独有，私密保存。

---

## 内部资料（不入站点）

- mentor 双签规则 + 入职手册：`mentors-den/mentors-rules.md`（**让智能体（Hermes / OpenClaw / WorkBuddy 等）读这个 → 自动 review**，v1.6，2026-09-04 Tree 修订：含 Thonny 日志解析 → 真实学习时长 ⑫ + mentor 持续学课 ⑬ + daily-practice 14:00 节奏 ⑭）
- KV 发布：`docs/index.html` 内嵌 JS + KV 内容 API（`https://tpg-hq.thawflow.com/learning/*`）

## 站点技术栈

- 静态站：纯 HTML + 内嵌 JS（无构建步骤）
- CDN：`learning.thawflow.com`（CDN 缓存 10min，sw.js 网络优先）
- 内容 API：Cloudflare Worker `tpg-hq.thawflow.com/learning/*`（KV 存储，发布走同源 API）
- 进度跟踪：localStorage（`learning-checks`）+ track.js 埋点（click:* 上报）
