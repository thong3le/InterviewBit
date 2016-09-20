from collections import deque
class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        B = B.strip()
        m, n = len(A), len(A[0])
        M = set()
        
        def rec(k, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if k == len(B):
                return 1
            if A[i][j] != B[k]:
                return 0
            if (k, i, j) in M:
                return 1
            if rec(k+1, i+1, j) or rec(k+1, i-1, j) or rec(k+1, i, j+1) or rec(k+1, i, j-1): 
                M.add((k, i, j))
                return 1
            else:
                return 0

        for i in range(m):
            for j in range(n):
                if rec(0, i, j):
                    return 1
        return 0