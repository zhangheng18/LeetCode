class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i,i+1)
            res = max(s1,s2,res, key=lambda x:len(x))
        return res

    def palindrome(self,s,left, right):
        while left >=0 and right <len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left+1:right]

