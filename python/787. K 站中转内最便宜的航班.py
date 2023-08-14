from collections import defaultdict


class Solution:
    MAX_VAL = float('inf')

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # 中转站个数转化为边数
        k += 1

        # 记录谁指向该节点，以及之间的权重
        indegree = defaultdict(list)
        for from_, to_, price in flights:
            indegree[to_].append((from_, price))

        memo = [[-8] * (k + 1) for _ in range(n)]

        def dp(s, k):
            # 从起点 src 出发，k 步到达节点 s 的最小路径权重为 dp(s, k)

            # 起点
            if s == src:
                return 0

            # 步数限制
            if k == 0:
                return -1

            # 备忘录
            if memo[s][k] != -8:
                return memo[s][k]

            res = self.MAX_VAL
            if s in indegree:
                for from_, price in indegree[s]:
                    sub_problem = dp(from_, k - 1)
                    if sub_problem != -1:
                        res = min(res, sub_problem + price)

            memo[s][k] = -1 if res == self.MAX_VAL else res
            return memo[s][k]

        return dp(dst, k)
