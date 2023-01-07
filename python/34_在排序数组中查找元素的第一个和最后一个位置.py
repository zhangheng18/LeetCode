class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [ self.left_bound(nums, target), self.right_bound(nums, target)]
    
    def left_bound(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + ( right - left) // 2
            if nums[mid] == target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left == len(nums):
            return -1
        return left  if nums[left] == target  else -1
    

    def right_bound(self, nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid +1
        if left -1  < 0:
            return -1
        return left-1 if nums[left-1] == target else -1
