# 930. Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array. 

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

from typing import List
import math


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pass
print(math.comb(5,2))