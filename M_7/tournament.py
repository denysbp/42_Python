from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2.strategy import BattleStrategy
from ex0.factory import CreatureFactory
from typing import List, Tuple
from ex0.factory import FlameFactory, AquaFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory


def battle(lista: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(lista)} opponents involved")
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            try:
                creature1, strategy1 = lista[i]
                creature2, strategy2 = lista[j]
                print(f"[({creature1.name}+\
{strategy1.__class__.__name__.replace("Strategy", "")}), ", end="")
                print(f"({creature2.name}+\
{strategy2.__class__.__name__.replace("Strategy", "")})]")
                print("* Battle *")
                print(creature1.describe())
                print("\tvs")
                print(creature2.describe())
                print("now fight!")
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(f"Battle error, aborting tournament {e}")
                return


if __name__ == '__main__':
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    agressive = AggressiveStrategy()
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    aqua_base = aqua_factory.create_base()
    aqua_evolved = aqua_factory.create_evolved()
    flame_base = flame_factory.create_base()
    flame_evolved = flame_factory.create_evolved()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    transform_base = transform_factory.create_base()
    transform_evolved = transform_factory.create_evolved()
    healing_base = healing_factory.create_base()
    healing_evolved = healing_factory.create_evolved()
    lista = [
        (flame_base, normal),
        (aqua_base, normal),
        (flame_evolved, normal),
        (aqua_evolved, normal),
        (healing_base, defensive),
        (transform_base, agressive),
        (healing_evolved, defensive),
        (transform_evolved, agressive),
        (healing_evolved, agressive),
        (transform_evolved, defensive)
    ]
    battle(lista)
