class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = n
        temp = 0
        j = 0
        if n == 1:
            return True

        while (temp != 1 and j != 9):
            temp = 0
            for i in range(len(str(number))):
                temp+=(number%10)**2
                number//=10
            number = temp
            if temp == n:
                return False
            j +=1
        if temp == 1: 
            return True
        return False


        
        