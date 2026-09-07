class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # given 
        dp = {len(days):0}
        def helper(i):
            if i not in dp:
                duration = [1,7,30]

                dp[i] = float('inf')
                for x in range(3):
                    j = i
                    while j < len(days) and days[j] < days[i] + duration[x]:
                        j+=1
                    dp[i] = min(dp[i], costs[x] + helper(j))
            return dp[i]
        return helper(0)
        