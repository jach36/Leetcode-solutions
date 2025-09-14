# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1
        return self.dfs(root, root.val)

    def dfs(self, curr, maxNum):
        if not curr:
            return 0

        if curr.val >= maxNum:
            maxNum = curr.val

        else:
            return self.dfs(curr.left, maxNum) + self.dfs(curr.right, maxNum)

        return 1 + self.dfs(curr.left, maxNum) + self.dfs(curr.right, maxNum) 
