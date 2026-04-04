class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # width between lines
            width = right - left
            
            # height of container = smaller line
            h = min(height[left], height[right])
            
            # calculate area
            max_water = max(max_water, width * h)

            # move pointer of smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water