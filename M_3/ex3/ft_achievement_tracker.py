import random


def gen_player_achievements() -> set:
    ACHIVEMENTS: list = [
        "Rank_0",
        "Rank_1",
        "Rank_2",
        "Rank_3",
        "Rank_4",
        "Rank_5",
        "Rank_6",
        "Master Mind",
        "Pace 8",
        "Piscine Reload",
        "Tumo",
        "life Guard"
    ]
    total: int = random.randint(1, len(ACHIVEMENTS))
    player: set = set()
    c: int = 0
    while c < total:
        player.add(random.choice(ACHIVEMENTS))
        c += 1
    return player


def main() -> None:
    p1: set = gen_player_achievements()
    p2: set = gen_player_achievements()
    p3: set = gen_player_achievements()
    p4: set = gen_player_achievements()
    all: set = p1.union(
        p2,
        p3,
        p4
    )
    shared: set = p1.intersection(
        p2,
        p3,
        p4
    )
    print("=== Achievement Tracker System ===")
    print("Player 1 : ", p1)
    print("Player 2 : ", p2)
    print("Player 3 : ", p3)
    print("Player 4 : ", p4)

    print(f"Shared achivements: {shared}")
    print("All unique achivements: ", all)

    print("Only player 1 has: ", p1.difference(p2, p3, p4))
    print("Only player 2 has: ", p2.difference(p1, p3, p4))
    print("Only player 3 has: ", p3.difference(p1, p2, p4))
    print("Only player 4 has: ", p4.difference(p1, p2, p3))

    print("Player 1 is missing: ", all.difference(p1))
    print("Player 2 is missing: ", all.difference(p2))
    print("Player 3 is missing: ", all.difference(p3))
    print("Player 4 is missing: ", all.difference(p4))


if __name__ == '__main__':
    main()
