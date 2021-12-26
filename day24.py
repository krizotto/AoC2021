import ray
import psutil

division = [1, 1, 1, 26, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26]
add_x = [12, 12, 12, -9, -9, 14, 14, -10, 15, -2, 11, -15, -9, -3]
add_y = [9, 4, 2, 5, 1, 6, 11, 15, 7, 12, 15, 9, 12, 12]


@ray.remote
def process(monad):
    matchings = []
    monad_list = [int(x) for x in str(monad)]
    if 0 in monad_list:
        return False
    curr_pos = 0
    x, z, w = 0, 0, 0
    for part in range(14):
        w = monad_list[curr_pos]
        curr_pos += 1
        x = z % 26
        z //= division[part]
        x += add_x[part]
        x = int(x != w)
        z = z * (25 * x + 1) + (w + add_y[part]) * x
    if z == 0:
        matchings.append(monad)
    return matchings


ray.init(num_cpus=psutil.cpu_count(logical=False))
matchings = []

# func_args = [
#     (11111111111111, 22222222222222),
#     (22222222222222, 33333333333333),
#     (33333333333333, 44444444444444),
#     (44444444444444, 55555555555555),
#     (55555555555555, 66666666666666),
#     (66666666666666, 77777777777777),
#     (77777777777777, 88888888888888),
#     (88888888888888, 100000000000000),
# ]

results = [process.remote(x) for x in range(33333333333333, 44444444444444)]


print(matchings)
