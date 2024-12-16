from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = prefix = nums[0]
        for i in range(1, len(nums)):
            prefix += nums[i]
            min_value = min(min_value, prefix)
        return abs(min_value) + 1 if min_value < 1 else 1
#time: O(n)
#space: O(1)