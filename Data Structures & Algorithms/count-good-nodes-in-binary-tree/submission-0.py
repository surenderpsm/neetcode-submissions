# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        # if we see values that are greater than max we saw till now then we add to res list and update max

        # max value needs to be specific to the branch.

        # So we need to perform DFS

        # 2 -> 1 -> 3
        # 2 -> 1 -> 1 
        #        -> 5

        # base case. if root is null, then we reached end
        # if val is greater than max, update max.
        # call dfs on children with max

        # max needs to be a stack variable. not global

        res = 0
        def dfs (root, maxval = -101):
            if root:
                if root.val >= maxval:
                    maxval = root.val
                    nonlocal res
                    res+=1
                dfs(root.right, maxval)
                dfs(root.left, maxval)
        
        dfs(root)
        return res  