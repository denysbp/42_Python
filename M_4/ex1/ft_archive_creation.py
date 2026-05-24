import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        raise Exception("Nothing To Read")
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Acessing file '{sys.argv[1]}'")
        print("\n")
        file: IO[str] = open(sys.argv[1])
        content: str = file.read()
        print("\n--")
        print("Transforming data")
        file.close()
        lines: list[str] = content.splitlines()
        new_mod: str = '\n'.join(linha + '#' for linha in lines) + '\n'
        print(new_mod)
        print("\n--")
        erro = 0
        while True:
            decision = input("Do you want to save?:")
            if decision not in ("y", "n"):
                print("y/n")
                erro += 1
                if erro == 3:
                    input("Really?")
                continue
            if decision in "y":
                file_name: str = str(input("Tell the python the name pls: "))
                file = open(f"{file_name}", "w")
                file.write(new_mod)
                print("We modificate it with sucess")
                print(f"It is save on {file_name}")
                file.close()
                print("Novo file fechado")
                break
            else:
                print("Bye evaluator :(")
                break
    except FileNotFoundError as e:
        print(f"\n{e}")
    except KeyboardInterrupt as e:
        print(f"\nEMERGENCY,WE STOP IT!!{e}")
    except IndexError as e:
        print(f"{e}")
    except PermissionError as e:
        print(f"\n {e}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{e}")
