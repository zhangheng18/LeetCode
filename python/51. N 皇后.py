from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化棋盘,避免引用
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board: List[List[str]], row: int):
        """回溯
        board: 二维棋盘
        row: 当前行
        """
        if row == len(board):
            # 最后一行 结束
            self.res.append(["".join(rows) for rows in board])
            return

        # 遍历每一行的 列
        for col in range(len(board)):
            # 不合法
            if not self.valid(board, row, col):
                continue
            # 选择
            board[row][col] = 'Q'
            # 选择下一行
            self.backtrack(board, row + 1)
            # 撤销
            board[row][col] = '.'

    @staticmethod
    def valid(board: List[List[str]], row: int, col: int) -> bool:
        """验证是否可防治皇后
        每行只放一列 不检查 行冲突
        从上往下遍历： 不检查 右下 左下
        """
        n = len(board)

        # 判断列上冲突
        for i in range(row + 1):
            if board[i][col] == 'Q':
                return False

        # 右上是否冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        # 左上是否冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        return True
