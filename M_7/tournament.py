from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2.strategy import BattleStrategy
from ex0.factory import CreatureFactory
from typing import List, Tuple


def battle(lista: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print(lista)
    print("*** Tournament ***")
    print(f"{len(lista)} opponents involved")
    print("* Battle *")
    creature = lista[0][0]
    strategy1 = lista[0][1]
    opponet = lista[1][0]
    strategy = lista[1][1]
    strategy1.act(creature)
    