'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        headNode = None
        if list1.val <= list2.val:
            headNode = list1
        else:
            headNode = list2
            
        
        pointer1 = list1
        pointer2 = list2
        
        while pointer1 and pointer2:

            if pointer1.val <= pointer2.val:
                while pointer1.next and pointer1.next.val <= pointer2.val:
                    pointer1 = pointer1.next
                temp = pointer1
                pointer1 = pointer1.next
                temp.next = pointer2
            else:
                while pointer2.next and pointer2.next.val <= pointer1.val:
                    pointer2 = pointer2.next
                temp = pointer2
                pointer2 = pointer2.next
                temp.next = pointer1
                
        
        return headNode
