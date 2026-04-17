class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;

        int buy = 0; // guaranteed to be length 1 minimum

        for (int i = 0; i < prices.size(); i++){
            if (prices[i] - prices[buy] > 0) {
                max = std::max(max, prices[i]-prices[buy]);
            } 
            else {
                buy = i;
            }
        }

        return max;
    }
};
