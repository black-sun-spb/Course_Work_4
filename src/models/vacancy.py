class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self._parse_salary(salary)
        self.description = description

    def _parse_salary(self, salary):
        if salary is None:
            return 0
        return salary.get("from") or salary.get("to") or 0

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __repr__(self):
        return f"{self.title} ({self.salary} руб): {self.url}"

    @classmethod
    def cast_to_object_list(cls, vacancies_json: list):
        return [
            cls(
                v["name"],
                v["alternate_url"],
                v["salary"],
                v["snippet"]["requirement"] or ""
            )
            for v in vacancies_json
        ]
