import time


def count_increases(depths):
    increases_count = 0
    for x, y in zip(depths, depths[1:]):
        increases_count += x < y
    return increases_count


def count_increasing_sums(depths):
    sums = []
    for x, y, z in zip(depths, depths[1:], depths[2:]):
        sums.append(x + y + z)
    return count_increases(sums)


start_time = time.time()
depths = [int(x) for x in open("data/day01.txt", "r")]
test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print("Part 1:", count_increases(depths))
print("Part 2:", count_increasing_sums(depths))
print("--- %s seconds ---" % (time.time() - start_time))
