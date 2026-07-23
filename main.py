from core.router import Router
from core.executor import Executor
from core.skill_manager import SkillManager

from agents.gilbert import GilbertAgent
from skills.system import SystemSkill


def main():

    # Criando gerenciador de skills
    skill_manager = SkillManager()

    skill_manager.register(
        "system",
        SystemSkill()
    )

    # Criando agentes
    gilbert = GilbertAgent(
        skill_manager
    )

    agents = {
        "gilbert": gilbert
    }

    # Criando núcleo de execução
    router = Router()

    executor = Executor(
        skill_manager,
        agents
    )

    # Entrada do usuário
    tarefa = "Mostre informações do sistema"

    # Entende a intenção
    intent = router.route(
        tarefa
    )

    print("Intenção:")
    print(intent)

    print()

    # Executa
    resposta = executor.execute(
        intent
    )

    print("Resposta:")
    print(resposta)


if __name__ == "__main__":
    main()
