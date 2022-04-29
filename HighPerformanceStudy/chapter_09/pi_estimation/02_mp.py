import multiprocessing
from base_function import estimate_pi


if __name__ == "__main__":
    trials = 10000000
    n_blocks = multiprocessing.cpu_count()
    samples_per_worker = trials / n_blocks
    pool = multiprocessing.Pool(processes=n_blocks)
    print("Making {:,} samples per {} worker".format(samples_per_worker, n_blocks))

    trials_per_process = [samples_per_worker] * n_blocks

    estimated_pi_list = pool.map(estimate_pi, trials_per_process)
    print(f'estimated pi list: ', estimated_pi_list)
    estimated_pi = sum(estimated_pi_list) / n_blocks

    print(f'estimated pi: {estimated_pi}')
