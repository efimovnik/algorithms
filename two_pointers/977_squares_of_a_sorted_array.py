from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = ans = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return list(reversed(res)) # speed complexity is O(n), but space complexity is O(n)
        ans = res.reverse()
        return ans # spped complexity is O(n), but space complexity is O(1)
        return res[::-1] # speed complexity is O(n), but space complexity is O(n)

print(Solution().sortedSquares([-4,-1,0,3,10])) # [0,1,9,16,100]
