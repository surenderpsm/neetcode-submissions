# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # returns height if balanced. -1 if unbalanced
        def check(root):
            if not root:
                return 0
            
            hl = check(root.left)
            if hl == -1:
                return -1
            
            hr = check(root.right)
            if hr == -1:
                return -1
            
            if abs(hl-hr)>1:
                return -1
            
            return 1+max(hl,hr)
            

        return False if check(root) == -1 else True