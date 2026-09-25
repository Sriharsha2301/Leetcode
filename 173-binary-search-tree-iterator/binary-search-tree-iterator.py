# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.l=[]
        self.idx=-1
        self.inorderTraversal(root)
    

    def inorderTraversal(self,node):
     
        if not node:
            return
        # left
        self.inorderTraversal(node.left)
        # process
        self.l.append(node.val)
        # right
        self.inorderTraversal(node.right)
        

    def next(self):
        """
        :rtype: int
        """
        self.idx=self.idx+1
        return self.l[self.idx]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx<len(self.l)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()