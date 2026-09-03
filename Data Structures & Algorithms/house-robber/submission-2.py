class Solution:
    def rob(self, nums: List[int]) -> int:
        # the max robbed till house n
        # dp(n) = max(dp(n-1), dp(n-2) + nums[n])



        prev1 = nums[0]
        prev2 = 0

        for i in range(1,len(nums)):
            curr = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1
    
        
        
        # return dp(len(nums)-1)