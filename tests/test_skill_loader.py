from core.skill_manager import SkillManager
from core.skill_loader import SkillLoader


manager = SkillManager()

loader = SkillLoader(manager)

loader.load()


print(
    manager.list_skills()
)
