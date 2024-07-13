#Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        res = digits[::-1]
        for id,x in enumerate(res):
            if x ==9:
                res[id] = 0
            else:
                res[id] = x+1
                return res[::-1]
        res +=[1]
    
        return res[::-1]