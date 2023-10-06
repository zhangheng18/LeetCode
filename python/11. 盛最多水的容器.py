class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            # 当前面积
            cur = min(height[left], height[right]) * (right - left)
            res = max(cur, res)
            # 移动较低的一边,使面积有可能变大
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
