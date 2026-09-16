# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self,node,targetSum,sum):
        if not node:
            return False
        
        sum=sum+node.val

        if node.left is None and node.right is None:
            if sum==targetSum:
                return True
            return False
        
        return (self.pathSum(node.left,targetSum,sum) or self.pathSum(node.right,targetSum,sum))
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        return self.pathSum(root,targetSum,0)
        