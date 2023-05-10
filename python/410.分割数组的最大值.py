class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def f(nums, target):
            # 根据容量求 m组
            m = 1
            cur = 0
            for i in nums:
                cur += i
                if cur > target:
                    m += 1
                    cur = i
            return m

        left, right = 0, 1
        for i in nums:
            left = max(left, i)
            right += i

        while left < right:
            mid = (left + right) // 2
            if f(nums, mid) > k:
                left = mid + 1
            else:
                right = mid
        return left