class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            row, col, grid = set(), set(), set()
            for j in range(9):
                if A[i][j] != '.':
                    if A[i][j] in row:
                        return 0
                    else:
                        row.add(A[i][j])
                if A[j][i] != '.':
                    if A[j][i] in col:
                        return 0
                    else:
                        col.add(A[j][i])
                r = i//3 * 3 + j//3
                c = i%3 * 3 + j % 3
                if A[r][c] != '.':
                    if A[r][c] in grid:
                        return 0
                    else:
                        grid.add(A[r][c])
        return 1