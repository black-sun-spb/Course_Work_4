from typing import Union


class Vacancy:
    """
    Класс для представления вакансии.

    Атрибуты:
        title (str): Название вакансии.
        salary (float): Зарплата.
        url (str): Ссылка на вакансию.
        company (str): Название компании.
    """

    __slots__ = ("_title", "_salary", "_url", "_company")

    def __init__(
        self, title: str, salary: Union[int, float], url: str, company: str
    ) -> None:
        self._title: str = self.__validate_str(title, "title")
        self._salary: float = self.__validate_salary(salary)
        self._url: str = self.__validate_str(url, "url")
        self._company: str = self.__validate_str(company, "company")

    def __validate_str(self, value: str, field_name: str) -> str:
        """
        Проверка, что значение — непустая строка.

        Args:
            value (str): Значение.
            field_name (str): Название поля для сообщения об ошибке.

        Returns:
            str: Очищенная строка.

        Raises:
            ValueError: Если строка пустая или не строка.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")
        return value.strip()

    def __validate_salary(self, value: Union[int, float]) -> float:
        """
        Проверка и преобразование зарплаты.

        Args:
            value (Union[int, float]): Зарплата.

        Returns:
            float: Зарплата как float.

        Raises:
            ValueError: Если зарплата отрицательная.
        """
        if not isinstance(value, (int, float)):
            return 0.0
        if value < 0:
            raise ValueError("salary must be non-negative")
        return float(value)

    @property
    def title(self) -> str:
        return self._title

    @property
    def salary(self) -> float:
        return self._salary

    @property
    def url(self) -> str:
        return self._url

    @property
    def company(self) -> str:
        return self._company

    def to_dict(self) -> dict:
        """
        Представление объекта как словаря (например, для JSON).

        Returns:
            dict: Словарь с данными вакансии.
        """
        return {
            "title": self.title,
            "salary": self.salary,
            "url": self.url,
            "company": self.company,
        }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __repr__(self) -> str:
        return f"Vacancy(title={self.title!r}, salary={self.salary}, company={self.company!r})"
