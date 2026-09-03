class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # greedy approach doesnt work
        

        # lets define dp which stores the min coins needed to make up that amount i

        dp = [float('inf')] * (amount+1)
        # it costs 0 coins to make 0 dollars
        dp[0] = 0
        # loop till amount
        for a in range(1,amount+1):
            
            for c in coins:
                if a-c >= 0:
                    # our bottom up approach ensures dp[a-c] is already calculated
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return -1 if dp[amount] == float('inf') else int(dp[amount])


