class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        def dfs(board, i, j, row, col):
            if i < 0 or j < 0 or  i >= row or j >= col or board[i][j] == 'X' or board[i][j] == '#':
                return
            board[i][j] = '#'
            dfs(board, i-1, j, row, col)
            dfs(board, i+1, j, row, col)
            dfs(board, i, j-1, row, col)
            dfs(board, i, j+1, row, col)


        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and board[i][j] == 'O':
                    dfs(board, i, j, row, col)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
