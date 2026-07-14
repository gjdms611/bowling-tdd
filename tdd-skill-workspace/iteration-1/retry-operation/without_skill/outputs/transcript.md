# Transcript: retry_operation implementation

Task: Write a `retry_operation(fn)` function in Python that retries a callable
up to 3 times if it raises, returning the result on success, and re-raising
after the 3rd failure.

## Commands run (in order)

### 1. Check environment

```
$ python --version
Python 3.11.5

$ pip show pytest
Name: pytest
Version: 9.1.1
```

### 2. Created source file

`retry_operation.py`

```python
def retry_operation(fn):
    """Call fn, retrying up to 3 times if it raises.

    Returns fn()'s result on the first success. If fn raises on all
    3 attempts, the exception from the last attempt is re-raised.
    """
    last_exception = None
    for _ in range(3):
        try:
            return fn()
        except Exception as exc:
            last_exception = exc
    raise last_exception
```

### 3. Created test file

`test_retry_operation.py` with 4 tests:
- `test_returns_result_on_first_success`
- `test_succeeds_after_failures_within_limit`
- `test_reraises_after_third_failure`
- `test_does_not_retry_beyond_three_attempts`

### 4. Ran tests

```
$ python -m pytest test_retry_operation.py -v

============================= test session starts =============================
platform win32 -- Python 3.11.5, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\user\education\2026_CRA_AI\workspace\bowling-tdd\tdd-skill-workspace\iteration-1\retry-operation\without_skill\outputs
collected 4 items

test_retry_operation.py::test_returns_result_on_first_success PASSED     [ 25%]
test_retry_operation.py::test_succeeds_after_failures_within_limit PASSED [ 50%]
test_retry_operation.py::test_reraises_after_third_failure PASSED        [ 75%]
test_retry_operation.py::test_does_not_retry_beyond_three_attempts PASSED [100%]

============================== 4 passed in 0.04s ==============================
```

## Result

All 4 tests pass. Implementation is complete: `retry_operation(fn)` calls
`fn()` up to 3 times, returning the result on the first successful call,
and re-raising the last exception if all 3 attempts fail.
