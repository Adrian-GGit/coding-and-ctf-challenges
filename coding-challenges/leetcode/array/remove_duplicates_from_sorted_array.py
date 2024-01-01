class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        update_index = 1
        for num in nums:
            if num != nums[update_index - 1]:
                nums[update_index] = num
                update_index += 1
        return update_index