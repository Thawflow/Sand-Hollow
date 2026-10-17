# B 方案：零依赖离线学习通道（立项书 v0.1 · 草稿）

> **状态**：v0.1 草稿 · 2026-10-17 08:30 立 · 冰爪起骨架
> **目标读者**：猴哥（owner）· 苗苗（学习体验 owner）· 小马（no-hermes 互不阻塞并行线）
> **落档位置**：`~/projects/Sand-Hollow/docs/B-plan-offline-learning.md`（本地写，**未 push**，等苗苗/猴哥拍板再合入 main）
> **关联**：10/16 19:00 苗苗共创的"沙坑登录系统设计"（`~/projects/skyclan/members/icepaw/docs/2026-10-16-sandbox-login-design.md`）—— 是 B 方案"零账号即学"的桥头堡，**不是 B 方案本身**；本条只立通道骨架

---

## 〇、问题陈述（猴哥 10/16 原话压缩）

> 「苗苗在开发，由 IcePaw 来继续推进，但是要求 IcePaw 把苗苗和她定的方案，写到 Sand-Hollow/docs」

**B 方案** = 零依赖离线学习通道：**学员没 OpenClaw / Hermes 账号也能学沙坑课**。当前 沙坑 `learning.thawflow.com` 学习路径强依赖 ① KV upsert（外部作业信箱）② chatroom ack ③ admin 94568945 玩家号体系 —— **三件都需 token / 账号**。B 方案 = 学员第一次访问即可看课、可写 demo 代码、可看答案对照，**全程不要求任何身份**。

---

## 一、现状调研（10/17 08:30 冰爪 · 查无此物 → 查有部分素材）

### ✅ 已实现（无需重做）
- **PWA 外壳**（commit `bba94a6`）：`docs/manifest.webmanifest` + `docs/sw.js` + `docs/assets/icons/` 三件套 + `apple-touch-icon`；Chrome 可装桌面应用
- **sw.js 离线缓存**：作为 service worker 的 cache-first 策略已生效（index.html line 8 manifest link + line 481 scroll 1s 退化方案）
- **沙坑登录系统设计**（10/16 苗苗+冰爪共创）：解决"学习前需注册"—— random/custom player-id + no nickname + mail button top-right；落 `~/projects/skyclan/members/icepaw/docs/2026-10-16-sandbox-login-design.md`
- **课程 SVG 零依赖实现**（algo-preview-summary-icepaw.md L8）：内联 SVG = 无需 backend 拉取，断网也能渲染
- **本站 5/13 已有的「📝 交作业」卡片**：外部学员可走 web submit（commit `8ae23eb` 注释）—— **当前卡点是 worker endpoint 部署**

### ❌ 待实现
- **worker endpoint**（提交作业的 worker hook）= 10/15 03:30 如意晨会"挂 3 天"项——`/learning/submit` 未部署 = 学员提交作业后无回执
- **离线写代码 demo**：当前 web submit 只接 KV，不接 thonny / 本地 python；学员离线写完**无法存盘**（无 IndexedDB / OPFS）
- **离线答案对照**：当前 W02-S1 的 `solution.py` 是 KV 拉，离线 = 无 solution

### ⚠️ 等苗苗口述（10/16 19:00 后窗口未现）
- "零依赖" 的具体边界：① 学员**不注册**能学到哪一步？② 离线写 demo 代码**存哪里**（localStorage / IndexedDB / 文件下载）？③ 学员**首次联网**是否要"上传 demo + 升级为正式学员"？④ 课程**哪几节**先做离线版（W02 字符串？W05 实战？W12 毕业作品？）
- "无 OpenClaw/Hermes 也能学" = 仅 web 端？还是包括"用 U 盘拷课程包回家"？

---

## 二、立项骨架（v0.1 等苗苗定稿）

### 2.1 范围（候选 3 层，由苗苗拍）
| 层 | 内容 | 当前状态 | 风险 |
|---|---|---|---|
| **L1 · 看课** | 13 周课程全量 web 离线浏览 | ✅ 已支持（sw.js cache-first） | 无 |
| **L2 · 写 demo** | 学员在本机写 .py，可保存到 IndexedDB | ❌ 未做 | 跨平台一致 |
| **L3 · 交作业** | 学员联网时把 demo → 信箱（worker endpoint） | ⚠️ worker 未部署 | KV 写权限 / 外部学员 admin 关系 |

### 2.2 依赖（待苗苗拍）
- **课程内容侧**：每节加 `solution.py` 离线副本（KV 同步落 sw.js cache）
- **后端侧**：worker endpoint `/learning/submit`（如意挂 3d）
- **前端侧**：是否引入 CodeMirror 6 / Monaco Editor 离线版（vs 现有 textarea）
- **信箱侧**：跟现有 `dm:idx:94568945` admin 通道怎么打通

### 2.3 验收（v0.1 阶段 = 草稿本条 = 立骨架 + 收集决策点）
- [ ] 苗苗 10/17-18 窗口口述 L1/L2/L3 范围
- [ ] 苗苗拍 worker endpoint owner（冰爪 / 如意 / 小马 之一）
- [ ] 猴哥拍 GitHub Pages 仓 push 授权窗口
- [ ] v0.2 草稿 = 苗苗口述后 + 冰爪落定

---

## 三、不重叠确认

- **小马 no-hermes.md 线**：等苗苗口述后由小马整理 `docs/no-hermes.md` —— B 方案是「**有 OpenClaw/Hermes 学员**的离线学习通道」，no-hermes.md 是「**外部学员**学沙坑的零依赖路径」= 互补不重叠
- **沙坑登录系统设计**：是 B 方案的"前置学习身份"模块（学员仍可学，但学了之后系统记住你是谁），不是 B 方案本身
- **外部学员作业 review 链路方案**（home-tasks L22 A/B/C）：是 B 方案的"联网后回传 demo"侧 — A/B/C 决策可跟 worker endpoint 部署一起拍

---

## 四、给猴哥/苗苗的 3 个问题

1. **范围**：L1 看课 / L2 写 demo / L3 交作业 哪几层进 v1？
2. **存储**：学员 demo 离线写完后，存 localStorage / IndexedDB / 文件下载 三选一？
3. **worker endpoint owner**：冰爪（如意 5d 等决策的 worker 挂账）/ 如意（晨会已挂）/ 小马（no-hermes 顺带）三选一？

---

> **下步**：14:00 前 iMessage 猴哥 v0.1 草稿 + 邀苗苗验证路径认可（如意 07:27 §5c 要求）
> **回执**：`1792193223916_15n0` 关联 → 14:00 后落 Sand-Hollow/docs push 决策
