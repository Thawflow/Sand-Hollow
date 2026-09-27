# W11-weekend · 打磨 + 家人对战赛

> 用时：60-90 分钟 · 难度：⭐⭐⭐ · 前置：W11 三课

---

## 一、本周武功盘点（3 分钟）

- W11-L01：random 模块（randint / choice / shuffle / sample）
- W11-L02：石头剪刀布（多局 + 计分 + emoji）
- W11-L03：文字 RPG 战斗（玩家 + 敌人 + 升级）

今天：打磨 + 邀请家人对战。

## 二、打磨清单（30 分钟）

### 打磨 1：菜单清晰

```python
def main():
    print("=== Game Menu ===")
    print("1. Single battle")
    print("2. Tournament (5 battles)")
    print("3. Quit")

    choice = input("> ").strip()
    if choice == "1":
        play_round()
    elif choice == "2":
        play_tournament()
    elif choice == "3":
        print("Bye!")
```

### 打磨 2：清晰反馈

每一步都要 print 让玩家知道发生了什么：

```python
# Before:
enemy["hp"] -= dmg

# After:
old_hp = enemy["hp"]
enemy["hp"] -= dmg
print(f"You hit {enemy['name']} for {dmg}! ({old_hp} -> {enemy['hp']})")
```

### 打磨 3：保存战绩

```python
import json
import os

STATS_FILE = "rpg_stats.json"

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE) as f:
            return json.load(f)
    return {"wins": 0, "losses": 0, "highest_level": 1}
```

### 打磨 4：随机事件

战斗间隙可触发随机事件：

```python
def random_event(player):
    roll = random.random()
    if roll < 0.3:
        print("You found a herb! +30 HP")
        player["hp"] = min(player["max_hp"], player["hp"] + 30)
    elif roll < 0.4:
        print("You tripped! -10 HP")
        player["hp"] = max(1, player["hp"] - 10)
    # 60% chance of nothing
```

## 三、家人对战赛（30 分钟）

### 流程

1. 给家人演示你的 RPG 战斗，让他们玩 1-2 局
2. 听他们反馈：哪里卡？哪里好？
3. 改一轮（同样只改细节，不重写）

### 常见反馈

- 「我看不懂能选什么」 → 加选项提示
- 「战斗太短不过瘾」 → 加更多敌人 / 加 boss
- 「死了想重来」 → 加重玩机制
- 「想升级但不知道规则」 → 加 help 命令

## 四、验收标准（自助验收）

- [ ] 打磨清单至少做 2 项
- [ ] 至少 2 个真人玩过
- [ ] 反馈改一轮（至少 3 处）
- [ ] 玩家能完整通关 + 升级

## 五、W11 全周自查

- [ ] L01：random 模块四件套
- [ ] L02：石头剪刀布
- [ ] L03：文字 RPG 战斗
- [ ] 周末：打磨 + 2 真人测试 + 改一轮
- [ ] 我能给家人完整玩一局 RPG

W11 毕业 🎮 → 进入 W12「🏆 毕业项目 🎓」。自选主题，从设计图到作品，100+ 行代码，向家人展示。
