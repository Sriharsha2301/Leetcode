# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def listToBST(self,start,end):
        if start==end:
            return None
        slow=start
        fast=start
        while fast!=end and fast.next!=end:
            slow=slow.next
            fast=fast.next.next
        curr=TreeNode(slow.val)
        curr.left=self.listToBST(start,slow)
        curr.right=self.listToBST(slow.next,end)
        return curr

    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head: 
            return None
        return self.listToBST(head,None)