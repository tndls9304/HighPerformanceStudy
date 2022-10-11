import math

from HighPerformanceStudy.utils import time_fn

ALL_DONE = b'WORK_FINISHED'
FINISHED_PROCESSING = b'PROCESS_FINISHED'
FLAG_CLEAR = b'0'
FLAG_NAME = b'redis_primes_flag'
FLAG_SET = b'1'
CHECK_EVERY = 1000


def check_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number) + 1), 2):
        if number % i == 0:
            return False
    return True


def create_range(n_start, n_end, n_worker):
    interval = int((n_end - n_start) / n_worker)
    if interval % 2 != 0:
        interval = interval + 1
    return [(n_start+(i*interval), n_start+((i+1)*interval)) for i in range(n_worker-1)] + [(n_start+(n_worker-1)*interval, n_end)]


def check_prime_in_range(n_from_v_to_v):
    (n, (from_v, to_v)) = n_from_v_to_v
    if n % 2 == 0:
        return False
    assert from_v % 2 != 0
    for i in range(from_v, int(to_v), 2):
        if n % i == 0:
            return False
    return True


def check_prime_in_range_value(n_from_v_to_v):
    (n, (from_v, to_v), value) = n_from_v_to_v
    if n % 2 == 0:
        return False
    assert from_v % 2 != 0
    for ii, i in enumerate(range(from_v, int(to_v), 2)):
        if (ii+1) % CHECK_EVERY == 0:
            if value.value == b'1':
                return False
        if n % i == 0:
            value.value = b'1'
            return False
    return True


def check_prime_queue(possible_queue, definite_queue):
    while True:
        n = possible_queue.get()
        if n == ALL_DONE:
            definite_queue.put(FINISHED_PROCESSING)
            break
        else:
            if n % 2 == 0:
                continue
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    break
            else:
                definite_queue.put(n)
