class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for e in tokens:
            if e == "+":
                stack.append(stack.pop() + stack.pop())
            elif e == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif e == "*":
                stack.append(stack.pop() * stack.pop())
            elif e == "/":
                a, b = stack.pop(), stack.pop()
                
                stack.append(int(float(b)/a))
            else:
                stack.append(int(e))

        return stack[-1]