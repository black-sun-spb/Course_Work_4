import json
from .base_saver import BaseSaver

class JSONSaver(BaseSaver):
    def __init__(self, path="data/vacancies.json"):
        self.path = path

    def add_vacancy(self, vacancy):
        data = self._load()
        data.append(vacancy.__dict__)
        self._save(data)

    def get_vacancies(self, filter_func=lambda x: True):
        data = self._load()
        return [v for v in data if filter_func(v)]

    def delete_vacancy(self, vacancy):
        data = self._load()
        data = [v for v in data if v["url"] != vacancy.url]
        self._save(data)

    def _load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
