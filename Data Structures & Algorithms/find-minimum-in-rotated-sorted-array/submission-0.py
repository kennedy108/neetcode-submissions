class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
        return min_num