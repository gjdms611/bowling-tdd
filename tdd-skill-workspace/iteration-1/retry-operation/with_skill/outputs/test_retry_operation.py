import pytest

from retry_operation import retry_operation


def test_retries_failed_operations_3_times():
    attempts = 0

    def operation():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise RuntimeError("fail")
        return "success"

    result = retry_operation(operation)

    assert result == "success"
    assert attempts == 3


def test_reraises_after_3rd_failure_and_stops_retrying():
    attempts = 0

    def operation():
        nonlocal attempts
        attempts += 1
        raise ValueError("always fails")

    with pytest.raises(ValueError, match="always fails"):
        retry_operation(operation)

    assert attempts == 3
