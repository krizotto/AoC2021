import time
from copy import deepcopy
from itertools import product


def flash(pos, neighbors, octopuses, flash_count=0):
    flash_count += 1
    octopuses[pos] = 0
    for n in neighbors:
        if octopuses[n] == 0:
            continue
        octopuses[n] += 1
        if octopuses[n] > 9:
            flash_count = flash(n, find_neighbors(n, octopuses), octopuses, flash_count)
    return flash_count


def find_neighbors(pos, octopuses):
    return [
        n
        for n in [
            (pos[0] - 1, pos[1] - 1),
            (pos[0] - 1, pos[1]),
            (pos[0] - 1, pos[1] + 1),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
            (pos[0] + 1, pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] + 1, pos[1] + 1),
        ]
        if n in octopuses
    ]


def step(octopuses):
    flash_count = 0
    for octo in octopuses:
        octopuses[octo] += 1

    for pos, val in octopuses.items():
        if val > 9:
            flash_count += flash(pos, find_neighbors(pos, octopuses), octopuses)
    return flash_count


def part_one(octopuses):
    return sum(step(octopuses) for i in range(100))


def part_two(octopuses):
    steps = 0
    while True:
        steps += 1
        if step(octopuses) == len(octopuses):
            return steps



start_time = time.time()
with open("data/day11.txt", "r") as file:
    data = [list(map(int, list(i.rstrip()))) for i in  file]
cords = list(product(range(10), range(10)))
octo = {c: data[c[1]][c[0]] for c in cords}

print("Part 1: result = ", part_one(deepcopy(octo)))
print("Part 2: result = ", part_two(octo))
print("--- %s seconds ---" % (time.time() - start_time))
