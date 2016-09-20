from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
    
    def anytwo(self, A):
        n = len(A)
        M = [[-1]*n for _ in range(n)]
        return self.rec(M, 0, 0, A) > 1
        
    def rec(self, M, i, j, A):
        if i == len(A) or j == len(A):
            return 0
        if M[i][j] != -1:
            return M[i][j]
        ans = max(self.rec(M,i+1,j,A), self.rec(M,i,j+1,A))
        M[i][j] = max(ans, 1 + self.rec(M,i+1,j+1,A)) if A[i] == A[j] and i!=j else ans
        return M[i][j]
        
    def anytwo2(self, A):
        n = len(A)
        M = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                M[i][j] = max(M[i-1][j], M[i][j-1])
                if A[i-1] == A[j-1] and i != j:
                    M[i][j] = max(M[i][j], M[i-1][j-1] + 1)
        return M[n][n] > 1
                    
    def anytwo1(self, A):
        if max(Counter(A).values()) >= 3:
            return True
        B = list(set(A))
        for i in range(len(B)-1):
            for j in range(i+1, len(B)):
                if self.verify(A, B[i], B[j]) or self.verify(A, B[j], B[i]):
                    return True
        return False
        
    def verify(self, A, a, b):
        B = ''.join([c for c in A if c == a or c == b])
        k = B.find(a+b)
        return False if k == -1 else (B[:k] + B[k+2:]).find(a+b) != -1