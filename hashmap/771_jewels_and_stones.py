class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        stones_count = Counter(stones)
        for i in set(jewels):
            ans += stones_count[i]
        return ans