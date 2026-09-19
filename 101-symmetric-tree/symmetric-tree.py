from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        queue=deque([root,root])

        while queue:
            node1=queue.pop()
            node2=queue.pop()
            if node1 is None and node2 is None:
                continue
            
            if node1 is None or node2 is None:
                return False

            if node1.val!=node2.val:
                return False
            
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)

        return True
            
        



        