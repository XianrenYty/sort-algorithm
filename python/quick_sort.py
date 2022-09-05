import numpy as np
import random
from pandas import pivot
import pytest


def randomized_partition(nums, l, r):
    pivot = random.randint(l, r)
    nums[pivot], nums[r] = nums[r], nums[pivot]
    i = l - 1
    for j in range(l, r):
        if nums[j] < nums[r]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

def quick_sort(nums, l, r):  # O(nlog(n))/O(n)
    if l < r:
        mid = randomized_partition(nums, l, r)
        quick_sort(nums, l, mid - 1)
        quick_sort(nums, mid + 1, r)

    return nums


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == quick_sort(nums, 0, len(nums) - 1)
    return


if __name__ == '__main__':
    random.seed(2023)
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(quick_sort(nums, 0, len(nums) - 1))
