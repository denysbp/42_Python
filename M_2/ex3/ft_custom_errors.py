class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden error") -> None:
        super().__init__(f"{message}")


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(f"{message}")


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water error") -> None:
        super().__init__(f"{message}")


def plant_test(temperatura: int = -1) -> None:
    if temperatura < 0:
        raise PlantError("The tomato plant is wilting!")
    else:
        print("The tomato is ok")


def water_test(water: int = 5) -> None:
    if water <= 5:
        raise WaterError("Not enough water in the tank!")
    else:
        print("The Tank is ok!")


def test_error() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        plant_test(-100)
    except PlantError as e:
        print(f"We caught Plant error: {e}")
    try:
        water_test(2)
    except WaterError as e:
        print(f"We caught Water Error: {e}")
    try:
        plant_test(10)
    except GardenError as e:
        print(f"We caught : {e}")
    try:
        water_test(6)
    except GardenError as e:
        print(f"We caught : {e}")
    print("All custom error types work correctly!")


# if __name__ == '__main__':
#     test_error()
