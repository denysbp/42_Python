def ft_harvest_total():
    c = 1
    total = 0
    while c < 4:
        total += int(input(f"Day {c} harvest: "))
        c += 1
    print(f"Total harvest: {total}")