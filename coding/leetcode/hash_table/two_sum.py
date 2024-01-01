class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if target - num in d:
                return [index, d.get(target - num)]
            d[num] = index