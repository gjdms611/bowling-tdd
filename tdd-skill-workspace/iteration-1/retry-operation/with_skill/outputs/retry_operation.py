def retry_operation(fn):
    for i in range(3):
        try:
            return fn()
        except Exception:
            if i == 2:
                raise
