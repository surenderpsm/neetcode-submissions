# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        c = res 

        while list1 or list2:
            if not list1:
                c.next = list2
                list2 = None
                break
            if not list2:
                c.next = list1
                list1 = None 
                break
        
            if list1.val <= list2.val:
                c.next = list1
                t = list1.next
                list1.next = None
                list1 = t
            else:
                c.next = list2
                t = list2.next
                list2.next = None
                list2 = t
            c = c.next

        return res.next