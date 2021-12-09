from copy import deepcopy
import time


def grow_fish(fish, days):
    for loop in range(days):
        new_fishes = {a: 0 for a in range(9)}
        for day in range(9):
            if day == 0:
                new_fishes[6] = fish[0]
                new_fishes[8] = fish[0]
            else:
                new_fishes[day - 1] += fish[day]
        fish = deepcopy(new_fishes)
    return fish


start_time = time.time()
with open("data/day06.txt", "r") as f:
    input = f.read().strip()
input = list(map(int, input.split(",")))
test = [3, 4, 3, 1, 2]

fishes = {a: 0 for a in range(9)}
for fish in input:
    fishes[fish] += 1

result_part_1 = grow_fish(fishes, 80)
result_part_2 = grow_fish(fishes, 256)

print(f"Part 1: result = {sum(result_part_1.values())}")
print(f"Part 2: result = {sum(result_part_2.values())}")
print("--- %s seconds ---" % (time.time() - start_time))
