# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # perform dfs on the tree and compute the diameter by maximising it to diameters at each level


        res = 0

        def dfs(root):

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res =  max(res, left+right)

            return 1 + max(right, left)

        dfs(root)
        return res