'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         
        ncurrent = head
        current = head
        
        while n > 0:
            if ncurrent:
                ncurrent = ncurrent.next
            n -= 1
            
        if ncurrent == None and n == 0:
            return head.next
        
        if ncurrent == None and n < 0:
            return head
            
        while ncurrent:
            if ncurrent.next == None:
                current.next = current.next.next
                break
                
            current = current.next
            ncurrent = ncurrent.next
            
        return head
