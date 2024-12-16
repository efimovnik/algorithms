class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calculate_digit_sum(num: int) -> int:
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        ans = -1
        seen = defaultdict(int)
        for i in nums:
            curr = calculate_digit_sum(i)
            if curr in seen:
                ans = max(ans, seen[curr] + i)
            seen[curr] = max(seen[curr], i)
        return ans 
# time: O(n)
# space: O(n)