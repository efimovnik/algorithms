class Solution:
    def repeatedCharacter(self, s: str) -> str:
        memory = set()
        for i in s:
            if i in memory:
                return i
            memory.add(i)
# time: O(n)
# space: O(n)