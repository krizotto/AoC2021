import time


def count_most_common(data):
    return max(set(data), key=data.count)


def count_least_common(data):
    return min(set(data), key=data.count)


def part_one(data):
    most_common = ""
    least_common = ""
    for i in range(len(data[0])):
        characters = [x[i] for x in data]
        most_common += count_most_common(characters)
        least_common += count_least_common(characters)
    return int(most_common, 2), int(least_common, 2)


def process_most_common(data, i):
    characters = [x[i] for x in data]
    to_save = count_most_common(characters)
    to_delete = count_least_common(characters)

    if to_save == to_delete:
        to_save = "1"
    data = [x for x in data if x[i] == to_save]

    if len(data) == 1:
        return int(data[0], 2)
    else:
        return process_most_common(data, i + 1)


def process_least_common(data, i):
    characters = [x[i] for x in data]
    to_save = count_least_common(characters)
    to_delete = count_most_common(characters)

    if to_save == to_delete:
        to_save = "0"

    data = [x for x in data if x[i] == to_save]

    if len(data) == 1:
        return int(data[0], 2)
    else:
        return process_least_common(data, i + 1)


def part_two(data):
    return process_most_common(data, 0), process_least_common(data, 0)


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

gamma, epsilon = part_one(data)
oxygen, co2 = part_two(data)

print(f"Part 1: result = {gamma*epsilon}, gamma = {gamma}, epsilon = {epsilon}")
print(f"Part 2: result = {oxygen*co2}, oxygen = {oxygen}, co2 = {co2}")
print("--- %s seconds ---" % (time.time() - start_time))
