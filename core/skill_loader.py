from pathlib import Path
import importlib


class SkillLoader:
    """
    Descobre e carrega skills automaticamente.
    """

    def __init__(self, manager):
        self.manager = manager

    def load(self):

        skills_path = Path("skills")

        for file in skills_path.glob("*.py"):

            if file.name.startswith("__"):
                continue

            module_name = (
                f"skills.{file.stem}"
            )

            module = importlib.import_module(
                module_name
            )

            for item in dir(module):

                obj = getattr(
                    module,
                    item
                )

                if (
                    isinstance(obj, type)
                    and obj.__name__.endswith("Skill")
                ):
                    skill = obj()

                    self.manager.register(
                        file.stem,
                        skill
                    )
