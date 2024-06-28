# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverse_linked_list(head):
            prev = None
            curr = head
            next_node = curr.next

            while next_node:
                curr.next = prev

                prev = curr
                curr = next_node
                next_node = next_node.next

            curr.next = prev

            return curr

        fast = head
        slow = head

        while fast:
            fast = fast.next.next
            slow = slow.next

        second = reverse_linked_list(slow)
        first = head

        max_twin_sum = 0
        while second:
            twin_sum = first.val + second.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            first = first.next
            second = second.next

        return max_twin_sum
        """
        def copy_list(head):
            nonlocal size_list
            dummy = head.next
            head2 = ListNode(head.val, None)
            dummy2 = head2
            size_list = 1

            while dummy:

                dummy2.next = ListNode(dummy.val, None)
                dummy2 = dummy2.next
                dummy = dummy.next
                size_list += 1
            
            return head2
        """
        """
        maximum_twin_sum = 0
        head2 = copy_list(head)

        head2 = reverse_linked_list(head2)
        dummy = head
        dummy2 = head2

        for _ in range(size_list // 2):
            twin_sum = dummy.val + dummy2.val
            maximum_twin_sum = max(maximum_twin_sum, twin_sum)
            dummy = dummy.next
            dummy2 = dummy2.next
        
        return maximum_twin_sum
        """
