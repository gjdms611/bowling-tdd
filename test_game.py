from game import Game


def test_gutter_game_scores_zero():
    game = Game()
    for _ in range(20):
        game.roll(0)

    assert game.score() == 0


def test_all_open_frames_of_one_pin_scores_20():
    game = Game()
    for _ in range(20):
        game.roll(1)

    assert game.score() == 20
