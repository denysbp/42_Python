import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        raise Exception("Nothing To Read")
    try:
        file: IO[str] = open(sys.argv[1])
        print(file.read())
        file.close()
    except FileNotFoundError as e:
        print(f"{e}")
    except KeyboardInterrupt as e:
        print(f"\n{e}")
    except IndexError as e:
        print(f"{e}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{e}")
