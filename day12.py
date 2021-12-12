import time
from collections import defaultdict


def part_one(graph, node="start", path=[]):
    path_count = 0
    if node.islower() and node in path:
        return path_count
    path.append(node)
    if "end" in path:
        return 1
    for child in graph[node]:
        if not child.islower() or child not in path:
            path_count += part_one(graph, child, path[:])
    return path_count

def part_two(graph, node="start", path=[], is_double_used=False):
    path_count = 0
    if node.islower() and node in path and (is_double_used or node in ["start","end"]):
        return path_count
    path.append(node)
    if node.islower() and path.count(node) == 2:
        is_double_used = True
    if "end" in path:
        return 1
    for child in graph[node]:
        if not child.islower() or child not in path or (not is_double_used and node not in ["start","end"]):
            path_count += part_two(graph, child, path[:], is_double_used)
    return path_count


start_time = time.time()
paths = []
with open("data/day12.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        a, b = line.strip().split("-")
        paths.append((a, b))
        paths.append((b, a))
graph = defaultdict(list)
for k, v in paths:
    graph[k].append(v)

print(f"Part 1: result = {part_one(graph)}")
print(f"Part 2: result = {part_two(graph)}")
print("--- %s seconds ---" % (time.time() - start_time))
