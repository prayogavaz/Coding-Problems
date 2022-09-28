'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def middleNode(self, head):
        
        
        current = head
        doubleCurrent = head
        
        if current.next == None:
            return current
        
        while doubleCurrent != None:
            current = current.next
            doubleCurrent = doubleCurrent.next
            if doubleCurrent:
                doubleCurrent = doubleCurrent.next
            if doubleCurrent and doubleCurrent.next == None:
                break
                
                
        return current
