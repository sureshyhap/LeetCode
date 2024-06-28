# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head

        def reverse_linked_list(prev, iterations):
            curr = prev.next
            next_node = curr.next
            next_next_node = next_node.next
        
            for _ in range(iterations):
                next_node.next = curr

                curr = next_node
                next_node = next_next_node
                if next_next_node:
                    next_next_node = next_next_node.next

            prev.next.next = next_node
            prev.next = curr


        sentinel_head = ListNode(next=head)
        prev = sentinel_head

        for _ in range(1, left):
            prev = prev.next

        iterations = right - left
        reverse_linked_list(prev, iterations)

        return sentinel_head.next
