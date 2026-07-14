# Transcript: Bowling Game Implementation (without_skill)

## Command 1

```
mkdir -p "D:/user/education/2026_CRA_AI/workspace/bowling-tdd/tdd-skill-workspace/iteration-1/bowling-game/without_skill/outputs" && cd "D:/user/education/2026_CRA_AI/workspace/bowling-tdd/tdd-skill-workspace/iteration-1/bowling-game/without_skill/outputs" && pwd
```

Output:
```
/d/user/education/2026_CRA_AI/workspace/bowling-tdd/tdd-skill-workspace/iteration-1/bowling-game/without_skill/outputs
```

## Step 2: Create game.py

Wrote `game.py` containing a `Game` class with `roll(pins)` and `score()`.
Scoring algorithm: iterate 10 frames; for each frame, check strike (10 + next
two rolls), spare (10 + next roll), or open frame (sum of two rolls). No
validation of pin counts or frame counts is performed. No per-frame score
reporting is provided (only the total via `score()`).

## Step 3: Create test_game.py

Wrote `test_game.py` (pytest) covering:
- all gutter balls (score 0)
- all open frames of 1s (score 20)
- a single spare followed by a normal roll
- a single strike followed by two normal rolls
- a perfect game (12 strikes -> 300)
- all spares (21 rolls of 5 -> 150)
- 10th frame spare + one bonus roll
- 10th frame strike + two bonus rolls

## Command 2

```
cd "/d/user/education/2026_CRA_AI/workspace/bowling-tdd/tdd-skill-workspace/iteration-1/bowling-game/without_skill/outputs" && python -m pytest test_game.py -v
```

Output:
```
============================= test session starts =============================
platform win32 -- Python 3.11.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\gjdms\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\user\education\2026_CRA_AI\workspace\bowling-tdd\tdd-skill-workspace\iteration-1\bowling-game\without_skill\outputs
collecting ... collected 8 items

test_game.py::test_all_gutter_balls PASSED                               [ 12%]
test_game.py::test_all_ones_open_frames PASSED                           [ 25%]
test_game.py::test_one_spare PASSED                                      [ 37%]
test_game.py::test_one_strike PASSED                                     [ 50%]
test_game.py::test_perfect_game PASSED                                   [ 62%]
test_game.py::test_all_spares PASSED                                     [ 75%]
test_game.py::test_tenth_frame_spare_bonus_roll PASSED                   [ 87%]
test_game.py::test_tenth_frame_strike_bonus_rolls PASSED                 [100%]

============================== 8 passed in 0.04s ==============================
```

## Result

All 8 tests pass. Implementation complete: `game.py` (Game class), `test_game.py`
(pytest test suite), and this transcript, all saved under
`D:\user\education\2026_CRA_AI\workspace\bowling-tdd\tdd-skill-workspace\iteration-1\bowling-game\without_skill\outputs\`.
