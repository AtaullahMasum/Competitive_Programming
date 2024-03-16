class Solution:
    def isSafe(self, col, row, n, board):
        row1 = row
        col1 = col
        #check upper traingle
        while col >= 0 and row >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        #check in these row
        row = row1
        col = col1
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
        #check lower triangle
        row = row1
        col = col1
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True
        
    def solve(self, col , board, n, result ):
        if col == n:
            result.append(["".join(row) for row in board])
            return 
        for row in range(n):
            if self.isSafe(col, row, n, board):
                board[row][col] = 'Q'
                self.solve(col+1, board, n, result)
                board[row][col] = '.'
    def solve1(self,col, board, result, upperDiagonal, lowerDiagonal, leftRow, n):
        if col == n:
            result.append(["".join(row) for row in board])
            return
        for row in range(n):
            if leftRow[row] == 0 and upperDiagonal[(n-1)+(col-row)]==0 and lowerDiagonal[row+col]==0:
                board[row][col] = "Q"
                leftRow[row] = 1
                upperDiagonal[(n-1)+(col-row)]= 1
                lowerDiagonal[row+col] = 1
                self.solve1(col+1, board, result, upperDiagonal, lowerDiagonal, leftRow, n)
                board[row][col] = "."
                leftRow[row] = 0
                upperDiagonal[(n-1)+(col-row)] = 0
                lowerDiagonal[row+col] = 0


    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        leftRow = [0]*n
        upperDiagonal = [0]*(2*n -1)
        lowerDiagonal = [0]*(2*n -1)
        result = []
        col = 0
        self.solve1(col, board, result, upperDiagonal, lowerDiagonal, leftRow, n)
        return result

        board = [['.' for _ in range(n)] for _ in range(n)]
        col = 0
        result = []
        self.solve(col, board, n, result)
        return result
        