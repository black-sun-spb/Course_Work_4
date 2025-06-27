from typing import Any, Dict, List, Optional

import requests

from src.api.abstract_api import AbstractAPI
from src.models.vacancy import Vacancy


class HHAPI(AbstractAPI):
    __BASE_URL: str = "https://api.hh.ru/vacancies"

    def __init__(self) -> None:
        self.__session = requests.Session()

    def __connect(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Приватный метод подключения к API hh.ru.

        Args:
            params (Optional[Dict[str, Any]]): Параметры запроса.

        Returns:
            Dict[str, Any]: Данные ответа в формате JSON.

        Raises:
            ConnectionError: Если статус ответа не 200.
        """
        response = self.__session.get(self.__BASE_URL, params=params)
        if response.status_code != 200:
            raise ConnectionError(
                f"Ошибка соединения с API hh.ru: статус {response.status_code}"
            )
        return response.json()

    def _connect(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Реализация абстрактного метода подключения.

        Args:
            params (Optional[Dict[str, Any]]): Параметры запроса.

        Returns:
            Dict[str, Any]: Данные ответа.
        """
        return self.__connect(params=params)

    def get_vacancies(self, keyword: str, per_page: int = 20) -> List[Vacancy]:
        """
        Получает вакансии с hh.ru по ключевому слову.

        Args:
            keyword (str): Ключевое слово для поиска.
            per_page (int): Количество вакансий на страницу.

        Returns:
            List[Vacancy]: Список объектов вакансий.
        """
        params = {"text": keyword, "per_page": per_page}
        data = self.__connect(params=params)
        raw_vacancies = data.get("items", [])

        vacancies: List[Vacancy] = []
        for item in raw_vacancies:
            title: str = item.get("name", "")
            url: str = item.get("alternate_url", "")
            company: str = item.get("employer", {}).get("name", "Unknown")

            salary_data = item.get("salary")
            salary: float = 0.0
            if salary_data:
                salary_from = salary_data.get("from")
                salary_to = salary_data.get("to")
                if salary_from is not None and salary_to is not None:
                    salary = (salary_from + salary_to) / 2
                elif salary_from is not None:
                    salary = salary_from
                elif salary_to is not None:
                    salary = salary_to

            try:
                vac = Vacancy(title=title, salary=salary, url=url, company=company)
                vacancies.append(vac)
            except ValueError:
                # Пропускаем некорректные вакансии
                continue

        return vacancies
