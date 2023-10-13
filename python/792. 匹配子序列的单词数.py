from bisect import bisect_left
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = [[] for _ in range(256)]

        # 初始化s索引 二分搜索加速
        for i, c in enumerate(s):
            index[ord(c)].append(i)

        res = 0
        # 判断是否为子序列
        for word in words:
            j = 0
            for c in word:
                if not index[ord(c)]:
                    break
                # 二分搜索
                pos = bisect_left(index[ord(c)], j, hi=-1)
                if pos == -1:
                    break

                j = index[ord(c)][pos] + 1
            else:
                res += 1
        return res
