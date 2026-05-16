import sys


def main() -> None:
    print("\033[42;31;40m=== Player Score Analytics ===\033[m")
    lista = list()
    c: int = 1
    try:
        if len(sys.argv) <= 1:
            raise IndexError("<score1> <score2> ...")
        while c < len(sys.argv):
            lista.append(int(sys.argv[c]))
            c += 1
        print(f"Scores processed: {lista}")
        print(f"Total players: {len(lista)}")
        print(f"Total score {sum(lista)}")
        print(f"Average score: {sum(lista) / len(sys.argv):.2f}")
        print(f"Max score: {max(lista)}")
        print(f"Min score: {min(lista)}")
        print(f"Score range: {max(lista) - min(lista)}")
    except IndexError as e:
        print(f"No scores provided: try {e}")
    except ValueError as e:
        print(f"Not number provides: {e}")


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("OPS!")
