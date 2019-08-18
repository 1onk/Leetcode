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


class Solution:
    def solve(self, board: List[List[str]]) -> None:
    # def solve(self, board):
        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])
        p = [*range(row * col + 1)]
        def node(i, j):
            return i * col + j

        def find(i):
            while p[i] != i:
                p[i] = p[p[i]]
                i = p[i]
            return i

        def union(i, j):
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                p[root1] = root2

        def isConnected(i, j):
            return find(i) == find(j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(node(i, j), node(row, 0))
                    else:
                        if i > 0 and board[i-1][j] == 'O':
                            union(node(i, j), node(i - 1, j))
                        if i < row - 1 and board[i+1][j] == 'O':
                            union(node(i, j), node(i + 1, j))
                        if j > 0 and board[i][j-1] == 'O':
                            union(node(i, j), node(i, j - 1))
                        if j < col - 1 and board[i][j+1] == 'O':
                            union(node(i, j), node(i, j + 1))
        for i in range(row):
            for j in range(col):
                if isConnected(node(i, j), node(row, 0)):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



# a = [["O","O","O"],["O","O","O"],["O","O","O"]]
#
# Solution().solve(a)
# print(a)

