class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cur_left, cur_right = 0, sum(nums)
        for i in range(0, len(nums)):
            cur_right -= nums[i]
            if cur_left == cur_right:
                return i
            cur_left += nums[i]
        return -1