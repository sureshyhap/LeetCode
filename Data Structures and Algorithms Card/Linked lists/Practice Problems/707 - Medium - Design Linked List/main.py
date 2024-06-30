class MyLinkedList:

    class Node:

        def __init__(self, val=None, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.size = 0
        self.head = MyLinkedList.Node()
        self.tail = MyLinkedList.Node(prev=self.head)
        self.head.next = self.tail
        
        
    def get(self, index: int) -> int:
        if self.size == 0:
            return -1
        elif index <= self.size // 2:
            dummy = self.head.next
            for _ in range(index):
                dummy = dummy.next
        elif self.size // 2 < index < self.size:
            dummy = self.tail.prev
            distance_from_end = self.size - 1 - index
            for _ in range(distance_from_end):
                dummy = dummy.prev
        else:
            return -1
        return dummy.val
            

    def addAtHead(self, val: int) -> None:
        old_first = self.head.next
        new_node = MyLinkedList.Node(val, old_first, self.head)
        old_first.prev = new_node
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        old_last = self.tail.prev
        new_node = MyLinkedList.Node(val, self.tail, old_last)
        old_last.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size // 2:
            dummy = self.head.next
            for _ in range(index):
                dummy = dummy.next
        elif self.size // 2 < index < self.size:
            distance_from_end = self.size - 1 - index
            dummy = self.tail.prev
            for _ in range(distance_from_end):
                dummy = dummy.prev
        elif index == self.size:
            self.addAtTail(val)
            return
        else:
            return
        before = dummy.prev
        new_node = MyLinkedList.Node(val, dummy, before)
        before.next = new_node
        dummy.prev = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0:
            return
        elif index <= self.size // 2:
            dummy = self.head.next
            for _ in range(index):
                dummy = dummy.next
        elif self.size // 2 < index < self.size:
            distance_from_end = self.size - 1 - index
            dummy = self.tail.prev
            for _ in range(distance_from_end):
                dummy = dummy.prev
        else:
            return
        before = dummy.prev
        after = dummy.next
        before.next = after
        after.prev = before
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
