# 🪄 Magic Achievement System for OpenClaw

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> A magical hidden achievement system that adds surprise and fun to your OpenClaw experience!

[简体中文](#chinese) | [日本語](#japanese)

---

## ✨ Features

- 🎭 **Profession-based Personalization** - Generate exclusive achievements based on your profession (Pharma/Programmer/Researcher/Manager/Student)
- 🎬 **Pop Culture References** - Rich cultural memes from movies, games, anime, internet culture, and history
- 🔒 **Completely Hidden** - Achievements remain secret until triggered, then reveal surprises
- 💝 **Emotional Rewards** - Warm, encouraging, and surprising messages with visual effects
- 🌐 **Multi-language Support** - English, 中文 (Chinese), 日本語 (Japanese)

---

## 📦 Installation

### Method 1: Clone Repository

```bash
# Clone to OpenClaw skills directory
cd ~/.openclaw/workspace/skills
git clone https://github.com/YOUR_USERNAME/openclaw-magic-achievement.git magic-achievement-system
```

### Method 2: Manual Installation

1. Download this repository
2. Copy to OpenClaw skills directory:
   ```bash
   cp -r magic-achievement-system ~/.openclaw/workspace/skills/
   ```

---

## 🚀 Usage

### Step 1: Initialize

```python
from magic_achievement_system import MagicAchievementSystem, ask_user_preferences

# Display initialization prompt
pref = ask_user_preferences()
print(pref["message"])
# User replies with format: "pharma en"
```

### Step 2: Create System Instance

```python
# Create system based on user selection
magic = MagicAchievementSystem(
    player_name="Jarvis",
    language="en",          # en / zh / ja
    profession="pharma"     # pharma / programmer / researcher / manager / student
)
```

### Step 3: Detect Achievement Triggers

```python
# 1. Keyword Trigger - Detect on user input
result = magic.check_message("The moon is so beautiful tonight")
if result:
    print(result["display_message"])
    # Unlocks: 🌙 To The Moon

# 2. Time Trigger - Check at session start
from datetime import datetime
result = magic.check_time(datetime.now())
if result:
    print(result["display_message"])
    # May unlock: 🦉 Midnight Watcher

# 3. Count Trigger - Check after actions
result = magic.increment_counter("pdf_processed")
if result:
    print(result["display_message"])
    # Unlocks milestone achievements
```

### Convenience Functions

```python
from magic_achievement_system import check_achievement, get_status

# Quick achievement check
message = check_achievement(
    player_name="Jarvis",
    trigger_type="message",  # message / time / counter
    trigger_data="The moon is beautiful",
    language="en",
    profession="pharma"
)
if message:
    print(message)

# Get player status
status = get_status("Jarvis")
print(f"Unlocked {status['total_unlocked']} achievements")
```

---

## 🎯 Trigger Mechanisms

### 1️⃣ Keyword Triggers

Detect specific keywords in user input:

| Keyword | Achievement | Cultural Reference |
|---------|-------------|-------------------|
| moon/luna | To The Moon | Movie "To The Moon" |
| dream | Inception Architect | Movie "Inception" |
| code/programming | Matrix Awakened | Movie "The Matrix" |
| compound/molecule | Molecular Magician | Harry Potter |
| CDE/regulatory | Regulatory Ninja | Ninja culture |
| bug/debug | Bug Hunter | Programmer culture |
| yyds/goat | GOAT | Internet slang |

### 2️⃣ Time Triggers

Time-based achievements:

| Time Period | Achievement | Rarity |
|-------------|-------------|--------|
| 00:00-06:00 | Midnight Watcher | 🥈 Rare |
| 06:00-09:00 | Early Bird | 🥉 Common |
| 22:00-24:00 | Night Owl | 🥉 Common |
| Weekend | Weekend Warrior | 🥉 Common |

### 3️⃣ Count Triggers

Behavior milestone achievements:

| Action | Milestones | Achievements | Rarity |
|--------|------------|--------------|--------|
| Send messages | 1/10/100/1000 | First Meeting/Chatterbox/Talkative/Chat Master | 🥉/🥉/🥈/🥇 |
| Complete tasks | 1/10/50/100 | Newbie Graduate/Task Master/Task Machine/Max Level Boss | 🥉/🥈/🥇/💎 |
| Process PDFs | 1/10/50/100 | PDF Newbie/PDF Skilled/PDF Conqueror/PDF Master | 🥉/🥉/🥈/🥇 |
| Create Excel | 1/10/50 | Excel Newbie/Excel Master/Excel Magician | 🥉/🥈/🥇 |

---

## 🏅 Rarity Levels

| Level | Icon | Distribution |
|-------|------|--------------|
| Common | 🥉 | ~40% |
| Rare | 🥈 | ~30% |
| Epic | 🥇 | ~20% |
| Legendary | 💎 | ~8% |
| Mythic | 👑 | ~2% |

---

## 📁 File Structure

```
magic-achievement-system/
├── SKILL.md                              # Detailed skill documentation
├── README.md                             # This file
├── scripts/
│   └── magic_achievement_system.py      # Core code
├── assets/
│   ├── visual_effects.json              # Visual effects config (optional)
│   ├── language_config.json             # Multi-language config (optional)
│   └── personalized_config.json         # Personalization config (optional)
└── examples/                             # Example code
    ├── basic_usage.py
    └── integration_example.py
```

---

## 🔧 Advanced Configuration

### Custom Keyword Triggers

```python
# Add custom keywords after initialization
magic.keyword_triggers[r"custom_keyword"] = "custom_achievement"

# Add corresponding achievement template
from magic_achievement_system import Achievement, Rarity

magic.achievements["custom_achievement"] = Achievement(
    id="custom_achievement",
    name="Custom Achievement",
    name_en="Custom Achievement",
    name_ja="カスタム実績",
    description="This is a custom achievement",
    trigger_condition="Trigger condition",
    reference="Custom cultural reference",
    rarity=Rarity.EPIC,
    category="custom",
)
```

### Custom Count Milestones

```python
# Add new counter milestones
magic.count_triggers["my_custom_action"] = {
    5: {"id": "custom_5", "name": "Custom 5 Times", "rarity": Rarity.COMMON},
    10: {"id": "custom_10", "name": "Custom 10 Times", "rarity": Rarity.RARE},
}
```

---

## 🎨 Achievement Unlock Effect Example

```
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

Ding Ding~ 🥇 Epic Achievement Unlocked 🥇 Ding Ding~

💫 **To The Moon** 💫

A beautiful wish to fly to the moon
📚 Reference: Movie "To The Moon" / Fly Me to the Moon
🎯 Trigger: Ask about the moon

📊 Collection Progress: 10 / 500+

✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
```

---

## 🤝 Contributing

Welcome to submit Issues and Pull Requests!

### Adding New Achievements

1. Add keyword mapping in `KEYWORD_TRIGGERS`
2. Add achievement definition in `ACHIEVEMENT_TEMPLATES`
3. Submit PR with cultural reference explanation

### Adding New Cultural Meme Categories

Supported cultural meme categories:
- 🎥 Movie references
- 🎮 Game references
- 📜 History references
- 😂 Internet memes
- 📺 Anime references

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- [OpenClaw](https://openclaw.ai) - Powerful AI assistant platform
- All contributors and users

---

## 📮 Contact Us

- GitHub Issues: [Submit Issue](https://github.com/YOUR_USERNAME/openclaw-magic-achievement/issues)
- Discussions: [Join Discussion](https://github.com/YOUR_USERNAME/openclaw-magic-achievement/discussions)

---

<h2 id="chinese">🇨🇳 简体中文</h2>

一个魔幻的隐藏成就系统，为 OpenClaw 用户提供个性化、惊喜的成就收集体验。

### 特性

- 🎭 职业个性化（医药研发/程序员/研究员/管理者/学生）
- 🎬 流行文化梗（电影/游戏/动漫/Meme/历史）
- 🔒 完全隐藏 - 触发前完全保密
- 💝 情绪价值奖励
- 🌐 多语言支持（中/英/日）

### 快速开始

```python
from magic_achievement_system import MagicAchievementSystem

magic = MagicAchievementSystem(
    player_name="YourName",
    language="zh",
    profession="pharma"
)

# 检测关键词触发
result = magic.check_message("今晚月亮好圆")
if result:
    print(result["display_message"])
```

---

<h2 id="japanese">🇯🇵 日本語</h2>

OpenClaw向けの魔法の隠し実績システム。

### 特徴

- 🎭 職業別実績（医薬品開発/プログラマー/研究者/管理者/学生）
- 🎬 ポップカルチャー梗（映画/ゲーム/アニメ/ミーム/歴史）
- 🔒 完全な秘密 - 解放されるまで非表示
- 💝 感情的報酬 - 視覚効果付き
- 🌐 多言語対応（日本語/英語/中国語）

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
