import time
import math
from multiprocessing import Pool, Manager

from base_function import check_prime_in_range_value, create_range, time_fn


SERIAL_CHECK_CUTOFF = 21
FLAG_CLEAR = b'0'
FLAG_SET = b'1'


@time_fn
def check_prime_value(n, pools, n_worker, values):
    n_start = 3
    n_end = SERIAL_CHECK_CUTOFF
    values.value = FLAG_CLEAR
    if not check_prime_in_range_value((n, (n_start, n_end), values)):
        print(f'{n} is not prime number')
        return False

    n_start, n_end = n_end, int(math.sqrt(n)) + 1
    ranges_to_check = create_range(n_start, n_end, n_worker)
    ranges_to_check = zip([n]*n_worker, ranges_to_check, [values]*n_worker)

    result = pools.map(check_prime_in_range_value, ranges_to_check)
    if False in result:
        print(f'{n} is not prime number')
        return False
    print(f'{n} is prime number')
    return True


if __name__ == "__main__":
    start_time = time.time()
    n_blocks = 4
    # target = 63018038201
    target = 6301803820159
    pool = Pool(processes=n_blocks)
    manager = Manager()
    value = manager.Value(b'c', FLAG_CLEAR)
    check_prime_value(target, pool, n_blocks, value)

    print(f'Took {time.time()-start_time} seconds')
