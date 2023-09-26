from typing import List


def reverse(arr: List[int], i: int, j: int):
    # 翻转
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.res = []
        self.sort(arr, len(arr))
        return self.res

    def sort(self, cakes, n: int):
        # 结束
        if n == 1:
            return

        # 查找最大的饼 元素和下标
        max_cake, max_index = max((v, i) for i, v in enumerate(cakes[:n]))

        # 第一次翻转，将最大的饼翻到最上面
        reverse(cakes, 0, max_index)

        # 答案下标从1开始计数
        self.res.append(max_index + 1)

        # 第二次翻转，将最大的饼翻到最下面
        reverse(cakes, 0, n - 1)
        self.res.append(n)

        # 递归
        self.sort(cakes, n - 1)
