import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {i:0 for i in t}, { i:0 for i in s }
        for i in t:
            need[i]+=1

        left , right = 0, 0
        valid = 0
        start , length = 0, sys.maxsize

        while right < len(s):
            c = s[right]
            right +=1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid+=1
            while valid == len(need):
                if (right - left) < length:
                    start = left
                    length = right - left
                d = s[left]
                left +=1
                if d in need:
                    if window[d] == need[d]:
                        valid -=1
                    window[d] -=1
        return ""  if length == sys.maxsize else s[start:start+length]
