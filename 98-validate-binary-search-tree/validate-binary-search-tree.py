# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isItValid(self, node,lower,upper):
        if not node:
            return True
        if (upper<=node.val and upper is not None) or(lower>=node.val and lower is not None):
            return False
        
        if not self.isItValid(node.left,lower,node.val):
            return False
        
        return self.isItValid(node.right,node.val,upper)
    
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isItValid(root,float('-inf'),float('inf'))
        