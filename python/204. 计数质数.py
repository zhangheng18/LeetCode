class Solution:
    def countPrimes(self, n: int) -> int:
        """Sieve of Eratosthenes"""
        if n < 2:
            return 0

        is_prim_list = [1] * n
        is_prim_list[0] = 0
        is_prim_list[1] = 0

        for i in range(2, n):
            if is_prim_list[i]:
                # i是质数， i的的倍数不可能是质数了
                for j in range(i * i, n, i):
                    is_prim_list[j] = 0

        # 计算质数个数
        return sum(is_prim_list)
