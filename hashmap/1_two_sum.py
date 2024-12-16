from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            main = nums[i]
            complement = target - main
            if complement in dic:
                return [i,dic[complement]]
            dic[main] = i
        return [-1,1]

# time: O(n)
# space: O(n)
            