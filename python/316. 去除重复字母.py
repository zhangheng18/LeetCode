from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 单调栈
        stock = []

        in_stock = set()

        #计数
        count = Counter(s)

        for c in s:
            count[c] -= 1
            #去重
            if c in in_stock:
                continue
            # 从栈中移除 比当前字符大的元素
            while stock and  stock[-1] > c:
                # 后续没有此字符 终止移除
                if count[stock[-1]] == 0:
                    break
                in_stock.remove( stock.pop())
            stock.append(c)

            in_stock.add(c)
        return "".join(stock)