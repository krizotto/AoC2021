from copy import deepcopy
import time


def solution(data, folding):
    for fold in folding:
        for p in data:
            if p[fold[0]] < fold[1]:
                continue
            p[fold[0]] = 2 * fold[1] - p[fold[0]]
        data = list(map(list, set(map(tuple, data))))
    return data


def part_one(data, folding):
    return len(solution(data, [folding[0]]))


def part_two(data, folding):
    data = solution(data, folding)
    data = sorted(data, key=lambda t: [t[0], t[1]])
    mx = data[-1][0] + 1
    my = data[-1][1] + 1
    for y in range(my):
        line = ""
        for x in range(mx):
            if [x, y] in data:
                line += "# "
            else:
                line += "  "
        print(line)


start_time = time.time()
data = []
folding = []
folds = {"x": 0, "y": 1}
with open("data/day13.txt", "r") as file:
    delimiter = ","
    for line in file.readlines():
        if line == "\n":
            delimiter = "="
            continue
        x, y = line.strip().split(delimiter)
        if not x.startswith("fold"):
            data.append([int(x), int(y)])
        else:
            folding.append([folds[x[-1]], int(y)])

print(f"Part 1: result = {part_one(deepcopy(data), folding)}")
print("Part 2: result:\n")
part_two(data, folding)
print("\n--- %s seconds ---" % (time.time() - start_time))
