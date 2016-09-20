class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        n = len(A)
        if n==0:
            return 0
        M = [0] * (n+1)
        M[0] = 1
        if A[0] == '0':
            return 0
        M[1] = 1
        for i in range(2, n+1):
            if A[i-1] == '0':
                if int(A[i-2]) <= 2:
                    M[i] = M[i-2]
                else:
                    return 0
            elif A[i-2] != '0' and int(A[i-2] + A[i-1]) <= 26:
                M[i] = M[i-1] + M[i-2]
            else:
                M[i] = M[i-1]
        return M[n]