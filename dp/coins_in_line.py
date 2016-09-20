class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        n = len(A)
        if n % 2:
            return -1
        P1 = [[0] * n for _ in range(n)]
        P2 = [[0] * n for _ in range(n)]
        for i in range(n):
            P1[i][i] = A[i]
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                P1[i][j] = max(A[i] + P2[i+1][j], A[j] + P2[i][j-1])
                P2[i][j] = min(P1[i][j-1], P1[i+1][j])
        for i in range(n):
            print(P1[i])
        print('----------')
        for i in range(n):
            print(P2[i])
        return P1[0][n-1]

    def maxcoin1(self, A):
        n = len(A)
        if n % 2:
            return -1
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = A[i]
        
        for k in range(n):
            i = 0
            j = k
            while j < n:
                if i == j:
                    dp[i][j] = A[i]
                elif i == j - 1:
                    dp[i][j] = max(A[i], A[j])
                else:
                    a = dp[i+2][j] if i+2 <= j else 0
                    b = dp[i+1][j-1] if i+1 <= j - 1 else 0
                    c = dp[i][j-2] if i <= j - 2 else 0
                    dp[i][j] = max(A[i]+min(a, b), A[j]+min(b,c))
                i += 1
                j += 1
        for i in range(n):
            print(dp[i])

        return dp[0][n-1]


A = [4,17,3,2,1,1]

print(Solution().maxcoin(A))
#print(Solution().maxcoin1(A))
