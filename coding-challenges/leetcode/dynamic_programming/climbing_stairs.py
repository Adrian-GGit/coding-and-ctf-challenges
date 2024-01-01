# binomial coefficient
class Solution:
    def fak(self, n):
        if n <= 1:
            return 1
        return n * self.fak(n - 1)

    def n_over_k(self, n, k):
        return (self.fak(n) / (self.fak(n - k) * self.fak(k)))

    def climbStairs(self, n: int) -> int:
        possible_steps = 0
        for k in range(n // 2 + 1):
            possible_steps += self.n_over_k(n - k, k)
        return int(possible_steps)
    
# fibonacci/dynamic programming
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)