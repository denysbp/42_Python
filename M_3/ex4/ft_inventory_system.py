import sys


def parse_args() -> dict:
    args: dict[str, int] = dict()
    lista: list = sys.argv
    if (len(lista) == 1):
        print("There is no args in inventory")
        return {}
    for arg in lista:
        item: str = arg
        if ":" not in item:
            continue
        key: str
        val: str
        try:
            key, val = item.split(":", 1)
            args[key] = int(val)
        except ValueError:
            raise SyntaxError("Wrong format: <item_name>:<quantity>")
    return args


def main() -> None:
    args: dict = parse_args()
    value: int = sum(args.values())
    print(f"Got inventory: {args}")
    print(f"Item List: {list(args.keys())}")
    print(f"Total quantity of the {len(args)} items: {value}")
    for key, item in args.items():
        percentagem: float = round((item / value) * 100)
        print(f"Item {key} represents {percentagem}%")
    maior_item: str
    maior_value: int = 0
    for key, value in args.items():
        if value > maior_value:
            maior_value = value
            maior_item = key
    print(f"The most abundant: {maior_item} with {maior_value}")
    menor_item: str
    menor_value: int
    ok: int = 1
    for key, value in args.items():
        if ok:
            menor_value = value
            ok = 0
        elif value < menor_value:
            menor_value = value
            menor_item = key
    print(f"The leat abundant: {menor_item} with {menor_value}")
    args.update({"money": 1000})
    print(f"Update inventory: {args}")


if __name__ == '__main__':
    try:
        parse_args()
    except Exception as e:
        print(f"{e}")
