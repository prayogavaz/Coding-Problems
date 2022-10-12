'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        while head and head.next and head.val == head.next.val:
            val = head.val
            while head and val == head.val:
                head = head.next

        result = head
        firstpointer = head
        if firstpointer:
            secondPointer = firstpointer.next

        while firstpointer and secondPointer:

            while secondPointer and secondPointer.next and secondPointer.val != secondPointer.next.val:
                secondPointer = secondPointer.next
                firstpointer = firstpointer.next

            if secondPointer and secondPointer.next:
                val = secondPointer.val
                while secondPointer and val == secondPointer.val:
                    secondPointer = secondPointer.next
                firstpointer.next = secondPointer
            else:
                break

        return result
