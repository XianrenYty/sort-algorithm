import numpy as np
import pytest


def selection_sort(nums):  # O(n**2)/O(1)
    n = len(nums)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_i]:
                min_i = j
        if i != min_i:
            nums[i], nums[min_i] = nums[min_i], nums[i]

    return nums


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == selection_sort(nums)
    return


if __name__ == '__main__':
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(selection_sort(nums))
