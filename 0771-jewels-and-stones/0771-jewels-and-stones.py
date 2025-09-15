class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        lib = {}
        count = 0 
        for j in jewels:
            lib[j] = 0
            if j in stones:
                count += stones.count(j)
        return count

            