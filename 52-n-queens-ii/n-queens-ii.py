class Solution:
    def isSafe(self, row, col, board, n):
        row1 = row
        col1 = col
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        row = row1
        col = col1
        while col>= 0:
            if board[row][col]=='Q':
                return False
            col -= 1
        row = row1
        col = col1
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True
    def solve (self, col, board, result, n):
        if col == n:
            result[0] += 1
            return 
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(col+1, board, result, n)
                board[row][col] = "."
    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = [0]
        col = 0
        self.solve(col, board, result, n)
        return result[0]
        