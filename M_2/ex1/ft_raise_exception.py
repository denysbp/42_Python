def input_temperature(temp_str: str) -> int:
    print(f"input data is {temp_str}")
    temp: int = int(temp_str)
    if (temp) < 0:
        raise ValueError(
            f"{temp}°C is too cold for plants min (0°C)"
        )
    elif temp >= 0 and temp <= 40:
        return temp
    else:
        raise ValueError(
            f"{temp}°C is too hot for plants max (40°C)"
        )


def test_temperature() -> None:
    try:
        numero: int = input_temperature("1000")
        print(f"Temperature is now {numero}°C")
    except TypeError as e:
        print(f"Caught input_temperature error: {e}")
    except ValueError as e:
        print(f"{e}")

# if __name__ == '__main__':
#     test_temperature()
