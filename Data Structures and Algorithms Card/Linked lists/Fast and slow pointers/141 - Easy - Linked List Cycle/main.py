# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        if not fast:
            return False
        while fast.next and fast.next.next:
            fast = fast.next
            if fast is slow:
                return True
            fast = fast.next
            if fast is slow:
                return True
            slow = slow.next
        return False
