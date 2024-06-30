# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def reverse_linked_list(head):
            prev = None
            curr = head
            next_node = curr.next
            while True:
                curr.next = prev
                if not next_node:
                    return curr
                prev = curr
                curr = next_node
                next_node = next_node.next
        dummy = reverse_linked_list(head)
        value = 0
        count = 0
        while dummy:
            if dummy.val == 1:
                value += (2 ** count)
            count += 1
            dummy = dummy.next
        return value
