from sortedcontainers import SortedList


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.start_map = {}
        self.end_map = {}

        def dist(x: tuple[int, int]):
            if x[0] == -1 or x[1] == n:
                return x[1] - x[0] - 1
            return (x[1] - x[0]) // 2

        # 根据线段长度有序线段 从小到大排序
        self.pq = SortedList(key=lambda x: (dist(x), -x[0]))

        # 虚拟哨兵
        self.add_interval((-1, n))

    def add_interval(self, line: tuple[int, int]):
        # 添加线段
        self.pq.add(line)
        self.start_map[line[0]] = line
        self.end_map[line[1]] = line

    def remove_interval(self, line: tuple[int, int]):
        # 移除线段
        self.pq.remove(line)
        del self.start_map[line[0]]
        del self.end_map[line[1]]

    def seat(self):
        # 从有序线段中取出最长的线段
        x, y = self.pq[-1]

        # 第一个人 最前
        if x == -1:
            seat = 0
        # 第二个人 最后
        elif y == self.n:
            seat = self.n - 1
        # 其他情况 取中间
        else:
            seat = (x + y) // 2

        # 移除最长线段
        self.remove_interval((x, y))
        # 分割成左右两段
        self.add_interval((x, seat))
        self.add_interval((seat, y))
        return seat

    def leave(self, p: int) -> None:
        right = self.start_map.get(p)
        left = self.end_map.get(p)
        # 移除左右两段
        self.remove_interval(left)
        self.remove_interval(right)
        # 合并左右两段
        self.add_interval((left[0], right[1]))


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
