from HighPerformanceStudy import time_fn


@time_fn
def get_fibonacci_from_list(n):
    numbers = [0, 1]
    if n == 0:
        return numbers[-2]
    elif n == 1:
        return numbers[-1]
    while len(numbers) <= n:
        numbers.append(numbers[-1] + numbers[-2])
    return numbers[-1]


@time_fn
def get_fibonacci_from_generator(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    for _ in range(n-1):
        a, b = b, a+b
    return b


if __name__ == "__main__":
    # get n-th fibonacci number
    target_n = 100000
    get_fibonacci_from_list(target_n)
    get_fibonacci_from_generator(target_n)
