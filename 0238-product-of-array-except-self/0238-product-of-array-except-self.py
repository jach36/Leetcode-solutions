class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        pre = 1
    
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
                

        pre = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= pre
            pre *= nums[i]
        
        return result

            