class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def fibo(n):
            nonlocal cache
            if n in cache:
                return cache[n]
            if n<2: return n
            res = fibo(n-1)+fibo(n-2)
            cache[n] = res
            return res
        return fibo(n)