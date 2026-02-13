import unittest

import pytest

from src.models.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_valid_creation(self):
        vac = Vacancy("Python Developer", 120000, "https://hh.ru/vacancy/1", "CompanyX")
        self.assertEqual(vac.title, "Python Developer")
        self.assertEqual(vac.salary, 120000)
        self.assertEqual(vac.url, "https://hh.ru/vacancy/1")
        self.assertEqual(vac.company, "CompanyX")

    def test_invalid_title(self):
        with self.assertRaises(ValueError):
            Vacancy("", 100000, "url", "company")

    def test_invalid_salary_negative(self):
        with self.assertRaises(ValueError):
            Vacancy("title", -100, "url", "company")

    def test_salary_zero_or_none(self):
        vac = Vacancy("title", 0, "url", "company")
        self.assertEqual(vac.salary, 0)

        vac2 = Vacancy("title", None, "url", "company")
        self.assertEqual(
            vac2.salary, 0
        )  # Если None передать — валидация в данном варианте упадет, можно поправить.

    def test_comparison(self):
        vac1 = Vacancy("A", 100, "url", "c")
        vac2 = Vacancy("B", 200, "url", "c")
        self.assertTrue(vac1 < vac2)
        self.assertTrue(vac2 > vac1)
        self.assertFalse(vac1 == vac2)
        vac3 = Vacancy("C", 100, "url", "c")
        self.assertTrue(vac1 == vac3)


if __name__ == "__main__":
    unittest.main()


def test_invalid_company():
    with pytest.raises(ValueError):
        Vacancy("Python", 100000, "https://url", "")


def test_repr():
    vac = Vacancy("Python", 100000, "url", "Yandex")
    assert repr(vac) == "Vacancy(title='Python', salary=100000.0, company='Yandex')"


def test_equality_and_comparison():
    v1 = Vacancy("Dev", 100000, "url1", "A")
    v2 = Vacancy("Dev2", 100000, "url2", "B")
    v3 = Vacancy("Dev3", 120000, "url3", "C")
    assert v1 == v2
    assert v1 < v3
