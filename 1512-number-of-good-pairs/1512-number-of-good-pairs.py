
class Solution(object):

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        res = 0 

        for n , c in count.items():
            res += c*(c-1)//2
        return res

            
        
            