import time
import numpy as np


def get_next_index(current, range):
    next_index = current + 1
    if next_index >= range:
        next_index -= range
    return next_index


def move_right(numbers: np.ndarray, horizontal: int, vertical: int):
    moved_to = []
    moved_from = []
    for y in range(vertical):
        for x in range(horizontal):
            if (x, y) in moved_to or numbers[y, x] != ">":
                continue
            nx = (x + 1) % horizontal
            if numbers[y, nx] != "v" and numbers[y, nx] != ">" and (nx, y) not in moved_from:
                moved_to.append((nx, y))
                moved_from.append((x, y))
    for (x, y) in moved_from:
        numbers[y, x] = "."
    for (x, y) in moved_to:
        numbers[y, x] = ">"
    return numbers, len(moved_to) > 0


def move_down(numbers: np.ndarray, horizontal: int, vertical: int):
    moved_to = []
    moved_from = []
    for y in range(vertical):
        for x in range(horizontal):
            if (x, y) in moved_to or numbers[y, x] != "v":
                continue
            ny = (y + 1) % vertical
            if numbers[ny, x] != "v" and numbers[ny, x] != ">" and (x, ny) not in moved_from:
                moved_to.append((x, ny))
                moved_from.append((x, y))
    for (x, y) in moved_from:
        numbers[y, x] = "."
    for (x, y) in moved_to:
        numbers[y, x] = "v"
    return numbers, len(moved_to) > 0


def part_one(numbers: np.ndarray, ysize: int, xsize: int):
    steps = 0
    while True:
        steps += 1
        print(steps)
        do_repeat = False
        numbers, has_moved = move_right(numbers, ysize, xsize)
        # print(numbers)
        do_repeat = do_repeat or has_moved
        numbers, has_moved = move_down(numbers, ysize, xsize)
        # print(numbers)
        do_repeat = do_repeat or has_moved
        if not do_repeat:
            break
    return steps


start_time = time.time()
numbers = []
with open("data/day25.txt", "r") as f:
    lines = f.readlines()
    vertical = len(lines)
    horizontal = len(lines[0].strip())
    for line in lines:
        numbers.extend(x for x in list(line.strip()))
numbers = np.array(numbers).reshape((vertical, horizontal))

print(numbers)
print(part_one(numbers, horizontal, vertical))
# print(f"Part 1: result = {solution(numbers)}")
# print(f"Part 2: result = {solution(extend(numbers))}")
print("--- %s seconds ---" % (time.time() - start_time))
