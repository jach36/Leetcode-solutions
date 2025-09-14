class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r)//2
            count = 0

            for i in piles:
                count += math.ceil(i/float(m))
            
            if count <= h:
                res = min(res, m)
                r = m - 1

            else:
                l = m + 1
        return res
