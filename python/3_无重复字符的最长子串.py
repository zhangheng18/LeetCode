class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        windows = {}

        res = 0
        while right < len(s):
            c = s[right]
            right +=1
            windows[c] = windows.get(c,0) +1

            while windows[c] > 1:
                d = s[left]
                left +=1
                windows[d] -=1
            res = max(res, right-left)
        return res
