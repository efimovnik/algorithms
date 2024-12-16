from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_tuple(element):
            return tuple(element)

        rows_dict = defaultdict(int)
        col_dict = defaultdict(int)

        for row in grid:
            rows_dict[convert_to_tuple(row)] += 1

        columns = list(zip(*grid))
        for column in columns:
            col_dict[convert_to_tuple(column)] += 1
        ans = 0
        for i in rows_dict:
            ans += rows_dict[i] * col_dict[i]
        return ans
    
# time: O(n ** 2)
# space: O(n ** 2)