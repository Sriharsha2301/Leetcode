# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None

        binary=TreeNode(preorder[0])
        i=inorder.index(preorder[0])

        left_preorder=preorder[1:i+1]
        right_preorder=preorder[i+1:]
        left_inorder=inorder[:i]
        right_inorder=inorder[i+1:]

        binary.left=self.buildTree(left_preorder,left_inorder)
        binary.right=self.buildTree(right_preorder,right_inorder)
        return binary