from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            
# Time complexity: O(n)
# Space complexity: O(1)