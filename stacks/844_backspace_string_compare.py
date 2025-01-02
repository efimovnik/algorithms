# 844. Backspace String Compare
# Easy

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def format_string(string: str) -> list:
            stack = []
            for char in string:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack
        
        return format_string(s) == format_string(t)
        
# time: O(n + k)
# space: O(n + k)