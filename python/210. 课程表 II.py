class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [False] * numCourses
        self.on_paths = [False] * numCourses
        self.has_cycle = False
        self.res = []

        graph = self.build_graph(numCourses, prerequisites)
        # 遍历
        for i in range(numCourses):
            self.traverse(graph, i)

        if self.has_cycle:
            return []
        return self.res

    def traverse(self, graph, s):
        if self.on_paths[s]:
            # 有环
            self.has_cycle = True

        if self.visited[s] or self.has_cycle:
            return

        self.on_paths[s] = True
        self.visited[s] = True

        for i in graph[s]:
            self.traverse(graph, i)

        # 后续位置
        self.res.append(s)
        self.on_paths[s] = False

    def build_graph(self, numCourses, prerequisites):
        # 构建图
        graph = [[] for _ in range(numCourses)]
        for to_, from_ in prerequisites:
            graph[to_].append(from_)
        return graph
