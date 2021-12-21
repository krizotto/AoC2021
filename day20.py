import numpy as np
from scipy import ndimage
from copy import deepcopy
import time


def count_square(subarray):
    return decoder[int("".join("1" if b else "0" for b in subarray), 2)]


def solution(output, iterations):
    for _ in range(iterations):
        output = ndimage.generic_filter(
            np.pad(output, 1, mode="edge"), count_square, size=(3, 3), mode="nearest"
        )

    return output


start_time = time.time()
with open("data/day20.txt", "r") as f:
    decoder, image = f.read().strip().split("\n\n")

decoder = np.fromiter(
    (True if char == "#" else False for char in decoder.strip()),
    dtype=bool,
    count=len(decoder.strip()),
)

image = np.array(
    [
        [True if char == "#" else False for char in line]
        for line in image.strip().split("\n")
    ]
)

output = np.pad(image, 1, mode="constant", constant_values=False)

p1 = solution(deepcopy(output), 2)
print("Part 1: result = ", np.count_nonzero(p1))
p2 = solution(output, 50)
print("Part 2: result = ", np.count_nonzero(p2))
print("--- %s seconds ---" % (time.time() - start_time))
