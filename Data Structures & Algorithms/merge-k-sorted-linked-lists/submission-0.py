# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            curr = head
            while curr != None:
                values.append(curr.val)
                curr = curr.next
        values.sort()
        dummy = ListNode(0)
        head = dummy
        for vals in values:
            Nodes = ListNode(vals)
            head.next = Nodes
            head = head.next
        return dummy.next


