from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 记录字符需要出现的次数
        need, windows = defaultdict(int), defaultdict(int)
        for i in s1:
            need[i] += 1

        left, right = 0, 0
        valid = 0

        # 扩大字符串
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                #更新窗口
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1

            # 收缩字符串
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                c = s2[left]
                left += 1
                if c in need:
                    #更新窗口
                    if windows[c] == need[c]:
                        valid -= 1
                    windows[c] -= 1
        # 未找到
        return False
