import math


def get_player_pos() -> tuple[float, float, float] | None:
    print("=== Game Coordinate System ===")
    print("Enter new coordinates as floats in format 'x,y,z'")
    while True:
        try:
            dados = input("input the coordinates: x, y, z: ")
            splited = dados.split(",")
        except KeyboardInterrupt:
            print("\nVocê fechou o programa!")
            return None
        try:
            x_input, y_input, z_input = splited
            x = float(x_input.strip())
            y = float(y_input.strip())
            z = float(z_input.strip())
            return (x, y, z)
        except Exception as e:
            print(f"Something went wrong: {e}")
            continue


def main() -> None:
    p1: tuple = get_player_pos()
    print(f"Got a first set of coordinates: {p1}")
    print(f"Tuple: X = {p1[0]} Y = {p1[1]} Z = {p1[2]}")
    distancia: float = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {distancia:.3f}")

    print("\n\n")
    print("Get a second set of coodinates")
    p2 = get_player_pos()
    distancia_2 = math.sqrt(
        (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)
    print(f"Distance between the 2 sets of coordinates {distancia_2}")


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("OPS!")
