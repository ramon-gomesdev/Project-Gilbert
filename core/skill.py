class Skill:
    """
    Classe base para todas as skills do Project Gilbert.
    """

    name = None

    def execute(self):
        """
        Toda skill deve implementar este método.
        """

        raise NotImplementedError(
            "Toda skill deve implementar execute()."
        )
