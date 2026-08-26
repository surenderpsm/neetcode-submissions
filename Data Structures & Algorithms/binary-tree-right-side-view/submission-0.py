# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # find the right most element on each level.
        # always start from right node and go left until you encounter a non null level.


        q = deque()

        q.append(root)
        currlevel = 1

        res = []
        fillCurrLevel = False
        while q:
            
            if fillCurrLevel:
                while currlevel:
                    node = q.popleft()
                    currlevel-=1
                    if node:
                       q.append(node.right)
                       q.append(node.left)

            if currlevel == 0:
                currlevel = len(q)
                fillCurrLevel = False
            
            node = q.popleft()
            currlevel-=1

            if node:
                if not fillCurrLevel:
                    res.append(node.val)
                    fillCurrLevel = True
                q.append(node.right)
                q.append(node.left)

        return res        

