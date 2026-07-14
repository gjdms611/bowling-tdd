import pytest

from retry_operation import retry_operation


def test_returns_result_on_first_success():
    calls = []

    def fn():
        calls.append(1)
        return "ok"

    assert retry_operation(fn) == "ok"
    assert len(calls) == 1


def test_succeeds_after_failures_within_limit():
    calls = []

    def fn():
        calls.append(1)
        if len(calls) < 3:
            raise ValueError("boom")
        return "recovered"

    assert retry_operation(fn) == "recovered"
    assert len(calls) == 3


def test_reraises_after_third_failure():
    calls = []

    def fn():
        calls.append(1)
        raise ValueError(f"fail {len(calls)}")

    with pytest.raises(ValueError, match="fail 3"):
        retry_operation(fn)

    assert len(calls) == 3


def test_does_not_retry_beyond_three_attempts():
    calls = []

    def fn():
        calls.append(1)
        raise RuntimeError("always fails")

    with pytest.raises(RuntimeError):
        retry_operation(fn)

    assert len(calls) == 3
