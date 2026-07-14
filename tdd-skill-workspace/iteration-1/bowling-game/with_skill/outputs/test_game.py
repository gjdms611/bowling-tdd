from game import Game


def test_gutter_game_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0


def test_all_open_frames_with_no_bonus_scores_sum_of_pins():
    game = Game()
    for _ in range(20):
        game.roll(1)
    assert game.score() == 20


def test_one_spare_adds_next_roll_as_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)  # spare in frame 1
    game.roll(3)
    game.roll(2)
    for _ in range(16):
        game.roll(0)
    # frame1 = 10 + 3 (bonus) = 13, frame2 = 5, rest = 0
    assert game.score() == 18


def test_one_strike_adds_next_two_rolls_as_bonus():
    game = Game()
    game.roll(10)  # strike in frame 1
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    # frame1 = 10 + 3 + 4 (bonus) = 17, frame2 = 3 + 4 = 7, rest = 0
    assert game.score() == 24


def test_perfect_game_scores_300():
    game = Game()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300


def test_tenth_frame_spare_gets_one_bonus_roll():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(5)
    game.roll(5)  # spare in frame 10
    game.roll(7)  # bonus roll
    # frames 1-9 = 0, frame10 = 10 + 7 (bonus) = 17
    assert game.score() == 17


def test_tenth_frame_strike_gets_two_bonus_rolls():
    game = Game()
    for _ in range(18):
        game.roll(0)
    game.roll(10)  # strike in frame 10
    game.roll(3)
    game.roll(4)  # two bonus rolls
    # frames 1-9 = 0, frame10 = 10 + 3 + 4 (bonus) = 17
    assert game.score() == 17
