import joblib
import multiprocessing

from base_function import estimate_pi


if __name__ == "__main__":
    trials = 10000000
    n_blocks = multiprocessing.cpu_count()
    samples_per_worker = trials / n_blocks
    estimated_pi = joblib.Parallel(n_jobs=n_blocks, verbose=1)(
        joblib.delayed(estimate_pi)(samples_per_worker) for sample_idx in range(n_blocks))

    print(f'estimated pi: {estimated_pi}')
