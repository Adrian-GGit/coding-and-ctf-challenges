class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        current = 0
        previous = 0
        result = 0

        for roman in s[::-1]:
            current = roman_to_int.get(roman)
            if previous > current:
                result -= current
            else:
                result += current
            previous = current
        return result