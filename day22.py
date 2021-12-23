import re
import time


def box_intersection(box_a, box_b):
    x_low, y_low, z_low = [max(box_a[i], box_b[i]) for i in (0, 2, 4)]  # max from lowest
    x_high, y_high, z_high = [min(box_a[i], box_b[i]) for i in (1, 3, 5)]  # min from highest
    if x_high - x_low >= 0 and y_high - y_low >= 0 and z_high - z_low >= 0:
        return x_low, x_high, y_low, y_high, z_low, z_high


def count_active_cubes(data):
    activated_cubes = 0
    counted_zones = []
    for d in reversed(data):
        action, box = d[0], d[1:]
        x_low, x_high, y_low, y_high, z_low, z_high = box
        if action == "on":
            dead_cubes = []
            for overlap_box in [box_intersection(zone, box) for zone in counted_zones]:
                if overlap_box:
                    dead_cubes.append(("on", *overlap_box))
            activated_cubes += (x_high - x_low + 1) * (y_high - y_low + 1) * (z_high - z_low + 1)
            activated_cubes -= count_active_cubes(dead_cubes)
        counted_zones.append(box)
    return activated_cubes


def part_one(data):
    square = []
    for row in data:
        x_low, x_high, y_low, y_high, z_low, z_high = row[1:]
        if x_low >= -50 and x_high <= 50 and y_low >= -50 and y_high <= 50 and z_low >= -50 and z_high <= 50:
            square.append(row)
    return count_active_cubes(square)


start_time = time.time()
data = []
with open("data/day22.txt") as f:
    for line in f.readlines():
        m = re.match(r"^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)$", line.strip()).groups()
        data.append([m[0]] + [int(i) for i in m[1:]])

print("Part 1: result = ", part_one(data))
print("Part 2: result = ", count_active_cubes(data))
print("--- %s seconds ---" % (time.time() - start_time))
