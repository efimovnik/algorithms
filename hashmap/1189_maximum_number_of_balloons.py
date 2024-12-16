from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        counter = defaultdict(int)
        ans = math.inf
        for i in text:
            if i in balloon:
                counter[i] += 1
        for key, value in balloon.items():
            if key in counter:
                ans = min(ans, counter[key] // value)
            else:
                return 0
        return ans