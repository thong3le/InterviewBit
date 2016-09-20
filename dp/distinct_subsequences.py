class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    
    def numDistinct(self, S, T):
        n = len(S)
        m = len(T)
        M = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            M[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S[i-1] == T[j-1]:
                    M[i][j] = M[i-1][j-1] + M[i-1][j]
                else:
                    M[i][j] = M[i-1][j]
        return M[n][m]
        
        
    def numDistinct1(self, S, T):
        M = {}
        return self.rec(M, 0, 0, S, T)
    
    def rec(self, M, i, j, S, T):
        if j == len(T):
            return 1
        if i == len(S):
            return 0
        if (i,j) in M:
            return M[(i,j)]
        if S[i] == T[j]:
            M[(i,j)] = self.rec(M,i+1,j+1,S,T) + self.rec(M,i+1,j,S,T)
        else:
            M[(i,j)] = self.rec(M,i+1,j,S,T)
        return M[(i,j)]
    
    def numDistinct2(self, S, T):
        M = [[-1] * len(T) for _ in range(len(S))]
        return self.count(M, 0, 0, S, T)
    
    def count(self, M, i, j, S, T):
        if j == len(T):
            return 1
        if i == len(S):
            return 0
        if M[i][j] != -1:
            return M[i][j]
        if S[i] == T[j]:
            M[i][j] = self.count(M, i+1, j+1, S, T) + self.count(M, i+1, j, S, T)
        else:
            M[i][j] = self.count(M, i+1, j, S, T)
        return M[i][j]
