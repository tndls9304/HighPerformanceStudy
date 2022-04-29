import joblib
import multiprocessing
import numpy as np


def estimate_pi(samples):
    np.random.seed()
    xs = np.random.uniform(0, 1, samples)
    ys = np.random.uniform(0, 1, samples)
    is_in_unit_circle = (xs * xs + ys * ys) <= 1.0
    pi_trials = sum(is_in_unit_circle)
    return 4 * float(pi_trials) / samples


if __name__ == "__main__":
    trials = 10000000
    n_blocks = multiprocessing.cpu_count()
    samples_per_worker = int(trials / n_blocks)
    estimated_pi = joblib.Parallel(n_jobs=n_blocks, verbose=1)(
        joblib.delayed(estimate_pi)(samples_per_worker) for _ in range(n_blocks))

    print(f'estimated pi: {estimated_pi}')
