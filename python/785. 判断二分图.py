class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.ok = True

        n = len(graph)

        self.color = [False] * n
        self.visted = [False] * n

        for v in range(n):
            if not self.visted[v]:
                self.traverse(graph, v)
        return self.ok

    def traverse(self, graph: List[List[int]], v: int):
        # dfs

        if not self.ok:
            # 不是二分图
            return
        self.visted[v] = True
        for i in graph[v]:
            # 相邻节点没被访问过
            if not self.visted[i]:
                # 不同颜色
                self.color[i] = not self.color[v]
                self.traverse(graph, i)
            else:
                # 相同颜色
                if self.color[i] == self.color[v]:
                    self.ok = False
