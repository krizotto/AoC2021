def count_fuel(crabs, i):
    total_fuel = 0
    total_increasing_fuel = 0
    for crab in crabs:
        steps = abs(crab - i)
        total_fuel += steps
        total_increasing_fuel += int(((steps + 1) * steps) / 2)
    return total_fuel, total_increasing_fuel


def solution(crabs):
    min_value, max_value = min(crabs), max(crabs)
    possible_fuels = []
    possible_increasing_fuels = []
    for i in range(min_value, max_value + 1):
        normal, increasing = count_fuel(crabs, i)
        possible_fuels.append(normal)
        possible_increasing_fuels.append(increasing)
    return min(possible_fuels), min(possible_increasing_fuels)


test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
with open("data/day07.txt", "r") as f:
    input = f.read().strip()
input = list(map(int, input.split(",")))

part_one, part_two = solution(input)
print(f"Part 1: result = {part_one}\nPart 2: result = {part_two}")
