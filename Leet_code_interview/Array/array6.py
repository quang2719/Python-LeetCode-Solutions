#Intersection of Two Arrays II


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        res = []
        while(i<len(nums1) and j <len(nums2)):
            if(nums1[i]== nums2[j]):
                res.append(nums1[i])
                i+=1
                j+=1
            elif(nums1[i] > nums2[j] or i == len(nums1)):
                j +=1
            else: i+=1
        return res