class UF:
    # 联通分量
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        # 压缩路径
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        # 小树接在大树下
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = self.parent[root_p]
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = self.parent[root_q]
            self.size[root_q] += self.size[root_p]
        self.count -= 1

    def count(self):
        self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)

        a_int = ord('a')
        for val_a, op_1, op_2, val_b in equations:
            # 相等的建立连接
            if op_1 == '=':
                uf.union(ord(val_a) - a_int, ord(val_b) - a_int)
        for val_a, op_1, op_2, val_b in equations:
            if op_1 == '!':
                # 破坏连接
                if uf.connected(ord(val_a) - a_int, ord(val_b) - a_int):
                    return False
        return True