# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel_head = ListNode(next=head)
        dummy = sentinel_head
        while dummy.next:
            while dummy.next.val == val:
                dummy.next = dummy.next.next
                if not dummy.next:
                    return sentinel_head.next
            dummy = dummy.next
            if not dummy:
                return sentinel_head.next
        return sentinel_head.next
