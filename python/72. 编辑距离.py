class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 递归法
        n, m = len(word1), len(word2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(word1, n - 1, word2, m - 1)

    def dp(self, word1: str, i: int, word2: str, j: int):
        """定义：返回 s1[0..i] 和 s2[0..j] 的最小编辑距离"""
        if i == -1:
            # word1 遍历结束， word2 剩余的字符都要插入
            return j + 1
        if j == -1:
            # word2 遍历结束， word1 剩余的字符都要插入
            return i + 1

        # 查看备忘录
        if self.memo[j][i] != -1:
            return self.memo[j][i]

        # 字符相同，不处理
        if word1[i] == word2[j]:
            self.memo[j][i] = self.dp(word1, i - 1, word2, j - 1)
            return self.memo[j][i]

        self.memo[j][i] = min(
            self.dp(word1, i, word2, j - 1) + 1,  # word2[j] 插入到word1
            self.dp(word1, i - 1, word2, j) + 1,  # word1[i] 删除
            self.dp(word1, i - 1, word2, j - 1) + 1,  # word2[j] 替换 word1[i]
        )
        return self.memo[j][i]


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         # 定义：s1[0..i] 和 s2[0..j] 的最小编辑距离是 dp[i+1][j+1]
#         # 迭代法
#         n, m = len(word1), len(word2)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#
#         # base case
#         for i in range(1, m + 1):
#             dp[i][0] = i
#
#         for j in range(1, n + 1):
#             dp[0][j] = j
#
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if word2[i - 1] == word1[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = min(
#                         dp[i][j - 1] + 1,  # insert
#                         dp[i - 1][j] + 1,  # delete
#                         dp[i - 1][j - 1] + 1,  # replace
#                     )
#         return dp[m][n]
