class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minHeap = []
        res = []

        for x, y in points:
            sqsum = (x**2) + (y**2) 
            minHeap.append([sqsum, x, y])

        heapq.heapify(minHeap)

        for i in range(k):
            dis, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res