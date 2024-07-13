#Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # Handle cases where k is larger than the length of nums
        nums[:] =   nums[-k:] + nums[:-k]

