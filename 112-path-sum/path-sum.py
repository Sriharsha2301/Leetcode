# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        stack=[(root,0)]

        while stack:
            p=stack.pop()
            node=p[0]
            val=p[1]

            val+=node.val
            if node.left is None and node.right is None:
                if targetSum==val:
                    return True
                # continue
            if node.right:
                stack.append((node.right,val))
            if node.left:
                stack.append((node.left,val))
        return False
            
        