from abc import ABC, abstractmethod
from typing import Generic


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        raise NotImplementedError

    def describe(self) -> str:
        return f"The creature {self.name} is {self.type}"


class Flameling(Creature):
    pass


class Pyrodon(Creature):
    pass


class Aquabub(Creature):
    pass


class Torragon(Creature):
    pass
