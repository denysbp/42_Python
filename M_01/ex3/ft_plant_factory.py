class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} years old")

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
    plant: Plant = Plant("Denys", 25.0, 30)
    plant1: Plant = Plant("42", 10.0, 10)
    plant.show()
    plant1.show()
