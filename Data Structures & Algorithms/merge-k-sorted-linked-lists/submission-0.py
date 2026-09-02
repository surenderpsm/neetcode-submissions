# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force
        # run through curr in all lists and find the minimum and insert. after inserting update that list to next. then repeat

        # O(n2)

        # approach 2
        # if we use a priority queue to store the list heads, then wed know which is the lowest one next. its stored in the top of heap. (min heap)
        # we pop the top, then we push it back in with next node

        # a tuple structure to store heap. key would be val and value would be the listnode reference. 
        # to prevent errors with duplicates use a ts or counter as a second key for measuring priority

        res = ListNode()
        
        heap = []
        i = 0
        def insert(node):
            nonlocal heap
            nonlocal i
            if node:
                heapq.heappush(heap,(node.val,i,node))
                i+=1


        for head in lists:
            insert(head)    
        # now heap has the lowest value on top
        c = res
        while heap:
            _, x, node = heapq.heappop(heap)
            c.next = node
            c = c.next
            node = node.next
            insert(node)
        return res.next

         