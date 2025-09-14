class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        ROW, COL = 0, len(matrix[0]) - 1

        while ROW < len(matrix):
            curr = matrix[ROW][COL]
            if curr < target:
                ROW += 1
            elif  curr == target:
                return True
            else:
                l, r = 0, COL
                
                while l <= r:
                    m = (l + r) / 2
                    if matrix[ROW][m] < target:
                        l = m + 1
                    elif matrix[ROW][m] > target:
                        r = m - 1 
                    else:
                        return True

                return False
        return False

