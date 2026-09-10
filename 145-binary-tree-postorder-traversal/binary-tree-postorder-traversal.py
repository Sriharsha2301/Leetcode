# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderHelper(self,node,out):
        if not node:
            return 

        self.postorderHelper(node.left,out)
        self.postorderHelper(node.right,out)
        out.append(node.val)
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        out=[]
        if not root:
            return out
        
        self.postorderHelper(root,out)

        return out