class Agent:
    """
    Classe base para todos os agentes do Project Gilbert.
    """

    name = None

    def __init__(self, skill_manager=None):

        if self.name is None:
            raise ValueError(
                "Todo agente deve possuir um nome."
            )

        self.skill_manager = skill_manager

    def execute(self, task: str):
        """
        Método obrigatório para agentes.
        """

        raise NotImplementedError(
            "Todo agente deve implementar execute()."
        )
