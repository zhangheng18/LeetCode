class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)

        # 记录遍历过的节点，防止走回头路
        self.visted = [False] * numCourses
        self.on_path = [False] * numCourses
        self.has_cycle = False

        # 遍历图所有节点
        for i in range(numCourses):
            self.traverse(graph, i)

        return not self.has_cycle

    def traverse(self, graph, s):
        if self.on_path[s]:
            # 有环
            self.has_cycle = True
            return

        if self.visted[s]:
            # 已经走过
            return

        self.visted[s] = True
        self.on_path[s] = True

        for i in graph[s]:
            self.traverse(graph, i)

        self.on_path[s] = False

    def build_graph(self, numCourses, prerequisites):
        # 构建邻接表
        graph = [[] for _ in range(numCourses)]
        for from_, to_ in prerequisites:
            graph[from_].append(to_)
        return graph
