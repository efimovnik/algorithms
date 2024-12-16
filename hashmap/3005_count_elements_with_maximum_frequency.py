from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Counter solution
        # time: O(3n)
        # space: (n)
        counts = Counter(nums)
        max_freq = max(counts.values())
        return sum([i for i in counts.values() if i == max_freq])