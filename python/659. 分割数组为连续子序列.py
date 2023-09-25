from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # freq：每个数字出现的次数 ， need: 被其他子序列使用的数字次数
        freq, need = Counter(nums), Counter()
        for num in nums:
            if freq[num] == 0:
                # 已经被用到其他子序列中
                continue

            if need[num] > 0:
                # 可以接到之前的某个序列后面
                freq[num] -= 1
                need[num] -= 1
                need[num + 1] += 1
            elif freq[num] > 0 and freq[num + 1] > 0 and freq[num + 2] > 0:
                # 将 num 作为开头，新建一个长度为 3 的子序列 [num,num+1,num+2]
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1

                need[num + 3] += 1
            else:
                # 无法分配
                return False
        return True
