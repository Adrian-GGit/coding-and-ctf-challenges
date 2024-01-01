class Solution:
    def isValid(self, s: str) -> bool:
        to_delete = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        brackets = []
        for c in s:
            is_closed_bracket = to_delete.get(c)
            if not is_closed_bracket:
                brackets.append(c)
            elif brackets and to_delete.get(c) == brackets[-1]:
                brackets.pop()
            else:
                return False
        return not brackets