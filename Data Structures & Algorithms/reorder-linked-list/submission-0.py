# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head
        while second != None and second.next != None:
            first = first.next
            second = second.next.next
        current = first
        prev = None
        while current != None:
            node = current.next
            current.next = prev
            prev = current
            current = node

        start = head
        tail = prev
        while tail != None and tail != start and tail != start.next:
            sNode = start.next
            tNode = tail.next
            start.next = tail
            tail.next = sNode
            start = sNode
            tail = tNode
        return None

            
