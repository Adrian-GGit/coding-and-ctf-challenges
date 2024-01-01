class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for c_s, c_t in zip(s, t):
            if c_s not in s_to_t and c_t not in t_to_s:
                s_to_t[c_s] = c_t
                t_to_s[c_t] = c_s
            elif c_s in s_to_t and c_t in t_to_s:
                if s_to_t[c_s] != c_t or t_to_s[c_t] != c_s:
                    return False
                else:
                    continue
            else:
                return False
        return True