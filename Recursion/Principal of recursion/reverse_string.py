class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #nomal
        # s[:] =  s[::-1]
        
        #recursion ver
        def swap(l,r):
            nonlocal s
            if(l<r):
                s[l],s[r] = s[r],s[l]
                swap(l+1,r-1)
        swap(0,len(s)-1)