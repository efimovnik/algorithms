class Solution:
    def reverse_string(s: List[str]):
        left, right = 0, len(s) - 1
        for i in s:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s