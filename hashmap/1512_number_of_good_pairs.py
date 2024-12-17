from typing import List
from collections import Counter
import math

# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([math.comb(i,2) for i in Counter(nums).values()])
    
# time: O(2 * n) = O(n)
# space: O(n)

# p.s. comb is a in-built function to create possible unrepeated pairs between number i and k

# alternative solution is a nested loop:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
            
        return ans