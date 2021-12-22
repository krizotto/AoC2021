from collections import defaultdict
import re


def count_active_cubes(cubes):
    activated_cubes = 0
    for z in range(-50, 51):
        for y in range(-50, 51):
            for x in range(-50, 51):
                if (x, y, z) in cubes.keys():
                    activated_cubes += cubes[(x, y, z)]
    return activated_cubes


def part_one(lines):
    cubes = defaultdict()
    for line in lines:
        m = re.match(r"^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)$", line)
        z_low = max(-50, int(m.group(6)))
        z_high = min(50, int(m.group(7)))

        y_low = max(-50, int(m.group(4)))
        y_high = min(50, int(m.group(5)))

        x_low = max(-50, int(m.group(2)))
        x_high = min(50, int(m.group(3)))

        for z in range(z_low, z_high + 1):
            for y in range(y_low, y_high + 1):
                for x in range(x_low, x_high + 1):
                    cubes[(x, y, z)] = states[m.group(1)]

    return count_active_cubes(cubes)


states = {"on": 1, "off": 0}

lines = []
with open("data/day22.txt") as f:
    for i, line in enumerate(f.readlines()):
        lines.append(line.strip())

print(part_one(lines))
