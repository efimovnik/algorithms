class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exists = set(nums)
        for i in range(len(nums) + 1):
            if i not in exists:
                return i