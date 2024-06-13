from abc import ABC, abstractmethod


class Location(ABC):
    

    @abstractmethod
    def __init__(self, name, message):
        self._name = name
        self._message = message

    