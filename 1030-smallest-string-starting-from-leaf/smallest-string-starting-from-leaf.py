# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafToRoot(self,node,st):
        if not node:
            return ""
        current=str(chr(ord('a')+node.val))
        st=current+st
        left=self.leafToRoot(node.left,st)
        right=self.leafToRoot(node.right,st)
        if node.left is None and node.right is None:
            return st
        if not left:
            return right
        if not right:
            return left

        return min(left,right)
    
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        if not root:
            return ""

        return self.leafToRoot(root,"")