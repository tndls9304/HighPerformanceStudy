import bisect
from HighPerformanceStudy import time_fn


@time_fn
def linear_search(array, target):
    for i, item in enumerate(array):
        if item == target:
            return i
    return -1


@time_fn
def binary_search(array, target):
    # array should be sorted before search
    i_min, i_max = 0, len(array)
    while True:
        if i_min > i_max:
            return -1
        mid = (i_min + i_max) // 2
        if array[mid] > target:
            i_max = mid
        elif array[mid] < target:
            i_min = mid+1
        else:
            return mid


@time_fn
def bisect_search(array, target):
    # bisect_left return the index which the first left value of the index which is ge than the input
    index = bisect.bisect_left(array, target)
    if index == len(array):
        return -1
    else:
        return index


@time_fn
def find_closest(array, target):
    left = bisect.bisect_left(array, target)
    if array[left] == target:
        return left
    else:
        if left > 0:
            left_pre = left-1
            if target - array[left_pre] < array[left] - target:
                return left_pre
    return left


if __name__ == "__main__":
    target_list = [3, 5, 22, 1, 9, 41, 15, 4, 2, 8]*1000 + [23]
    print(linear_search(target_list, 23))
    print(target_list[linear_search(target_list, 23)])
