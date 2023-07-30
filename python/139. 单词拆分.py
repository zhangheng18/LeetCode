class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # hash 提升判断速度
        self.wordDict = set(wordDict)

        # -1 未计算 False不能拼 True可以拼
        self.memo = [-1] * len(s)

        return self.dp(s, 0)

    def dp(self, s, i):
        # 最后一个字符匹配
        if i == len(s):
            return True

        # 剪枝
        if self.memo[i] != -1:
            return self.memo[i]

        for l in range(1, len(s) - i + 1):
            # s[i..] 的前缀被匹配，去尝试匹配 s[i+len..]
            if s[i : i + l] in self.wordDict and self.dp(s, i + l):
                self.memo[i] = True
                return True

        self.memo[i] = False
        return False
