from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set(ascii_lowercase)
        for i in sentence:
            if i in alphabet:
                alphabet.remove(i)
        return len(alphabet) == 0

# time: O(n)
# space: O(1) because the alphabet set is constant size