        self.res = []
        self.length = 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.length = len(nums) 
        i = 0
        while i < self.length -1:
            # 存在了，不重复添加
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            two_result  = self.twoSum(nums, i+1, 0- nums[i])
            for two in two_result:
                two.append( nums[i])
                self.res.append( two)
            i+=1
 
        return self.res
    

    def twoSum(self, nums:List[int], start:int ,target:int):
        left, right = start, self.length -1
        res = []
        while left < right:
            tmp_left, tmp_right = nums[left], nums[right]

            total = tmp_left + tmp_right
            if total < target:
                while left < right and nums[left] == tmp_left:
                    left +=1
            if total > target:
                while left< right and nums[right] == tmp_right:
                    right -=1
            elif total == target:
                res.append( [tmp_left, tmp_right])
                while left < right and nums[left] == tmp_left:
                    left +=1
                while left < right and nums[right] == tmp_right:
                    right-=1
        return res

