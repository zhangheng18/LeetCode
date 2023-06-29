class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        # 生成所有边和权重
        for i, (xi, yi) in enumerate(points):
            for j,(xj,yj) in enumerate(points[i+1:],i+1):
                # 用坐标点在 points 中的索引表示坐标点
                edges.append([i, j, abs(xi - xj) + abs(yi - yj)])
        # 权重从小到大
        edges.sort(key=lambda x: x[2])

        total = 0
        uf = UF(n)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            weight = edge[2]
            # 若这条边会产生环，则不能加入 mst
            if uf.connected(u, v):
                continue
            # 若这条边不会产生环，则属于最小生成树
            total += weight
            uf.union(u, v)

        return total


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x: int):
        # 路径压缩
        while self.parent[x] != x:
            self.parent[x] = self.parent[ self.parent[x]]
            x = self.parent[x]
        return x

    def count(self):
        return self.count

    def union(self, p: int, q: int):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        # 小树接在大树下
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

        # 分量合并
        self.count -= 1

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)
