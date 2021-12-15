import networkx as nx
import numpy as np


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


def prepare_graph(numbers):
    G = nx.DiGraph()
    size = len(numbers)
    edges = []
    for y in range(size):
        for x in range(size):
            weight = numbers[y][x]
            if y - 1 >= 0:
                edges.append(((x, y - 1), (x, y), weight))
            if x - 1 >= 0:
                edges.append(((x - 1, y), (x, y), weight))
            if y < size:
                edges.append(((x, y + 1), (x, y), weight))
            if x < size:
                edges.append(((x + 1, y), (x, y), weight))
    G.add_weighted_edges_from(edges)
    return G


def solution(numbers):
    size = len(numbers)
    graph = prepare_graph(numbers)
    path = nx.shortest_path(graph, (0, 0), (size - 1, size - 1), weight="weight")
    return sum([numbers[p[1]][p[0]] for p in path]) - numbers[0][0]


numbers = []
with open("data/day15.txt", "r") as f:
    lines = f.readlines()
    grid_size = len(lines)
    for line in lines:
        numbers.extend(int(x) for x in list(line.strip()))
numbers = np.array(numbers).reshape((grid_size, grid_size))

print(f"Part 1: result = {solution(numbers)}")
numbers = extend(numbers)
print(f"Part 2: result = {solution(numbers)}")
