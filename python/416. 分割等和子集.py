from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        W = sum(nums)
        if W % 2:
            # 和为奇数 不可能装满
            return False

        # 背包容量W= sum(nums) /2， 物体个数n
        W = W // 2
        N = len(nums)
        # dp[i][w] = 第i个物品放入容量w 可以装满 True 不可以装满 False
        dp = [[False] * (W + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            # base
            dp[i][0] = True

        for i in range(1, N + 1):
            for w in range(1, W + 1):
                # 背包容量不足，不能装入第 i 个物品
                if w - nums[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    # 不装入背包 或者装入
                    dp[i][w] = dp[i - 1][w] or dp[i - 1][w - nums[i - 1]]
        return dp[N][W]
