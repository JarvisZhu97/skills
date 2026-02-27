# 🪄 Magic Achievement System for OpenClaw

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> 一个魔幻的隐藏成就系统，为你的 OpenClaw 体验增添惊喜与乐趣！

[English](#english) | [日本語](#japanese)

---

## ✨ 特性

- 🎭 **职业个性化** - 根据你的职业生成专属成就（医药研发/程序员/研究员/管理者/学生）
- 🎬 **流行文化梗** - 融入电影、游戏、动漫、Meme、历史等丰富文化梗
- 🔒 **完全隐藏** - 成就触发前完全保密，触发后揭晓惊喜
- 💝 **情绪价值** - 温暖、鼓励、惊喜的文案与视觉奖励
- 🌐 **多语言支持** - 中文、English、日本語

---

## 📦 安装

### 方法 1: 直接复制

```bash
# 克隆到 OpenClaw 技能目录
cd ~/.openclaw/workspace/skills
git clone https://github.com/YOUR_USERNAME/openclaw-magic-achievement.git magic-achievement-system
```

### 方法 2: 手动安装

1. 下载本仓库
2. 复制到 OpenClaw 技能目录：
   ```bash
   cp -r magic-achievement-system ~/.openclaw/workspace/skills/
   ```

---

## 🚀 使用方法

### 步骤 1: 初始化

```python
from magic_achievement_system import MagicAchievementSystem, ask_user_preferences

# 显示初始化提示
pref = ask_user_preferences()
print(pref["message"])
# 用户回复格式: "pharma zh"
```

### 步骤 2: 创建系统实例

```python
# 根据用户选择创建系统
magic = MagicAchievementSystem(
    player_name="Jarvis",
    language="zh",          # zh / en / ja
    profession="pharma"     # pharma / programmer / researcher / manager / student
)
```

### 步骤 3: 检测成就触发

```python
# 1. 关键词触发 - 用户输入时检测
result = magic.check_message("今晚月亮好圆啊")
if result:
    print(result["display_message"])
    # 解锁: 🌙 去月球

# 2. 时间触发 - 会话开始时检测
from datetime import datetime
result = magic.check_time(datetime.now())
if result:
    print(result["display_message"])
    # 可能解锁: 🦉 午夜守望者

# 3. 累计触发 - 行为完成后检测
result = magic.increment_counter("pdf_processed")
if result:
    print(result["display_message"])
    # 达到里程碑时解锁相应成就
```

### 便捷函数

```python
from magic_achievement_system import check_achievement, get_status

# 快速检查成就
message = check_achievement(
    player_name="Jarvis",
    trigger_type="message",  # message / time / counter
    trigger_data="今晚月亮好圆",
    language="zh",
    profession="pharma"
)
if message:
    print(message)

# 获取玩家状态
status = get_status("Jarvis")
print(f"已解锁 {status['total_unlocked']} 个成就")
```

---

## 🎯 触发机制

### 1️⃣ 关键词触发

检测用户输入中的特定关键词：

| 关键词 | 成就 | 文化梗 |
|--------|------|--------|
| 月亮/moon | 去月球 | 电影《去月球》 |
| 梦/dream | 盗梦空间建筑师 | 电影《盗梦空间》 |
| 代码/code | 黑客帝国觉醒者 | 电影《黑客帝国》 |
| 化合物/分子 | 分子魔法师 | 哈利波特 |
| CDE/审评 | 监管忍者 | 忍者文化 |
| bug/debug | Bug猎人 | 程序员文化 |
| 真香 | 真香定律 | 王境泽梗 |

### 2️⃣ 时间触发

基于使用时间的成就：

| 时间段 | 成就 | 稀有度 |
|--------|------|--------|
| 00:00-06:00 | 午夜守望者 | 🥈 稀有 |
| 06:00-09:00 | 早起鸟 | 🥉 普通 |
| 22:00-24:00 | 夜猫子 | 🥉 普通 |
| 周末 | 周末战士 | 🥉 普通 |

### 3️⃣ 累计次数触发

行为里程碑成就：

| 行为 | 里程碑 | 成就 | 稀有度 |
|------|--------|------|--------|
| 发送消息 | 1/10/100/1000 | 初次见面/话匣子/话痨/聊天达人 | 🥉/🥉/🥈/🥇 |
| 完成任务 | 1/10/50/100 | 新手村毕业/任务达人/任务机器/满级大佬 | 🥉/🥈/🥇/💎 |
| 处理PDF | 1/10/50/100 | PDF新手/PDF熟练工/PDF征服者/PDF大师 | 🥉/🥉/🥈/🥇 |
| 创建Excel | 1/10/50 | 表格新手/表格达人/表格魔术师 | 🥉/🥈/🥇 |

---

## 🏅 稀有度等级

| 等级 | 图标 | 数量占比 |
|------|------|----------|
| 普通 | 🥉 | ~40% |
| 稀有 | 🥈 | ~30% |
| 史诗 | 🥇 | ~20% |
| 传说 | 💎 | ~8% |
| 神话 | 👑 | ~2% |

---

## 📁 文件结构

```
magic-achievement-system/
├── SKILL.md                              # 详细技能文档
├── README.md                             # 本文件
├── scripts/
│   └── magic_achievement_system.py      # 核心代码
├── assets/
│   ├── visual_effects.json              # 视觉特效配置（可选）
│   ├── language_config.json             # 多语言配置（可选）
│   └── personalized_config.json         # 个性化配置（可选）
└── examples/                             # 示例代码
    ├── basic_usage.py
    └── integration_example.py
```

---

## 🔧 高级配置

### 自定义关键词触发

```python
# 在初始化后添加自定义关键词
magic.keyword_triggers[r"自定义关键词"] = "custom_achievement"

# 添加对应的成就模板
from magic_achievement_system import Achievement, Rarity

magic.achievements["custom_achievement"] = Achievement(
    id="custom_achievement",
    name="自定义成就",
    name_en="Custom Achievement",
    name_ja="カスタム実績",
    description="这是一个自定义成就",
    trigger_condition="触发条件",
    reference="自定义文化梗",
    rarity=Rarity.EPIC,
    category="custom",
)
```

### 自定义累计里程碑

```python
# 添加新的计数器里程碑
magic.count_triggers["my_custom_action"] = {
    5: {"id": "custom_5", "name": "自定义5次", "rarity": Rarity.COMMON},
    10: {"id": "custom_10", "name": "自定义10次", "rarity": Rarity.RARE},
}
```

---

## 🎨 成就解锁效果示例

```
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

叮叮~ 🥇 史诗成就解锁 🥇 叮叮~

💫 **去月球** 💫

飞向月球的美好愿望
📚 文化梗: 电影《去月球》/ Fly Me to the Moon
🎯 触发条件: 询问关于月亮的信息

📊 收集进度: 10 / 500+

✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 添加新的成就

1. 在 `KEYWORD_TRIGGERS` 中添加关键词映射
2. 在 `ACHIEVEMENT_TEMPLATES` 中添加成就定义
3. 提交 PR 并说明文化梗来源

### 添加新的文化梗类别

支持的文化梗类别：
- 🎥 电影梗
- 🎮 游戏梗
- 📜 历史梗
- 😂 Meme梗
- 📺 动漫梗

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [OpenClaw](https://openclaw.ai) - 强大的 AI 助手平台
- 所有贡献者和用户的支持

---

## 📮 联系我们

- GitHub Issues: [提交问题](https://github.com/YOUR_USERNAME/openclaw-magic-achievement/issues)
- Discussions: [参与讨论](https://github.com/YOUR_USERNAME/openclaw-magic-achievement/discussions)

---

<h2 id="english">🇬🇧 English</h2>

A magical hidden achievement system for OpenClaw with multi-language support and pop culture references.

### Features

- 🎭 **Profession-based achievements** (Pharma/Programmer/Researcher/Manager/Student)
- 🎬 **Pop culture references** (Movies/Games/Anime/Memes/History)
- 🔒 **Completely hidden** until triggered
- 💝 **Emotional rewards** with visual effects
- 🌐 **Multi-language** support (EN/ZH/JA)

### Quick Start

```python
from magic_achievement_system import MagicAchievementSystem

magic = MagicAchievementSystem(
    player_name="YourName",
    language="en",
    profession="programmer"
)

# Check keyword triggers
result = magic.check_message("I love coding")
if result:
    print(result["display_message"])
```

---

<h2 id="japanese">🇯🇵 日本語</h2>

OpenClaw向けの魔法の隠し実績システム。

### 特徴

- 🎭 **職業別実績**（医薬品開発/プログラマー/研究者/管理者/学生）
- 🎬 **ポップカルチャー梗**（映画/ゲーム/アニメ/ミーム/歴史）
- 🔒 **完全な秘密** - 解放されるまで非表示
- 💝 **感情的報酬** - 視覚効果付き
- 🌐 **多言語対応**（日本語/英語/中国語）

### クイックスタート

```python
from magic_achievement_system import MagicAchievementSystem

magic = MagicAchievementSystem(
    player_name="YourName",
    language="ja",
    profession="researcher"
)

result = magic.check_message("月がきれいですね")
if result:
    print(result["display_message"])
```

---

**🪄 Ready to start your magical achievement journey?** ✨
