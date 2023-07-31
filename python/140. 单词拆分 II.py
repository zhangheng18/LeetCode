class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.wordDict = None

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = set(wordDict)
        self.backtrack(s, 0)
        return self.res

    def backtrack(self, s: str, i: int):
        # 匹配到s的最后一个字符 返回
        if len(s) == i:
            self.res.append(" ".join(self.track))
            return

        for l in range(1, len(s) - i + 1):
            if s[i : i + l] in self.wordDict:
                self.track.append(s[i : i + l])
                self.backtrack(s, i + l)
                self.track.pop()
