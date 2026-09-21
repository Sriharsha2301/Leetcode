# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoHelper(self,node,val):
        if val<node.val:
            if not node.left:
                node.left=TreeNode(val)
                return
            else:
                self.insertIntoBST(node.left,val)
        else:
            if not node.right:
                node.right=TreeNode(val)
                return 
            else:
                self.insertIntoBST(node.right,val)
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)

        self.insertIntoHelper(root,val)
        return root
       


            

        