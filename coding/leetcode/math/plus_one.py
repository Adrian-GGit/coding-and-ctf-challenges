class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for d in range(len(digits) - 1, -1, -1):
            last_inc = (digits[d] + 1) % 10
            digits[d] = last_inc
            if last_inc != 0:
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits