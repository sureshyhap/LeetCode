# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        iterator = dummy = head
        while True:
            while iterator.next and (iterator.next.val == iterator.val):
                iterator = iterator.next
            if iterator.next:
                dummy.next = iterator.next
                dummy = dummy.next
                iterator = dummy
            else:
                dummy.next = None
                break
        return head
