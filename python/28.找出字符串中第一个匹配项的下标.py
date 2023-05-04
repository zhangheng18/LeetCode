class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need_hash, window_hash = 0, 0

        # 只有26个字母
        R = 26

        L = len(needle)
        RL = R ** (L - 1)

        # 计算数字hash
        for i in needle:
            need_hash = need_hash * R + ord(i)

        left, right = 0, 0
        while right < len(haystack):
            # 扩大窗口
            window_hash = window_hash * R + ord(haystack[right])
            right += 1
            if right - left == L:
                # 相等
                if window_hash == need_hash:
                    return left
                # 减小窗口
                window_hash = window_hash - ord(haystack[left]) * RL
                left += 1

        return -1