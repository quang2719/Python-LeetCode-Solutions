#Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        sign = (1 if x > 0 else -1)
        x *= sign 
        res = 0
        while x:
            res = res*10 + int(x%10)
            x //= 10
            
        if res > (2**31 - 1) or res < -2**31:
            return 0
        
        return (res)*sign