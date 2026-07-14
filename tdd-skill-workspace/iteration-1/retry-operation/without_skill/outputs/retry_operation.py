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
