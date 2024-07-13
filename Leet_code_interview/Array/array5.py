#  Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if(x not in s):
                s.add(x)
            else:
                s.remove(x)
        return s.pop()
                