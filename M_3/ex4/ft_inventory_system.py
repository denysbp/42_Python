import sys


def parse_args() -> dict:
    args: dict[str, int] = dict()
    lista: list = sys.argv[1:]
    if (len(lista) == 0):
        print("There is no args in inventory")
        return {}
    for arg in lista:
        item: str = arg
        if ":" not in item:
            print(f"Item rejeitado: {item}")
            continue
        key: str
        val: str
        try:
            key, val = item.split(":", 1)
            args[key] = int(val)
        except ValueError:
            print(f"Wrong format for {val}: <item_name>:<quantity>")
            continue
    return args


def main() -> None:
    args: dict = parse_args()
    values: int = sum(args.values())
    print(f"Got inventory: {args}")
    print(f"Item List: {list(args.keys())}")
    print(f"Total quantity of the {len(args)} items: {values}")
    for key, qty in args.items():
        try:
            percentagem: float = round((qty / values) * 100)
            print(f"Item {key} represents {percentagem}%")
        except ZeroDivisionError as e:
            print(f"We caught {e}")
    maior_item: str = ""
    maior_value: int = 0
    ok_1: int = 1
    for key, value in args.items():
        if ok_1:
            maior_value = value
            maior_item = key
            ok_1 = 0
        if value > maior_value:
            maior_value = value
            maior_item = key
    print(f"The most abundant: {maior_item} with {maior_value}")
    menor_item: str = ""
    menor_value: int = 0
    ok: int = 1
    for key, value in args.items():
        if ok:
            menor_value = value
            menor_item = key
            ok = 0
        elif value < menor_value:
            menor_value = value
            menor_item = key
    print(f"The least abundant: {menor_item} with {menor_value}")
    args.update({"money": 1000})
    print(f"Update inventory: {args}")


if __name__ == '__main__':
    main()
