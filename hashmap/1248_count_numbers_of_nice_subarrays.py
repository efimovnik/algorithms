from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        for i in nums:
            curr += i % 2
            ans += counts[curr - k]
            counts[curr] += 1
        return ans
# time: O(n)
# space: O(n)