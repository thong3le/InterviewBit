class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, K):
        A = A.strip()
        n = len(A)
        if n < K:
            return -1
        ans = 0
        W = []
        B = []
        countw = countb = 0
        for i in range(n):
            if A[i] == 'W':
                countw += 1
            else:
                countb += 1
            W.append(countw)
            B.append(countb)
        c = lambda i,j: (W[j] - W[i-1]) * (B[j] - B[i-1])
        M = [0] * n
        for i in range(n):
            M[i] = W[i] * B[i]
        temp = [0] * n
        for k in range(1, K):
            for p in range(k, n):
                best = float('inf')
                for i in range(k, p+1):
                    best = min(best, M[i-1] + c(i, p))
                temp[p] = best
            for i in range(n):
                M[i] = temp[i]
        return M[n-1]