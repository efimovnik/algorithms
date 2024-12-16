from collections import Counter
from typing import List


# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        return len(set(counts.values())) == len(set(counts.keys()))
    
# time: O(n)
# space: O(n)