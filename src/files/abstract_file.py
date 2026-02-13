from abc import ABC, abstractmethod


class AbstractFileHandler(ABC):
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def add_data(self, data):
        pass

    @abstractmethod
    def remove_data(self, identifier):
        pass
