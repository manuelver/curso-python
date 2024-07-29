from abc import ABC, abstractmethod


class Movie(ABC):

    id = 0
    name = ''
    type = ''

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.type = None

    def get_name(self):
        return self.name
