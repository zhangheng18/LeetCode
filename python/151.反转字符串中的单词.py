class Solution:

    @staticmethod
    def strip_space(s):
        # 移除多余空格
        start, end = 0, len(s) - 1

        # 移除开头空格
        while start <= end and s[start] == ' ':
            start += 1

        # 移除结尾空格
        while start < end and s[end] == ' ':
            end -= 1
        # 移除单词中间多余的空格
        slow, fast = start, start
        while fast <= end:
            if s[fast] != ' ' or s[fast - 1] != ' ':
                s[slow] = s[fast]
                slow += 1
            fast += 1
        return start, slow

    @staticmethod
    def reverse_string(s,start,end):
        # 反转字符串
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverse_world(self, s,start, end):
        # 反转单词
        slow, fast = start,start
        while slow < end:
            while fast < end and s[fast] != " ":
                fast +=1
            self.reverse_string(s, slow, fast-1)
            slow  = fast +1
            fast +=1

    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])

        ss = list(s)
        s,e = self.strip_space(ss)
        self.reverse_string(ss, s, e-1)
        self.reverse_world(ss, s, e)
        return "".join(ss[s:e])

