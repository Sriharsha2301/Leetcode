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
        self.stack=[]
        self.leftTraversal(root)

    def leftTraversal(self,root):
        curr=root
        while curr:
            self.stack.append(curr)
            curr=curr.left
        

    def next(self):
        """
        :rtype: int
        """
        node=self.stack.pop()
        if node.right:
            self.leftTraversal(node.right)
        return node.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if  not self.stack:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()