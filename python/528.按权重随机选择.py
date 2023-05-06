import random


class Solution:
    def __init__(self, w: List[int]):
        self.pre = [0] * (len(w) + 1)
        # 初始化权重数组
        for i in range(1, len(w) + 1):
            self.pre[i] = self.pre[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        # 在闭区间 [1, pre[n - 1]] 中随机选择一个数字
        target = random.randint(1, self.pre[-1])
        # pre 索引偏移 (多了一位)
        return self.binary_left(self.pre, target) - 1

    @staticmethod
    def binary_left(nums, target):
        # 二分查找左边界
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                r = mid - 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
