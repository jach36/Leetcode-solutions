# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def valid(Node, right, left):

            if not Node:
                return True
            
            if not (left < Node.val and right > Node.val):
                return False
            
            return valid(Node.left, Node.val, left) and valid(Node.right, right, Node.val)
            

        return valid(root, float("inf"), float("-inf"))

