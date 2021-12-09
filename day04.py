import time


class Board:
    def __init__(self):
        self.grid = []

    def mark(self, number):
        for cell in self.grid:
            if cell.value == number:
                cell.marked = True

    def check_horizontal(self):
        for row in range(5):
            check_row = True
            for column in range(5):
                check_row = check_row and self.grid[row * 5 + column].marked
            if check_row:
                return True

        return False

    def check_vertical(self):
        for row in range(5):
            check_col = True
            for column in range(5):
                check_col = check_col and self.grid[row + column * 5].marked
            if check_col:
                return True

        return False

    def check(self):
        return self.check_horizontal() or self.check_vertical()

    def sum_unmarked(self):
        unmarked_sum = 0
        for cell in self.grid:
            if not cell.marked:
                unmarked_sum += cell.value

        return unmarked_sum


class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False


def part_one(boards, numbers):
    for num in numbers:
        for board in boards:
            board.mark(num)
            if board.check():
                return board.sum_unmarked(), num


def part_two(boards, numbers):
    for num in numbers:
        for board in boards:
            board.mark(num)
        if len(boards) == 1 and boards[0].check():
            return boards[0].sum_unmarked(), num
        boards = [x for x in boards if not x.check()]


start_time = time.time()
with open("data/day04_numbers.txt", "r") as file:
    line = file.readline()
    numbers = [int(x) for x in line.split(",")]

grid = [[int(num) for num in line.split()] for line in open("data/day04.txt", "r")]

boards = []
temp_board = Board()

for line in grid:
    if line == []:
        boards.append(temp_board)
        temp_board = Board()
    else:
        temp_board.grid.extend(Cell(x) for x in line)

boards.append(temp_board)

unmarked_sum, num = part_one(boards[:], numbers[:])
print(
    f"Part 1: result = {unmarked_sum * num}, unmarked sum = {unmarked_sum}, last number = {num}"
)
unmarked_sum, num = part_two(boards[:], numbers[:])
print(
    f"Part 2: result = {unmarked_sum * num}, unmarked sum = {unmarked_sum}, last number = {num}"
)
print("--- %s seconds ---" % (time.time() - start_time))
