class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            odd = self.expand_from_center(s, i, i)
            even = self.expand_from_center(s, i, i + 1)
            palindrom_len = max(even, odd)
            if palindrom_len > (end - start):
                start, end = i - (palindrom_len - 1) // 2, i + palindrom_len // 2
        return s[start:end + 1]

    def expand_from_center(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1