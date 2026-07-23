import platform
import sys


class SystemSkill:
    """
    Skill responsável por informações do sistema.
    """

    def execute(self):
        info = self.get_system_info()

        return (
            f"Sistema: {info['sistema']}\n"
            f"Versão: {info['versao']}\n"
            f"Arquitetura: {info['maquina']}\n"
            f"Python: {info['python']}"
        )

    def get_system_info(self):

        return {
            "sistema": platform.system(),
            "versao": platform.version(),
            "maquina": platform.machine(),
            "python": sys.version.split()[0]
        }
