class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0,0
        windows = {i:0 for i in p}

        res = []
        need = {}
        valid = 0
        for i in p:
            need.setdefault(i, 0)
            need[i] +=1
        
        while right < len(s):
            c = s[right]
            if c in need:
                windows[c] +=1
                if windows[c] == need[c]:
                    valid +=1
            right +=1

            while (right - left)>= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left+=1
                if d in  need:
                    if windows[d] == need[d]:
                        valid -=1
                    windows[d]-=1
        return res
