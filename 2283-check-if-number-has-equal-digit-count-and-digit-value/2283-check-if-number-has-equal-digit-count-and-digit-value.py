class LinkNode:
    def __init__(self ):
        self.count = 0
        self.next = None

class Solution(object):
    def __init__(self):
        self.map = [LinkNode() for i in range(10)]

    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for n in num:
            # if self.map[int(n)].count == 0:
            self.map[int(n)].count += 1
            # else:
            #     self.map[int(n)].count = 1
        
        for n in range(len(num)):
            if self.map[int(n)].count != int(num[n]):
                return False
        return True
            

    
        
        