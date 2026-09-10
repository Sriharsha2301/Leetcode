# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recurmaxDepth(self,node,depth):
        if not node:
            return depth

        left=self.recurmaxDepth(node.left,depth+1)
        right=self.recurmaxDepth(node.right,depth+1)

        return max(left,right)
        
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth=0
        if not root:
            return 0

        result=self.recurmaxDepth(root,depth)

        return result

        