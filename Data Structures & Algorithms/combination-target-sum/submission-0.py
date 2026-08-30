class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(i, curr, currsum):
            if currsum == target:
                res.append(curr.copy())
                return
            
            if currsum > target:
                return
                # stop searching this branch
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                helper(j, curr,currsum+nums[j])
                curr.pop()
        
        helper(0, [], 0)
        return res
