class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + int(low % 2 != 0 or high % 2 != 0)