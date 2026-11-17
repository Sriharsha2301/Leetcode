# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not postorder:
            return None
        if not inorder:
            return None
        
        i=inorder.index(postorder[-1])



        left_in=inorder[:i]
        right_in=inorder[i+1:]

        left_post=postorder[:i]
        right_post=postorder[i:-1]

        bi=TreeNode(postorder[-1])
        bi.left=self.buildTree(left_in,left_post)
        bi.right=self.buildTree(right_in,right_post)
        return bi

