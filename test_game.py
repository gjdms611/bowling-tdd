from game import Game


def test_gutter_game():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0


def test_spare_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    assert game.score() == 16


def test_spare_bonus_roll_also_counts_toward_next_frame():
    game = Game()
    game.roll(2)
    game.roll(8)
    game.roll(2)
    game.roll(3)
    for _ in range(16):
        game.roll(0)
    assert game.score() == 17


def test_strike_bonus():
    game = Game()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    assert game.score() == 24


def test_strike_in_ninth_frame():
    game = Game()
    for _ in range(16):
        game.roll(0)
    game.roll(10)
    game.roll(6)
    game.roll(2)
    assert game.score() == 26


def test_perfect_game():
    game = Game()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300


def test_tenth_frame_spare_with_bonus_roll():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(9)
    game.roll(1)
    game.roll(5)
    assert game.score() == 15


def test_tenth_frame_strike_with_bonus_rolls():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(10)
    game.roll(4)
    game.roll(5)
    assert game.score() == 19
