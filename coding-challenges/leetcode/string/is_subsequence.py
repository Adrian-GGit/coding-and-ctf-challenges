class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): 
            return False
        index = 0

        for c_t in t:
            if len(s) == index:
                return True
            if s[index] == c_t:
                index += 1
        return len(s) == index