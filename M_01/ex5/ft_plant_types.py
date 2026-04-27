class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def show(self) -> None:
        print(f"Created: {self.__name}: {self.__height}cm,", end=" ")
        print(f"{self.__age} years old", end=" ")

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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print("""
            ✿ ✿ ✿
        ✿           ✿
        ✿     ✿     ✿
         ✿          ✿
            ✿ ✿ ✿
        """)

    def show(self):
        super().show()
        print(f"color: {self.color}")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f"trunk_diameter: {self.trunk_diameter}")

    def produce_shade(self) -> None:
        print("\t\tCover your self")
        for c in range(0, 10):
            print("*"*4, end=" _")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest_season: {self.harvest_season},", end=" ")
        print(f"NV: {self.nutritional_value}")

    def incrise(self):
        super().grow()
        super()._age()
        self.nutritional_value += 1
        print("YOU JUST UPGRADE THE PLANT")


if __name__ == "__main__":
    tree: Tree = Tree("denys", 4, 3, 10)
    tree.produce_shade()
    flower: Flower = Flower("Sakura", 32, 4, "blue")
    flower.bloom()
    vegetable: Vegetable = Vegetable("TOMATO", 1, 4, "3 of april", 0)
    vegetable.incrise()
    vegetable.incrise()
    vegetable.show()
