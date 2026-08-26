# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We use a queue, and we need to append to sublist when we get to new level

        res = []

        q = deque()

        if not root:
            return []

        q.append(root)
        currlevel = 1
        curr = []
        while q:
            
            if currlevel == 0:
                res.append(curr)
                curr = []
                currlevel = len(q)
            
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
                curr.append(node.val)
            currlevel-=1
        return res   
                                    