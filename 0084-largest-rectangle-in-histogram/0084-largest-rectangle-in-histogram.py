class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_height = 0 
        for index, height in enumerate(heights):
            n = index
            while stack and stack[-1][1] > height:
                i,h = stack.pop()
                n = i
                if (index - i)*h > max_height:
                    max_height = (index - i)*h
            stack.append([n, height])

        while stack:
            i,h = stack.pop()
            if (len(heights) - i)*h > max_height: 
                max_height = (len(heights) - i)*h
        return max_height
            

        