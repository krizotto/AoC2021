def calcuateIncreases(depths):
    increasesCount = 0
    for x, y in zip(depths, depths[1:]):
        increasesCount += x < y

    return increasesCount


def calculateIncresaingSums(depths):
    sums = []
    for x, y, z in zip(depths, depths[1:], depths[2:]):
        sums.append(x + y + z)

    return calcuateIncreases(sums)


depths = [int(x) for x in open("day01.txt", "r")]
test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print("Part 1:", calcuateIncreases(depths))
print("Part 2:", calculateIncresaingSums(depths))
