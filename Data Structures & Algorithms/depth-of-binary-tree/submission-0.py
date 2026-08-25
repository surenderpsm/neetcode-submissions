# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # count current as 1 level

        def depth(node, cd):
            if not node:
                return cd
            cd+=1
            # if node exists, we count it into depth
            return max(depth(node.left, cd), depth(node.right, cd))




        return depth(root, 0)