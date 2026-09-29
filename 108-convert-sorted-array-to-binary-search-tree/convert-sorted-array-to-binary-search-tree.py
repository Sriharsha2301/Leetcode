# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def intoBST(self,nums,start,end):
        if start>end:
            return None
        mid=start+(end-start)/2
        curr=TreeNode(nums[mid])
        curr.left=self.intoBST(nums,start,mid-1)
        curr.right=self.intoBST(nums,mid+1,end)
        return curr
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.intoBST(nums,0,len(nums)-1)
        