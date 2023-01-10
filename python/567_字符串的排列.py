class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0,0
        windows = {i:0 for i in s1}
        need = {}

        for i in s1:
            need.setdefault(i, 0)
            need[i] +=1



        valid = 0
        while right < len(s2):
            c= s2[right]
            right +=1
            if c in need:
                windows[c] +=1
                if need[c] == windows[c]:
                    valid +=1
            
            while (right - left) >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left +=1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
        return False
