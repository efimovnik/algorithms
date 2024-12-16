from collections import Counter 

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        return max([key for key, value in Counter(nums).items() if value == 1], default=-1)
# Time complexity: O(N)
# space complexity: O(N)