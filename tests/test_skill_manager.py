from core.skill_manager import SkillManager
from skills.system import SystemSkill


manager = SkillManager()

manager.register(
    "system",
    SystemSkill()
)

print(manager.list_skills())

skill = manager.get("system")

print(skill.execute())
