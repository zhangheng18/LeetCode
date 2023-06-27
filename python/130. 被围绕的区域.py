class UF:
    def __init__(self, n):
        self.count = n
        # 初始化，每个节点的父节点都是自己
        self.parent = [i for i in range(n)]

    def union(self, p: int, q: int):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        # 将两棵树合并为一棵
        self.parent[root_q] = root_p
        self.count -= 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # 路径压缩
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def count(self) -> int:
        return self.count

    def connected(self, p: int, q: int) -> bool:
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)  # 行
        n = len(board[0])  # 列

        dummy = m * n
        uf = UF(m * n + 1)

        for i in range(m):
            # 将每行 首位/末位的 O与dummy联通
            if board[i][0] == "O":
                uf.union(i * n, dummy)
            if board[i][n - 1] == "O":
                # 二维数组展平 一维数组
                uf.union(i * n + (n - 1), dummy)

        for j in range(n):
            # 每列 首位/末位的 O与dummy联通
            if board[0][j] == "O":
                uf.union(j, dummy)
            if board[m - 1][j] == "O":
                uf.union((m - 1) * n + j, dummy)

        # 方向数组 d 是 右下左上 搜索
        d = [[-1,0], [1, 0], [0, 1], [0, -1], [-1, 0]]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O":
                    # 将此 O 与 右下左上 的 O 连通
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == "O":
                            uf.union(x * n + y, i * n + j)

        # 所有不和 dummy 连通的 O，都要被替换
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = "X"
