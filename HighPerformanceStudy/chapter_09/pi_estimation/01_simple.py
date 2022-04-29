from base_function import estimate_pi

if __name__ == "__main__":
    trials = 10000000
    estimated_pi = estimate_pi(trials)
    print(f'estimated pi: {estimated_pi}')
    