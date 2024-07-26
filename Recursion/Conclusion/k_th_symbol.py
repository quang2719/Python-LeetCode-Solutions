class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth(n,k):
            if n==1: return 0
            if n ==2: return (0 if k==1 else 1)
            res = kth(n-1,((k-1)//2)+1)
            if res == 0: 
                return (0 if k%2==1 else 1)
            if res == 1: 
                return (1 if k%2==1 else 0)
        return kth(n,k)