from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = res = 0
        curr = 1
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            res += right - left + 1
        return res

Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100) # 8
# speed complexity: O(n)
# space complexity: O(1)