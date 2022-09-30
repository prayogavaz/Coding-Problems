'''Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        pointer1 = head
        pointer2 = head.next
        returnHead = pointer2
        pointer3 = head.next.next

        while pointer1 and pointer2:

            pointer2.next = pointer1
            if pointer3:
                if pointer3.next:
                    pointer1.next = pointer3.next
                else:
                    pointer1.next = pointer3
            else:
                pointer1.next = None

            pointer1 = pointer3
            if pointer1:
                pointer2 = pointer1.next
            else:
                pointer2 = None
            if pointer2:
                pointer3 = pointer2.next
            else:
                pointer3 = None

        return returnHead
