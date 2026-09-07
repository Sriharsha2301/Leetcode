from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []
        queue=deque([root])
        l=[]
        sum=0
        while queue:
            level_size=len(queue)
            n=level_size
            while level_size:
                c=queue.popleft()
                sum+=float(c.val)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
                level_size-=1
            average=float(sum/n)
            l.append(average)
            sum=0
        return l


        