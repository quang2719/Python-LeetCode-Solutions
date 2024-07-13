#Two Sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        s.add(nums[0])
        for i in range(1,len(nums)):
            j = target - nums[i]
            if j in s:
                for k in range(len(nums)):
                    if(nums[k]==j):
                        return [k,i]
            s.add(nums[i])
                
            