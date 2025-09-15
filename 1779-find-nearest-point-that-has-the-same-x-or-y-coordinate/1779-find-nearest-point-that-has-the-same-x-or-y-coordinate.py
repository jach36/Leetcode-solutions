class Solution(object):

    def dist(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min = float('inf')
        index = -1 

        p = 0
        for p in range(len(points)):
            if points[p][0] == x or points[p][1] == y:
                if ( abs(x - points[p][0]) + abs(y - points[p][1]) ) < min:
                    min = abs(x - points[p][0]) + abs(y - points[p][1])
                    index = p

            else:
                continue
        return index
    

                