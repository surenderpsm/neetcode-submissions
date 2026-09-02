# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find size of list.
        # sz-n+1 will give the node to remove from first

        # then traverse to that point and remove the node and update list


        c = head
        sz = 0
        while c:
            sz+=1
            c = c.next
        
        index = sz - n
        
        # add sentinal node
        t = head
        head = ListNode()
        head.next = t

        c, p = head.next, head
        for i in range(sz):
            if not c:
                break
            if i == index:
                p.next = c.next
                c.next = None
                break
            p = c
            c = c.next
        return head.next