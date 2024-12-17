from typing import List

# 1695. Maximum Erasure Value
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

# Example 1:
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

# Example 2:
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, ans, curr = 0, 0, 0
        seen = set()
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr -= nums[left]
                left += 1
            curr += nums[right]
            ans = max(ans, curr)
            seen.add(nums[right])
        return ans
    
    # time: O(n)
    # space: O(n)
