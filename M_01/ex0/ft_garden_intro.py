#!/usr/bin/env python3
def content(display: str) -> None:
    print("=" * 3 + f" {display} " + "=" * 3)


def garden(name: str, height: int, age: int) -> None:
    content("Welcome To My Garden")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    content("End of Program")


if __name__ == "__main__":
    name: str = "Denys"
    height: int = 80
    age: int = 19
    garden(name, height, age)
