# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searching(self,node,val):
        if not node:
            return 
        if val==node.val:
            return node
        elif val<node.val:
            return self.searching(node.left,val)
        else:
            return self.searching(node.right,val)
        
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return

        return self.searching(root,val)


        