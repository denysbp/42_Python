import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        raise Exception("Nothing To Read")
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Acessing file {sys.argv[1]}")
        print("\n")
        file: IO[str] = open(sys.argv[1])
        file_1: IO[str] = open(sys.argv[1])
        content: str = file.read()
        content_1: str = file_1.read()
        lines_1: list[str] = content_1.splitlines()
        for i, line in enumerate(lines_1):
            print(f"[FRAGMENT {i}] {line}")
        print("\n--")
        print(f"File {sys.argv[1]} closed")
        print("\n--")
        print("Transforming data")
        file.close()
        lines: list[str] = content.splitlines()
        new_mod: str = ""
        for line in lines:
            new_mod += line + "#\n"
        file_name: str = str(input("Tell the python the name pls: "))
        file = open(f"{file_name}", "w")
        file.write(new_mod)
        file.close()
        print("We modificate it with sucess")
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
