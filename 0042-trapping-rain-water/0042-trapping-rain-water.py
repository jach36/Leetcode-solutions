class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        result = 0

        while l < r:
            print(l , r )
            left, right = height[l], height[r]
            if left < right: 
                l += 1
                if max_left - left > 0: 
                    result += max_left - left
                
                max_left = max(left,max_left)
            else:
                r -= 1
                if max_right - right > 0:
                    result += max_right - right
                
                max_right = max(right, max_right)
                
        return result