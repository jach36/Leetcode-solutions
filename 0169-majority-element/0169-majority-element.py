class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        library = {}
        for n in nums:
            if n not in library.keys():
                library[n] = 0
            library[n] += 1
            if library[n] > len(nums)/2:
                return n
        return False

