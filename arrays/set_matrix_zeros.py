class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n = len(A)
        m = len(A[0])
        row = set()
        col = set()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    A[i][j] = 0
        return A

    def setZeroes2(self, A):
        n, m = len(A), len(A[0])
        ZR, ZC = False, False
        for r in range(n):
            if A[r][0] == 0:
                ZC = True
        for c in range(m):
            if A[0][c] == 0:
                ZR = True
                
        for r in range(1,n):
            for c in range(1,m):
                if A[r][c] == 0:
                    A[r][0] = 0
                    A[0][c] = 0

        for r in range(1,n):
            for c in range(1,m):
                if A[r][0] == 0 or A[0][c] == 0:
                    A[r][c] = 0

        if ZR:
            for c in range(m):
                A[0][c] = 0
        if ZC:
            for r in range(n):
                A[r][0] = 0

        return A 
