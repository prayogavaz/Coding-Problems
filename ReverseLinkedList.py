'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        
        pointer1 = head.next
        pointer2 = head
        first = True
        
        
        while pointer1:
            
            temp = pointer1.next
            pointer1.next = pointer2
            if first:
                pointer2.next = None
                first = False
                
            pointer2 = pointer1
            pointer1 = temp
            
            
        return pointer2
