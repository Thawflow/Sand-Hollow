# W10-weekend · 宠物图鉴 v1：完整版

> 用时：60-90 分钟 · 难度：⭐⭐⭐ · 前置：W10 三课

---

## ⓪ 🤖 课前 AI 一分钟 · 第 35 颗：词向量（不用学，见识下）

图鉴 v1 收工。进阶冷知识：AI 把每个词变成**一串数字坐标**（词向量），「猫」和「狗」的坐标离得近。中学以后学。

**⚔️ 判一判**（AI 营线上测评题型热身，先自己答再看答案）：

> 1. AI 可以把文字变成数字来处理
> 2. 词向量现在就要掌握

<details><summary>答案</summary>

**1.** ✓　**2.** ✗ 见识即可

</details>

## 一、本周武功盘点（3 分钟）

- W10-L01：字典基础（增删改查 + 遍历）
- W10-L02：嵌套（字典套字典 / 字典套列表）
- W10-L03：实战宠物图鉴（4 个核心函数）

今天把宠物图鉴升级到「**完整版**」——能搜索、能加技能、能战斗、保存到文件。

## 二、项目：完整版图鉴（60 分钟）

> 📁 项目存 `~/learning-homework/<你的学员名>/homework/`，新建 `pet_codex_v1.py`。

### 完整代码

```python
import json
import os

CODE_FILE = "pet_codex.json"

def load_codex():
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE) as f:
            return json.load(f)
    return {}

def save_codex(codex):
    with open(CODE_FILE, "w") as f:
        json.dump(codex, f, indent=2)
    print("Saved!")

def show_pet(codex, name):
    if name not in codex:
        print(f"{name} not in codex")
        return
    pet = codex[name]
    print(f"\n=== {name} ===")
    print(f"Species: {pet['species']}")
    stats = pet["stats"]
    print(f"HP: {stats['hp']}  ATK: {stats['attack']}  DEF: {stats['defense']}")
    print(f"Skills: {', '.join(pet['skills']) if pet['skills'] else '(none)'}")

def add_pet(codex, name, species, hp, attack, defense):
    if name in codex:
        print(f"{name} already exists")
        return
    codex[name] = {
        "species": species,
        "stats": {"hp": hp, "attack": attack, "defense": defense},
        "skills": [],
    }
    print(f"Added {name}!")

def add_skill(codex, name, skill):
    if name not in codex:
        print(f"{name} not in codex")
        return
    if skill in codex[name]["skills"]:
        print(f"{name} already knows {skill}")
        return
    codex[name]["skills"].append(skill)
    print(f"{name} learned {skill}!")

def search_by_species(codex, species):
    print(f"\n=== {species}s ===")
    found = False
    for name in codex:
        if codex[name]["species"] == species:
            print(f"- {name}")
            found = True
    if not found:
        print("(none)")

def list_all(codex):
    print("\n=== All Pets ===")
    for name in codex:
        pet = codex[name]
        print(f"- {name} ({pet['species']}): HP {pet['stats']['hp']}")

def main():
    codex = load_codex()

    while True:
        print("\n(show/add/skill/search/list/save/quit)")
        action = input("> ").strip().lower()

        if action == "show":
            name = input("Pet name: ")
            show_pet(codex, name)
        elif action == "add":
            name = input("Name: ")
            species = input("Species: ")
            hp = int(input("HP: "))
            atk = int(input("Attack: "))
            df = int(input("Defense: "))
            add_pet(codex, name, species, hp, atk, df)
        elif action == "skill":
            name = input("Pet name: ")
            skill = input("Skill: ")
            add_skill(codex, name, skill)
        elif action == "search":
            species = input("Species to search: ")
            search_by_species(codex, species)
        elif action == "list":
            list_all(codex)
        elif action == "save":
            save_codex(codex)
        elif action == "quit":
            save_codex(codex)
            break
        else:
            print("Unknown action")

main()
```

## 三、验收标准（自助验收）

- [ ] 完整代码跑通，能加宠物 / 加技能 / 搜索 / 列出
- [ ] 重启程序后数据还在（save + load）
- [ ] 至少加 3 只宠物 + 给它们分别加 2 个技能
- [ ] 给家人 / 朋友演示一遍

## 四、W10 全周自查

- [ ] L01：字典基础（增删改查）
- [ ] L02：嵌套（字典套字典 / 列表）
- [ ] L03：实战图鉴
- [ ] 周末：完整版图鉴能加能查能存
- [ ] 我能给家人解释「字典 = 名字找东西」

W10 毕业 📚 → 进入 W11「随机与游戏」。W03-weekend 已经借过 `random.randint`，W11 正式学 random 模块 + 实战石头剪刀布 + 文字 RPG 战斗。
