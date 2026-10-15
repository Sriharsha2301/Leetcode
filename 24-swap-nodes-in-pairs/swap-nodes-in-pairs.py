# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def swapIt(self,curr,prev):

    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy


        while prev.next and prev.next.next:
            first=head
            second=head.next

            first.next=second.next
            second.next=first
            prev.next=second



            prev=first
            head=prev.next

        return dummy.next

        