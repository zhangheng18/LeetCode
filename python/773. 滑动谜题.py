from collections import deque
from typing import List


def swap(board: str, i, j) -> str:
    """移动到相邻位置"""
    bl = list(board)
    bl[i], bl[j] = bl[j], bl[i]
    return ''.join(bl)


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = 2, 3

        # 一维数组
        board_one = []
        for i in range(m):
            for j in range(n):
                board_one.append(str(board[i][j]))
        start = "".join(board_one)

        """  
        二维数组(m 行,n 列)  转1维数组
        index 左 i -1  右 i+1 上 i -n  下 i+n

        neig： idx 相邻索引（上下左右）
        """
        neig = [
            (1, 3),  #  idx=0[1] 右idx=1[2] 下idx=3[4]
            (0, 2, 4),
            (1, 5),
            (0, 4),
            (3, 1, 5),
            (4, 2),
        ]

        step = 0

        # bfs
        visted = set([start])
        q = deque([start])
        target = "123450"
        while q:
            # 广度穷举每一种可能
            for _ in range(len(q)):
                cur = q.popleft()
                # 找到
                if cur == target:
                    return step
                # 找到0的index （一次 移动 定义为选择 0 与一个相邻的数字进行交换.）
                idx = cur.find('0')

                # 穷举所有可移动的位置
                for i in neig[idx]:
                    # 移动到新位置
                    new_board = swap(cur, idx, i)
                    if new_board not in visted:
                        # 不走回头路
                        visted.add(new_board)
                        q.append(new_board)
            step += 1

        # 未找到
        return -1
