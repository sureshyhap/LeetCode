# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        node_vals = []
        current = head
        while current:
            node_vals.append(current.val)
            current = current.next
        result = ListNode()
        current = result
        while len(node_vals) > 1:
            current.val = node_vals.pop()
            current.next = ListNode()
            current = current.next
        current.val = node_vals.pop()
        return result

"""
        if head:
            lyst = []
            current = head
            while current:
                lyst.append(current.val)
                current = current.next
            reversed_list = ListNode()
            current = reversed_list
            for i in range(len(lyst) - 1, -1, -1):
                current.val = lyst[i]
                if i > 0:
                    current.next = ListNode()
                current = current.next
            return reversed_list
"""

"""
        reversed_list = None
        if not head:
            return None
        def revList(head_node):
            nonlocal reversed_list
            reversed_list = ListNode(head_node.val, reversed_list)
            if head_node.next:
                revList(head_node.next)
        revList(head)
        return reversed_list
"""
