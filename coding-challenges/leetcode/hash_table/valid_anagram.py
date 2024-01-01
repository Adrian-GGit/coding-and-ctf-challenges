class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for s_c, t_c in zip(s, t):
            s_dict[s_c] = s_dict[s_c] + 1 if s_c in s_dict else 1
            t_dict[t_c] = t_dict[t_c] + 1 if t_c in t_dict else 1
        return s_dict == t_dict
