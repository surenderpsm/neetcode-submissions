class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[0] = memo[1] = 1
        def dp(n):
            if memo[n]:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return dp(n-1)+dp(n-2)
        
        return dp(n)