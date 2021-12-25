import re


def do_action(action, v1, v2):
    if action == "add":
        return v1 + v2
    if action == "mul":
        return v1 * v2
    if action == "div":
        return None if v2 == 0 else v1 // v2
    if action == "mod":
        return None if v1 < 0 and v2 <= 0 else v1 % v2
    if action == "eql":
        return 1 if v1 == v2 else 0


def process_instruction(action, arg1, arg2, x, y, z, w):
    d = {"x": x, "y": y, "z": z, "w": w}
    v1, v2 = 0, 0
    if re.match("(0-9)+", arg2) is not None:
        v2 = int(arg2)
    else:
        v2 = d[arg2]

    v1 = d[arg1]
    result = do_action(action, v1, v2)
    if result is None:
        return x, y, z, True

    if arg1 == "x":
        x = result
    elif arg1 == "y":
        y = result
    elif arg1 == "z":
        z = result

    return x, y, z, False


def process(monad: int, instructions: list):
    monad = [int(x) for x in str(monad)]
    curr_pos = 0
    x, y, z, w = 0, 0, 0, 0
    action, arg1, arg2 = "", "", ""
    for instruction in instructions:
        actions = instruction.split(" ")
        action = actions[0]
        arg1 = actions[1]
        if len(actions == 3):
            arg2 = actions[2]

        if action == "inp":
            w = monad[curr_pos]
            curr_pos += 1
        else:
            x, y, z, error = process_instruction(action, arg1, arg2, x, y, z, w)
            if error:
                break

    return z == 0



with open("data/day24.txt") as f:
    instructions = [x.strip() for x in f.readlines()]

monad_min = 11111111111111
monad_max = 99999999999999
highest_monad = 0

for i in range(monad_min, monad_max + 1):
    print(i)
    if process(i, instructions):
        highest_monad = i


print(highest_monad)
