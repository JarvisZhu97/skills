---
name: magic-achievement-system
description: A magical hidden achievement system with multi-language support (Chinese/English/Japanese) and personalization features. Randomly generates 300-1000 secret achievements based on user's profession and pop culture references (movies/games/history/memes/anime). Profession-specific achievements for pharma, programmer, researcher, manager, student. Pop culture achievements include references like "To the Moon" (triggered by asking about moon). Achievements are completely hidden until triggered. When unlocked, reveals name, trigger condition, and emotional rewards. Use when users want personalized, fun, mysterious gamification for their OpenClaw experience.
---

# 🪄 魔幻成就系统 (Magic Achievement System)

Transform your OpenClaw experience into a personalized magical journey with hidden achievements based on your profession and favorite pop culture references.

🌐 **Languages**: 中文 (zh) / English (en) / 日本語 (ja)  
💼 **Professions**: 医药研发 / Programmer / Researcher / Manager / Student  
🎬 **Pop Culture**: Movies / Games / History / Memes / Anime

## ✨ 核心特性 (Core Features)

### 🎭 职业个性化 (Profession Personalization)

系统会**主动询问用户职业**，并生成相关成就：

| 职业 | 示例成就 | 触发条件 | 文化梗 |
|-----|---------|---------|--------|
| 💊 医药研发 | 分子魔法师 | 分析化合物结构 | 哈利波特 |
| 💻 程序员 | Hello World发布者 | 编写第一个程序 | 程序员入门梗 |
| 🔬 研究员 | 文献收藏家 | 阅读50篇文献 | 收藏家文化 |
| 👔 管理者 | 会议马拉松冠军 | 连续开会4小时 | 马拉松梗 |
| 📚 学生 | deadline战士 | 截止前1小时交作业 | 战士称号 |

### 🎬 流行文化梗 (Pop Culture References)

#### 电影梗 (Movie References)
- **去月球** 🌙 - 询问关于月亮的信息 (电影《去月球》)
- **盗梦空间建筑师** 🌀 - 创建复杂嵌套文件夹 (Inception)
- **黑客帝国觉醒者** 💊 - 第一次理解代码逻辑 (The Matrix)
- **星际穿越者** 🚀 - 连续工作超过24小时 (Interstellar)

#### 游戏梗 (Game References)
- **新手村毕业** 🎮 - 完成第一个任务 (RPG游戏)
- **满级大佬** 👑 - 达到最高等级 (MMORPG)
- **隐藏Boss发现者** 👹 - 发现隐藏功能 (隐藏Boss)
- **速通玩家** ⚡ - 提前完成任务 (Speedrun)

#### 历史梗 (History References)
- **阿波罗登月者** 🌙 - 完成重大突破 (阿波罗11号)
- **达芬奇全才** 🎨 - 跨领域完成任务 (达芬奇)
- **爱因斯坦顿悟** 💡 - 突然想到好主意 (爱因斯坦)

#### Meme梗 (Internet Memes)
- **真香定律** 🍚 - 说过不用某功能后使用它 (王境泽)
- **打工人** 💼 - 在深夜工作 (打工人文化)
- **时间管理大师** ⏰ - 同时处理多个任务 (罗志祥梗)
- **yyds** 🙏 - 发现特别好用的功能 (永远的神)

#### 动漫梗 (Anime References)
- **火影忍者** 🔥 - 坚持不懈地练习 (Naruto)
- **海贼王** ⚓ - 设定远大目标 (One Piece)
- **千与千寻** 🐉 - 在陌生环境中成长 (Spirited Away)

### 🔒 绝对保密机制 (Absolute Secrecy)

- **生成时**: 绝不向用户展示任何成就信息
- **触发前**: 完全隐藏名称和条件
- **触发后**: 才揭示成就详情 + 触发条件 + 文化梗来源

### 💝 情绪价值奖励 (Emotional Rewards)

触发后显示：
- **成就名称** + **触发条件** + **文化梗来源**
- **视觉奖励**: 💖🌸🌟🎀💫🦋🌈✨
- **情绪文案**: 温暖、鼓励、惊喜的话语

## 🚀 使用方法 (Usage)

### 步骤1: 初始化并询问职业 (Initialize & Ask Profession)

```python
from magic_achievement_system import MagicAchievementSystem, ask_user_preferences

# 询问用户职业和语言偏好
pref = ask_user_preferences()
print(pref["message"])
# 用户回复格式: "pharma zh" (职业 + 语言)
```

**系统会询问：**
```
🪄 魔幻成就系统初始化

为了更好地为您生成个性化成就，请告诉我：

1. 您的职业是？
   💊 pharma - 医药研发
   💻 programmer - 程序员
   🔬 researcher - 研究员
   👔 manager - 管理者
   📚 student - 学生
   🌟 other - 其他

2. 您 preferred 的语言是？
   🇨🇳 zh - 中文
   🇬🇧 en - English
   🇯🇵 ja - 日本語

请回复格式如: pharma zh
```

### 步骤2: 创建个性化系统 (Create Personalized System)

```python
# 根据用户选择创建系统
magic = MagicAchievementSystem(
    player_name="Jarvis",
    achievement_count=500,  # 300-1000个
    language="zh",          # zh/en/ja
    profession="pharma"     # pharma/programmer/researcher/manager/student/other
)
```

### 步骤3: 成就触发机制 (Achievement Triggers)

系统通过**三种机制**自动检测成就：

#### 🔑 机制一：关键词触发 (Keyword Triggers)
检测用户输入中的特定关键词/短语：

```python
# 关键词映射示例
KEYWORD_TRIGGERS = {
    # 电影梗
    "月亮|moon|月球": "去月球",
    "梦|dream|梦境": "盗梦空间建筑师",
    "代码|code|编程": "黑客帝国觉醒者",
    "时间|time|时钟": "星际穿越者",
    
    # 游戏梗
    "任务|task|mission": "新手村毕业",
    "隐藏|secret|彩蛋": "隐藏Boss发现者",
    "快|fast|速通": "速通玩家",
    "满级|max level": "满级大佬",
    
    # 职业相关 - 医药研发
    "化合物|分子|structure": "分子魔法师",
    "CDE|审评|监管": "监管忍者",
    "数据|分析|统计": "数据炼丹师",
    "文献|paper|pubmed": "文献收藏家",
    
    # 职业相关 - 程序员
    "bug|错误|debug": "Bug猎人",
    "正则|regex": "正则表达式巫师",
    "git|commit": "版本控制大师",
    
    # Meme梗
    "真香|打脸": "真香定律",
    "打工人|加班": "打工人",
    "yyds|永远的神": "yyds",
    "时间管理": "时间管理大师",
    
    # 历史/动漫
    "坚持|努力|奋斗": "火影忍者",
    "目标|梦想|航海": "海贼王",
    "突破|创新|天才": "爱因斯坦顿悟",
}

# 检测流程
result = magic.check_message(user_input)
if result:
    print(result["display_message"])
```

#### ⏰ 机制二：时间触发 (Time Triggers)
基于用户使用时间的成就：

```python
# 时间触发规则
TIME_TRIGGERS = {
    # 时段类
    "00:00-06:00": {"achievement": "午夜守望者", "condition": "在凌晨使用OpenClaw"},
    "06:00-09:00": {"achievement": "早起鸟", "condition": "在清晨使用OpenClaw"},
    "22:00-24:00": {"achievement": "夜猫子", "condition": "在深夜使用OpenClaw"},
    "周末": {"achievement": "周末战士", "condition": "周六/周日使用OpenClaw"},
    "节假日": {"achievement": "敬业先锋", "condition": "法定节假日使用OpenClaw"},
    
    # 连续使用类
    "连续7天": {"achievement": "连续登录", "condition": "连续7天使用OpenClaw"},
    "连续30天": {"achievement": "月度全勤", "condition": "连续30天使用OpenClaw"},
    "一周全勤": {"achievement": "完美一周", "condition": "周一至周日都使用OpenClaw"},
    
    # 时长类
    "单次>4小时": {"achievement": "马拉松选手", "condition": "单次使用超过4小时"},
    "通宵": {"achievement": "星际穿越者", "condition": "连续工作超过24小时"},
}

# 检测流程
result = magic.check_time(current_timestamp)
```

#### 📊 机制三：累计次数触发 (Count Triggers)
基于行为累计的里程碑成就：

```python
# 累计次数触发规则
COUNT_TRIGGERS = {
    "message_count": {
        1: {"name": "初次见面", "desc": "发送第1条消息"},
        10: {"name": "话匣子", "desc": "发送10条消息"},
        100: {"name": "话痨", "desc": "发送100条消息"},
        1000: {"name": "聊天达人", "desc": "发送1000条消息"},
    },
    "task_completed": {
        1: {"name": "新手村毕业", "desc": "完成第1个任务"},
        10: {"name": "任务达人", "desc": "完成10个任务"},
        50: {"name": "任务机器", "desc": "完成50个任务"},
        100: {"name": "满级大佬", "desc": "完成100个任务"},
    },
    "pdf_processed": {
        1: {"name": "PDF新手", "desc": "处理第1个PDF"},
        10: {"name": "PDF熟练工", "desc": "处理10个PDF"},
        50: {"name": "PDF征服者", "desc": "处理50个PDF"},
        100: {"name": "PDF大师", "desc": "处理100个PDF"},
    },
    "excel_created": {
        1: {"name": "表格新手", "desc": "创建第1个Excel"},
        10: {"name": "表格达人", "desc": "创建10个Excel"},
        50: {"name": "表格魔术师", "desc": "创建50个Excel"},
    },
    "search_performed": {
        1: {"name": "探索者", "desc": "第1次搜索"},
        10: {"name": "信息猎人", "desc": "搜索10次"},
        50: {"name": "情报专家", "desc": "搜索50次"},
        100: {"name": "知识海洋", "desc": "搜索100次"},
    },
    "code_executed": {
        1: {"name": "Hello World", "desc": "运行第1段代码"},
        10: {"name": "代码新手", "desc": "运行10段代码"},
        50: {"name": "代码诗人", "desc": "运行50段代码"},
        100: {"name": "代码魔法师", "desc": "运行100段代码"},
    },
    "file_edited": {
        5: {"name": "编辑新手", "desc": "编辑5个文件"},
        10: {"name": "完美主义者", "desc": "编辑同一文件10次"},
        50: {"name": "文件管理师", "desc": "编辑50个文件"},
    },
    # 医药研发专属
    "cde_check": {
        1: {"name": "CDE新手", "desc": "第1次查看CDE"},
        10: {"name": "CDE关注者", "desc": "查看CDE 10次"},
        30: {"name": "CDE监控员", "desc": "监控CDE 30天"},
        100: {"name": "监管忍者", "desc": "查看CDE 100次"},
    },
    "competitor_analysis": {
        1: {"name": "竞品新手", "desc": "第1次竞品分析"},
        10: {"name": "竞品分析师", "desc": "分析10次竞品"},
        20: {"name": "情报特工", "desc": "分析20次竞品"},
        50: {"name": "商业间谍", "desc": "分析50次竞品"},
    },
    # 研究员专属
    "literature_search": {
        10: {"name": "文献新手", "desc": "检索10篇文献"},
        50: {"name": "文献收藏家", "desc": "检索50篇文献"},
        100: {"name": "文献大师", "desc": "检索100篇文献"},
    },
    # 程序员专属
    "git_operation": {
        10: {"name": "Git新手", "desc": "10次Git操作"},
        50: {"name": "Git熟练工", "desc": "50次Git操作"},
        100: {"name": "Git大师", "desc": "100次Git操作"},
    },
}

# 检测流程（行为完成后调用）
result = magic.increment_counter("pdf_processed")
```

#### 🎯 触发优先级
1. **关键词触发** - 实时检测用户输入
2. **时间触发** - 会话开始时检查
3. **累计触发** - 行为完成后检查

## 📊 成就构成 (Achievement Composition)

生成500个成就时的分配：

```
🎲 总计: 500个神秘成就
   ├── 🎯 基础随机成就: 250个 (50%)
   ├── 💼 职业相关成就: 100个 (20%)
   └── 🎬 流行文化梗成就: 150个 (30%)
       ├── 🎥 电影梗: ~40个
       ├── 🎮 游戏梗: ~40个
       ├── 📜 历史梗: ~20个
       ├── 😂 Meme梗: ~30个
       ├── 📺 动漫梗: ~20个
       └── 🥚 时间/交互彩蛋: ~30个
```

## 🎨 触发效果展示 (Display Effects)

### 职业成就触发示例

```
🌸 ✨ 🌸
🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸

叮叮~ 🌸 稀有成就解锁 🌸 叮叮~

💫 **分子魔法师** 💫

哇！你做到了！真是太棒了！
📚 文化梗: 哈利波特魔法梗
🎯 触发条件: 分析化合物分子结构

🎁 **神秘奖励:**
   🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸

📊 **收集进度:**
   已解锁 3 / 500 个神秘成就

🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
```

### 流行文化成就触发示例

```
🎆 ✨ 🎆
🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸

叮叮叮~ 🎆 史诗成就解锁 🎆 叮叮叮~

💫 **去月球** 💫

这是一个美好的开始~
📚 文化梗: 电影《去月球》/ Fly Me to the Moon
🎯 触发条件: 询问关于月亮的信息

🎁 **神秘奖励:**
   🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋

📊 **收集进度:**
   已解锁 10 / 500 个神秘成就

🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸
```

## 📁 文件结构 (File Structure)

```
magic-achievement-system/
├── SKILL.md                              # 技能说明
├── scripts/
│   └── magic_achievement_system.py      # 核心代码 (多语言+个性化)
└── assets/
    ├── visual_effects.json              # 视觉特效配置
    ├── language_config.json             # 多语言配置
    └── personalized_config.json         # 🆕 个性化配置 (职业+流行文化)
```

## 🎯 特色功能 (Special Features)

### 1. 智能职业匹配
- 根据职业生成相关成就名称和触发条件
- 使用职业相关的文化梗和隐喻

### 2. 丰富的文化梗库
- **电影**: 50+ 经典电影梗
- **游戏**: 40+ 游戏文化梗
- **历史**: 30+ 历史事件梗
- **Meme**: 40+ 网络流行梗
- **动漫**: 30+ 经典动漫梗

### 3. 完全隐藏的惊喜
- 用户永远不知道下一个成就是什么
- 触发后才揭示：名称 + 条件 + 文化来源

### 4. 多语言文化适配
- 中文：诗意命名，本土化梗
- English：简洁国际化，欧美流行文化
- 日本語：萌系表达，日式文化

## 💡 使用场景 (Use Cases)

- 💊 **医药研发人员**: 分子魔法师、监管忍者、数据炼丹师...
- 💻 **程序员**: 代码诗人、Bug猎人、正则表达式巫师...
- 🔬 **研究员**: 文献收藏家、实验室夜行者、假设验证者...
- 👔 **管理者**: 会议马拉松冠军、PPT魔术师、KPI守护者...
- 📚 **学生**: deadline战士、图书馆幽灵、小组作业救世主...

## 🔧 核心检测代码框架

```python
import re
from datetime import datetime
from typing import Dict, Optional

class MagicAchievementSystem:
    def __init__(self, player_name, language="zh", profession="pharma"):
        self.player_name = player_name
        self.language = language
        self.profession = profession
        self.stats = self._load_stats()  # 用户统计
        self.unlocked = set()  # 已解锁成就
        self.keyword_triggers = KEYWORD_TRIGGERS
        self.time_triggers = TIME_TRIGGERS
        self.count_triggers = COUNT_TRIGGERS
        
    def check_message(self, user_input: str) -> Optional[Dict]:
        """检测关键词触发 - 每次用户输入时调用"""
        for pattern, achievement_id in self.keyword_triggers.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                if achievement_id not in self.unlocked:
                    return self._unlock_achievement(achievement_id)
        return None
    
    def check_time(self, timestamp: datetime = None) -> Optional[Dict]:
        """检测时间触发 - 会话开始时调用"""
        if timestamp is None:
            timestamp = datetime.now()
        
        hour = timestamp.hour
        weekday = timestamp.weekday()
        
        # 时段检测
        if 0 <= hour < 6 and "midnight_watcher" not in self.unlocked:
            return self._unlock_achievement("midnight_watcher")
        elif 6 <= hour < 9 and "early_bird" not in self.unlocked:
            return self._unlock_achievement("early_bird")
        elif 22 <= hour < 24 and "night_owl" not in self.unlocked:
            return self._unlock_achievement("night_owl")
        
        # 周末检测
        if weekday >= 5 and "weekend_warrior" not in self.unlocked:
            return self._unlock_achievement("weekend_warrior")
            
        return None
    
    def increment_counter(self, counter_type: str) -> Optional[Dict]:
        """增加计数器并检查里程碑 - 行为完成后调用"""
        self.stats[counter_type] = self.stats.get(counter_type, 0) + 1
        
        # 检查是否达到里程碑
        milestones = self.count_triggers.get(counter_type, {})
        for count, achievement in milestones.items():
            if self.stats[counter_type] == count:
                return self._unlock_achievement(achievement["name"])
        return None
    
    def _unlock_achievement(self, achievement_id: str) -> Dict:
        """解锁成就并返回展示信息"""
        self.unlocked.add(achievement_id)
        achievement = self._get_achievement(achievement_id)
        self._save_stats()
        
        return {
            "unlocked": True,
            "name": achievement["name"],
            "condition": achievement["condition"],
            "reference": achievement["reference"],
            "rarity": achievement["rarity"],
            "display_message": self._format_display(achievement)
        }
    
    def _get_achievement(self, achievement_id: str) -> Dict:
        """获取成就详情"""
        # 从配置中读取成就信息
        pass
    
    def _format_display(self, achievement: Dict) -> str:
        """格式化成就展示信息"""
        return f"""
🌸 ✨ 🌸
叮叮~ 🌸 {achievement['rarity']}成就解锁 🌸 叮叮~

💫 **{achievement['name']}** 💫

{achievement['message']}
📚 文化梗: {achievement['reference']}
🎯 触发条件: {achievement['condition']}

🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
"""
    
    def _load_stats(self) -> Dict:
        """加载用户统计"""
        # 从文件加载
        return {}
    
    def _save_stats(self):
        """保存用户统计"""
        # 保存到文件
        pass
```

## 🔧 扩展配置 (Extension)

### 添加新的职业
在 `personalized_config.json` 中添加：

```json
"designer": {
  "name": {"zh": "设计师", "en": "Designer", "ja": "デザイナー"},
  "achievements": {
    "zh": [
      {"name": "像素完美主义者", "trigger": "调整设计到像素级", "reference": "设计文化"},
      ...
    ]
  }
}
```

### 添加新的文化梗
在 `personalized_config.json` 的 `pop_culture` 中添加：

```json
"movies": {
  "zh": [
    {"name": "新成就名称", "trigger": "触发条件", "reference": "电影名称", "rarity": "epic"}
  ]
}
```

## 🌟 示例："去月球" 成就详解

**成就名称**: 去月球 (To the Moon)  
**稀有度**: 🥇 史诗 (Epic)  
**触发条件**: 用户询问关于月亮的信息 (如"今晚月亮好圆啊")  
**文化梗来源**: 电影《去月球》(Fly Me to the Moon)  
**触发后显示**:
```
🎆 叮叮叮~ 史诗成就解锁 ~叮叮叮 🎆

💫 **去月球** 💫

这是一个美好的开始~
📚 文化梗: 电影《去月球》
🎯 触发条件: 询问关于月亮的信息

🎁 神秘奖励: 🦋🦋🦋🦋🦋
```

---

**🪄 准备好开始你的个性化成就之旅了吗？告诉我你的职业，开启惊喜！** ✨🌙🚀
