from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from src.models.vacancy import Vacancy


class AbstractAPI(ABC):
    @abstractmethod
    def _connect(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Защищённый метод подключения к API.

        Args:
            params (Optional[Dict[str, Any]]): Параметры для запроса.

        Returns:
            Dict[str, Any]: JSON-ответ от API.
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Vacancy]:
        """
        Получить вакансии по ключевому слову.

        Args:
            keyword (str): Строка запроса для поиска вакансий.

        Returns:
            List[Vacancy]: Список вакансий.
        """
        pass
