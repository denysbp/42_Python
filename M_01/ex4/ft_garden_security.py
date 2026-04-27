def content(display: str) -> None:
    print("=" * 3 + f" {display} " + "=" * 3)


class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def show(self) -> None:
        print(f"Created: {self.__name}: {self.__height}cm,", end=" ")
        print(f"{self.__age} years old")

    def grow(self) -> float:
        if self.__height < 30:
            self.__height = round(self.__height + 0.10, 2)
            return (0.10)
        else:
            self.__height = round(self.__height + 0.07, 2)
            return (0.07)

    def _age(self) -> None:
        self.__age = self.__age + 1

    def set_height(self, value: float) -> None:
        if value < 0:
            print("You cannot modify height to negatives values")
        else:
            self.__height = value

    def set_age(self, value: int):
        if value < 0:
            print("You cannot modify ages to negatives values")
        else:
            self.__age = value

    def get_age(self):
        print(f"The plant have {self.__age} days old")

    def get_height(self):
        print(f"The plant have {self.__height}cm")


if __name__ == "__main__":
    content("Garden Security System")
    plant: Plant = Plant("Denys", 15, 10)
    plant.set_height(-70)
    plant.set_age(-1)
    plant.show()
