# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            
            qLen = len(q)
            
            track = 0 
            for i in range(qLen):
                root = q.popleft()
                if root and track == 0:
                    res.append(root.val)
                    track += 1
            
                if root:
                    q.append(root.right)
                    q.append(root.left)

        return res