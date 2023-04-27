from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        windows = defaultdict(int)

        res = 0

        while right < len(s):
            # 扩大窗口
            c = s[right]
            windows[c] += 1
            right += 1

            # 存在重复字符，缩小窗口
            while windows[c] > 1:
                windows[s[left]] -= 1
                left += 1

            # 更新结果
            res = max(res, right-left)

        return res
