class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def getR(n):
            if n ==0: return [1]
            if n==1: return [1,1]
            
            n_row = []
            n_minor1_row = getR(n-1)
            for i in range(n+1):
                if i==0 or i == n: n_row.append(1)
                else: n_row.append((n_minor1_row[i-1]+n_minor1_row[i]))
            return n_row
        return getR(rowIndex)
                    