from abc import ABC, abstractmethod


class BaseSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, filter_func=lambda x: True):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
