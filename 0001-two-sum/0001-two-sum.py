class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        result = []

        ind = 0
        for i in nums:
            curr = target - i 
            if (curr) in store and store[curr] != ind:
                result.append(store[curr])
                store[i] = ind
                result.append(store[i])
                return result
            store[i] = ind
            ind += 1
        return False
        