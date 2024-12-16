class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: 
            return nums 
        n = len(nums)
        prefix = [nums[0]]
        ans = [-1] * n
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        for j in range(n):
            if j in range(k, n - k):
                ans[j] = (prefix[j + k] - prefix[j - k] + nums[j - k])// (2 * k + 1)
        return ans
# time: O(n)
# space: O(n)