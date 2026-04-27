def content(display: str) -> None:
    print("=" * 3 + f" {display} " + "=" * 3)


class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} years old")

    def grow(self) -> float:
        if self.height < 30:
            self.height = round(self.height + 0.10, 2)
            return (0.10)
        else:
            self.height = round(self.height + 0.07, 2)
            return (0.07)

    def _age(self) -> None:
        self.age = self.age + 1


if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25, 30)
    content("Garden Plant Registr")
    plant.show()
    total_grow: float = 0
    for day in range(1, 8):
        total_grow += plant.grow()
        plant._age()
        content(f"Day {day}")
        plant.show()
    print(f"Growth this week {round(total_grow, 2)}")
