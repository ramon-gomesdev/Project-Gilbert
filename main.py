from agents.gilbert import GilbertAgent
from core.skill_manager import SkillManager
from skills.system import SystemSkill


def main():

    skill_manager = SkillManager()

    skill_manager.register(
        "system",
        SystemSkill()
    )

    gilbert = GilbertAgent(
        skill_manager
    )

    resposta = gilbert.execute(
        "Mostre informações do sistema"
    )

    print(resposta)


if __name__ == "__main__":
    main()
