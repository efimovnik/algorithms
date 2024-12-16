from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ans = -1
        for number, freq in counts.items():
            if number == freq:
                ans = max(ans, number)
        return ans
    
# time: O(2 * n) = O(n)
# space: O(n)