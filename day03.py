import time


def countMostCommon(data):
    return max(set(data), key=data.count)


def countLeastCommon(data):
    return min(set(data), key=data.count)


def processPart1(data):
    mostCommon = ""
    leastCommon = ""
    for i in range(len(data[0])):
        characters = [x[i] for x in data]
        mostCommon += countMostCommon(characters)
        leastCommon += countLeastCommon(characters)
    return int(mostCommon, 2), int(leastCommon, 2)


def processMostCommon(data, i):
    characters = [x[i] for x in data]
    toSave = countMostCommon(characters)
    toDelete = countLeastCommon(characters)

    if toSave == toDelete:
        toSave = "1"
    data = [x for x in data if x[i] == toSave]

    if len(data) == 1:
        return int(data[0], 2)
    else:
        return processMostCommon(data, i + 1)


def processLeastCommon(data, i):
    characters = [x[i] for x in data]
    toSave = countLeastCommon(characters)
    toDelete = countMostCommon(characters)

    if toSave == toDelete:
        toSave = "0"

    data = [x for x in data if x[i] == toSave]

    if len(data) == 1:
        return int(data[0], 2)
    else:
        return processLeastCommon(data, i + 1)


def processPart2(data):
    return processMostCommon(data, 0), processLeastCommon(data, 0)


start_time = time.time()
test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

data = [x.strip() for x in open("data/day03.txt", "r")]

gamma, epsilon = processPart1(data)
oxygen, co2 = processPart2(data)

print(f"Part 1: result = {gamma*epsilon}, gamma = {gamma}, epsilon = {epsilon}")
print(f"Part 2: result = {oxygen*co2}, oxygen = {oxygen}, co2 = {co2}")
print("--- %s seconds ---" % (time.time() - start_time))
