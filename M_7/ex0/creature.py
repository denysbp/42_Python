from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        super().__init__()
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature."


class Flameling(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self) -> str:
        return "Flameling uses Ember!"

    def describe(self):
        return super().describe()


class Pyrodon(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"

    def describe(self):
        return super().describe()


class Aquabub(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"

    def describe(self):
        return super().describe()


class Torragon(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"

    def describe(self):
        return super().describe()


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...
