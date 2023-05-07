class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            if self.f(piles, mid) > h:
                left = mid + 1
            else:
                right = mid

        return left

    @staticmethod
    def f(nums, x):
        hours = 0
        for i in nums:
            hours += i // x if x else 0
            if i % x > 0:
                hours += 1
        return hours
