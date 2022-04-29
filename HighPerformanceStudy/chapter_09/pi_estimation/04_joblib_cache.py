import os
import joblib
import multiprocessing

from base_function import estimate_pi

memory = joblib.Memory('./joblib_cache', verbose=0)


@memory.cache
def estimate_pi_idx(estimates, idx):
    print(f"Executing estimate_pi with {estimates} on sample {idx} on pid {os.getpid()}")
    return estimate_pi(estimates)


if __name__ == "__main__":
    trials = 100000000
    n_blocks = multiprocessing.cpu_count()
    samples_per_worker = trials / n_blocks
    estimated_pi = joblib.Parallel(n_jobs=n_blocks, verbose=1)(
        joblib.delayed(estimate_pi_idx)(samples_per_worker, idx) for idx in range(n_blocks))

    print(f'estimated pi: {estimated_pi}')
