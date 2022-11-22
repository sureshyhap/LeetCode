# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
