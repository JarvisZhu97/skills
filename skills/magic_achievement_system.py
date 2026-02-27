#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🪄 Magic Achievement System for OpenClaw
A magical hidden achievement system with multi-language support and pop culture references.

Author: OpenClaw Community
Version: 1.0.0
"""

import re
import json
import os
from datetime import datetime
from typing import Dict, Optional, List
from dataclasses import dataclass, asdict
from enum import Enum


class Rarity(Enum):
    """成就稀有度等级"""
    COMMON = "common"      # 🥉 普通
    RARE = "rare"          # 🥈 稀有
    EPIC = "epic"          # 🥇 史诗
    LEGENDARY = "legendary" # 💎 传说
    MYTHIC = "mythic"      # 👑 神话


@dataclass
class Achievement:
    """成就数据类"""
    id: str
    name: str
    name_en: str
    name_ja: str
    description: str
    trigger_condition: str
    reference: str
    rarity: Rarity
    category: str
    hidden: bool = True
    unlocked_at: Optional[str] = None
    
    def get_name(self, lang: str = "zh") -> str:
        if lang == "en":
            return self.name_en
        elif lang == "ja":
            return self.name_ja
        return self.name


@dataclass
class PlayerStats:
    """玩家统计数据"""
    player_name: str
    profession: str
    language: str
    total_achievements: int = 0
    unlocked_achievements: List[str] = None
    counters: Dict[str, int] = None
    first_used: Optional[str] = None
    last_used: Optional[str] = None
    streak_days: int = 0
    
    def __post_init__(self):
        if self.unlocked_achievements is None:
            self.unlocked_achievements = []
        if self.counters is None:
            self.counters = {}


# ============================================================================
# 关键词触发配置
# ============================================================================

KEYWORD_TRIGGERS = {
    # 电影梗
    r"月亮|moon|月球": "to_the_moon",
    r"梦|dream|梦境": "inception_architect",
    r"代码|code|编程": "matrix_awakened",
    r"时间|time|时钟": "interstellar_traveler",
    
    # 游戏梗
    r"任务|task|mission": "newbie_graduate",
    r"隐藏|secret|彩蛋": "hidden_boss_finder",
    r"快|fast|速通": "speedrunner",
    r"满级|max level": "max_level_boss",
    
    # 医药研发专属
    r"化合物|compound|分子": "molecular_magician",
    r"CDE|审评|监管": "regulatory_ninja",
    r"数据|data|分析": "data_alchemist",
    r"文献|paper|pubmed": "literature_collector",
    
    # 程序员专属
    r"bug|错误|debug": "bug_hunter",
    r"正则|regex": "regex_wizard",
    r"git|commit": "version_control_master",
    
    # Meme梗
    r"真香|打脸": "true_fragrance",
    r"打工人|加班": "hard_worker",
    r"yyds|永远的神": "yyds",
    r"时间管理": "time_management_master",
    
    # 动漫梗
    r"坚持|努力|奋斗": "naruto_spirit",
    r"目标|梦想|航海": "one_piece_pirate",
    r"突破|创新|天才": "einstein_insight",
}


# ============================================================================
# 累计次数触发配置
# ============================================================================

COUNT_TRIGGERS = {
    "message_count": {
        1: {"id": "first_meeting", "name": "初次见面", "rarity": Rarity.COMMON},
        10: {"id": "chatterbox", "name": "话匣子", "rarity": Rarity.COMMON},
        100: {"id": "chatterbox_king", "name": "话痨", "rarity": Rarity.RARE},
        1000: {"id": "chat_master", "name": "聊天达人", "rarity": Rarity.EPIC},
    },
    "task_completed": {
        1: {"id": "newbie_graduate", "name": "新手村毕业", "rarity": Rarity.COMMON},
        10: {"id": "task_master", "name": "任务达人", "rarity": Rarity.RARE},
        50: {"id": "task_machine", "name": "任务机器", "rarity": Rarity.EPIC},
        100: {"id": "max_level_boss", "name": "满级大佬", "rarity": Rarity.LEGENDARY},
    },
    "pdf_processed": {
        1: {"id": "pdf_newbie", "name": "PDF新手", "rarity": Rarity.COMMON},
        10: {"id": "pdf_skilled", "name": "PDF熟练工", "rarity": Rarity.COMMON},
        50: {"id": "pdf_conqueror", "name": "PDF征服者", "rarity": Rarity.RARE},
        100: {"id": "pdf_master", "name": "PDF大师", "rarity": Rarity.EPIC},
    },
    "excel_created": {
        1: {"id": "excel_newbie", "name": "表格新手", "rarity": Rarity.COMMON},
        10: {"id": "excel_skilled", "name": "表格达人", "rarity": Rarity.RARE},
        50: {"id": "excel_magician", "name": "表格魔术师", "rarity": Rarity.EPIC},
    },
}


# ============================================================================
# 成就模板库
# ============================================================================

ACHIEVEMENT_TEMPLATES = {
    "to_the_moon": Achievement(
        id="to_the_moon",
        name="去月球",
        name_en="To The Moon",
        name_ja="月へ行こう",
        description="飞向月球的美好愿望",
        trigger_condition="询问关于月亮的信息",
        reference="电影《去月球》",
        rarity=Rarity.EPIC,
        category="movie",
    ),
    "newbie_graduate": Achievement(
        id="newbie_graduate",
        name="新手村毕业",
        name_en="Newbie Graduate",
        name_ja="初心者村卒業",
        description="踏上真正的冒险之旅",
        trigger_condition="完成第一个任务",
        reference="RPG游戏新手教程",
        rarity=Rarity.COMMON,
        category="game",
    ),
    "molecular_magician": Achievement(
        id="molecular_magician",
        name="分子魔法师",
        name_en="Molecular Magician",
        name_ja="分子魔法使い",
        description="操纵分子的艺术",
        trigger_condition="分析化合物分子结构",
        reference="哈利波特魔法梗",
        rarity=Rarity.RARE,
        category="profession_pharma",
    ),
    "midnight_watcher": Achievement(
        id="midnight_watcher",
        name="午夜守望者",
        name_en="Midnight Watcher",
        name_ja="真夜中の見守り人",
        description="深夜依然清醒",
        trigger_condition="在凌晨00:00-06:00使用OpenClaw",
        reference="夜猫子文化",
        rarity=Rarity.RARE,
        category="time",
    ),
}


# ============================================================================
# 核心成就系统类
# ============================================================================

class MagicAchievementSystem:
    """魔幻成就系统核心类"""
    
    def __init__(self, player_name: str, language: str = "zh", profession: str = "pharma"):
        self.player_name = player_name
        self.language = language
        self.profession = profession
        self.stats = self._load_stats()
        self.achievements = ACHIEVEMENT_TEMPLATES.copy()
        self.keyword_triggers = KEYWORD_TRIGGERS
        self.count_triggers = COUNT_TRIGGERS
        
    def _get_workspace_dir(self) -> str:
        """获取工作目录"""
        return "/home/node/.openclaw/workspace"
    
    def _load_stats(self) -> PlayerStats:
        """加载玩家统计"""
        stats_file = os.path.join(
            self._get_workspace_dir(),
            "magic_achievements",
            f"{self.player_name}_stats.json"
        )
        
        if os.path.exists(stats_file):
            try:
                with open(stats_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return PlayerStats(**data)
            except Exception as e:
                print(f"Error loading stats: {e}")
        
        return PlayerStats(
            player_name=self.player_name,
            profession=self.profession,
            language=self.language
        )
    
    def _save_stats(self):
        """保存玩家统计"""
        stats_dir = os.path.join(self._get_workspace_dir(), "magic_achievements")
        os.makedirs(stats_dir, exist_ok=True)
        
        stats_file = os.path.join(stats_dir, f"{self.player_name}_stats.json")
        
        try:
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(asdict(self.stats), f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving stats: {e}")
    
    def check_message(self, user_input: str) -> Optional[Dict]:
        """检测关键词触发 - 每次用户输入时调用"""
        if not user_input:
            return None
            
        for pattern, achievement_id in self.keyword_triggers.items():
            if achievement_id in self.stats.unlocked_achievements:
                continue
                
            if re.search(pattern, user_input, re.IGNORECASE):
                if achievement_id in self.achievements:
                    return self._unlock_achievement(achievement_id)
        
        return None
    
    def check_time(self, timestamp: datetime = None) -> Optional[Dict]:
        """检测时间触发 - 会话开始时调用"""
        if timestamp is None:
            timestamp = datetime.now()
        
        hour = timestamp.hour
        
        time_achievements = {
            (0, 6): "midnight_watcher",
        }
        
        for (start, end), achievement_id in time_achievements.items():
            if start <= hour < end:
                if achievement_id not in self.stats.unlocked_achievements:
                    if achievement_id in self.achievements:
                        return self._unlock_achievement(achievement_id)
        
        return None
    
    def increment_counter(self, counter_type: str) -> Optional[Dict]:
        """增加计数器并检查里程碑 - 行为完成后调用"""
        self.stats.counters[counter_type] = self.stats.counters.get(counter_type, 0) + 1
        
        if counter_type in self.count_triggers:
            milestones = self.count_triggers[counter_type]
            current_count = self.stats.counters[counter_type]
            
            for count, achievement_info in milestones.items():
                if current_count == count:
                    achievement_id = achievement_info["id"]
                    if achievement_id not in self.stats.unlocked_achievements:
                        return self._unlock_achievement(achievement_id)
        
        self._save_stats()
        return None
    
    def _unlock_achievement(self, achievement_id: str) -> Optional[Dict]:
        """解锁成就并返回展示信息"""
        achievement = self.achievements.get(achievement_id)
        if not achievement:
            return None
        
        self.stats.unlocked_achievements.append(achievement_id)
        self.stats.total_achievements += 1
        achievement.unlocked_at = datetime.now().isoformat()
        self._save_stats()
        
        return {
            "unlocked": True,
            "achievement": achievement,
            "display_message": self._format_display(achievement),
            "total_unlocked": len(self.stats.unlocked_achievements),
        }
    
    def _format_display(self, achievement: Achievement) -> str:
        """格式化成就展示信息"""
        rarity_icons = {
            Rarity.COMMON: "🥉",
            Rarity.RARE: "🥈",
            Rarity.EPIC: "🥇",
            Rarity.LEGENDARY: "💎",
            Rarity.MYTHIC: "👑",
        }
        
        icon = rarity_icons.get(achievement.rarity, "✨")
        
        return f"""
{'✨' * 15}

叮叮~ {icon} 成就解锁 {icon} 叮叮~

💫 **{achievement.get_name(self.language)}** 💫

{achievement.description}
📚 文化梗: {achievement.reference}
🎯 触发条件: {achievement.trigger_condition}

📊 收集进度: {len(self.stats.unlocked_achievements)} / 500+

{'✨' * 15}
"""
    
    def get_status(self) -> Dict:
        """获取玩家当前状态"""
        return {
            "player_name": self.player_name,
            "profession": self.profession,
            "language": self.language,
            "total_unlocked": len(self.stats.unlocked_achievements),
            "unlocked_achievements": self.stats.unlocked_achievements,
            "counters": self.stats.counters,
        }


def ask_user_preferences() -> Dict:
    """询问用户职业和语言偏好"""
    message = """
🪄 魔幻成就系统初始化

请告诉我：

1. 您的职业是？
   💊 pharma - 医药研发
   💻 programmer - 程序员
   🔬 researcher - 研究员
   👔 manager - 管理者
   📚 student - 学生

2. 语言偏好？
   🇨🇳 zh - 中文
   🇬🇧 en - English
   🇯🇵 ja - 日本語

回复格式: pharma zh
"""
    return {"message": message}


# 便捷使用函数
def check_achievement(player_name: str, trigger_type: str, trigger_data: any, 
                      language: str = "zh", profession: str = "pharma") -> Optional[str]:
    """
    检查是否触发成就
    
    Args:
        player_name: 玩家名称
        trigger_type: 触发类型 (message/time/counter)
        trigger_data: 触发数据
        language: 语言
        profession: 职业
        
    Returns:
        成就展示消息或None
    """
    magic = MagicAchievementSystem(player_name, language, profession)
    
    result = None
    if trigger_type == "message":
        result = magic.check_message(trigger_data)
    elif trigger_type == "time":
        result = magic.check_time(trigger_data)
    elif trigger_type == "counter":
        counter_name, _ = trigger_data
        result = magic.increment_counter(counter_name)
    
    if result and result.get("unlocked"):
        return result["display_message"]
    return None


def get_status(player_name: str, language: str = "zh", profession: str = "pharma") -> Dict:
    """获取玩家状态"""
    magic = MagicAchievementSystem(player_name, language, profession)
    return magic.get_status()


if __name__ == "__main__":
    # 测试代码
    print("🪄 Magic Achievement System")
    print("Testing keyword trigger...")
    
    result = check_achievement("test_user", "message", "今晚月亮好圆")
    if result:
        print(result)
    else:
        print("No achievement triggered")
