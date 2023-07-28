class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 备忘录
        self.memo = [[-1] * len(t) for _ in range(len(s))]

        return self.dp(s, 0, t, 0)

    def dp(self, s, i, t, j):
        """定义：s[i..] 的子序列中 t[j..] 出现的次数为 dp(s, i, t, j)"""
        # 匹配到 t的最后一个字符位置j
        if j == len(t):
            return 1
        # s的长度 比t的长度小，不可能有
        if len(s) - i < len(t) - j:
            return 0

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        res = 0
        for k in range(i, len(s)):
            if s[k] == t[j]:
                res += self.dp(s, k + 1, t, j + 1)

        self.memo[i][j] = res

        return res
