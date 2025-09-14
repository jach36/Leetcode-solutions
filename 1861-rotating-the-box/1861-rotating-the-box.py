class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        ROW, COL = len(boxGrid), len(boxGrid[0])

        res = [["."] * ROW for _ in range(COL)]

        for r in range(ROW):
            i = COL - 1

            for c in reversed(range(COL)):
                if boxGrid[r][c] == "#":
                    res[i][ROW - r - 1] = "#"
                    i -= 1
                elif boxGrid[r][c] == "*":
                    res[c][ROW - r - 1] = "*"
                    i = c - 1 
        return res