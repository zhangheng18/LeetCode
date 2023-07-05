import heapq


class State:
    __slots__ = ["id", "weight"]

    def __init__(self, id: int, weight: float):
        self.id = id
        self.weight = weight

    def __lt__(self, other):
        # 逆序,每次取最大的
        return self.weight > other.weight

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.weight})'


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        # 构建临界矩阵
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            from_, to_ = edges[i]
            weight = succProb[i]

            graph[from_].append((to_, weight))
            graph[to_].append((from_, weight))

        res = self.dijkstra(start_node, end_node, graph)
        return res

    def dijkstra(self, start_node, end_node, graph):
        # 订阅权重表
        distTo = [-1] * len(graph)
        # 初始化 开始权重
        distTo[start_node] = 1

        pq = []
        # 权重，开始节点
        heapq.heappush(pq, State(start_node, 1))

        while pq:
            cur_ = heapq.heappop(pq)
            cur_node, cur_weight = cur_.id, cur_.weight

            # 结束节点
            if cur_node == end_node:
                return cur_weight

            # 存在更优路径
            if cur_weight < distTo[cur_node]:
                continue

            for next_node, next_weight in graph[cur_node]:

                new_weight = distTo[cur_node] * next_weight

                # 更新队列
                if distTo[next_node] < new_weight:
                    distTo[next_node] = new_weight
                    heapq.heappush(pq, State(next_node, new_weight))
        return 0.0
