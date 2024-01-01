class Solution:
    def reverse(self, x: int) -> int:
        x_s = str(abs(x))[::-1]
        x_i = int(x_s) * -1 if  x < 0 else int(x_s)
        return x_i if (x_i >= (-2 ** 31) and x_i <= (2 ** 31) - 1) else 0
