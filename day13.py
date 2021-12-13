data = []
folding = []
with open("data/day13_test.txt", "r") as file:
    delimiter = ","
    for line in file.readlines():
        if line == "\n":
            delimiter = "="
            continue
        x, y = line.strip().split(delimiter)
        if not x.startswith("fold"):
            data.append((int(x), int(y)))
        else:
            folding.append((x[-1], int(y)))
data = sorted(data, key=lambda tup: (tup[0], tup[1]))
print(data)
print(folding)
