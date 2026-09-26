# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pVal=p.val
        qVal=q.val
        curr=root

       
        if pVal>curr.val and qVal>curr.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pVal<curr.val and qVal<curr.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return curr
        