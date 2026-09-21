# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node=TreeNode(val)

        if not root:
            return node
        
        prev=TreeNode(root)
        curr=root

        while curr:
            if val<curr.val:
                prev=curr
                curr=curr.left
                if not curr:
                    prev.left=node
                    return root
            else:
                prev=curr
                curr=curr.right
                if not curr:
                    prev.right=node
                    return root
        return root
        