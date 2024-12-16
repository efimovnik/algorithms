from collections import defaultdict
from typing import List
# 1st solution - keep indices in dict
# time complexity: O(n + m*k)
# space complexity: O(n + m)

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indices = defaultdict(list)
        res = float("inf")
        
        # Populate indices with card positions
        for i, card in enumerate(cards):
            indices[card].append(i)
        
        # Check minimum distance between adjacent indices for each card
        for positions in indices.values():
            for index in range(len(positions) - 1):
                res = min(res, positions[index + 1] - positions[index] + 1)
        
        return res if res < float("inf") else -1
    
# solution with dict(int) and enum
# time: O(n)
# space: O(n)
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ind = defaultdict(int)
        res = float("inf")
        for i, v in enumerate(cards):
            if v in ind:
                res = min(res, i - ind[v] + 1)
            ind[v] = i
        return res if res < float("inf") else -1