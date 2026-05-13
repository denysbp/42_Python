def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("ola")
    elif operation_number == 1:
        operation_number / 0
    elif operation_number == 2:
        open("sixseven.txt")
    elif operation_number == 3:
        "six" + 7
    else:
        print("All Operations completed sucessfuly!")


def test_error_types() -> None:
    print("== Garden Error  Types Demo")
    for error in [0, 1, 2, 3, 4]:
        try:
            print(f"Testing operation {error}")
            garden_operations(error)
        except ValueError as e:
            print(f"caught value error: {e}")
        except ZeroDivisionError as e:
            print(f"Caught division by zero: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypErro: {e}")
    print("\nAll error types tested successfuly")

# if __name__ == '__main__':
#     test_error_types()
