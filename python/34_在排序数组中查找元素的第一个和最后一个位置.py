class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def left_bound(self, nums, target):
        left, right = 0, len(nums) - 1

        # 搜索区间为 [left, right]
        while left <= right:
            # 防止溢出
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            # 向左收缩
            elif target == nums[mid]:
                right = mid - 1
        # 越界
        if left == len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        # 搜索区间为 [left, right]
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            # 向右收缩
            elif target == nums[mid]:
                left = mid + 1
        # 越界
        if right < 0 or nums[right] != target:
            return -1

        return right