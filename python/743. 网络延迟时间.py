import heapq


class State:
    def __init__(self, id: int, dist_from_start: int):
        self.id = id
        self.dist_from_start = dist_from_start

    def __lt__(self, other):
        return self.dist_from_start < other.dist_from_start


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        # 构建邻接表
        for edge in times:
            from_, to_, weight = edge
            graph[from_].append((to_, weight))
        # 查找最短路径
        dist_to = self.dijkstra(k, graph)

        # 找最长的 最短路径
        res = 0
        for i in dist_to[1:]:
            if i == float('inf'):
                return -1
            res = max(res, i)
        return res

    def dijkstra(self, start, graph):
        dist_to = [float('inf')] * len(graph)
        dist_to[start] = 0

        # 优先级队列， dist_from_start 排在前面
        pq = [State(start, 0)]
        heapq.heapify(pq)

        while pq:
            cur_stat = heapq.heappop(pq)
            cur_id, cur_from_dist = cur_stat.id, cur_stat.dist_from_start

            if cur_from_dist > dist_to[cur_id]:
                continue

            # 将 cur_node 的相邻节点装入队列
            for neig in graph[cur_id]:
                next_id, next_from_dist = neig[0], dist_to[cur_id] + neig[1]

                if dist_to[next_id] > next_from_dist:
                    dist_to[next_id] = next_from_dist
                    heapq.heappush(pq, State(next_id, next_from_dist))
        return dist_to
