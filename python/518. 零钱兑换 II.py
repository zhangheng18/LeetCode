class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] 使用i枚硬币  凑容量j 有dp[i][j]种凑法

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # dp[i][0] 凑容量0 有一种： 啥也不做
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                # 容量不足, 不放入
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 放入： 不放入凑法+放入的凑法
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[n][amount]
