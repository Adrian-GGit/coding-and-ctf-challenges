class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag_list = [""] * numRows
        counter = 0
        rev = True
        for c in s:
            if counter == numRows - 1 or counter == 0:
                rev = not rev
            zigzag_list[counter] += c
            counter = counter + 1 if not rev else counter - 1
        zigzag = "".join([c for c in zigzag_list])
        return zigzag