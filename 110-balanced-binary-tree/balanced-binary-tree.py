# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isItBalanced(self,node):
        if node is None:
            return (-1,True)
        left_height,left_Balanced=self.isItBalanced(node.left)

        if not left_Balanced:
            return (-1,False)

        right_height,right_Balanced=self.isItBalanced(node.right)

        if not right_Balanced:
            return (-1,False)

        if abs(left_height-right_height)>1:
            return (-1,False)

        return (1+max(left_height,right_height),True)




    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        height,balanced=self.isItBalanced(root)
        return balanced
        