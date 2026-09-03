class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane algorithm

        # we compute the min and max till the point i. min and max product of the subarray till i.
        # we update a global res variable with the max.

        # tracking min helps us keep track of negative number products

        res = nums[0]
        curr_min = curr_max = 1
        
        for n in nums:
            t = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(t, n*curr_min, n)

            res = max(res, curr_max)
        return res
        
