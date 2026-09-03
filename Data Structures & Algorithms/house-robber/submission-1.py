class Solution:
    def rob(self, nums: List[int]) -> int:
        # the max robbed till house n
        # dp(n) = max(dp(n-1), dp(n-2) + nums[n])

        # m = [-1]*(len(nums))
        # m[0] = nums[0]
        # m[1] = max(nums[0], nums[1])
        # def dp(n):
        #     if m[n]==-1:
        #         m[n] = max(dp(n-1), dp(n-2) + nums[n])
        #     return m[n]

        prev1 = nums[0]
        prev2 = 0

        for i in range(1,len(nums)):
            curr = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1
    
        
        
        # return dp(len(nums)-1)