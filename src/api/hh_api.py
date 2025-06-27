import requests
from .base_api import BaseAPI

class HeadHunterAPI(BaseAPI):
    def get_vacancies(self, keyword: str) -> list:
        url = "https://api.hh.ru/vacancies"
        params = {"text": keyword, "area": 113, "per_page": 50}
        response = requests.get(url, params=params)
        return response.json()["items"]
