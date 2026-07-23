from core.agent import Agent


class GilbertAgent(Agent):
    """
    Primeiro agente oficial do Project Gilbert.
    """

    def __init__(self):
        super().__init__("Gilbert")

    def execute(self, task: str):
        """
        Executa uma tarefa recebida.
        """

        return f"Gilbert recebeu a tarefa: {task}"
