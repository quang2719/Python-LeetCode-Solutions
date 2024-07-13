#Valid Sudoku

def isValidSudoku(board):
    used_col = [[False for _ in range(10)] for _ in range(9)]
    used_row = [[False for _ in range(10)] for _ in range(9)]
    sub_matrix = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]
    
    for r in range(9):
        for c in range(9):
            if(board[r][c]) != '.':
                num = int(board[r][c])  
                
                #check row
                if(used_row[r][num]):
                    return False
                else:
                    used_row[r][num] = True
                
                #check colum
                if(used_col[c][num]):
                    return False
                else: used_col[c][num] = True
                
                #check sub_maxtrix
                sub_row = r//3 
                sub_col = c//3
                if(sub_matrix[sub_row][sub_col][num]):
                    return False
                else:
                    sub_matrix[sub_row][sub_col][num] = True
    
    return True
matrix = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(matrix))
                    

