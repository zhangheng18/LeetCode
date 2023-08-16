from dataclasses import dataclass


@dataclass
class Pair:
    first: int
    second: int
    __solt__ = ('first', 'second')


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # 先手赢：得分高， 得分一样
        return self.stoneGame(nums) >= 0

    def stoneGame(self, piles: List[int]) -> int:
        n = len(piles)

        # dp[i][j]: piles 从i .... j  first 先手最大得分  second 后手最大得分
        dp = [[Pair(0, 0) for _ in range(n)] for _ in range(n)]

        # 初始化对角线的值  piles[i:i] 先手得分 后手为0分
        for i in range(n):
            dp[i][i].first = piles[i]
            dp[i][i].second = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # 先手选择

                # 先选左边， 第二次成为后手
                left = piles[i] + dp[i + 1][j].second
                # 选右边， 第二次成为后手
                right = piles[j] + dp[i][j - 1].second

                # 先手选最优
                if left > right:
                    dp[i][j].first = left
                    dp[i][j].second = dp[i + 1][j].first
                else:
                    dp[i][j].first = right
                    dp[i][j].second = dp[i][j - 1].first
        # 最后得分
        res = dp[0][n - 1]

        return res.first - res.second
