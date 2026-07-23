from core.agent import Agent
from core.skill_manager import SkillManager


class GilbertAgent(Agent):
    """
    Primeiro agente oficial do Project Gilbert.
    """

    def __init__(self, skill_manager: SkillManager):
        super().__init__("Gilbert")

        self.skill_manager = skill_manager

    def execute(self, task: str):
        """
        Executa uma tarefa recebida pelo Gilbert.
        """

        task = task.lower()

        if "sistema" in task:

            system_skill = self.skill_manager.get("system")

            info = system_skill.get_system_info()

            return (
                f"Sistema: {info['sistema']}\n"
                f"Versão: {info['versao']}\n"
                f"Arquitetura: {info['maquina']}\n"
                f"Python: {info['python']}"
            )

        return f"Gilbert recebeu a tarefa: {task}"
