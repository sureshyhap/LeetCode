# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        head = ListNode()
        l3 = head
        carry = 0
        while True:
            sum = current1.val + current2.val + carry
            this_val = sum % 10
            carry = sum // 10
            l3.val = this_val
            current1 = current1.next
            current2 = current2.next
            if current1 != None and current2 != None:
                l3.next = ListNode()
                l3 = l3.next
            else:
                break
        while current1 != None:
            l3.next = ListNode()
            l3 = l3.next
            sum = current1.val + carry
            this_val = sum % 10
            carry = sum // 10
            l3.val = this_val
            current1 = current1.next
        while current2 != None:
            l3.next = ListNode()
            l3 = l3.next
            sum = current2.val + carry
            this_val = sum % 10
            carry = sum // 10
            l3.val = this_val
            current2 = current2.next
        if carry == 1:
            l3.next = ListNode(1)
        return head
