import platform
import sys


class SystemSkill:
    """
    Skill responsável por informações do sistema.
    """

    def get_system_info(self):
        return {
            "sistema": platform.system(),
            "versao": platform.version(),
            "maquina": platform.machine(),
            "python": sys.version.split()[0]
        }
