class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = ""
        for c in s:
            if c not in substring:
                substring += c
            else:
                longest = max(len(substring), longest)
                substring = substring[substring.find(c) + 1:] + c
        return max(len(substring), longest)