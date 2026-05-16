import random


def main() -> None:
    lista: list = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]
    print(f"Initial list of playears: {lista}")
    all_lista_capit: list = [x for x in lista if x == str.capitalize(x)]
    new_lista_capit: list = [str.capitalize(x) for x in lista]
    print(f"New list with all names capitalized: {new_lista_capit}")
    print(f"New list of capitalized names only {all_lista_capit}")
    # The subject allow if it pass line size
    dici: dict[str, int] = {
        nome: random.randint(0, 600) for nome in all_lista_capit
    }
    print(f"Score dict: {dici}")
    total_value: int = 0
    for value in dici.values():
        total_value += value
    print(f"Score average is {round(total_value / len(dici))}")
    # The subject allow if it pass line size
    high_score: dict = {
        nome: score for (nome, score) in dici.items() if score > 300
    }
    print(f"High Scores: {high_score}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{e}")
