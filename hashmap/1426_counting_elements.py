from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set, result = set(arr), 0
        for i in arr:
            if i + 1 in hash_set:
                result += 1
        return result