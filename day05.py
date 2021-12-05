from collections import Counter


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def check_horizontal(self):
        return self.start.y == self.end.y

    def check_vertical(self):
        return self.start.x == self.end.x


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def solution(lines, is_part_two):
    if not is_part_two:
        lines = [x for x in lines if x.check_horizontal or x.check_vertical()]
    grid = []
    for line in lines:
        reversed_y = -1 if line.start.y > line.end.y else 1
        reversed_x = -1 if line.start.x > line.end.x else 1
        if line.check_vertical():
            for y in range(line.start.y, line.end.y + reversed_y, reversed_y):
                grid.append((line.start.x, y))
        elif line.check_horizontal():
            for x in range(line.start.x, line.end.x + reversed_x, reversed_x):
                grid.append((x, line.start.y))
        elif is_part_two:
            for count in range(abs(line.start.x - line.end.x) + 1):
                grid.append(
                    (
                        line.start.x + count * reversed_x,
                        line.start.y + count * reversed_y,
                    )
                )

    more_than_2 = 0
    for count in Counter(grid).items():
        if count[1] >= 2:
            more_than_2 += 1
    return more_than_2


def part_one(lines):
    return solution(lines, False)


def part_two(lines):
    return solution(lines, True)


test = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]
input = []
with open("data/day05.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())
lines = []

for cords in input:
    start, end = cords.split(" -> ")
    start_xy = [int(x) for x in start.split(",")]
    end_xy = [int(x) for x in end.split(",")]
    start = Point(start_xy[0], start_xy[1])
    end = Point(end_xy[0], end_xy[1])
    lines.append(Line(start, end))

print(f"Part 1: result = {part_one(lines[:])}")
print(f"Part 2: result = {part_two(lines[:])}")
