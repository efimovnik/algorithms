from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)  
        for i in s:
            counts[i] += 1
        frequencies = counts.values()
        return len(set(frequencies)) == 1
    
# one liner:
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
    
    # time O(n)
    # space O(k) where k is the number of unique characters in the string (26)