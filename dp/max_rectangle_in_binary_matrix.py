class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    def maximalRectangle(self, A):
        n, m = len(A), len(A[0])
        dp = [[0] * m for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if A[i][j]:
                    dp[i][j] = 1 if j == 0 else dp[i][j-1] + 1
        ans = 0
        for j in range(m):
            stack = [0]
            for i in range(1, n+1):
                while stack and dp[i][j] < dp[stack[-1]][j]:
                    h = dp[stack.pop()][j]
                    w = i if not stack else i-stack[-1]-1
                    ans = max(ans, w * h)
                stack.append(i)
        return ans
        
        
    def maximalRectangle1(self, A):
        n, m = len(A), len(A[0])
        dp = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                for k in range(i, n):
                    for l in range(j, m):
                        if k == i and l == j:
                            dp[i][j][k][l] = 1 if A[i][j] else 0
                        elif k == i:
                            dp[i][j][k][l] = 1 if A[k][l] and dp[i][j][k][l-1] else 0
                        elif l == j:
                            dp[i][j][k][l] = 1 if A[k][l] and dp[i][j][k-1][l] else 0
                        else:
                            dp[i][j][k][l] = 1 if A[k][l] and dp[i][j][k-1][l] and dp[i][j][k][l-1] else 0
                        if dp[i][j][k][l]:
                            ans = max(ans, (k-i+1) * (l-j+1))
        return ans