from collections import Counter


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        x, y = 0, 0
        seen.add((x, y))
        for i in path:
            if i == "E":
                x += 1
            elif i == "W":
                x -= 1
            elif i == "N":
                y += 1
            elif i == "S":
                y -= 1
            if (x,y) in seen:
                return True
            else:
                seen.add((x,y))
        return False
