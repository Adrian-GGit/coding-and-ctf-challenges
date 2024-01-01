from itertools import zip_longest
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        for c1, c2 in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            c1, c2 = int(c1), int(c2)
            result = str(c1 ^ c2 ^ carry) + result
            carry = int(c1 + c2 + carry >= 2)
            a = a[:-1]
            b = b[:-1]
        if carry:
            result = str(carry) + result
        return result