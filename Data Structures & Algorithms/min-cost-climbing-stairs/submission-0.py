class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost to reach this step.
        m = [-1] * (len(cost)+1)
        # cost to reach 0 and 1
        m[0] = m[1] = 0

        # minimum cost to reach n
        def dp(n):
            if m[n]==-1:
                m[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
            return m[n]
        
        return dp(len(cost))