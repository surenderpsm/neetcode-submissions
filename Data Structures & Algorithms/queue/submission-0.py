class Deque:
    class ListNode:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = Deque.ListNode()
        self.tail = Deque.ListNode(None, self.head, None)
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return True if self.head.next == self.tail else False

    def appendleft(self, value: int) -> None:
        node = Deque.ListNode(value, self.head, self.head.next)
        self.head.next = node
        node.next.prev = node

    def append(self, value: int) -> None:
        node = Deque.ListNode(value, self.tail.prev, self.tail)
        self.tail.prev = node
        node.prev.next = node

    def pop(self) -> int:
        node = self.tail.prev
        if node == self.head: 
            return -1
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node.val

    def popleft(self) -> int:
        node = self.head.next
        if node == self.tail: 
            return -1
        self.head.next = node.next
        node.next.prev = self.head
        return node.val