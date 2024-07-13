#Valid Palindrome

class Solution:
    def preprocess(self, s:str) -> str:
        s = s.lower()
        res = ""
        for x in s:
            if ('0'<=str(x)<='9') or (ord('a') <= ord(x)<=ord('z')):
                res += x
        return res
         
                                 
    def isPalindrome(self, s: str) -> bool:
        s = self.preprocess(s)
        if len(s) <=1: return True
        
        l = 0
        r = len(s)-1
        mid = len(s)//2
        while(l<mid):
            if(s[l]!=s[r]): return False
            l+=1
            r-=1
        return True
        