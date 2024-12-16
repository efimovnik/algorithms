from typing import List

# straightforward sliding window solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = curr = res = 0
        while right < k:
            curr += nums[right]
            right += 1
        res = curr
        while right < len(nums):
            curr += nums[right] - nums[left]
            res = max(res, curr)
            right += 1
            left += 1
        return res/k
    # optimized sliding window solution
    def findMaxAverageOptimized(self, nums: List[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum/k

        
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75)
print(Solution().findMaxAverageOptimized([1,12,-5,-6,50,3], 4) == 12.75)


