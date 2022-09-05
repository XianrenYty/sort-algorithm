from heapq import merge
import numpy as np
import random
from pandas import pivot
import pytest


def merge_sort(nums, l, r):  # O(nlog(n))/O(n)
    if l == r:
        return

    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    tmp = []
    i, j = l, mid + 1
    while i <= mid or j <= r:
        if i > mid or (j <= r and nums[j] < nums[i]):
            tmp.append(nums[j])
            j += 1
        else:
            tmp.append(nums[i])
            i += 1
    nums[l:r+1] = tmp

    return nums


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == merge_sort(nums, 0, len(nums) - 1)
    return


if __name__ == '__main__':
    random.seed(2023)
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(merge_sort(nums, 0, len(nums) - 1))
