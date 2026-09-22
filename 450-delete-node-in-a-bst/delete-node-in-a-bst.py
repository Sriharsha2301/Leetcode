# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        parent=None
        curr=root

        while curr and curr.val!=key:
            parent=curr
            if key<curr.val:
                curr=curr.left
            else:
                curr=curr.right
            
        if not curr:
            return root
        
            # if node has two childs
        if curr.left is not None and curr.right is not None:
            successor=curr.right
            successorParent=curr

            while successor.left:
                successorParent=successor
                successor=successor.left
            
            curr.val=successor.val
            
            curr=successor
            parent=successorParent

        
        # if node is a leaf node
        if curr.left is None and curr.right is None:
            if not parent: 
                # //root node to be deleted 
                return None
            if curr==parent.right:
                parent.right=None
            else:
                parent.left=None


            # if node has one child
        elif curr.left is None or curr.right is None:
            if not parent: return curr.right if not curr.left else curr.left
            if curr==parent.right:
                parent.right=curr.right if not curr.left else curr.left
            else:
                 parent.left=curr.right if not curr.left else curr.left
        return root


            
        