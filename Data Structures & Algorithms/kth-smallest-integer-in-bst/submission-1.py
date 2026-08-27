# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curr = root
        stack = deque()
        pos = 0
        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            pos += 1
            if pos == k:
                return curr.val
            curr = curr.right
        return -1 # wont go here because constraints wont allow it. but its just a failsafe
