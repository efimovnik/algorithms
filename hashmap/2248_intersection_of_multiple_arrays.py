from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        ans = []
        for array in nums:
            for i in array:
                counts[i] += 1
        for key in counts:
            if counts[key] == len(nums):
                ans.append(key)
        return sorted(ans)
    
# time: O(n * m)
# space: O(n)