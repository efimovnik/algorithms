from collections import Counter


# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a 
# permutation
#  of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts, window, matched = Counter(s1), len(s1), 0
        
        for i in range(len(s2)):
            if s2[i] in counts:
                counts[s2[i]] -= 1
                if counts[s2[i]] == 0:
                    matched += 1
            if s2[i-window] in counts and i >= window:
                if counts[s2[i-window]] == 0:
                    matched -= 1
            if matched == len(counts):
                return True
        
        return False

# time: O(n)
# space: O(1)