class Game:
    """Ten-pin bowling scorer.

    Usage:
        game = Game()
        game.roll(pins)   # call once per roll, in order
        game.score()      # total score after all rolls are recorded
    """

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        roll_index = 0

        for _ in range(10):
            if self._is_strike(roll_index):
                total += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                total += self._frame_score(roll_index)
                roll_index += 2

        return total

    def _is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def _frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
