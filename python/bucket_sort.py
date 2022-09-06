import numpy as np
from quick_sort import quick_sort
import pytest


def bucket_sort(nums, bucket_size=25):  # O(n)/O(n + m), m is the num of buckers
    # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
    nums_min, nums_max = min(nums), max(nums)
    # 定义桶的个数为 (最大值元素 - 最小值元素) // 每个桶的大小 + 1
    bucket_count = (nums_max - nums_min) // bucket_size + 1
    # 定义桶数组 buckets
    buckets = [[] for _ in range(bucket_count)]

    # 遍历原始数组元素，将每个元素装入对应区间的桶中
    for num in nums:
        buckets[(num - nums_min) // bucket_size].append(num)

    # 对每个桶内的元素单独排序，并合并到 res 数组中
    res = []
    for bucket in buckets:
        quick_sort(bucket, 0, len(bucket) - 1)
        res.extend(bucket)

    return res


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == bucket_sort(nums)
    return


if __name__ == '__main__':
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(bucket_sort(nums))
