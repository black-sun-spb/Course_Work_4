import json
import os

from src.files.abstract_file import AbstractFileHandler


class JSONFileHandler(AbstractFileHandler):
    def __init__(self, filename: str = "vacancies.json") -> None:
        self.__filename = os.path.join("data", filename)

    def read_data(self):
        if not os.path.exists(self.__filename):
            return []
        with open(self.__filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []

    def add_data(self, new_data: list):
        if not isinstance(new_data, list):
            raise ValueError("Данные должны быть списком словарей")

        existing_data = self.read_data()
        existing_urls = {item.get("url") for item in existing_data if "url" in item}

        filtered_new = []
        for item in new_data:
            url = item.get("url")
            if url is None or url not in existing_urls:
                filtered_new.append(item)
                if url:
                    existing_urls.add(url)

        all_data = existing_data + filtered_new

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)

    def remove_data(self, url_to_remove):
        if not url_to_remove:
            return
        data = self.read_data()
        filtered = [item for item in data if item.get("url") != url_to_remove]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(filtered, f, ensure_ascii=False, indent=4)
