import time


class Die:
    def __init__(self, number=0) -> None:
        self.number = number
        self.times_rolled = 0

    def throw(self) -> list:
        roll1 = (self.number) % 100 + 1
        roll2 = (self.number + 1) % 100 + 1
        roll3 = (self.number + 2) % 100 + 1
        self.number = roll3
        self.times_rolled += 3
        return [roll1, roll2, roll3]


class Player:
    def __init__(self, pos: int, score: int = 0) -> None:
        self.pos = pos
        self.score = score

    def move(self, move: int) -> None:
        self.pos = (self.pos + move - 1) % 10 + 1
        self.score += self.pos


def part_one(die: Die, p1: Player, p2: Player):
    while True:
        p1.move(sum(die.throw()))
        if p1.score >= 1000:
            break
        p2.move(sum(die.throw()))
        if p2.score >= 1000:
            break
    return min(p1.score, p2.score) * die.times_rolled


start_time = time.time()
die = Die()
p1 = Player(7)
p2 = Player(4)

print("Part 1: result = ", part_one(die, p1, p2))
print("--- %s seconds ---" % (time.time() - start_time))
