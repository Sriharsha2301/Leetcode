# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetricHelper(self,node1,node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False
        
        if node1.val!=node2.val:
            return False
        
        result1=self.isSymmetricHelper(node1.left,node2.right)

        if not result1:
            return False
            
        result2=self.isSymmetricHelper(node1.right,node2.left)

        if not result2:
            return False
        return True
        
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        result=self.isSymmetricHelper(root,root)
        return result
        