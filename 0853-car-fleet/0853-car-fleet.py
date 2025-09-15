class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            time = (target - p)/float(s)
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
                


        return len(stack)