class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for n in nums:
            if n%2 == 0:
                count +=1
            if count >= 2 :
                return True 
        return False
        