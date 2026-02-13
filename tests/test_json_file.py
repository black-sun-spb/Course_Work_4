import os
import tempfile
import unittest

from src.files.json_file import JSONFileHandler


class TestJSONFileHandler(unittest.TestCase):

    def setUp(self):
        # Создаём временный файл для тестов
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()
        self.handler = JSONFileHandler(self.test_file.name)

    def tearDown(self):
        os.unlink(self.test_file.name)

    def test_add_and_read_data(self):
        data = [
            {"title": "Vac1", "salary": 100, "url": "url1", "company": "Company1"},
            {"title": "Vac2", "salary": 200, "url": "url2", "company": "Company2"},
        ]
        self.handler.add_data(data)
        read_back = self.handler.read_data()
        self.assertEqual(len(read_back), 2)
        self.assertTrue(any(v["title"] == "Vac1" for v in read_back))

    def test_no_duplicates(self):
        data1 = [{"title": "Vac1", "salary": 100, "url": "url1", "company": "Company1"}]
        data2 = [{"title": "Vac1", "salary": 100, "url": "url1", "company": "Company1"}]
        self.handler.add_data(data1)
        self.handler.add_data(data2)  # Добавляем те же данные
        read_back = self.handler.read_data()
        self.assertEqual(len(read_back), 1)  # Дубликатов нет

    def test_remove_data(self):
        data = [
            {"title": "Vac1", "salary": 100, "url": "url1", "company": "Company1"},
            {"title": "Vac2", "salary": 200, "url": "url2", "company": "Company2"},
        ]
        self.handler.add_data(data)
        self.handler.remove_data("url1")
        read_back = self.handler.read_data()
        self.assertEqual(len(read_back), 1)
        self.assertEqual(read_back[0]["url"], "url2")


if __name__ == "__main__":
    unittest.main()
