class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        comb = {}
        for h, n in zip(heights, names):
            comb[h] = n

        res = []
        
        for i in reversed(sorted(heights)):
            res.append(comb[i])

        return res
        return comb.keys()