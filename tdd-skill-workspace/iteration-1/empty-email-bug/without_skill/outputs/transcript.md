# Transcript: fixing empty-email bug in `submit_form`

Working directory:
`D:\user\education\2026_CRA_AI\workspace\bowling-tdd\tdd-skill-workspace\iteration-1\empty-email-bug\without_skill\outputs`

## 1. Task

`submit_form(data)` currently allows an empty email through. Reproduce a
plausible buggy version, then fix it so empty / whitespace-only emails
are rejected with `{"error": "Email required"}`.

## 2. Buggy version created

File: `submit_form_buggy.py`

```python
def submit_form(data):
    if "email" not in data:
        return {"error": "Email required"}

    # BUG: no check that data["email"] is actually non-blank.
    # An empty string "" or "   " passes right through here.

    return {"success": True, "data": data}
```

This only checks that the `"email"` key is *present* in `data`, not that
its value is non-blank. `""` and `"   "` both pass the `"email" not in
data` check and fall through to `success: True`.

## 3. Commands run

### Reproduce the bug

```
$ python -c "
from submit_form_buggy import submit_form
print(submit_form({'name': 'Alice', 'email': ''}))
print(submit_form({'name': 'Alice', 'email': '   '}))
"
```

Output:

```
{'success': True, 'data': {'name': 'Alice', 'email': ''}}
{'success': True, 'data': {'name': 'Alice', 'email': '   '}}
```

Confirms the bug: empty and whitespace-only emails are accepted as
successful submissions.

### Fix applied

File: `submit_form.py`

```python
def submit_form(data):
    email = data.get("email", "")

    if not email or not email.strip():
        return {"error": "Email required"}

    return {"success": True, "data": data}
```

`data.get("email", "")` handles a missing key the same way as an empty
value. `not email.strip()` catches whitespace-only strings. Both
collapse to the same clear error response.

### Tests written

File: `test_submit_form.py` — covers:
- missing `"email"` key
- empty string email
- whitespace-only email
- valid email (must still succeed)

### Test run

```
$ python -m pytest -v
```

Output:

```
collected 4 items

test_submit_form.py::test_missing_email_key_is_rejected PASSED         [ 25%]
test_submit_form.py::test_empty_string_email_is_rejected PASSED        [ 50%]
test_submit_form.py::test_whitespace_only_email_is_rejected PASSED     [ 75%]
test_submit_form.py::test_valid_email_is_accepted PASSED               [100%]

============================== 4 passed in 0.03s ==============================
```

All tests pass against the fixed `submit_form.py`.

## 4. Files produced

- `submit_form_buggy.py` — original buggy implementation (reference only)
- `submit_form.py` — fixed implementation (the actual deliverable)
- `test_submit_form.py` — pytest test suite
- `transcript.md` — this file
