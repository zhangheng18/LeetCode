from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.char2idx = defaultdict(list)
        self.memo = []

        m, n = len(ring), len(key)

        self.memo = [[0] * n for _ in range(m)]

        # ring 字符 位置索引
        for i, char in enumerate(ring):
            self.char2idx[char].append(i)

        return self.dp(ring, 0, key, 0)

    def dp(self, ring, i, key, j):
        # 圆盘指针在 ring[i]，到 key[j] 的最少操作数

        # 结束
        if j == len(key):
            return 0

        # 备忘录
        if self.memo[i][j] != 0:
            return self.memo[i][j]

        n = len(ring)
        res = float('inf')
        for k in self.char2idx[key[j]]:
            # 拨动次数
            delta = abs(k - i)

            # 顺 / 逆
            delta = min(delta, n - delta)

            # 拨动到ring[k] , key[j+1]
            sub_problem = self.dp(ring, k, key, j + 1)
            res = min(res, 1 + delta + sub_problem)

        self.memo[i][j] = res
        return res
