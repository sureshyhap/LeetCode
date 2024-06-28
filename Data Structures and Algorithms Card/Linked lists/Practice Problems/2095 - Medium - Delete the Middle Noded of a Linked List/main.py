# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = fast = head
        while True:
            fast = fast.next.next
            if not fast or not fast.next:
                break
            slow = slow.next
        slow.next = slow.next.next
        return head
