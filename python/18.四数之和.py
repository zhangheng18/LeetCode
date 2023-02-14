class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
  
        def nSum(nums:List[int], n:int,start:int, target:int ):
            res  = []
            sz = len(nums)
            if n < 2 or sz<n:
                return res
            elif n == 2:
                low, hight = start , sz -1
                while low < hight:
                    val_l , val_h = nums[low], nums[hight]
                    sum = val_l + val_h
                    if sum < target:
                        while low < hight and nums[low] == val_l:
                            low +=1
                    elif sum > target:
                        while low < hight and nums[hight] == val_h:
                            hight -=1
                    else:
                        res.append([val_l,val_h])
                        while low < hight and nums[low] == val_l:
                            low +=1
                        while low < hight and nums[hight] == val_h:
                            hight -=1
                    
            else:
                i = start
                while i < sz:
                    sub = nSum(nums, n-1, i+1, target - nums[i])
                    for item in sub:
                        item.append(nums[i])
                        res.append(item)
                    while i < sz-1 and nums[i]== nums[i+1]:
                        i+=1
                    else:
                        i+=1
            return res

        nums.sort()
        res = nSum(nums, 4, 0, target)
        return res

