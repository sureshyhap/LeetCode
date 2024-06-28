# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_army = [head]
        while pointer_army[-1].next:
            pointer_army.append(pointer_army[-1].next)
        if pointer_army[-n] == head:
            return head.next
        pointer_army[-n - 1].next = pointer_army[-n - 1].next.next
        return head
        
