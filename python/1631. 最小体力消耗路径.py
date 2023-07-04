from queue import PriorityQueue as PQ


class Solution:
    # 方向数组， 右下左上
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 构建体力消耗 邻接表
        m, n = len(heights), len(heights[0])
        effort_to = [[float('inf')] * n for _ in range(m)]

        effort_to[0][0] = 0

        pq = PQ()
        # bfs 0,0点
        pq.put((0, (0, 0)))

        while not pq.empty():
            cur_effor_from_start, (cur_x, cur_y) = pq.get()

            # 到达终点
            if cur_x == m - 1 and cur_y == n - 1:
                return cur_effor_from_start

            if cur_effor_from_start > effort_to[cur_x][cur_y]:
                continue

            # 相邻坐标
            for x, y in self.adj(heights, cur_x, cur_y):
                effor_to_item = max(
                    effort_to[cur_x][cur_y], abs(heights[cur_x][cur_y] - heights[x][y])
                )
                if effort_to[x][y] > effor_to_item:
                    effort_to[x][y] = effor_to_item
                    pq.put((effor_to_item, (x, y)))
        return -1

    def adj(self, matrix, x, y):
        # 获取(x,y)的相邻坐标
        m, n = len(matrix), len(matrix[0])
        neighbors = []
        for path in self.dirs:
            nx = x + path[0]
            ny = y + path[1]
            # 越界
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            neighbors.append((nx, ny))
        return neighbors
