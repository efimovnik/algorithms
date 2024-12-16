from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
    
# time: O(n)
# space: O(n)