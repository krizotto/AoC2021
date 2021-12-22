import time
from functools import lru_cache


class Die:
    def __init__(self, number=0, max_number=100) -> None:
        self.number = number
        self.times_rolled = 0
        self.max_number = max_number

    def throw(self) -> list:
        roll1 = (self.number) % self.max_number + 1
        roll2 = (self.number + 1) % self.max_number + 1
        roll3 = (self.number + 2) % self.max_number + 1
        self.number = roll3
        self.times_rolled += 3
        return roll1 + roll2 + roll3


class Player:
    def __init__(self, pos: int, score: int = 0) -> None:
        self.pos = pos
        self.score = score

    def move(self, move: int) -> None:
        self.pos = (self.pos + move - 1) % 10 + 1
        self.score += self.pos


@lru_cache(maxsize=None)
def new_turn(p1_score, p2_score, p1_place, p2_place, p1_turn):
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1

    total_p1_wins = 0
    total_p2_wins = 0

    for roll1 in range(1, 4):
        for roll2 in range(1, 4):
            for roll3 in range(1, 4):
                total_move = roll1 + roll2 + roll3

                if p1_turn:
                    new_place = (p1_place + total_move - 1) % 10 + 1
                    new_score = p1_score + new_place

                    p1_wins, p2_wins = new_turn(new_score, p2_score, new_place, p2_place, not p1_turn)
                else:
                    new_place = (p2_place + total_move - 1) % 10 + 1
                    new_score = p2_score + new_place

                    p1_wins, p2_wins = new_turn(p1_score, new_score, p1_place, new_place, not p1_turn)

                total_p1_wins += p1_wins
                total_p2_wins += p2_wins
    return total_p1_wins, total_p2_wins


def part_one(die: Die, p1: Player, p2: Player):
    while True:
        p1.move(die.throw())
        if p1.score >= 1000:
            break
        p2.move(die.throw())
        if p2.score >= 1000:
            break
    return min(p1.score, p2.score) * die.times_rolled


def part_two(p1_place, p2_place):
    return new_turn(0, 0, p1_place, p2_place, True)


start_time = time.time()
p1_start = 7
p2_start = 4
die = Die()
p1 = Player(p1_start)
p2 = Player(p2_start)
p1_wins, p2_wins = part_two(p1_start, p2_start)

print("Part 1: result = ", part_one(die, p1, p2))
print("Part 2: result = ", max(p1_wins, p2_wins))
print("--- %s seconds ---" % (time.time() - start_time))
