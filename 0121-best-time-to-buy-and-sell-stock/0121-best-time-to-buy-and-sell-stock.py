class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        profit = 0
        while  r < len(prices):
            maxP, minP = prices[r], prices[l]
            if maxP - minP < 0:
                l = r
            else:
                profit = max(profit, maxP - minP)
            r += 1
            
        return profit