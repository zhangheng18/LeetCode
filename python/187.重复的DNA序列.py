class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # 字符 映射为数字
        s_map = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3
        }
        nums = [s_map.get(c) for c in s]

        # 数字映射
        R = 4
        L = 10
        RL = R ** (L - 1)

        left, right = 0, 0
        window_hash = 0

        seen, res = set(), set()

        while right < len(s):
            # 向左增大
            window_hash = window_hash * R + nums[right]
            right += 1

            # 满足长度
            if right - left == L:
                # 存在重复
                if window_hash in seen:
                    res.add(s[left:right])
                else:
                    # 记录新值
                    seen.add(window_hash)

                # 向右减小
                window_hash = window_hash - RL * nums[left]
                left += 1
        return list(res)