import time
import math

from multiprocessing import Pool
from base_function import FLAG_NAME, FLAG_CLEAR, rds, check_prime_in_range_redis, create_range

SERIAL_CHECK_CUTOFF = 21


def check_prime_redis(n, pools, n_worker):
    n_start = 3
    n_end = SERIAL_CHECK_CUTOFF
    rds[FLAG_NAME] = FLAG_CLEAR
    if not check_prime_in_range_redis((n, (n_start, n_end))):
        print(f'{n} is not prime number')
        return False

    n_start, n_end = n_end, int(math.sqrt(n)) + 1
    ranges_to_check = create_range(n_start, n_end, n_worker)
    ranges_to_check = zip([n]*n_worker, ranges_to_check)

    result = pools.map(check_prime_in_range_redis, ranges_to_check)
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
    check_prime_redis(target, pool, n_blocks)

    print(f'Took {time.time()-start_time} seconds')
