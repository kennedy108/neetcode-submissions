class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            minHeight = min(heights[left], heights[right])
            area = minHeight * width

            if total < area:
                total = area
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return total
        
