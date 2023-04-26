from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        need, windows = defaultdict(int), defaultdict(int)

        for i in p:
            need[i] += 1

        valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            # 扩大
            if c in need:
                windows[c] += 1
                if need[c] == windows[c]:
                    valid += 1

            # 收缩
            while right - left >= len(p):
                #符合条件
                if valid == len(need):
                    res.append(left)

                c = s[left]
                left += 1
                if c in windows:
                    if need[c] == windows[c]:
                        valid -= 1
                    windows[c] -= 1

        return res
