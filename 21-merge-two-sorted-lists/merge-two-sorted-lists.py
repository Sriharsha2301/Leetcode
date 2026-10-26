# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeIt(self,list1,list2,curr):
        if list1 is None:
            curr.next=list2
            return list2
           
        if list2 is None:
            curr.next=list1
            return list1
           
        
        if list1.val<=list2.val:
            curr.next=list1
            return self.mergeIt(list1.next,list2,curr.next)
        else:
            curr.next=list2
            return self.mergeIt(list1,list2.next,curr.next)
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        curr=dummy

        self.mergeIt(list1,list2,curr)
                
        return dummy.next

        






        