class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            # Width of the container
            width = right - left

            # Height is limited by the shorter bar
            height = min(heights[left], heights[right])

            # Calculate current area
            current_water = width * height

            # Update maximum
            max_water = max(max_water, current_water)

            # Move the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
        