from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = defaultdict(int), defaultdict(int)
        for game in matches:
            
            winners[game[0]] += 1
            losers[game[1]] += 1
        ans_winners, ans_losers = [], []
        for i in winners.keys():
            if i not in losers:
                ans_winners.append(i)
        for key in losers.keys():
            if losers[key] == 1:
                ans_losers.append(key)
        return [sorted(ans_winners),sorted(ans_losers)]
    
# Time complexity: O(N) * O(logN) = O(NlogN)
# Space complexity: O(N)

# solution 2 - using set

from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = defaultdict(int), defaultdict(int)
        for game in matches:
            winners[game[0]] += 1
            losers[game[1]] += 1
        ans_winners = list(set(winners.keys() - set(losers.keys())))
        ans_losers = [key for key, value in losers.items() if value == 1]
        return [sorted(ans_winners),sorted(ans_losers)]
    
# second solution is slower than the first one