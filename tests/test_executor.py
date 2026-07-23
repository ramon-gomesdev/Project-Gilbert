from core.executor import Executor


class TestSkill:

    def execute(self):
        return "Skill executada"


class TestAgent:

    def execute(self, task):
        return f"Agente executou: {task}"


class TestSkillManager:

    def get(self, name):
        return TestSkill()


executor = Executor(
    TestSkillManager(),
    {
        "teste": TestAgent()
    }
)


print(
    executor.execute(
        {
            "type": "skill",
            "name": "teste"
        }
    )
)


print(
    executor.execute(
        {
            "type": "agent",
            "name": "teste"
        }
    )
)
