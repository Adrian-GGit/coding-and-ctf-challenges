class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_info = collections.Counter()
        max_of_fours = 2*n
        for row, col in reservedSeats:
            bit = 0
            if col >= 2 and col <= 3:
                bit = 4
            elif col >= 4 and col <= 5:
                bit = 6
            elif col >= 5 and col <= 7:
                bit = 3
            elif col >= 8 and col <= 9:
                bit = 1
            reserved_info[row] |= bit
        for rev_info in reserved_info.values():
            max_of_fours -= 1 if rev_info >= 1 and rev_info <= 6 else 0 if rev_info == 0 else 2
        return max_of_fours