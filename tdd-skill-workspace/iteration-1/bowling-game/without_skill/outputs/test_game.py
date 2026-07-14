from game import Game


def roll_many(game, n, pins):
    for _ in range(n):
        game.roll(pins)


def test_all_gutter_balls():
    game = Game()
    roll_many(game, 20, 0)
    assert game.score() == 0


def test_all_ones_open_frames():
    game = Game()
    roll_many(game, 20, 1)
    assert game.score() == 20


def test_one_spare():
    game = Game()
    game.roll(5)
    game.roll(5)  # spare
    game.roll(3)
    roll_many(game, 17, 0)
    assert game.score() == 16  # 10 + 3 bonus + 3


def test_one_strike():
    game = Game()
    game.roll(10)  # strike
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)
    assert game.score() == 24  # 10 + 3 + 4 bonus + 7


def test_perfect_game():
    game = Game()
    roll_many(game, 12, 10)
    assert game.score() == 300


def test_all_spares():
    game = Game()
    roll_many(game, 21, 5)
    assert game.score() == 150


def test_tenth_frame_spare_bonus_roll():
    game = Game()
    roll_many(game, 18, 0)
    game.roll(5)
    game.roll(5)  # spare in 10th frame
    game.roll(7)  # bonus roll
    assert game.score() == 17


def test_tenth_frame_strike_bonus_rolls():
    game = Game()
    roll_many(game, 18, 0)
    game.roll(10)  # strike in 10th frame
    game.roll(3)
    game.roll(4)
    assert game.score() == 17
