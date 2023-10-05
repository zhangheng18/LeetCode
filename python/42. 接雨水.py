class Solution:
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     res = 0
    #     # 备忘录
    #     left_max, right_max = [0] * n, [0] * n
    #     # 初始化 base case
    #     left_max[0] = height[0]
    #     right_max[-1] = height[-1]
    #
    #     # 从左向右计算 left_max
    #     for i in range(1, n):
    #         left_max[i] = max(height[i], left_max[i - 1])
    #
    #     # 从右向左计算 right_max
    #     for i in range(n - 2, -1, -1):
    #         right_max[i] = max(height[i], right_max[i + 1])
    #
    #     for i in range(n):
    #         # 接的雨水= min(左边最高，右边最高) - 当前高度
    #         w = min(left_max[i], right_max[i]) - height[i]
    #         res += w
    #     return res

    def trap(self, height: List[int]) -> int:
        """双指针 空间复杂度O(1)"""
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res
