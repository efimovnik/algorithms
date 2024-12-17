from collections import defaultdict

# 791. Custom Sort String
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.

 

# Example 1:
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation:  "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:
# Input: order = "bcafg", s = "abcd"
# Output: "bcad"
# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.


# Solution with 2 lists
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = defaultdict(int)
        head, tail = [], []
        for i in s:
            if i in order:
                count[i] += 1
            else:
                tail.append(i) 
        for j in order:
            head.append(j * count[j])
        return "".join(head) + "".join(tail)
    
    # time: O(n + m)
    # space: O(n)

    # optimized solution with pop() and Counter, time and space are the same

from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        res = []
        for i in order:
            res.append(i * counts.pop(i, 0))
        for j in counts:
            res.append(j * counts[j])
        return "".join(res)