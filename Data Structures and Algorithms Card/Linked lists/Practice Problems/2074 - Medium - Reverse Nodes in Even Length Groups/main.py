# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import math

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(group_head, group_length):
            if not group_head.next:
                return None
            prev = None
            curr = group_head.next
            group_tail = curr
            next_node = curr.next
            for _ in range(group_length):
                curr.next = prev
                prev = curr
                curr = next_node
                if not next_node:
                    break
                next_node = next_node.next
            group_head.next = prev
            group_tail.next = curr
            return group_tail

        def gen_squares():
            i = 1
            while True:
                yield i ** 2
                i += 1

        dummy = head
        odd_node_count = 1
        squares_gen = gen_squares()
        while dummy.next:
            next_square = next(squares_gen)
            potential_start_of_last_group = dummy
            potential_count_of_last_group = 0
            while odd_node_count != next_square:
                dummy = dummy.next
                if not dummy:
                    if potential_count_of_last_group % 2 == 0:
                        reverse_linked_list(potential_start_of_last_group, potential_count_of_last_group)
                    return head
                odd_node_count += 1
                potential_count_of_last_group += 1
            potential_start_of_last_group = dummy
            potential_count_of_last_group = 0
            expected_even_group_size = int(sqrt(next_square)) * 2
            for _ in range(expected_even_group_size):
                potential_start_of_last_group = potential_start_of_last_group.next
                if not potential_start_of_last_group:
                    if potential_count_of_last_group % 2 == 0:
                        reverse_linked_list(dummy, potential_count_of_last_group)
                    return head
                potential_count_of_last_group += 1
            dummy = reverse_linked_list(dummy, expected_even_group_size)
        return head
