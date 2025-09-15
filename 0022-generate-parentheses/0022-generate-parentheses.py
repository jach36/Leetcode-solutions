class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack  = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN > closeN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
        backtrack(0,0)
        return res