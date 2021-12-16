import math, time

h2b = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def b2d(b):
    pos_value = 1
    decimal_value = 0
    for i in reversed(range(len(b))):
        if b[i] == "1":
            decimal_value += pos_value
        pos_value *= 2
    return decimal_value


def slice_bits(n, bits):
    return bits[:n], bits[n:]


def process_literal(bits):
    binary_string = ""
    keep_reading = True
    while keep_reading:
        first_bit, bits = slice_bits(1, bits)
        remaining_bits, bits = slice_bits(4, bits)
        binary_string += remaining_bits
        if first_bit == "0":
            keep_reading = False
    return b2d(binary_string), bits


def get_value_by_type_id(type_id, subpackets_values):
    if type_id == "000":
        value = sum(subpackets_values)
    elif type_id == "001":
        value = math.prod(subpackets_values)
    elif type_id == "010":
        value = min(subpackets_values)
    elif type_id == "011":
        value = max(subpackets_values)
    elif type_id == "101":
        value = 1 if subpackets_values[0] > subpackets_values[1] else 0
    elif type_id == "110":
        value = 1 if subpackets_values[0] < subpackets_values[1] else 0
    elif type_id == "111":
        value = 1 if subpackets_values[0] == subpackets_values[1] else 0
    return value


def solution(bits):
    version, bits = slice_bits(3, bits)
    type_id, bits = slice_bits(3, bits)

    global version_numbers
    version_numbers += b2d(version)

    if type_id == "100":
        value, bits = process_literal(bits)
        return value, bits
    else:
        subpackets_values = []
        length_type, bits = slice_bits(1, bits)
        if length_type == "0":
            length, bits = slice_bits(15, bits)
            subpacket, bits = slice_bits(b2d(length), bits)
            while subpacket:
                value, subpacket = solution(subpacket)
                subpackets_values.append(value)
        else:
            number, bits = slice_bits(11, bits)
            for _ in range(b2d(number)):
                value, bits = solution(bits)
                subpackets_values.append(value)

    return get_value_by_type_id(type_id, subpackets_values), bits


start_time = time.time()
bits = ""
version_numbers = 0
with open("data/day16.txt", "r") as f:
    for hex in f.readline().strip():
        bits += h2b[hex]

eval, bits = solution(bits)
print("Part 1: result = ", version_numbers)
print("Part 2: result = ", eval)
print("--- %s seconds ---" % (time.time() - start_time))
