class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def f(nums, target):
            # 获取指定载重需要天数
            days = 1
            cap = 0
            for i in nums:
                cap += i
                if cap > target:
                    days += 1
                    cap = i
            return days

        left, right = 0, 1
        # 最小装一件最重的， 最大所有一次运完
        for i in weights:
            left = max(left, i)
            right += i

        while left < right:
            mid = (left + right) // 2
            if f(weights, mid) > days:
                left = mid + 1
            else:
                right = mid

        return left
