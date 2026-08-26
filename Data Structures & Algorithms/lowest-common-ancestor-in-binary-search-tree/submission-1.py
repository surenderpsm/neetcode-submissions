# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # until it diverges we keep going. since its bst, we know its all ordered
        # once we realize p and q will be in different nodes, then we assign that as teh lcs
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        # moment wehere it diverges
        else:
            return root