import sys

print("== command_quest ==")
c: int = 1
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) == 1:
    print("No Arguments provided!")
if len(sys.argv) >= 1:
    print(f"Arguments received: {len(sys.argv)}")
while c < len(sys.argv):
    print(f"Argument {c}: {sys.argv[c]}")
    c += 1
print(f"Total arguments: {len(sys.argv)}")
