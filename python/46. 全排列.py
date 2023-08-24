class Solution:
    def __init__(self):
        self.res = []
        self.used = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 记录已经被使用过的数字
        self.used = [False] * len(nums)

        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums: List[int], track: List[int]):
        # 回溯路径

        # 结束
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for idx, num in enumerate(nums):
            # 跳过 使用过的选择
            if self.used[idx] is True:
                continue
            # 选择
            self.used[idx] = True
            track.append(num)

            # 下一层
            self.backtrack(nums, track)

            # 取消选择
            track.pop()
            self.used[idx] = False
