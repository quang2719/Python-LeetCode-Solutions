# Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count  = 0
        for i,x in enumerate(s):
            if i== len(s)-1:
                count+= convert[s[i]]
                break
            else:
                if convert[x] < convert[s[i+1]]:
                    count -= convert[x]
                else: count+= convert[x]
        
        
        return count

        
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
