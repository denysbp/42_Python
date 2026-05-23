import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Nothing To Read")
        return
    try:
        file: IO[str] = open(sys.argv[1])
        print(f"Abrindo o file '{sys.argv[1]}'")
        print(file.read())
        file.close()
        print(f"File '{sys.argv[1]}' closed")
    except FileNotFoundError as e:
        print(f"Algo inesperado aconteceu: {e}")
    except KeyboardInterrupt as e:
        print(f"\nAlgo inesperado aconteceu: {e}")
    except IndexError as e:
        print(f"Algo inesperado aconteceu: {e}")
    except PermissionError as e:
        print(f"Algo inesperado aconteceu: {e}")
    except Exception as e:
        print(f"Algo inesperado aconteceu: {e}")


if __name__ == '__main__':
    main()
