class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        path = []
        self.traverse(graph, 0, path)
        return self.res

    def traverse(self, graph, s, path):

        # 添加路径
        path.append(s)

        if s == len(graph):
            # 到达终点
            self.res.append(path[:])
            path.pop()
            return

        # 递归遍历
        for i in graph[s]:
            self.traverse(graph, i, path)

        # 移除路径
        path.pop()
