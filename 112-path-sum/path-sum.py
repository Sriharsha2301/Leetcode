# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rootToLeaf(self,node,targetSum,sum):
        if not node:
            return False
        sum+=node.val
        if node.left is None and node.right is None:
            if targetSum==sum:
                return True
            return False

        return (self.rootToLeaf(node.left,targetSum,sum) or self.rootToLeaf(node.right,targetSum,sum))

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.rootToLeaf(root,targetSum,0)