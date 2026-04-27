def content(display: str) -> None:
    print("=" * 3 + f" {display} " + "=" * 3)


class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        content("Garden Plant Registr")
        print(f"{self.name}: {self.height}cm {self.age} years old")
        content("End of show")


if __name__ == "__main__":
    plant1 = Plant("Denys", 25, 19)
    plant1.show()
