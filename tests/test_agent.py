from core.agent import Agent


class TestAgent(Agent):
    def execute(self, task: str):
        return f"Executando: {task}"


agent = TestAgent("Teste")

print(agent.name)
print(agent.execute("primeira tarefa"))
