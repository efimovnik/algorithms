    # * Write a Python function to find the factorial of a number.

# def fact(n):
#     ans = 1
#     if n in (0, 1):
#         return ans
#     for i in range(1,n):
#         ans *= i
#     return ans

# print(fact(5))

#     * How would you implement a binary search algorithm?
# def binary_search(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(list(zip(*grid)))