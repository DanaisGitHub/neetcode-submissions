# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prevNode = None
        node = head

        # caused a cycle, head still had a connection to next node, head becomes tail
        # prevNode = head
        # node = prevNode.next

        while node:
            nextNode = node.next
            node.next = prevNode # curr points to prev
            prevNode = node # curr becomes previous
            node = nextNode
        
        return prevNode
        