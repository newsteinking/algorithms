from algorithms.sort import sort_colors
import random

def sort_colors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

#
# if __name__ == "__main__":
#     nums = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 2]
#     sort_colors(nums)
#     print(nums)

alist=[random.randint(0,2) for i in range(10)]
print(alist)
sort_colors(alist)
print(alist)