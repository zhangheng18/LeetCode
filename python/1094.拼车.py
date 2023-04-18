class Solution:

    @staticmethod
    def diff_init(nums):
        diff_nums = [0] * len(nums)
        diff_nums[0] = nums[0]
        for i in range(1,len(nums)):
            diff_nums[i] = nums[i-1] - nums[i]
        return diff_nums

    @staticmethod
    def diff_add(nums, start, end ,val):
        nums[start] += val
        if end +1 < len(nums):
            nums[end+1] -=val
    
    @staticmethod
    def diff_res(diff_nums):
        res = [0] * len(diff_nums)
        res[0] = diff_nums[0]
        for i in range(1, len(diff_nums)):
            res[i] = res[i-1] + diff_nums[i]
        return res

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_len = max(trips,key=lambda x:x[2])[2] + 1
        diff_nums = [0] * max_len
        
        diff_nums = self.diff_init(diff_nums)
        for trip in trips:
            val, start, end  = trip
            self.diff_add(diff_nums, start, end-1, val)
        res = self.diff_res(diff_nums)
        for i in res:
            if i > capacity:
                return False
        return True
