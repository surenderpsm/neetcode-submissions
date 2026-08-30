class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currset = []
        
        def helper(i, subsets, currset):

            if i >= len(nums):
                subsets.append(currset.copy())
                return
            
            currset.append(nums[i])

            helper(i+1, subsets, currset)

            currset.pop()

            helper(i+1, subsets, currset)
        helper(0,subsets,currset)
        return subsets