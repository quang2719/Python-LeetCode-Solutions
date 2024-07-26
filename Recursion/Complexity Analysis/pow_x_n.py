class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}
        def pow(x,n):
            nonlocal cache
            if n<0:
                return pow(1/x,-n)
            
            if n==0: return 1
            if n==1: return x
            
            if n in cache:
                return cache[i]
            n_2 = pow(x,n//2)
            cache[n//2] = n_2
            if n%2==0:
                return n_2*n_2
            else: return x*n_2*n_2
        return pow(x,n)
            
                