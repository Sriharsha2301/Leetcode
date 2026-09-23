# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # //inorder Traversal
    def isItValid(self,node):
        if not node:
            return True
        
        left=self.isItValid(node.left)

        if not left: 
            return False 

        if self.last is not None and node.val<=self.last:
            return False
        self.last=node.val
        
        right=self.isItValid(node.right)
        return right
        
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.last=None
      
        return self.isItValid(root)
        