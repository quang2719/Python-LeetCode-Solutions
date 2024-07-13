#Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        isPrime = [1 for _ in range(n)]
        isPrime[0],isPrime[1] =0,0
        count = 0
        for i in range(2,n):
            if isPrime[i]:
                count+=1
                j = i*i
                while(j<n):
                    isPrime[j] =0
                    j+=i
        return count
                