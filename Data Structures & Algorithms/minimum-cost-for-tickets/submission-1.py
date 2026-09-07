class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        duration = [1,7,30]
        dp = [-1] * (len(days)+1)
        dp[len(days)] = 0
        for i in range(len(days)-1, -1,-1):
            dp[i] = float('inf')
            for x in range(3):
                j = i
                while j < len(days) and days[j] < duration[x] + days[i]:
                    j+=1
                dp[i] = min(dp[i],dp[j] + costs[x])
                # we know j is always greater than i
                # so j subproblem would be computed before i

        return dp[0]