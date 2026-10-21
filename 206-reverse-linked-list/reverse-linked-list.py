# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseIt(self,prev,curr):
        if curr is None:
            return prev
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
        return self.reverseIt(prev,curr)
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # prev=None
        # curr=head

        
            

        return self.reverseIt(None,head)

        