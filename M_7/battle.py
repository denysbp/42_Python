from ex0 import FlameFactory, AquaFactory, CreatureFactory


if __name__ == '__main__':
    flame = FlameFactory()
    aqua = AquaFactory()

    def create_factory(obj: CreatureFactory) -> None:
        print("Testing factory")
        print("Testing create_base()")
        based = obj.create_base()
        print(based.describe())
        print(based.attack())
        print("Testing create_envolved()")
        envoled = obj.create_evolved()
        print(envoled.describe())
        print(envoled.attack())

    def fight(aqua: AquaFactory, flame: FlameFactory):
        base_flame = flame.create_base()
        aqua_base = aqua.create_base()

        print(base_flame.describe())
        print("\t\t vs")
        print(aqua_base.describe())

        print("\t fight")
        print(base_flame.attack())
        print(aqua_base.attack())

    create_factory(flame)
    print("\n")
    create_factory(aqua)

    fight(aqua, flame)
