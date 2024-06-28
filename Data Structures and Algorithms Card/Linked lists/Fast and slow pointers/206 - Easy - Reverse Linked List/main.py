# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        elif not head.next:
            return head
        
        temp_prev = head
        temp = head.next
        temp_next = head.next.next

        while temp_next:
            temp.next = temp_prev

            temp_prev = temp
            temp = temp_next
            temp_next = temp_next.next

        temp.next = temp_prev
        head.next = None
        return temp
            
        """
        new_head = None
        def revList(head):
            if not head:
                return
            if head.next:
                revList(head.next).next = head
                return head
            else:
                nonlocal new_head
                new_head = head
                return new_head
        return revList(head)
        """
