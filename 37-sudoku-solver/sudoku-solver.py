class Solution:
    def isValid(self, row, col, board, char):
        for i in range(9):
            if board[i][col] == char:
                return False
            if board[row][i] == char:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]== char:
                return False
        return True

    def solve(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    for i in range(1, 10):
                        if self.isValid(row,col,board, str(i)):
                            board[row][col] = str(i)
                            if self.solve(board) == True:
                                return True
                            else:
                                board[row][col] = "."
                    return False
        return True


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        