def ft_count_harvest_iterative():
    days = int(input("Days unntil harvest: "))
    for c in range(1, days + 1):
        if c == days:
            print(f"Day {c}")
            print("Harvest time!")
        else:
            print(f"Day {c}")
