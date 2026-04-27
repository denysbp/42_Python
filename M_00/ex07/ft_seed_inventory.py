def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed: str = seed_type.capitalize()
    if "packets" in unit:
        print(f"{seed} seeds: {quantity} {unit} available")
    elif "grams" in unit:
        print(f"{seed} seeds: {quantity} {unit} in total")
    elif "area" in unit:
        print(f"{seed} seeds: cover {quantity} square {unit}")
    else:
        print("Unknown unit type")
