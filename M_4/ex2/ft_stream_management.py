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
            print("Do you want to save?: ", end="")
            sys.stdout.flush()
            decision = sys.stdin.readline().strip()
            if decision not in ("y", "n"):
                print("y/n")
                erro += 1
                if erro == 3:
                    sys.stdout.flush()
                    print("Really?")
                    sys.stdin.readline()
                continue
            if decision in "y":
                print("Tell the python the name pls: ", end="")
                sys.stdout.flush()
                file_name: str = sys.stdin.readline().strip()
                file = open(f"{file_name}", "w")
                file.write(new_mod)
                print("We modificate it with sucess")
                file.close()
                print(f"It is save on {file_name}")
                break
            else:
                print("Bye evaluator :(")
                break
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR]: {e}\n")
    except KeyboardInterrupt:
        sys.stderr.write("\nVoce fechou o programa\n")
    except IndexError as e:
        sys.stderr.write(f"[STDERR]: {e}\n")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR]: {e}\n")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"[STDERR]: {e}\n")
