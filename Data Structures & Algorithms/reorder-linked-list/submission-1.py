# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #  we find the mid break by using fast and slow pointers
        # the slow pointer determines the mid when fast pointer can no longer move to valid position. for odd it reached end. for even it will reach past end in next move

        mid, fast = head,head.next

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        # we got mid. split to second half
        tail = mid.next
        mid.next = None

        # reverse tail
        p = None
        while tail:
            t = tail.next
            tail.next = p
            p = tail
            tail = t
        tail = p

        res = ListNode()
        c = res
        while tail and head:
            c.next = head
            c=c.next
            head = head.next
            c.next = tail
            c=c.next
            tail = tail.next

        # if odd, then first half (head) will be longer than tail by 1
        if head:
            c.next = head

        head = res
            
