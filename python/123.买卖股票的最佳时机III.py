class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     days = len(prices)
    #     max_k = 2
    #
    #     # dp[day][k][state]  天数，交易次数   持有/卖出
    #     dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(days)]
    #
    #     for day in range(days):
    #         # 遍历交易次数
    #         for k in range(max_k, 0, -1):
    #             # base
    #             if day == 0:
    #                 dp[0][k][0] = 0
    #                 dp[0][k][1] = -prices[day]
    #                 continue
    #             # day天 k次 不持有： day-1天k次不持有，  持有卖出
    #             dp[day][k][0] = max(dp[day - 1][k][0], dp[day - 1][k][1] + prices[day])
    #             # day天k次 持有: day-1天k次持有， day-1天 k-1次 不持有 买入
    #             dp[day][k][1] = max(
    #                 dp[day - 1][k][1], dp[day - 1][k - 1][0] - prices[day]
    #             )
    #
    #     return dp[days - 1][max_k][0]
    def maxProfit(self, prices: List[int]) -> int:
        # k为2 ，直接拆解, 内存优化
        dp_i_1_0, dp_i_1_1 = 0, float('-inf')
        dp_i_2_0, dp_i_2_1 = 0, float('-inf')
        for price in prices:
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + price)
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - price)

            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + price)
            dp_i_1_1 = max(dp_i_1_1, -price)
        return dp_i_2_0
