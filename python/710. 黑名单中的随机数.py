import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.map_black = {}

        # 初始化黑名单设备
        for b in blacklist:
            self.map_black[b] = None

        self.not_black_len = n - len(blacklist)

        last = n - 1
        for b in blacklist:
            # 已经在黑名单区域的不重新映射
            if b >= self.not_black_len:
                continue
            # 可用的last
            while last in self.map_black:
                last -= 1
            self.map_black[b] = last
            last -= 1

    def pick(self) -> int:
        # 在黑名单里重新映射否则 直接返回index
        index = random.randint(0, self.not_black_len - 1)
        return self.map_black.get(index, index)

    # Your Solution object will be instantiated and called as such:


# obj = Solution(n, blacklist)
# param_1 = obj.pick()
