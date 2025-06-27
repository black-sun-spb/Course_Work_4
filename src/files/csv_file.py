import csv
import os

from src.files.abstract_file import AbstractFileHandler


class CSVFileHandler(AbstractFileHandler):

    def __init__(self, filename="vacancies.csv"):
        self.__filename = filename

    def read_data(self):
        if not os.path.exists(self.__filename):
            return []
        with open(self.__filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def add_data(self, new_data: list):
        # Здесь должна быть логика добавления без дублей, например по url
        pass

    def remove_data(self, identifier):
        # Логика удаления по идентификатору
        pass
