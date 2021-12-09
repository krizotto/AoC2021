import numpy


def part_one(numbers):
    cords = []
    global rows, cols
    for i in range(rows):
        for j in range(cols):
            is_lowest = True
            # UP
            if i - 1 >= 0:
                is_lowest = numbers[i][j] < numbers[i - 1][j]
                if not is_lowest:
                    continue
            # LEFT
            if j - 1 >= 0:
                is_lowest = numbers[i][j] < numbers[i][j - 1]
                if not is_lowest:
                    continue
            # DOWN
            if i + 1 < rows:
                is_lowest = numbers[i][j] < numbers[i + 1][j]
                if not is_lowest:
                    continue
            # RIGHT
            if j + 1 < cols:
                is_lowest = numbers[i][j] < numbers[i][j + 1]
                if not is_lowest:
                    continue
            cords.append((i, j))
    return cords


def count_basin(numbers, basin, cord):
    global rows, cols
    i, j = cord[0], cord[1]
    if numbers[i, j] == 9 or cord in basin:
        return
    basin.append(cord)
    if i - 1 >= 0:
        count_basin(numbers, basin, (i - 1, j))
    if j - 1 >= 0:
        count_basin(numbers, basin, (i, j - 1))
    if i + 1 < rows:
        count_basin(numbers, basin, (i + 1, j))
    if j + 1 < cols:
        count_basin(numbers, basin, (i, j + 1))


def part_two(numbers, cords):
    basins = [[] for x in range(len(cords))]
    for i in range(len(cords)):
        count_basin(numbers, basins[i], cords[i])
    basins = sorted([len(basin) for basin in basins], reverse=True)
    return basins[0] * basins[1] * basins[2]


numbers = []
with open("data/day09.txt", "r") as file:
    lines = file.readlines()
    cols = len(lines[0].strip())
    rows = len(lines)
    for line in lines:
        numbers.extend(int(x) for x in list(line.strip()))
numbers = numpy.array(numbers).reshape((rows, cols))

part_one_cords = part_one(numbers[:])

print("Part 1: result = ", sum([numbers[i][j] + 1 for i, j in part_one_cords]))
print("Part 2: result = ", part_two(numbers[:], part_one_cords))
