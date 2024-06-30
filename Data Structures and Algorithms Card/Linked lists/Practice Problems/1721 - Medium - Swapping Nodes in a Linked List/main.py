# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel_head = ListNode(next=head)
        slow = sentinel_head
        fast = slow
        count = 0
        while count < k:
            fast = fast.next
            count += 1
        left_node = fast
        while fast:
            fast = fast.next
            slow = slow.next
        right_node = slow
        left_node.val, right_node.val = right_node.val, left_node.val
        return head
