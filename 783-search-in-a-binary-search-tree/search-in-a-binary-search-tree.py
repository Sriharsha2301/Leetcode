# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchIt(self,node,val):
        if node is None:
            return None
        
        if node.val==val:
            return node
        elif node.val<val:
            return self.searchIt(node.right,val)
        else:
            return self.searchIt(node.left,val)
        
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        return self.searchIt(root,val)


        