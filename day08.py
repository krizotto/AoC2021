class Segment:
    def __init__(self, signals, output):
        self.signals = signals
        self.output = output
        self.mask = [None] * 7
        self.number_strings = []

    def count_1478(self):
        unique = [2, 3, 4, 7]
        return [x for x in self.output if len(x) in unique]

    def get_2_5_mask(self):
        return_list = self.mask[2][:]
        if len(self.mask[2]) == 1:
            return_list.extend(self.mask[5][:])
        return return_list

    def get_1_3_mask(self):
        return_list = self.mask[1][:]
        if len(self.mask[1]) == 1:
            return_list.extend(self.mask[3][:])
        return return_list

    def count_mask(self):
        codes = self.signals[:]
        codes.extend(self.output[:])
        codes = sorted([sorted(x) for x in codes], key=len)
        for code in codes:
            if len(code) == 2:
                self.mask[2] = code
                self.mask[5] = code
            elif len(code) == 3:
                self.mask[0] = [e for e in code if e not in self.mask[2]]
                # For now the 0th element should be known
            elif len(code) == 4:
                self.mask[1] = [e for e in code if e not in self.mask[2]]
                self.mask[3] = self.mask[1][:]
            elif len(code) == 5:
                if all(x in code for x in self.get_2_5_mask()):
                    # MUST BE 3
                    used_letters = []
                    if len(self.mask[1]) == 2:
                        used_letters.extend(self.mask[1][:])
                        if self.mask[1][0] in code:
                            self.mask[3] = list(self.mask[1][0])
                            self.mask[1] = list(self.mask[1][1])
                        else:
                            self.mask[3] = list(self.mask[1][1])
                            self.mask[1] = list(self.mask[1][0])
                    # now we know 0, 1, 3
                    code.remove(self.mask[2][0])
                    used_letters.extend(self.mask[2][0])
                    if len(self.mask[2]) == 2:
                        code.remove(self.mask[2][1])
                        used_letters.extend(self.mask[2][1])
                    else:
                        code.remove(self.mask[5][0])
                        used_letters.extend(self.mask[5][0])

                    code.remove(self.mask[0][0])
                    used_letters.extend(self.mask[0][:])
                    code.remove(self.mask[3][0])
                    used_letters.extend(self.mask[3][:])
                    used_letters.extend(code)
                    # last element must be 6
                    self.mask[6] = code
                    # last unused letter must be 4
                    if self.mask[4] is None or len(self.mask[4]) > 1:
                        self.mask[4] = [
                            e
                            for e in ["a", "b", "c", "d", "e", "f", "g"]
                            if e not in used_letters
                        ]
                elif all(x in code for x in self.get_1_3_mask()):
                    used_letters = []
                    # MUST BE 5
                    if len(self.mask[2]) == 2:
                        used_letters.extend(self.mask[2][:])
                        if self.mask[2][0] in code:
                            self.mask[5] = list(self.mask[2][0])
                            self.mask[2] = list(self.mask[2][1])
                        else:
                            self.mask[5] = list(self.mask[2][1])
                            self.mask[2] = list(self.mask[2][0])
                    else:
                        used_letters.extend(self.mask[2][0])
                    # now we know 0, 2, 5
                    code.remove(self.mask[1][0])
                    used_letters.extend(self.mask[1][0])
                    if len(self.mask[1]) == 2:
                        code.remove(self.mask[1][1])
                        used_letters.extend(self.mask[1][1])
                    else:
                        code.remove(self.mask[3][0])
                        used_letters.extend(self.mask[3][0])

                    code.remove(self.mask[0][0])
                    used_letters.extend(self.mask[5][:])
                    code.remove(self.mask[5][0])
                    # last element must be 6
                    self.mask[6] = code

                    # used_letters = self.get_1_3_mask()
                    used_letters.extend(self.mask[0][:])
                    used_letters.extend(self.get_1_3_mask())
                    used_letters.extend(code)

                    if self.mask[4] is None or len(self.mask[4]) > 1:
                        self.mask[4] = [
                            e
                            for e in ["a", "b", "c", "d", "e", "f", "g"]
                            if e not in used_letters
                        ]
                else:
                    # MUST BE 2
                    if len(self.mask[2]) == 2:
                        if self.mask[2][0] in code:
                            self.mask[5] = list(self.mask[2][1])
                            self.mask[2] = list(self.mask[2][0])
                        else:
                            self.mask[5] = list(self.mask[2][0])
                            self.mask[2] = list(self.mask[2][1])
                    # now we know 0, 2, 5
                    if len(self.mask[1]) == 2:
                        if self.mask[1][0] in code:
                            self.mask[3] = list(self.mask[1][0])
                            self.mask[1] = list(self.mask[1][1])
                        else:
                            self.mask[3] = list(self.mask[1][1])
                            self.mask[1] = list(self.mask[1][0])
                    # now we know 0, 1, 2, 3, 5
                    code.remove(self.mask[0][0])
                    code.remove(self.mask[2][0])
                    code.remove(self.mask[3][0])
                    # 4 and 6 are one of possible 2 letters
                    if self.mask[4] is None or len(self.mask[4]) != 1:
                        self.mask[4] = code
                    if self.mask[6] is None or len(self.mask[6]) != 1:
                        self.mask[6] = code

            if None not in self.mask:
                mask_len = [len(x) for x in self.mask]
                if mask_len == [1, 1, 1, 1, 1, 1, 1]:
                    return self.mask

    def set_number_strings(self):
        self.number_strings = [
            # 0
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[1][0]
                    + self.mask[2][0]
                    + self.mask[4][0]
                    + self.mask[5][0]
                    + self.mask[6][0]
                )
            ),
            # 1
            "".join(sorted(self.mask[2][0] + self.mask[5][0])),
            # 2
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[2][0]
                    + self.mask[3][0]
                    + self.mask[4][0]
                    + self.mask[6][0]
                )
            ),
            # 3
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[2][0]
                    + self.mask[3][0]
                    + self.mask[5][0]
                    + self.mask[6][0]
                )
            ),
            # 4
            "".join(
                sorted(
                    self.mask[1][0]
                    + self.mask[2][0]
                    + self.mask[3][0]
                    + self.mask[5][0]
                )
            ),
            # 5
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[1][0]
                    + self.mask[3][0]
                    + self.mask[5][0]
                    + self.mask[6][0]
                )
            ),
            # 6
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[1][0]
                    + self.mask[3][0]
                    + self.mask[4][0]
                    + self.mask[5][0]
                    + self.mask[6][0]
                )
            ),
            # 7
            "".join(sorted(self.mask[0][0] + self.mask[2][0] + self.mask[4][0])),
            # 8
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[1][0]
                    + self.mask[2][0]
                    + self.mask[3][0]
                    + self.mask[4][0]
                    + self.mask[5][0]
                    + self.mask[6][0]
                )
            ),
            # 9
            "".join(
                sorted(
                    self.mask[0][0]
                    + self.mask[1][0]
                    + self.mask[2][0]
                    + self.mask[3][0]
                    + self.mask[5][0]
                    + self.mask[6][0]
                )
            ),
        ]

    def count_output(self):
        self.count_mask()
        self.set_number_strings()
        numbers = []
        for num in self.output:
            if len(num) == 2:
                numbers.append(1)
            elif len(num) == 3:
                numbers.append(7)
            elif len(num) == 4:
                numbers.append(4)
            elif len(num) == 7:
                numbers.append(8)
            else:
                num = "".join(sorted(num))
                for i, v in enumerate(self.number_strings):
                    if v == num:
                        numbers.append(i)
        return 1000 * numbers[0] + 100 * numbers[1] + 10 * numbers[2] + numbers[3]


def split_input(input):
    input = [x for x in input.split(" ")]
    return input[0:10], input[11:16]


input = []
with open("data/day08.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())

segments = []
for i in input:
    signals, output = split_input(i)
    segments.append(Segment(signals, output))

# part 1
total_1478 = 0
total_output = 0
for segment in segments:
    total_1478 += len(segment.count_1478())
    total_output += segment.count_output()


print(f"Part 1: result = {total_1478}")
print(f"Part 2: result = {total_output}")
