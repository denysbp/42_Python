def input_temperature(temp_str: str) -> int:
    tem: int = int(temp_str)
    return int(temp_str)

def test_temperature() -> None:
    try:
        numero: int =  input_temperature("abs")
        print(f"Temperature is now {numero}c")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

# if __name__ == '__main__':
#     test_temperature()