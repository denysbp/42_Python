def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if "packets" in unit:
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif "grams" in unit:
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} in total")
    elif "area" in unit:
        print(f"{seed_type.capitalize()} seeds: cover {quantity} square {unit}")
