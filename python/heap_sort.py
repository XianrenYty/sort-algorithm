import numpy as np
import pytest


def max_heapify(heap, root, heap_len):
    p = root
    while p * 2 + 1 < heap_len:
        l, r = 2 * p + 1, 2 * p + 2
        if r >= heap_len or heap[r] < heap[l]:
            max_index = l
        else:
            max_index = r
        if heap[p] < heap[max_index]:
            heap[p], heap[max_index] = heap[max_index], heap[p]
            p = max_index
        else:
            break


def build_heap(heap):
    n = len(heap)
    for i in range((n - 2) // 2, -1, -1):
        max_heapify(heap, i, n)


def heap_sort(nums):  # O(nlogn)/O(1)
    build_heap(nums)
    n = len(nums)
    for i in range(n - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)

    return nums


def test_sort():
    for i in range(1000):
        nums = list(np.random.randint(0, 1000, size=50))
        assert sorted(nums) == heap_sort(nums)
    return


if __name__ == '__main__':
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(heap_sort(nums))
