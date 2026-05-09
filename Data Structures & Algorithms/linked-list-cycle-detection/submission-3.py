# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.index = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        else:
            ptr1 = head
            ptr2 = head.next
            ptr1.index = 1
        if ptr2==None:
            return False
        else:
            ptr2.index = 2
        while ptr1.next != None and ptr2.next != None:
            ptr1.next.index = ptr1.index + 1
            ptr1 = ptr1.next
            
            ptr2 = ptr2.next
            if ptr2.next != None:
                ptr2 = ptr2.next
            else:
                return False
            if ptr2.index != None:
                return True
        return False