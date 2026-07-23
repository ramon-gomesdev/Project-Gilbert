from core.agent import Agent
from skills.system import SystemSkill


class GilbertAgent(Agent):
    """
    Primeiro agente oficial do Project Gilbert.
    """

    def __init__(self):
        super().__init__("Gilbert")

        self.system_skill = SystemSkill()

    def execute(self, task: str):
        """
        Executa uma tarefa recebida pelo Gilbert.
        """

        task = task.lower()

        if "sistema" in task:
            info = self.system_skill.get_system_info()

            return (
                f"Sistema: {info['sistema']}\n"
                f"Versão: {info['versao']}\n"
                f"Arquitetura: {info['maquina']}\n"
                f"Python: {info['python']}"
            )

        return f"Gilbert recebeu a tarefa: {task}"
