class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        dp_i_0 = 0
        dp_i_1 = -prices[0] - fee
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max( dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        return dp_i_0

