import platform
import sys

from core.skill import Skill


class SystemSkill(Skill):
    """
    Skill responsável por informações do sistema.
    """

    name = "system"

    def execute(self):

        return (
            f"Sistema: {platform.system()}\n"
            f"Versão: {platform.version()}\n"
            f"Arquitetura: {platform.machine()}\n"
            f"Python: {sys.version.split()[0]}"
        )
