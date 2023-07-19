class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxArea = 0
        curArea = 0
        width = len(height) - 1

        while left < right:
            curArea = width * min(height[left], height[right])
            maxArea = max(maxArea, curArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            width -= 1

        return maxArea
