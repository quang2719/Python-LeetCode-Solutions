# Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        res = [0]*len(nums)
        for x in nums:
            if(x != 0):
                res[i] = x
                i+=1
        nums[:] = res