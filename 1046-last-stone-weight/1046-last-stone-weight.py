class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        negStones = [-s for s in stones]
        heapq.heapify(negStones)
        while len(negStones) > 1:
            y = heapq.heappop(negStones)
            x = heapq.heappop(negStones)
            
            if x != y:
                heapq.heappush(negStones, y - x)
            else:  heapq.heappush(negStones, 0)
        return negStones[0] * -1