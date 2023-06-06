class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.count = 0
        self.lower = lower
        self.upper = upper
        self.temp = [0] * (len(nums) + 1)

        # 构造前缀树
        self.pre_num = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pre_num[i + 1] = self.pre_num[i] + nums[i]

        self.sort(self.pre_num, 0, len(self.pre_num) - 1)
        return self.count

    def sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = (lo + hi) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        # 统计区间和的个数 count[i] = COUNT(j) where lower <= preSum[j] - preSum[i] <= upper
        start, end = mid + 1, mid + 1
        for i in range(lo, mid + 1):
            while start <= hi and nums[start] - nums[i] < self.lower:
                start += 1
            while end <= hi and nums[end] - nums[i] <= self.upper:
                end += 1
            self.count += end - start

        # 归并排序
        i, j = lo, mid + 1
        for p in range(lo, hi + 1):
            if i > mid:
                nums[p] = self.temp[j]
                j += 1
            elif j > hi:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
