from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.abilites import TransformCapability, HealCapability
from typing import cast


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"The {creature.name} is \
not valid for this method")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"The {creature.name} is \
not valid for this method")
        tcreature = cast(TransformCapability, creature)
        print(tcreature.transform())
        print(creature.attack())
        print(tcreature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"The {creature.name} is \
not valid for this method")
        hcreature = cast(HealCapability, creature)
        print(creature.attack())
        print(hcreature.heal())
