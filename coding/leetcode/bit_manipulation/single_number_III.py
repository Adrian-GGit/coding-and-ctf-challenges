class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        twice = reduce(xor, nums)
        bit_mask = next(
            1 << bit for bit in range(32)
            if twice & 1 << bit
        )
        first_single = reduce(xor, filter(
            lambda num: num & bit_mask, nums
        ))
        return [first_single, first_single ^ twice]