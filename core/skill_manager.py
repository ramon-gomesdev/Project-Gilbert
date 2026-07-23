from core.skill import Skill


class SkillManager:
    """
    Gerenciador responsável por registrar e executar skills.
    """

    def __init__(self):
        self.skills = {}

    def register(self, name: str, skill: Skill):
        """
        Registra uma nova skill.
        """

        if not isinstance(skill, Skill):
            raise TypeError(
                "A skill deve herdar da classe Skill."
            )

        self.skills[name] = skill

    def get(self, name: str):
        """
        Retorna uma skill registrada.
        """

        return self.skills.get(name)

    def list_skills(self):
        """
        Lista todas as skills disponíveis.
        """

        return list(self.skills.keys())
