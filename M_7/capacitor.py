from typing import cast
from ex1.abilites import HealCapability, TransformCapability
from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == '__main__':
    heal = HealingCreatureFactory()
    mutant = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    print("base:")
    heal_base = heal.create_base()
    heal_base_cap = cast(HealCapability, heal_base)
    print(heal_base.describe())
    print(heal_base.attack())
    print(heal_base_cap.heal())

    print("evolved:")
    heal_evolved = heal.create_evolved()
    heal_evolved_cap = cast(HealCapability, heal_evolved)
    print(heal_evolved.describe())
    print(heal_evolved.attack())
    print(heal_evolved_cap.heal())

    print("\n")

    print("Testing Creature with transform capability")
    print("base:")
    mutant_base = mutant.create_base()
    mutant_base_cap = cast(TransformCapability, mutant_base)
    print(mutant_base.describe())
    print(mutant_base_cap.transform())
    print(mutant_base.attack())
    print(mutant_base_cap.revert())

    print("evolved: ")
    mutant_evolved = mutant.create_evolved()
    mutant_evolved_cap = cast(TransformCapability, mutant_evolved)
    print(mutant_evolved.describe())
    print(mutant_evolved.attack())
    print(mutant_evolved_cap.transform())
    print(mutant_evolved_cap.revert())
