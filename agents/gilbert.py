from core.agent import Agent


class GilbertAgent(Agent):
    """
    Primeiro agente oficial do Project Gilbert.
    """

    name = "gilbert"

    def execute(self, task: str):

        return (
            f"Gilbert recebeu a tarefa: {task}"
        )
