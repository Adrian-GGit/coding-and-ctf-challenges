class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        cur = 0
        while cur <= last:
            if nums[cur] == val:
                cur_last = nums[last]
                nums[last] = nums[cur]
                nums[cur] = cur_last
                last -= 1
            else:
                cur += 1
        return cur