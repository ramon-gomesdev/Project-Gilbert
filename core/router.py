class Router:
    """
    Responsável por identificar a melhor ação para uma tarefa.
    """

    def route(self, task: str):
        """
        Analisa uma tarefa e retorna a intenção.
        """

        task = task.lower()

        if "sistema" in task or "computador" in task:
            return {
                "type": "skill",
                "name": "system"
            }

        if (
            "pesquisa" in task
            or "pesquise" in task
            or "buscar" in task
            or "procure" in task
        ):
            return {
                "type": "skill",
                "name": "research"
            }

        if "código" in task or "programação" in task:
            return {
                "type": "agent",
                "name": "coding_agent"
            }

        return {
            "type": "agent",
            "name": "gilbert"
        }
