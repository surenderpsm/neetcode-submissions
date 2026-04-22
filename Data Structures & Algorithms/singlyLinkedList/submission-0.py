class LinkedList:
    class ListNode:
        def __init__(self, val = None, next = None):
            self.val = val
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None

    # if head and tail are None: empty list
    # if one element it is both head and tail

    
    def get(self, index: int) -> int:
        node = self.head
        i = 0
        # invariant: node is ith node, is None if out of bounds
        while node and i < index:
            i+=1
            node = node.next
        return node.val if node else -1

    def insertHead(self, val: int) -> None:
        node = LinkedList.ListNode(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node

    def insertTail(self, val: int) -> None:
        node = LinkedList.ListNode(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    def remove(self, index: int) -> bool:
        node = self.head
        prev = None
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i+=1
        if not node:
            return False

        if node == self.head:
            self.head = node.next
        elif node == self.tail:
            self.tail = prev
            prev.next = None
        else:
            prev.next = node.next
        return True
            

    def getValues(self) -> List[int]:
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next
        return arr
