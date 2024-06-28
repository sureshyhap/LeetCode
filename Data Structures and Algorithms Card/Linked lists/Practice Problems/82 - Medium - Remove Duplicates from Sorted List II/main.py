# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        sentinel_head = ListNode(next=head)
        slow = sentinel_head
        fast = slow.next
        while fast:
            while True:
                if not fast.next:
                    return sentinel_head.next
                duplicate_phase = False
                while fast.next.val == slow.next.val:
                    duplicate_phase = True
                    fast = fast.next
                    if not fast.next:
                        slow.next = None
                        return sentinel_head.next
                if duplicate_phase:
                    slow.next = fast.next
                    fast = fast.next
                else:
                    break
                if not fast.next:
                    return sentinel_head.next
                if fast.val != fast.next.val:
                    break
            slow = fast
            fast = fast.next
        return sentinel_head.next
