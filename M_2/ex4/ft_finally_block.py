class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden error") -> None:
        super().__init__(f"{message}")


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(f"{message}")


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError("Invalid plant name to water")
    elif plant_name == plant_name.capitalize():
        print(f"Watering {plant_name} [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valids plants...")
    try:
        water_plant("Sakura")
    except PlantError as e:
        print(f"We caught a PlantError: {e}")
    finally:
        print("Closing watering system\n")

    print("Testing invalids Plants...")
    try:
        water_plant("sakura")
    except PlantError as e:
        print(f"We caught a PlantError: {e}")
    finally:
        print("Closing watering system\n")

# if __name__ == '__main__':
#     test_watering_system()
#     print("Cleanup always happens, even with errors!")
