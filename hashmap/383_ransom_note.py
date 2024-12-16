from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        for i in ransom_counts:
            if magazine_counts[i] < ransom_counts[i]:
                return False

        return True
    
# Time: O(k * (m + n))
# Space: O(26) -> O(1)

# Optimized solution

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False

        return True

# Time: O(k * (n + m))
# Space: O(n + m)