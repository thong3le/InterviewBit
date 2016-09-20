class Solution:
    # @param A : list of list of chars
    def dfs(self, A, i, j):
        m, n = len(A), len(A[0])
        if A[i][j] == 'O':
            stack = [(i,j)]
            while stack:
                a, b = stack.pop()
                A[a][b] = 'B'
                if a > 0 and A[a-1][b] == 'O':
                    stack.append((a-1, b))
                if a < m-1 and A[a+1][b] == 'O':
                    stack.append((a+1, b))
                if b > 0 and A[a][b-1] == 'O':
                    stack.append((a, b-1))
                if b < n-1 and A[a][b+1] == 'O':
                    stack.append((a, b+1))

    def solve(self, A):
        m, n = len(A), len(A[0])
        for j in range(n):
            if A[0][j] == 'O':
                self.dfs(A, 0, j)
            if A[m-1][j] == 'O':
                self.dfs(A, m-1, j)
        for i in range(1, m-1):
            if A[i][0] == 'O':
                self.dfs(A, i, 0)
            if A[i][n-1] == 'O':
                self.dfs(A, i, n-1)
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == 'B':
                    A[i][j] = 'O'
        return A