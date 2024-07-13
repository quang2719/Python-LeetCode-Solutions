#Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x and y:
            if x%2 != y%2:
                count+=1
            x//=2
            y//=2
        while x:
            if x%2==1:
                count+=1
            x//=2
        while y:
            if y%2==1:
                count+=1
            y//=2
        return count
            