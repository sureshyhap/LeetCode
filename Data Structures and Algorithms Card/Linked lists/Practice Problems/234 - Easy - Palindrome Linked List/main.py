# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        sentinel_head = ListNode(next=head)
        slow = sentinel_head
        fast = slow.next
        while fast:
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next

        def reverse_linked_list(head):
            prev = None
            curr = head.next
            next_node = curr.next
            while True:
                curr.next = prev
                if not next_node:
                    return curr
                prev = curr
                curr = next_node
                next_node = next_node.next

        slow.next = reverse_linked_list(slow)
        first = sentinel_head
        while slow.next:
            first = first.next
            slow = slow.next
            if first.val != slow.val:
                return False
        return True
        
