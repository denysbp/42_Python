from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    action_list: list = [
        "Run",
        "Walk",
        "Cry",
        "Laught",
        "Go to the bathroom",
        "Cagar",
        "Get a job",
        "Fired",
        "Nothing",
        "Listen to Spotify",
        "Get black hole",
        "Reproved",
        "T-rex",
        "Study",
        "code",
        "Drive",
        "Draw",
        "git push",
        "git add",
        "git commit",
        "Drink(water)",
        "Smoke(O2)",
    ]
    name_list: list = [
        "Denys",
        "Paulo",
        "Pedro",
        "Lucas",
        "Mariana",
        "Joao",
        "Sofia",
        "Tiago",
        "Carla",
        "Miguel",
        "Beatriz",
        "Andre",
        "Rita",
        "Afonso",
        "Diana"
    ]
    name: str = random.choice(name_list)
    action: str = random.choice(action_list)
    while True:
        yield (name, action)


list_10: list[tuple] = list()
for i in range(0, 10):
    list_10.append(next(gen_event()))


def consume_event(list_10: list[tuple]) -> \
        Generator[tuple[str, str], None, None]:
    while list_10 is not None:
        choice: tuple = random.choice(list_10)
        list_10.remove(choice)
        yield choice


def main() -> None:
    for i in range(1, 1001):
        dados: tuple = next(gen_event())
        print(f"Event {i} : {dados[0]} did action {dados[1]}")
    print(f"Built list of 10 events: {list_10}")
    while list_10 is not None:
        try:
            print(f"Got event from list: {next(consume_event(list_10))}")
            print(f"Remain in list: {list_10}")
        except Exception:
            return


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{e}")
