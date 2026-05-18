import sys

if __name__ == '__main__':
    print("== command_quest ==")
    c: int = 1
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No Arguments provided!")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
    while c < len(sys.argv):
        print(f"Argument {c}: {sys.argv[c]}")
        c += 1
    if len(sys.argv) > 1:
        print(f"Total arguments: {len(sys.argv)}")
