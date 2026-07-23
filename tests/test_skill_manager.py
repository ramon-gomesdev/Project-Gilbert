from core.skill_manager import SkillManager


class TestSkill:
    pass


manager = SkillManager()

manager.register(
    "teste",
    TestSkill()
)


print(manager.list_skills())

skill = manager.get("teste")

print(skill)
