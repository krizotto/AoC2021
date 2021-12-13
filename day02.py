import time


def count_position_and_depth(movement):
    position = 0
    depth = 0

    for command, change in movement:
        if command == "forward":
            position += change
        elif command == "down":
            depth += change
        elif command == "up":
            depth -= change

    return (position, depth)


def count_position_and_depth_with_aiming(movement):
    position = 0
    depth = 0
    aim = 0

    for command, change in movement:
        if command == "down":
            aim += change
        elif command == "up":
            aim -= change
        elif command == "forward":
            position += change
            depth += change * aim

    return (position, depth)


start_time = time.time()
inputFile = []
test = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]

with open("data/day02.txt", "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for line in lines:
    command, size = line.split(" ")
    inputFile.append((command, int(size)))

(pos, dep) = count_position_and_depth(inputFile)
print(f"Part 1: {pos*dep} (position = {pos}, depth = {dep})")
(pos, dep) = count_position_and_depth_with_aiming(inputFile)
print(f"Part 2: {pos*dep} (position = {pos}, depth = {dep})")
print("--- %s seconds ---" % (time.time() - start_time))
