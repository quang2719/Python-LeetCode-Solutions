#Rotate Image

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    # A -> A.T -> row.reverse
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))