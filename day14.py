from collections import defaultdict
import time


def solution(polymer, inserts, times):
    letters_count = defaultdict(int)
    old_pairs = defaultdict(int)

    for i in range(len(polymer) - 1):
        old_pairs[polymer[i : i + 2]] += 1
        letters_count[polymer[i]] += 1
    letters_count[polymer[-1]] += 1

    for _ in range(times):
        new_pairs = defaultdict(int)
        for pair in old_pairs.keys():
            addition = inserts[pair]
            new_pairs[pair[0] + addition] += old_pairs[pair]
            new_pairs[addition + pair[1]] += old_pairs[pair]
            letters_count[addition] += old_pairs[pair]
        old_pairs = new_pairs
    cnt = letters_count.values()
    return max(cnt) - min(cnt)


def part_one(polymer, inserts):
    return solution(polymer, inserts, 10)


def part_two(polymer, inserts):
    return solution(polymer, inserts, 40)


start_time = time.time()
inserts = defaultdict(str)
with open("data/day14.txt", "r") as file:
    lines = file.readlines()
    polymer = lines[0].strip()
    for i in range(2, len(lines)):
        x, y = lines[i].strip().split(" -> ")
        inserts[x] = y


print(f"Part 1: result = {part_one(polymer, inserts)}")
print(f"Part 2: result = {part_two(polymer, inserts)}")
print("--- %s seconds ---" % (time.time() - start_time))
