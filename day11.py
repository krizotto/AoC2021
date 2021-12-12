import time
import numpy
from copy import deepcopy


def check_neighbors(x, y):
    possible_neighbors = []
    # check row above
    if y - 1 >= 0:
        possible_neighbors.append((x, y - 1))
        if x - 1 >= 0:
            possible_neighbors.append((x - 1, y - 1))
        if x + 1 < 10:
            possible_neighbors.append((x + 1, y - 1))
    # check row below
    if y + 1 < 10:
        possible_neighbors.append((x, y + 1))
        if x - 1 >= 0:
            possible_neighbors.append((x - 1, y + 1))
        if x + 1 < 10:
            possible_neighbors.append((x + 1, y + 1))
    # check my row
    if x - 1 >= 0:
        possible_neighbors.append((x - 1, y))
    if x + 1 < 10:
        possible_neighbors.append((x + 1, y))
    return possible_neighbors


def flash(x, y, octopuses, flash_count=0):
    flash_count += 1
    octopuses[y][x] = 0
    for nx, ny in check_neighbors(x, y):
        if octopuses[ny][nx] == 0:
            continue
        octopuses[ny][nx] += 1
        if octopuses[ny][nx] > 9:
            flash_count = flash(nx, ny, octopuses, flash_count)
    return flash_count


def step(octopuses):
    flash_count = 0
    for y in range(10):
        for x in range(10):
            octopuses[y][x] += 1

    for y in range(10):
        for x in range(10):
            if octopuses[y][x] > 9:
                flash_count += flash(x, y, octopuses)
    return flash_count


def part_one(octopuses):
    return sum(step(octopuses) for i in range(100))


def part_two(octopuses):
    steps = 0
    while True:
        steps += 1
        if step(octopuses) == 100:
            return steps


start_time = time.time()

octopuses = []
with open("data/day11.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        octopuses.extend(int(x) for x in list(line.strip()))
octopuses = numpy.array(octopuses).reshape((10, 10))

print("Part 1: result = ", part_one(deepcopy(octopuses)))
print("Part 2: result = ", part_two(octopuses))
print("--- %s seconds ---" % (time.time() - start_time))
