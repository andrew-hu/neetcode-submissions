# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode(0)
        current = dummy
        # while loop
        while ptr1 != None and ptr2 != None:
            # take value of 1st list, compare with 2nd list
            # if 1st less, add value to list and move ptr1 to next node
            if ptr1.val < ptr2.val:
                current.next = ptr1
                current = current.next
                ptr1 = ptr1.next
            # if 2nd is less, add value to list and move ptr2 to next node
            else:
                current.next = ptr2
                current = current.next
                ptr2 = ptr2.next
            # if ptr2.next is None, end loop and add rest of list1 to current
        if ptr1 == None:
            current.next = ptr2
        else:
            current.next = ptr1
        return dummy.next
            