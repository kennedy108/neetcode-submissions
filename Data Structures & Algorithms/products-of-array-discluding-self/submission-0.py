class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        left = []
        left_prod = 1
        for i in range(len(nums)):
            left.append(left_prod)
            left_prod *= nums[i]
        index = len(left) - 1
        right_prod = 1
        for j in reversed(nums):
            left[index] *= right_prod
            right_prod *= j
            index -= 1
        result = list(left)
        return result

            
