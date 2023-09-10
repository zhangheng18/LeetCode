class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        遍历 grid2 中的所有岛屿，把那些不可能是子岛的岛屿排除掉，剩下的就是子岛。
        如果grid2 中存在一片陆地，在grid1 的对应位置是海水，那么grid2 就不是grid1 的子岛。
        """

        # 排除不可能是子岛的
        m, n = len(grid2), len(grid2[0])
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i, j)

        # 统计子岛
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    # 淹没
                    self.dfs(grid2, i, j)
        return res

    def dfs(self, grid, i, j):
        # 结束： 越界 /是海水
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return
        # 淹没
        grid[i][j] = 0
        # 上下左右
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
