class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(nums):
            if not nums:
                return 0
            prev1 = nums[0]
            prev2 = 0
            for i in range(1,len(nums)):
                curr = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(nums[0],help(nums[0:-1]), help(nums[1:]))
