class Solution:
    
    @staticmethod
    def init_diff(nums):
        diff = [ 0 for _ in range(len(nums))]
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i-1] - nums[i]
        return diff

    @staticmethod
    def diff_add(nums, i ,j, val):
        nums[i] += val
        if j +1 < len(nums):
            nums[j+1] -= val

    @staticmethod
    def diff_result(diff):
        res = [0 for _ in range(len(diff))]
        res[0] = diff[0]
        for i in range(1, len(diff)):
            res[i] = res[i-1] + diff[i]
        return res
            
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff_nums = self.init_diff( [ 0 for _ in range(n)])

        for book in bookings:
            i, j ,val = book
            self.diff_add(diff_nums,i-1, j-1,val)
            
        return self.diff_result(diff_nums)
