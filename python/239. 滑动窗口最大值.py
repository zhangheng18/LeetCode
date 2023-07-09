from collections import deque


class MonotonicQueue:
    "单调栈"

    __slots__ = ["que"]

    def __init__(self):
        # 双向队列
        self.que = deque()

    def push(self, n: int):
        # 从大到小 保留
        while self.que and self.que[-1] < n:
            self.que.pop()
        self.que.append(n)

    def max(self):
        # 第一个最大
        return self.que[0]

    def pop(self, n):
        if self.que[0] == n:
            self.que.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows = MonotonicQueue()

        res = []
        for i, num in enumerate(nums):
            if i < k - 1:
                # 填充k-1
                windows.push(num)
            else:
                # 滑动
                windows.push(num)
                res.append(windows.max())
                windows.pop(nums[i - k + 1])
        return res