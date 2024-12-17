from collections import defaultdict
from itertools import zip_longest

# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        char_to_word = defaultdict(str)
        word_to_char = defaultdict(str)
        for word, symbol in zip(words, pattern):
            if symbol in char_to_word and char_to_word[symbol] != word:
                return False
            if word in word_to_char and word_to_char[word] != symbol:
                return False
            char_to_word[symbol] = word
            word_to_char[word] = symbol
        return True
    
# time: O(n)
# space: O(n + k) = O(n)

# 2-liner solution with zip_longest
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(zip_longest(s, pattern))
    # the only reason to use zip_longest - is to handle edge case where len(s) != len(pattern). otherwise we could use normal zip

    