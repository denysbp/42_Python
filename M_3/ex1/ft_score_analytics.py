import sys

print("=== Player Score Analytics ===")
print("Scores processed: [", end="")
c: int = 1
while c < len(sys.argv):
    if c < len(sys.argv):
        print(f"{sys.argv[c]}", end=", ")
    c += 1
print("]")
lista = list()
for i in sys.argv:
    try:
        lista.append(int(sys.argv[i]))
    except IndexError as e:
        print(f"Index errado: {e}")
print(f"Total players: {len(sys.argv)}")
total: int = 0
c: int = 1
while c < len(sys.argv):
    total += int(sys.argv[c])
    c += 1
print(f"Total score {total}")
print(f"Average score: {total / len(sys.argv):.2f}")
max: int = 0
min: int = int(sys.argv[1])
c = 1
while c < len(sys.argv):

    if max < int(sys.argv[c]):
        max = int(sys.argv[c])
    elif min > int(sys.argv[c]):
        min = int(sys.argv[c])
    c += 1
print(f"Max score: {max}")
print(f"Min score: {min}")
