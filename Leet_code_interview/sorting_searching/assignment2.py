#   First Bad Version
# 
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        if r==1:
            return 1
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    r = mid-1
            else:
                l = mid+1
            