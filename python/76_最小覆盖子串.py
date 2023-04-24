
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        # 初始化
        need, windows = defaultdict(int), defaultdict(int)
        for i in t:
            need[i] += 1

        left, right = 0, 0
        valid = 0
        start, str_len = 0, len(s) + 1

        while right < len(s):
            # 扩大字符串 直至包含所有 t
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1

            # 收缩字符串， 更新最小长度
            while valid == len(need):
                if right - left < str_len:
                    str_len = right - left
                    start = left
                # 移除
                c = s[left]
                left += 1
                if c in need:
                    if windows[c] == need[c]:
                        valid -= 1
                    windows[c] -= 1
        return '' if str_len > len(s) else s[start:start+str_len]

    
    def minWindow2(self, s: str, t: str) -> str:
        # 暴力求解法
        from collections import Counter

        str_length = len(s)+1
        t_l, s_l = len(t), len(s)
        start, end = 0, 0

        t_c = Counter(t)
        for i in range(s_l):
            for j in range(i+t_l, s_l+1):
                tmp_c = Counter(s[i:j])
                for c in t_c:
                    if tmp_c[c] < t_c[c]:
                        break
                else:
                    if (j-i) <= str_length:
                        str_length = j - i
                        start, end = i, j
        return "" if str_length > len(s) else s[start:end]
