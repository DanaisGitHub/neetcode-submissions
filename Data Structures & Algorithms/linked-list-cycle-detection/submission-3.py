# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head.next or not head.next.next:
            return False
        fast,slow = head.next.next,head.next
        while fast and slow:
            if fast.val == slow.val:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
        