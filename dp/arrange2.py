class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, K):
        n = len(A)
        if n < K:
            return -1
        ans = 0
        W = list(map(lambda x: 1 if x == 'W' else 0, A))
        B = list(map(lambda x: 1 if x == 'B' else 0, A))
        for i in range(1,n):
            W[i] += W[i-1]
            B[i] += B[i-1]
        c = lambda i,j: (W[j] - W[i-1]) * (B[j] - B[i-1])
        prev = [0] * n
        for i in range(n):
            prev[i] = W[i] * B[i]
        cur = [0] * n
        #print(prev)
        for k in range(1, K):
            for p in range(k, n):
                best = float('inf')
                for i in range(k, p+1):
                    #print(p, i, prev[i-1] + c(i,p))
                    best = min(best, prev[i-1] + c(i, p))
                cur[p] = best
            #print(cur)
            for i in range(n):
                prev[i] = cur[i]
        return prev[n-1]

A = "BWBWWWBBBWBBWBBBWWBWWWWWBBWBBWBWWBBBW"
K = 1

print(Solution().arrange(A, K))