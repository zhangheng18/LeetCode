from collections import deque


def plus_one(s: str, j: int):
    """向上拨动 0-9"""
    ch = list(s)
    ch[j] = str((int(ch[j]) + 1) % 10)
    return "".join(ch)


def minus_one(s, j):
    """向下拨动 0-9"""
    ch = list(s)
    ch[j] = str((int(ch[j]) - 1) % 10)
    return "".join(ch)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque(['0000'])

        # 已经遍历过/死亡, 跳过
        visted = set(deadends)
        if '0000' in visted:
            return -1

        step = 0
        while q:
            # bfs 扩散
            for i in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return step
                # 拨动一次  8种可能
                for i in range(4):
                    up = plus_one(cur, i)
                    if up not in visted:
                        q.append(up)
                        visted.add(up)
                    down = minus_one(cur, i)
                    if down not in visted:
                        q.append(down)
                        visted.add(down)
            # 拨动次数+1
            step += 1
        # 没找到
        return -1
