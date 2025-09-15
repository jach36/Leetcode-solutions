class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0, len(height) - 1
        maxh = 0
        while(l < r):
            area = min(height[l],height[r]) * (r - l)
            if (area > maxh):
                maxh = area
            if(height[r] > height[l]):
                l += 1
            else:
                r -= 1

        return maxh

                
        