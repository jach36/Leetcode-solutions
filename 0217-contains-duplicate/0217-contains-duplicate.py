class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        store = {} 
    
        for n in nums:
            if n not in store:
                store[n] = 1 # {n:1,}
            else:
                return True
        return False        
        