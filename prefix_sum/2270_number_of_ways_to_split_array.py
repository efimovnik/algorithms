class Solution:
# prefix sum straightforward soultion
#    def waysToSplitArray(self, nums: List[int]) -> int:
#         prefix = [nums[0]]
#        res = 0
#        for i in range(1, len(nums)):
#            prefix.append(nums[i] + prefix[-1])
#        for j in range(len(prefix) - 1):
#            if prefix[j] >= prefix[-1] - prefix[j]:
#                res += 1
#        return res
    
# time complexity: O(n)
# space complexity: O(n)

# prefix sum optimized solution, without using prefix array, just using prefix sum
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = right_sum = res = 0
        for i in nums:
            right_sum += i
        for j in range(len(nums) - 1):
            left_sum += nums[j]
            if left_sum >= right_sum - left_sum:
                res += 1
        return res

# time complexity: O(n)
# space complexity: O(1)
```