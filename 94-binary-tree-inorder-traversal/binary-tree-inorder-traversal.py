# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        stack=[]
        curr=root
        output=[]
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            output.append(curr.val)
            curr=curr.right
        return output
        