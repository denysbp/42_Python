import sys


def main() -> None:
    print("\033[42;31;40m=== Player Score Analytics ===\033[m")
    lista = list()
    c: int = 1
    if len(sys.argv) <= 1:
        print("<score1> <score2> ...")
        return
    while c < len(sys.argv):
        try:
            lista.append(int(sys.argv[c]))
            c += 1
        except IndexError as e:
            print(f"No scores provided: try {e}")
            c += 1
            continue
        except ValueError as e:
            print(f"Not number provides: {e}")
            c += 1
            continue
    if len(lista) >= 1:
        print(f"Scores processed: {lista}")
        print(f"Total players: {len(lista)}")
        print(f"Total score {sum(lista)}")
        score = (sum(lista) / len(lista))
        print(f"Average score: {score}")
        print(f"Max score: {max(lista)}")
        print(f"Min score: {min(lista)}")
        print(f"Score range: {max(lista) - min(lista)}")


if __name__ == '__main__':
    main()
