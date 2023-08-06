class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word[0].isupper() and word[1:].islower() or word.isupper() or word.islower()