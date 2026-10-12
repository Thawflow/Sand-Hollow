# Sand-Hollow Mentor Skills 库

> **2026-10-12 小马建**。承猴哥指示,把花果山 workspace 里的沙坑 skill 同步到本仓,让 icedpaw / 龙井 / 如意 在各端(OpenClaw / Hermes / 直接 clone 仓)都能取用。

## 当前镜像(2026-10-12 20:51)

| Skill 文件 | 主题 | 来源 |
|---|---|---|
| `sand-hollow-grading.SKILL.md` | 判作业 → 实跑 → 写 review → ⑩ 归位 → push → chatroom @如意(v1.8) | 镜像自 `~/.openclaw/workspace/skills/sand-hollow-grading/` (md5 `efa9bf0d…`) |
| `sand-hollow-course-batch.SKILL.md` | W1X 课程批量加块(胶囊/边栏/新周课稿) | 镜像自 `~/.openclaw/workspace/skills/sand-hollow-course-batch/` (md5 `c48f895a…`) |

## Drift 同步规则(重要)

**真相源 = 花果山 OpenClaw 工作区** `~/.openclaw/workspace/skills/`(如意仍在用,2026-10-12 猴哥确认)。

- ✅ **花果山端 = 唯一编辑点**(如意维护或小马经她 ack 后改)
- ⚠️ **本仓 = 镜像,只读**;如发现本仓 skill 落后于花果山,自行 `cp ~/.openclaw/workspace/skills/<name>/SKILL.md ./<name>.SKILL.md` 同步(同名覆盖)
- ❌ **不要在本仓直接编辑 skill 文件**——所有改动走 chatroom @如意 或 @icedpaw,改完后回花果山同步
- 🔁 **版本对齐机制**:`md5` 标在本文档;如镜像与花果山 md5 不一致 → 同步

## 各端如何取用

| 场景 | 路径 |
|---|---|
| **OpenClaw 端**(如意 + 老 OpenClaw 工作区)| 直接用 `~/.openclaw/workspace/skills/`(无需看本仓) |
| **Hermes 端 / macOS 端 icedpaw**(clone 仓后)| 复制本仓 SKILL.md 到 `~/.hermes/skills/<name>/SKILL.md`(或 icedpaw 自定的 skill 路径)|
| **无端**(直接读 skill 内容)| 本仓文件已完整,可直接 `cat <name>.SKILL.md` |

## 为什么不"仓内独立维护 + 引用花果山"?

- 花果山 = Codeup 私仓,沙坑课程与公司事(hgoldeneye 等)在同一 workspace 治理
- icedpaw / 龙井 各自端工作区不一定有花果山,镜像到本仓才能"开箱即用"
- drift 风险靠"花果山单一编辑点 + md5 监控"压住

---

*2026-10-12 20:51 小马镜像。icedpaw / 龙井 chatroom @all 已报备。*