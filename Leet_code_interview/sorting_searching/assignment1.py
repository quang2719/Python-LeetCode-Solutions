#  Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        sorted_arr = []
        while(i<m and j < n):
            if nums1[i] < nums2[j]:
                sorted_arr.append(nums1[i])
                i+=1
            else: 
                sorted_arr.append(nums2[j])
                j+=1
        while(i<m):
            sorted_arr.append(nums1[i])
            i+=1
        while(j<n):
            sorted_arr.append(nums2[j])
            j+=1
        nums1[:] = sorted_arr[:]