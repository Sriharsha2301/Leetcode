# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
      
        prev=None
        currentNode=head

        if head is None:
            return None
        while currentNode:
            newNode=currentNode.next
            currentNode.next=prev
            prev=currentNode
            currentNode=newNode

        return prev



                
                


