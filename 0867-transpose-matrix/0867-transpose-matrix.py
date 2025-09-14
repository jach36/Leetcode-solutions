class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for ROW in range(len(matrix)):
            for COL in range(len(matrix[0])):
                res[COL][ROW] = matrix[ROW][COL]
            
        return res
