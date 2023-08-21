class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     days = len(prices)
    #
    #     # dp[i][0] 第i天 不持有的利润   dp[i][1] 第i天持有的利润
    #     dp = [ [0,0] for _ in range(days)]
    #
    #
    #     # base   第1天不可能持有 最小值
    #     dp[0][0] = 0
    #     dp[0][1] = -prices[0] -fee
    #
    #     for i in range(1,days):
    #         # 不持有：   前一天不持有， 前一天持有 卖出
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    #         # 持有： 前一天持有， 前一天不持有 买入 扣1次手续费
    #         dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
    #
    #     # 最后一天 不持有利润最大
    #     return dp[days-1][0]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)

        # 优化空间占用
        dp_i_0, dp_i_1 = 0, -prices[0] - fee
        for i in range(1, days):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i] - fee)
        return dp_i_0
