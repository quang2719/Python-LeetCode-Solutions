# Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        count  = 0
        while n:
            if not n%2==0:
                count+=1
            n//=2
        return count