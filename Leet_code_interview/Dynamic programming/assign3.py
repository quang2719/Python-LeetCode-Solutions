# Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        cur_max = [nums[0]]
        for i in range(1,len(nums)):
            cur_val = max(nums[i],cur_max[i-1]+nums[i])
            cur_max.append(cur_val)
        return max(cur_max)
        