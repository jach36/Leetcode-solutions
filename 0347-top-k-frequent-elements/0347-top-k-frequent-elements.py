class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        store = [None] * (len(nums) + 1)
        res = []
        for n in set(nums):
            if store[nums.count(n)]: 
                store[nums.count(n)].append(n) 
            else:
                store[nums.count(n)] = [n] 
        
        for n in reversed(store):
            if n:
                for i in n:
                    res.append(i)
                    return res if k == len(res) else: continue
        


