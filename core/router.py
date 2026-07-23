class Router:
    """
    Responsável por direcionar tarefas para os agentes corretos.
    """

    def route(self, task: str):
        """
        Analisa uma tarefa e retorna o agente responsável.
        """

        task = task.lower()

        if "código" in task or "programação" in task:
            return "coding_agent"

        if "pesquisa" in task or "buscar" in task:
            return "research_agent"

        return "gilbert_agent"
