import sys
sys.setrecursionlimit(10000)

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        a = [0] + B + [A]
        n = len(a)
        dp = [[0]*n for _ in range(n)]
        s = [[-1]*n for _ in range(n)]
        for k in range(1, n):
            for i in range(0, n-k):
                j = i + k
                if k == 1:
                    dp[i][j] = a[j] - a[i]
                else:
                    temp = float('inf')
                    for p in range(i+1, j):
                        if dp[i][p] + dp[p][j] < temp:
                            s[i][j] = p
                            temp = dp[i][p] + dp[p][j]
                    dp[i][j] = temp + a[j] - a[i]
        #for i in range(n):
         #   print(dp[i])
        #print()
        #for i in range(n):
         #   print(s[i])
        result = []
        self.findoptimal(result, 0, n-1, s)
        return [a[i] for i in result]
    
    def findoptimal(self, result, i, j, s):
        if j - i == 1:
            return
        p = s[i][j]
        result.append(p)
        self.findoptimal(result, i, p, s) 
        self.findoptimal(result, p, j, s)

A = 6
B = [1,2,5]
print(Solution().rodCut(A,B))