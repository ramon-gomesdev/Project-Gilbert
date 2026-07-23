class Executor:
    """
    Responsável por executar intenções identificadas pelo Router.
    """

    def __init__(self, skill_manager, agents):
        self.skill_manager = skill_manager
        self.agents = agents

    def execute(self, intent):
        """
        Executa uma intenção recebida.
        """

        if intent["type"] == "skill":

            skill = self.skill_manager.get(
                intent["name"]
            )

            if skill:
                return skill.execute()

            return "Skill não encontrada."

        if intent["type"] == "agent":

            agent = self.agents.get(
                intent["name"]
            )

            if agent:
                return agent.execute(
                    "Tarefa recebida"
                )

            return "Agente não encontrado."

        return "Tipo de intenção desconhecido."
