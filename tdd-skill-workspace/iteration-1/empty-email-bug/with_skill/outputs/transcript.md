# Transcript: Fix "empty email allowed" bug in submit_form

Following `.claude/skills/tdd-skill/SKILL.md`, section "디버깅 통합" (bug-fixing
integration): reproduce the bug with a failing test first, confirm RED, then
fix minimally, confirm GREEN.

## Starting point: the buggy code (pre-existing, given)

Since this task requires fixing an existing bug, a plausible buggy
`submit_form` was created first to represent "the codebase as found" — this
is the artifact under test, not code written ahead of a test in violation of
the Iron Law. The bug: it checks `"email" in data` (key presence) but never
checks that the value is non-blank, so `{"email": ""}` is treated as valid.

`submit_form.py` (buggy, before any fix):

```python
def submit_form(data):
    if "email" in data:
        # TODO: send confirmation email, persist record, etc.
        return {"success": True}
    return {"error": "Email required"}
```

## RED — write the failing reproduction test

`test_submit_form.py` (first test written):

```python
from submit_form import submit_form


def test_rejects_empty_email():
    result = submit_form({"email": ""})
    assert result["error"] == "Email required"
```

Command:

```
python -m pytest test_submit_form.py -v
```

Actual output (against the buggy code above):

```
test_submit_form.py::test_rejects_empty_email FAILED                     [100%]

================================== FAILURES ===================================
__________________________ test_rejects_empty_email ___________________________

    def test_rejects_empty_email():
        result = submit_form({"email": ""})
>       assert result["error"] == "Email required"
               ^^^^^^^^^^^^^^^
E       KeyError: 'error'

test_submit_form.py:6: KeyError
=========================== short test summary info ===========================
FAILED test_submit_form.py::test_rejects_empty_email - KeyError: 'error'
1 failed in 0.15s
```

RED verified: it fails for the expected reason — the buggy code returns
`{"success": True}` for `{"email": ""}` because `"email" in data` is `True`
even when the value is blank, so `result["error"]` doesn't exist
(`KeyError: 'error'`). Not a typo, not an import error — genuinely missing
behavior.

## GREEN — minimal fix

Edited `submit_form.py`:

```python
def submit_form(data):
    email = data.get("email", "")
    if not email.strip():
        return {"error": "Email required"}
    # TODO: send confirmation email, persist record, etc.
    return {"success": True}
```

Command:

```
python -m pytest test_submit_form.py -v
```

Actual output:

```
test_submit_form.py::test_rejects_empty_email PASSED                     [100%]

1 passed in 0.03s
```

GREEN verified: test passes, clean output, no warnings/errors.

## Additional edge case: whitespace-only email

The task calls out "empty/whitespace-only emails" explicitly, so a
parametrized test was added (following the skill's pytest guidance: use
`parametrize` for the same behavior/rule across multiple inputs):

```python
@pytest.mark.parametrize("email", ["", "   ", "\t\n"])
def test_rejects_blank_email(email):
    result = submit_form({"email": email})
    assert result["error"] == "Email required"
```

### RED check against the original buggy code

Before trusting that the existing fix already covered this, the buggy
`submit_form` was temporarily restored and the full test file re-run to
confirm every case fails against the bug (not just pass by accident):

Command:

```
python -m pytest test_submit_form.py -v
```

Actual output (against buggy code):

```
test_submit_form.py::test_rejects_empty_email FAILED                     [ 25%]
test_submit_form.py::test_rejects_blank_email[] FAILED                   [ 50%]
test_submit_form.py::test_rejects_blank_email[   ] FAILED                [ 75%]
test_submit_form.py::test_rejects_blank_email[\t\n] FAILED               [100%]

... (KeyError: 'error' for all four) ...

4 failed in 0.21s
```

RED verified for all four cases (empty string, spaces, tab+newline).

### GREEN check against the fixed code

The fix was restored (no additional code changes were required — `.strip()`
already handles whitespace-only strings, since an all-whitespace string
stripped to `""` is falsy) and the suite re-run:

Command:

```
python -m pytest test_submit_form.py -v
```

Actual output:

```
test_submit_form.py::test_rejects_empty_email PASSED                     [ 25%]
test_submit_form.py::test_rejects_blank_email[] PASSED                   [ 50%]
test_submit_form.py::test_rejects_blank_email[   ] PASSED                [ 75%]
test_submit_form.py::test_rejects_blank_email[\t\n] PASSED               [100%]

4 passed in 0.02s
```

GREEN verified: all 4 tests pass, clean output.

## REFACTOR

No refactor needed — the fix is already minimal (3 lines) and there is only
one validation rule, so there's no duplication to extract yet. Per the
skill's guidance, extraction of a shared validation helper should wait until
more fields need similar validation.

## Verification checklist (from SKILL.md)

- [x] New function has tests
- [x] Each test was seen failing before implementation
- [x] Each test failed for the expected reason (missing behavior, not a typo)
- [x] Minimal code written to pass each test
- [x] All tests pass
- [x] Output is clean (no errors/warnings)
- [x] Tests use real code, no mocks
- [x] Edge cases covered (empty string, whitespace-only, tab/newline)

## Final files

- `submit_form.py` — fixed implementation
- `test_submit_form.py` — test file (2 tests, 4 cases total)
- `transcript.md` — this file
