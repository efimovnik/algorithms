from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        return sum([i for i in counts if counts[i] == 1])
    
# time: O(n)
# space: O(n)