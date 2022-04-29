import time
import math
from multiprocessing import Pool
from base_function import check_prime_in_range, create_range, time_fn


@time_fn
def check_prime_pool_complex(n, pools, n_worker):
    n_start = 3
    n_end = 21
    if not check_prime_in_range((n, (n_start, n_end))):
        return False

    n_start, n_end = n_end, int(math.sqrt(n)) + 1
    ranges_to_check = create_range(n_start, n_end, n_worker)
    ranges_to_check = zip([n]*n_worker, ranges_to_check)

    result = pools.map(check_prime_in_range, ranges_to_check)
    if False in result:
        print(f'{n} is not prime number')
        return False
    print(f'{n} is prime number')
    return True


if __name__ == "__main__":
    start_time = time.time()
    n_blocks = 4
    target = 63018038201579
    pool = Pool(processes=n_blocks)

    check_prime_pool_complex(target, pool, n_blocks)

    print(f'Took {time.time()-start_time} seconds')
