import json
from pathlib import Path


class Memory:
    """
    Sistema simples de memória do Project Gilbert.
    """

    def __init__(self, file_path="memory.json"):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self._create_memory()

    def _create_memory(self):
        data = {
            "history": [],
            "preferences": []
        }

        self.file_path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )

    def load(self):
        return json.loads(
            self.file_path.read_text(
                encoding="utf-8"
            )
        )

    def save(self, key, value):
        data = self.load()

        data[key].append(value)

        self.file_path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )
