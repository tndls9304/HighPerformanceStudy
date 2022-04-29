import os
import random

from HighPerformanceStudy.utils import time_fn


@time_fn
def estimate_pi(estimates):
    print(f"Executing estimate_pi with {estimates}:, on pid {os.getpid()}")
    pi_trials = 0
    for step in range(int(estimates)):
        x = random.random()
        y = random.random()
        is_in_unit_circle = x * x + y * y <= 1.0
        if is_in_unit_circle:
            pi_trials += 1
    return 4 * float(pi_trials) / estimates
