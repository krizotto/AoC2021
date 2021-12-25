import time
import numpy as np
import os


def clear():
    return os.system("clear")


def print_array(numbers: np.ndarray):
    return print("\n".join(["".join([str(cell) for cell in row]) for row in numbers]))


def process(numbers: np.ndarray, direction: str, axis: int):
    not_empty = numbers != "."
    dest_elements = numbers == direction

    all_moved = np.roll(dest_elements, axis=axis, shift=1)  # yet not checked if landed on proper spot
    dest_to = all_moved & ~not_empty  # find every moved that landed on "."
    numbers[dest_to] = direction  # change to new value
    dest_from = np.roll(dest_to, axis=axis, shift=-1)  # find the origin of every correctly moved
    numbers[dest_from] = "."  # make origin positions "."

    return dest_to, numbers


def part_one(numbers: np.ndarray, show_steps: bool):
    steps = 0
    if show_steps:
        clear()
        print(steps)
        print_array(numbers)
        time.sleep(1)
    while True:
        steps += 1
        # EAST
        moved_east, numbers = process(numbers, ">", 1)
        # SOUTH
        moved_south, numbers = process(numbers, "v", 0)

        total_moves = np.sum(moved_east + moved_south)
        if show_steps:
            clear()
            print(f"Step: {steps}. Moved: {total_moves}")
            print_array(numbers)
            time.sleep(0.15)
        if total_moves == 0:
            break
    return steps


start_time = time.time()
show_steps = False
numbers = []
with open("data/day25.txt") as f:
    for line in f.readlines():
        numbers.append([x for x in line.rstrip()])
    numbers = np.array(numbers)
print("Part 1: result = ", part_one(numbers, show_steps))
print("--- %s seconds ---" % (time.time() - start_time))
