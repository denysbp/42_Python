def see_days(days: int, c: int) -> None:
    if c == days:
        print(f"Day {c}")
        print("Harvest time")
    else:
        print(f"Day {c}")
        return (see_days(days, c + 1))


def ft_count_harvest_recursive() -> None:
    c: int = 1
    days: int = int(input("Days until harvest: "))
    see_days(days, c)
