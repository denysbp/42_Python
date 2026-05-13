class Plant():
    class Stats:
        def __init__(self) -> None:
            self.grow_call: int = 0
            self.age_call: int = 0
            self.show_call: int = 0

        def display(self):
            print(f"you called age {self.age_call} times ")
            print(f"you called grow {self.grow_call} times ")
            print(f"you called show {self.show_call} times ")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anon(cls):
        return cls("anonymous", 0.00, 0)

    def display_stats(self) -> None:
        content(f"[statics for {self.__name}]")
        self._stats.display()

    def show(self) -> None:
        self._stats.show_call += 1
        print(f"Created: {self.__name}: {self.__height}cm,", end=" ")
        print(f"{self.__age} years old", end=" ")

    def grow(self) -> float:
        self._stats.grow_call += 1
        if self.__height < 30:
            self.__height = round(self.__height + 0.10, 2)
            return (0.10)
        else:
            self.__height = round(self.__height + 0.07, 2)
            return (0.07)

    def _age(self) -> None:
        self._stats.age_call += 1
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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed: int
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed: int = seed

    def show(self) -> None:
        super().show()
        self._seed += 1
        print(f"The atual seed is {self._seed}")

    def display_stats(self) -> None:
        super().display_stats()
        print(f"seed = {self._seed}")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        numbers_shades: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self.numbers_shade: int = numbers_shades

    def show(self):
        super().show()
        print(f"trunk_diameter: {self.trunk_diameter}")

    def produce_shade(self) -> None:
        self.numbers_shade += 1
        print("\t\tCover your self")
        for c in range(0, 10):
            print("*"*4, end=" _")

    def display_stats(self) -> None:
        super().display_stats()
        print(f"shade = {self.numbers_shade}")


def content(display: str) -> None:
    print("=" * 3 + f" {display} " + "=" * 3)


def statics():
    flower1 = Flower("SAKURA", 5.4, 10, "RED")
    content("GARDEN STATICS")
    content("Check years old")
    print(f"Is {30} days older than a year -> {flower1.is_older(30)}")
    print(f"Is {400} days older than a year -> {flower1.is_older(400)} \n")
    content("Flower")
    flower1.show()
    flower1.display_stats()
    content("[Askig the flower to grow and bloom]")
    flower1.grow()
    flower1.bloom()
    flower1._age()
    flower1.display_stats()

    content("\nTree")
    tree = Tree("BIA", 13.7, 90, 12.6, 3)
    tree.show()
    tree.display_stats()
    tree.produce_shade()
    tree.display_stats()

    content("SEED")
    seed = Seed("Cimbrão", 23.6, 210, "green", 10)
    seed.show()
    seed.display_stats()
    print("[Asking seed to bloom and grow]")
    seed.grow()
    seed.bloom()
    seed.show()
    seed.display_stats()

# if __name__ == "__main__":
#     statics()
