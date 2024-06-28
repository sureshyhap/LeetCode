# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start_sentinel = ListNode(-1, head)

        prev = start_sentinel
        curr = prev.next
        next_node = curr.next
        next_next_node = next_node.next

        count = 0
        while next_next_node:
            if count % 2 == 0:
                prev.next = next_node
                next_node.next = curr
                curr.next = next_next_node

                temp = curr
                curr = next_node
                next_node = temp

            prev = prev.next
            curr = curr.next
            next_node = next_node.next
            next_next_node = next_next_node.next
            count += 1
        
        if count % 2 == 0:
            prev.next = next_node
            next_node.next = curr
            curr.next = next_next_node

        return start_sentinel.next
