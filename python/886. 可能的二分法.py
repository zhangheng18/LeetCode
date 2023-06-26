class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g_n = n + 1
        graph = self.build_graph(g_n, dislikes)

        self.ok = True
        self.visited = [False] * g_n
        self.color = [False] * g_n

        for v in range(1, g_n):
            if not self.visited[v]:
                self.traverse(graph, v)
        return self.ok

    def traverse(self, graph, v):
        if not self.ok:
            return

        self.visited[v] = True
        for w in graph[v]:
            if not self.visited[w]:
                # 没有访问过 涂上不同的颜色
                self.color[w] = not self.color[v]
                self.traverse(graph, w)
            else:
                # 相邻银色相同
                if self.color[w] == self.color[v]:
                    self.ok = False

    def build_graph(self, n, dislikes):
        # 构建邻接表
        graph = [[] for _ in range(n)]
        for v, w in dislikes:
            # 无向图  v->w   w->v
            graph[v].append(w)
            graph[w].append(v)
        return graph
