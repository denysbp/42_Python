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
        content: str = file.read()
        lines: list[str] = content.splitlines()
        for i, line in enumerate(lines):
            print(f"[FRAGMENT {i}] {line}")
        print("\n--")
        print(f"File {sys.argv[1]} closed")
        print("\n--")
        print("Transforming data")
        file.close()
        new_mod: str = ""
        for line in lines:
            new_mod += line + "#\n"
        file_name: str = str(input("Tell the python the name pls: "))
        file = open(f"{file_name}", "w")
        file.write(new_mod)
        file.close()
        print("We modificate it with sucess")
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR]: {e}\n")
    except KeyboardInterrupt as e:
        sys.stderr.write(f"\n[STDERR]: {e}\n")
    except IndexError as e:
        sys.stderr.write(f"[STDERR]: {e}\n")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR]: {e}\n")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"[STDERR]: {e}\n")
