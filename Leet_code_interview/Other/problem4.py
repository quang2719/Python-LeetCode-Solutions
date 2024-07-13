# Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j ==0 or j == (i):
                    row.append(1)
                else:
                    row.append(a[i-1][j-1]+a[i-1][j])
            a.append(row)
        return a