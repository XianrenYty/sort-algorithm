import numpy as np

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    np.random.seed(2023)
    nums = list(np.random.randint(0, 20, size=10))
    print(nums)
    print(bubble_sort(nums))