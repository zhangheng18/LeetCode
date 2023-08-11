class Solution:
    MAX_VAL = float('inf')
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.m, self.n = len(dungeon), len(dungeon[0])

        # 备忘录
        self.memo = [ [-1] * self.n for _ in range(self.m)]

        return self.dp(dungeon, 0,0)

    def dp(self, dungeon, i, j):
        # dp[i][j]: i，j出发 到终点 所需要的最小生命点

        #结束： 终点
        if i == self.m -1 and j == self.n-1:
            return 1 if dungeon[i][j] >= 0 else -dungeon[i][j] +1

        # 出界
        if i == self.m or j ==self.n:
            return self.MAX_VAL

        # 避免重复计算
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        # 转移方程， 到达 下 右 相邻所需最小生命
        self.memo[i][j] = min (
            self.dp(dungeon, i+1, j),
            self.dp(dungeon, i ,j+1)
        ) - dungeon[i][j]

        #骑士生命至少为1
        if self.memo[i][j] <= 0:
            self.memo[i][j] = 1

        return  self.memo[i][j]