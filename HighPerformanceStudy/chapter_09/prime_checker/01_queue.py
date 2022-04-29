import time
import multiprocessing

from base_function import check_prime_queue, ALL_DONE, FINISHED_PROCESSING


if __name__ == "__main__":
    n_worker = 2
    primes = list()

    # manager = multiprocessing.Manager()
    possible_queue = multiprocessing.Queue()
    definite_queue = multiprocessing.Queue()

    pool = multiprocessing.Pool(n_worker)
    processes = list()
    for _ in range(n_worker):
        p = multiprocessing.Process(target=check_prime_queue, args=(possible_queue, definite_queue))
        processes.append(p)
        p.start()
    t_start = time.time()

    number_range = range(100000000, 100100000)
    for possible_prime in number_range:
        possible_queue.put(possible_prime)
    for n in range(n_worker):
        possible_queue.put(ALL_DONE)

    finished_processors = 0
    while True:
        new_result = definite_queue.get()
        if new_result == FINISHED_PROCESSING:
            finished_processors += 1
            if finished_processors == n_worker:
                break
        else:
            primes.append(new_result)

    assert finished_processors == n_worker

    print("Took:", time.time() - t_start)
    print(len(primes), primes[0:10], primes[-10:])
