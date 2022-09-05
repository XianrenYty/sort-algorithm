import numpy as np
import pytest


def insertion_sort(nums):  # O(n**2)/O(1)
    n = len(nums)
    # 遍历无序序列
    for i in range(1, n):
        tmp = nums[i]
        j = i
        # 从右至左遍历有序序列
        while j > 0 and nums[j - 1] > tmp:
            # 将有序序列中插入位置右侧的元素依次右移一位
            nums[j] = nums[j - 1]
            j -= 1
        # 将该元素插入到适当位置
        nums[j] = tmp

    return nums


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == insertion_sort(nums)
    return


if __name__ == '__main__':
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(insertion_sort(nums))
