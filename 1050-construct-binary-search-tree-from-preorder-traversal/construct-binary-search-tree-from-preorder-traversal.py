# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstHelper(self,preorder,lower,upper):
       
        if self.i>=len(preorder):
            return None
        if not preorder:
            return None
        val=preorder[self.i]
        if val>=upper or val<=lower:
            return None
        self.i+=1
        bi=TreeNode(val)
       
        bi.left=self.bstHelper(preorder,lower,val)
        
        bi.right=self.bstHelper(preorder,val,upper)
        return bi


    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.i=0
        return self.bstHelper(preorder,float('-inf'),float('+inf'))
        

        