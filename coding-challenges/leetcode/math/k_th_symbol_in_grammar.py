class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if (n <= 2): return int(k == 2)
        current_path = True
        num_leafs = 1 << n-1
        while num_leafs > 1:
            num_leafs //= 2
            if k > num_leafs:
                current_path = not current_path
                k -= num_leafs
        return int(not current_path)