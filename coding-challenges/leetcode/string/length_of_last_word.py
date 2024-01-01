class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_len = 0
        for c in s[::-1]:
            if c == ' ' and last_word_len:
                break
            last_word_len += 1 if c != ' ' else 0
        return last_word_len