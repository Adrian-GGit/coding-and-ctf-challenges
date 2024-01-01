class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weaknesses = []
        for index, elem in enumerate(mat):
            weaknesses.append((sum(mat[index]), index))
        return [strength for _, strength in sorted(weaknesses)][:k]