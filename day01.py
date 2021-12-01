def calcuateIncreases(depths):
    increasesCount = 0
    for d in range(len(depths) - 1):
        if depths[d] < depths[d + 1]:
            increasesCount += 1
            
    return increasesCount


def calculateIncresaingSums(depths):
    sums = []
    for d in range(len(depths) - 2):
        sums.append(depths[d] + depths[d + 1] + depths[d + 2])

    return calcuateIncreases(sums)


depths = [int(x) for x in open("day01.txt", "r")]
test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print('Part 1: ' + calcuateIncreases(depths))
print('Part 2: ' + calculateIncresaingSums(depths))
