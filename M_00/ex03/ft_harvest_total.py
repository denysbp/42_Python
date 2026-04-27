def ft_harvest_total() -> None:
    c: int = 1
    total: int = 0
    while c < 4:
        total += int(input(f"Day {c} harvest: "))
        c += 1
    print(f"Total harvest: {total}")
