# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        frequency=defaultdict(int)
        current_sum=0

        def dfs(node):

            if node is None:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            if node is None:
                return 0

            current_sum=node.val+left+right

            frequency[current_sum]+=1

            return current_sum
        
        dfs(root)
        
        max_frequency=max(frequency.values())
        ans=[]
        for total in frequency:
            if frequency[total]==max_frequency:
                ans.append(total)
        ans.sort()
        return ans



        