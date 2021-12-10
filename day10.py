import time
import statistics


def corresponding_character(c):
    characters = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]
    for pair in characters:
        if c == pair[0]:
            return pair[1]
        elif c == pair[1]:
            return pair[0]


def get_illegal_points(c):
    if c == ")":
        return 3
    elif c == "]":
        return 57
    elif c == "}":
        return 1197
    else:
        return 25137


def get_autocomplete_points(c):
    if c == ")":
        return 1
    elif c == "]":
        return 2
    elif c == "}":
        return 3
    else:
        return 4


def count_autocomplete_score(stack):
    score = 0
    for c in stack:
        score = score * 5 + get_autocomplete_points(c)
    return score


def part_one(chunk):
    stack = []
    for c in chunk:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            last_opened = stack.pop()
            if not last_opened == corresponding_character(c):
                return get_illegal_points(c)
    return 0


def part_two(chunk):
    stack = []
    for c in chunk:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            last_opened = stack.pop()
            if not last_opened == corresponding_character(c):
                return 0
    stack = [corresponding_character(c) for c in stack[::-1]]
    return count_autocomplete_score(stack)


start_time = time.time()
chunks = []
with open("data/day10.txt", "r") as file:
    input = file.readlines()
    for chunk in input:
        chunks.append(list(chunk.strip()))


error_score = 0
for chunk in chunks:
    error_score += part_one(chunk)

autocomplete_scores = []
for chunk in chunks:
    autocomplete_scores.append(part_two(chunk))

autocomplete_scores = statistics.median(sorted([i for i in autocomplete_scores if i != 0]))
print(f"Part 1: result = {error_score}")
print(f"Part 1: result = {autocomplete_scores}")
print("--- %s seconds ---" % (time.time() - start_time))
