from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {}
        ans = curr = 0
        for ind, val in enumerate(nums):
            curr += 1 if val == 1 else  -1
            if curr == 0:
                ans = ind + 1
            elif curr in seen:
                ans = max(ans, ind - seen[curr])
            else:
                seen[curr] = ind
        return ans