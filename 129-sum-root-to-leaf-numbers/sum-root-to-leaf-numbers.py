# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rootToLeaf(self,node,st,sum):
        if not node:
            return 0
        st+=str(node.val)
        if node.left is None and node.right is None:
            sum+=int(st)
            return sum

        return (self.rootToLeaf(node.left,st,sum)+self.rootToLeaf(node.right,st,sum))

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        result=self.rootToLeaf(root,"",0)
        return result
        