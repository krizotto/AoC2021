import networkx as nx
import numpy as np
import time


def extend(numbers):
    size = len(numbers)
    new_numbers = []
    for row in numbers:
        temp_row = []
        temp_row.extend(row)
        for i in range(size, 5 * size):
            temp_row.append(temp_row[i - size] % 9 + 1)
        new_numbers.append(temp_row)
    for i in range(size, 5 * size):
        new_numbers.append([i % 9 + 1 for i in new_numbers[i - size]])
    return new_numbers


def get_neighbors(x, y, size):
    potential_neighbors = [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
    return [(x, y) for x, y in potential_neighbors if 0 <= x < size and 0 <= y < size]


def prepare_graph(numbers):
    G = nx.DiGraph()
    size = len(numbers)
    edges = []
    for y in range(size):
        for x in range(size):
            weight = numbers[y][x]
            for neighbor in get_neighbors(x, y, size):
                edges.append((neighbor, (x, y), weight))
    G.add_weighted_edges_from(edges)
    return G


def solution(numbers):
    size = len(numbers)
    graph = prepare_graph(numbers)
    path = nx.shortest_path(graph, (0, 0), (size - 1, size - 1), weight="weight")
    return sum([numbers[p[1]][p[0]] for p in path]) - numbers[0][0]


start_time = time.time()
numbers = []
with open("data/day15.txt", "r") as f:
    lines = f.readlines()
    grid_size = len(lines)
    for line in lines:
        numbers.extend(int(x) for x in list(line.strip()))
numbers = np.array(numbers).reshape((grid_size, grid_size))

print(f"Part 1: result = {solution(numbers)}")
print(f"Part 2: result = {solution(extend(numbers))}")
print("--- %s seconds ---" % (time.time() - start_time))
