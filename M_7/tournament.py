from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2.strategy import BattleStrategy, InvalidStrategyError
from ex0.creature import Creature
from typing import List, Tuple
from ex0.factory import FlameFactory, AquaFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory


def battle(lista: List[Tuple[Creature, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(lista)} opponents involved")
    print()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            try:
                creature1, strategy1 = lista[i]
                creature2, strategy2 = lista[j]
                print("* Battle *")
                print(creature1.describe())
                print("\tvs")
                print(creature2.describe())
                print("now fight!")
                strategy1.act(creature1)
                strategy2.act(creature2)
                print()
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == '__main__':
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    agressive = AggressiveStrategy()
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    aqua_base = aqua_factory.create_base()
    flame_base = flame_factory.create_base() 
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    transform_base = transform_factory.create_base()
    healing_base = healing_factory.create_base()
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame_base, normal), (healing_base, defensive)])
    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_base, agressive), (healing_base, defensive)])
    print()
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), \
(Transform+Aggressive) ]")
    battle([
        (aqua_base, normal),
        (healing_base, defensive),
        (transform_base, agressive)
    ])
