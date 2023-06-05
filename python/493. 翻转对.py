class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.temp = [0] * len(nums)
        self.sort(nums, 0, len(nums) - 1)
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

        end = mid + 1
        for i in range(lo, mid + 1):
            while end <= hi and nums[i] > nums[end] * 2:
                end += 1
            self.count += end - (mid + 1)

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
