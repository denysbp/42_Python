import math


def get_player_pos() -> tuple:
    print("=== Game Coordinate System ===")
    print("Enter new coordinates as floats in format 'x,y,z'")
    while True:
        try:
            x: float = float(input("What is your position in x: "))
            y: float = float(input("What is your position in y: "))
            z: float = float(input("What is your position in z: "))
            tupla: tuple = tuple()
            tupla = (x, y, z)
            break
        except ValueError as e:
            print(f"Try again, and pass a correct value: {e}")
            continue
        except Exception as e:
            print(f"Something went wrong: {e}")
            continue
        except KeyboardInterrupt:
            print("\nVocê fechou o programa!")
            break
    return tupla


def main() -> None:
    map: tuple = get_player_pos()
    print(f"Got a first tuple: {map}")
    print(f"Tuple: X = {map[0]}Y = {map[1]}Z = {map[2]}")
    distancia: float = math.sqrt(map[0]**2 + map[1]**2 + map[2]**2)
    print(f"Distance to center: {distancia:.3f}")


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("OPS!")
