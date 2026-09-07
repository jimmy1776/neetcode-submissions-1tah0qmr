class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #number of cols and rows 
        rows,cols = len(board), len(board[0])
        
        def capture(r,c): 
            #base case 
            if (r < 0 or c < 0 or c == cols or r == rows or board[r][c] != "O"):
                return 
            #recursive case 
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        #1) Capture everything except surrounded regions 
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0, rows-1] or c in [0,cols-1])): 
                    capture(r,c)
        
        #2) Capture the surrounde regions 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        #3) Uncpature non-surrounded regions 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
    
