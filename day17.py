import re
import time


def parse_data(data):
    m = re.match(r"^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data)
    coords = {
        "x": [int(m.group(1)), int(m.group(2))],
        "y": [int(m.group(3)), int(m.group(4))],
    }

    return coords


def simulate(velocity, target):
    x, y = [0, 0]
    max_y = y
    vx, vy = velocity
    while (x < target["x"][1] + 1 and not (vx == 0 and x < target["x"][0])) and not (
        x > target["x"][0] and y < target["y"][0]
    ):
        x += vx
        y += vy
        vx += 1 if vx < 0 else -1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if y > max_y:
            max_y = y
        if (x in range(target["x"][0], target["x"][1] + 1)) and (
            y in range(target["y"][0], target["y"][1] + 1)
        ):
            return True, velocity, max_y

    return False, velocity, max_y


start_time = time.time()
target = parse_data("target area: x=175..227, y=-134..-79")
max_y = 0
count = 0
optimal = []
for x in range(0, target["x"][1] * 2):
    for y in range(target["y"][0], target["x"][1]):
        result, velocity, new_max_y = simulate([x, y], target)
        if result:
            count += 1
            if new_max_y > max_y:
                max_y = new_max_y
                optimal = velocity

print("Part 1: result = ", max_y)
print("Part 2: result = ", count)
print("--- %s seconds ---" % (time.time() - start_time))
