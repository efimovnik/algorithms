from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = ans = 0
        for i in nums:
            prefix += i
            ans += counts[prefix-k]
            counts[prefix] += 1
        return ans
    
# time: O(n)
# space: O(n)