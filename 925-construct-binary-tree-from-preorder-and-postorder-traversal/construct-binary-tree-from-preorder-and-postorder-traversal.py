# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        if not postorder:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])

        i=postorder.index(preorder[1])
        left_pre=preorder[1:i+2]
        right_pre=preorder[i+2:]

        left_post=postorder[:i+1]
        right_post=postorder[i+1:-1]

        bi=TreeNode(preorder[0])
        bi.left=self.constructFromPrePost(left_pre,left_post)
        bi.right=self.constructFromPrePost(right_pre,right_post)
        return bi
        