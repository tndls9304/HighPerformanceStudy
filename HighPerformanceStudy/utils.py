import time

from functools import wraps


def time_fn(func):
    @wraps(func)
    def measure_time(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        print(f"@time_fn: {func.__name__} took {t_end-t_start:.6f} seconds")
        return result
    return measure_time
