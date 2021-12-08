class Segment:
    def __init__(self, signals, output):
        self.signals = signals
        self.output = output
        self.mask = [None] * 7

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
                # For now the 0 element should be known
            elif len(code) == 4:
                self.mask[1] = [e for e in code if e not in self.mask[2]]
                self.mask[3] = self.mask[1][:]
            elif len(code) == 5:
                if all(x in code for x in self.get_2_5_mask()):
                    # MUST BE 3
                    if len(self.mask[1]) == 2:
                        if self.mask[1][0] in code:
                            self.mask[3] = list(self.mask[1][0])
                            self.mask[1] = list(self.mask[1][1])
                        else:
                            self.mask[3] = list(self.mask[1][1])
                            self.mask[1] = list(self.mask[1][0])
                    # now we know 0, 1, 3
                    code.remove(self.mask[2][0])
                    if len(self.mask[2]) == 2:
                        code.remove(self.mask[2][1])

                    code.remove(self.mask[0][0])
                    code.remove(self.mask[3][0])

                    used_letters = self.get_2_5_mask()
                    used_letters.extend(self.get_1_3_mask())
                    used_letters.extend(self.mask[0][:])
                    used_letters.extend(self.mask[3][:])
                    used_letters.extend(code)
                    # last element must be 6
                    self.mask[6] = code
                    # last unused letter must be 4
                    if self.mask[4] is None or len(self.mask[4]) > 2:
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
                    # now we know 0, 2, 5
                    code.remove(self.mask[1][0])

                    if len(self.mask[1]) == 2:
                        code.remove(self.mask[1][1])

                    code.remove(self.mask[0][0])
                    used_letters.extend(self.mask[5][:])
                    code.remove(self.mask[5][0])
                    # last element must be 6
                    self.mask[6] = code

                    used_letters = self.get_1_3_mask()
                    used_letters.extend(self.mask[0][:])
                    used_letters.extend(self.get_1_3_mask())
                    used_letters.extend(code)

                    if self.mask[4] is None or len(self.mask[4]) > 2:
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
                    self.mask[4] = code
                    self.mask[6] = code

            if None not in self.mask:
                mask_len = [len(x) for x in self.mask]
                if mask_len == [1, 1, 1, 1, 1, 1, 1]:
                    return self.mask
        print("self.mask")


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
for segment in segments:
    total_1478 += len(segment.count_1478())
    # segment.count_mask()


print(f"Part 1: result = {total_1478}")
