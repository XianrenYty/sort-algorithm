import numpy as np
import pytest


def counting_sort(nums):  # O(n + k)/O(k), k is the range of nums
    nums_max, nums_min = max(nums), min(nums)
    size = (nums_max - nums_min + 1)
    counts = [0] * size

    # 统计值为 num 的元素出现的次数
    for num in nums:
        counts[num - nums_min] += 1

    # 计算元素排名
    for j in range(1, size):
        counts[j] += counts[j - 1]

    # 反向填充数组
    res = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        # 根据排名，将 nums[i] 放在数组对应位置
        res[counts[nums[i] - nums_min] - 1] = nums[i]
        # 将 nums[i] 的对应排名减 1
        counts[nums[i] - nums_min] -= 1

    return res


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == counting_sort(nums)
    return


if __name__ == '__main__':
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(counting_sort(nums))
