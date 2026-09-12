# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recurmaxDepth(self,node):
        if not node:
            return 0
        left=self.recurmaxDepth(node.left)
        right=self.recurmaxDepth(node.right)
        return 1+max(left,right)
        
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
       
        if not root:
            return 0

        result=self.recurmaxDepth(root)
        return result

        

        