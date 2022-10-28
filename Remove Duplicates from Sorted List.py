'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        result = head

        while head and head.next:

            if head.val == head.next.val:
                next = head.next
                while next and next.val == head.val:
                    next = next.next
                head.next = next
            head = head.next
            
        return result
