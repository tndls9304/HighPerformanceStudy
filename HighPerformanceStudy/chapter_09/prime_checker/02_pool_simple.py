import math
from multiprocessing import Pool
from base_function import create_range, check_prime_in_range, time_fn


@time_fn
def check_prime_pool(n, pools, n_worker):
    n_start = 3
    n_end = int(math.sqrt(n)) + 1
    ranges_to_check = create_range(n_start, n_end, n_worker)
    ranges_to_check = zip(len(ranges_to_check) * [n], ranges_to_check)
    # assert len(ranges_to_check) == n_worker

    result = pools.map(check_prime_in_range, ranges_to_check)
    if False in result:
        print(f'{n} is not prime number')
        return False
    print(f'{n} is prime number')
    return True


if __name__ == "__main__":
    n_blocks = 4
    target = 63018038201
    pool = Pool(processes=n_blocks)

    check_prime_pool(target, pool, n_blocks)
