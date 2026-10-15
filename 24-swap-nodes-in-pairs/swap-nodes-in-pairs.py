# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapIt(self,curr,prev):
        if curr is None or curr.next is None:
            return curr

        first=curr
        second=curr.next

        first.next=second.next
        second.next=first
        prev.next=second

        self.swapIt(first.next,first) 



    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy


        self.swapIt(head,prev)

        return dummy.next

        