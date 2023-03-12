class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        self.pre_sum = [0] * (length +1)
        for i in range(1,length+1):
            self.pre_sum[i] = self.pre_sum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right+1] - self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
