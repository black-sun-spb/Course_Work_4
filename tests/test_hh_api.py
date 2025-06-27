import unittest
from unittest.mock import patch

from src.api.hh_api import HHAPI
from src.models.vacancy import Vacancy


class TestHHAPI(unittest.TestCase):
    def setUp(self):
        self.api = HHAPI()

    def test_get_vacancies_returns_list_of_vacancies(self):
        vacancies = self.api.get_vacancies("python", per_page=5)
        self.assertIsInstance(vacancies, list)
        self.assertTrue(all(isinstance(v, Vacancy) for v in vacancies))

    def test_vacancy_attributes(self):
        vacancies = self.api.get_vacancies("python", per_page=1)
        if vacancies:
            vac = vacancies[0]
            self.assertIsInstance(vac.title, str)
            self.assertIsInstance(vac.salary, float)
            self.assertIsInstance(vac.url, str)
            self.assertIsInstance(vac.company, str)


if __name__ == "__main__":
    unittest.main()


@patch("src.api.hh_api.requests.Session.get")
def test_get_vacancies_returns_list(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [
            {
                "name": "Python Dev",
                "alternate_url": "https://hh.ru/vac1",
                "employer": {"name": "Company A"},
                "salary": {"from": 100000, "to": 150000},
            }
        ]
    }

    api = HHAPI()
    vacancies = api.get_vacancies("Python")

    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Dev"
    assert vacancies[0].salary == 125000
