with open("data/day16.txt", "r") as f:
    hex_val = f.readline().strip()
    b = bin(int(hex_val, 16))[2:]
print(b)
