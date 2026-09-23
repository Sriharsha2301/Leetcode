# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isItValid(self,node,lower,upper):
        if not node:
            return True
        if upper is not None and node.val>=upper or lower is not None and node.val<=lower:
            return False
        
        left=self.isItValid(node.left,lower,node.val)
        right=self.isItValid(node.right,node.val,upper)

        return left and right
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isItValid(root,float('-inf'),float('inf'))
        