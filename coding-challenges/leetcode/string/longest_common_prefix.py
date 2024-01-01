class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = []
        first = strs[0]
        cont = False
        for i, c in enumerate(first):
            for word in strs[1:]:
                if i >= len(word):
                    cont = True
                    break
                if word[i] != c:
                    cont = True
                    break
            if cont:
                break
            l.append(c)
        return "".join(l)