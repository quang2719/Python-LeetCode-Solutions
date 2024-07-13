#  String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        num = 0
        start = False
        
        for id in range(len(s)):
            i = s[id]
            if start:
                if not i.isdigit(): break
                else: num = num * 10 + ord(i) - ord('0')
            else:
                if i.isdigit():
                    num = ord(i) - ord('0')
                    start = True
                    continue
                if i ==' ': continue
                if(i in ['+','-']):
                    sign = (1 if i =='+' else -1)
                    start = True
                    continue
                break
                    
                    
        num = (num*sign if sign != 0 else num)
        num = max(num,(-2)**31)
        num = min(num,(2**31)-1)
        return num