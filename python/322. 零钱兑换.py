from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # 递归
        # # 备忘录
        # memo = [-2] * (amount + 1)
        #
        # def dp(coins, amount):
        #     if amount == 0:
        #         return 0
        #     elif amount < 0:
        #         return -1
        #     if memo[amount] != -2:
        #         return memo[amount]
        #
        #     res = float('inf')
        #     for coin in coins:
        #         # 计算子问题
        #         sub_p = dp(coins, amount - coin)
        #         if sub_p == -1:
        #             continue
        #         # 最优解 +1枚硬币
        #         res = min(sub_p + 1, res)
        #
        #     # 结果保存备忘录 避免重复计算
        #     memo[amount] = res if res < float('inf') else -1
        #     return memo[amount]
        #
        # return dp(coins, amount)

        # 迭代法
        # 当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
