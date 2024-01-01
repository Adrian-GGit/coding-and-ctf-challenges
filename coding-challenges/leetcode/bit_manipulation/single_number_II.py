from operator import ixor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                num = num & 0xFFFFFFFF if num < 0 else num
                bit_sum += (abs(num) >> i) & 1
            bit_sum %= 3
            once |= bit_sum << i
        if once > 0x7FFFFFFF:
            once -= 0x100000000
        return once