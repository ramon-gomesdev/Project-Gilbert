class Agent:
    """
    Classe base para todos os agentes do Project Gilbert.
    """

    def __init__(self, name: str):
        self.name = name

    def execute(self, task: str):
        """
        Executa uma tarefa recebida pelo agente.
        """
        raise NotImplementedError(
            "Cada agente deve implementar seu próprio método execute()."
        )
