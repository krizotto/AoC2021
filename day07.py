def count_fuel(crabs, i):
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab - i)
    return total_fuel


def count_increasing_fuel(crabs, i):
    total_fuel = 0
    for crab in crabs:
        steps = abs(crab - i)
        total_fuel += int(((steps + 1) * steps) / 2)
    return total_fuel


def part_one(crabs):
    min_value, max_value = min(crabs), max(crabs)
    possible_fuels = []
    for i in range(min_value, max_value + 1):
        possible_fuels.append(count_fuel(crabs, i))
    return min(possible_fuels)


def part_two(crabs):
    min_value, max_value = min(crabs), max(crabs)
    possible_fuels = []
    for i in range(min_value, max_value + 1):
        possible_fuels.append(count_increasing_fuel(crabs, i))
    return min(possible_fuels)


test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
with open("data/day07.txt", "r") as f:
    input = f.read().strip()
input = list(map(int, input.split(",")))

print(part_one(input[:]))
print(part_two(input[:]))
