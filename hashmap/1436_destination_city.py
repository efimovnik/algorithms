class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations, arrivals = set(), set()
        for i in paths:
            arrivals.add(i[0])
            destinations.add(i[1])
        return next(iter(destinations.difference(arrivals)))

# time: O(n)
# space: O(n)    
# optimized for readability

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities, end_cities = map(set, zip(*paths))
        destination = (end_cities - start_cities).pop()
        return destination