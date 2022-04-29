from HighPerformanceStudy.utils import time_fn


@time_fn
def linear_search(array, target):
    for i, item in enumerate(array):
        if item == target:
            return i
    return -1


if __name__ == "__main__":
    target_list = [3, 5, 22, 1, 9, 41, 15, 4, 2, 8]*1000 + [23]
    print(linear_search(target_list, 23))
    print(target_list[linear_search(target_list, 23)])
