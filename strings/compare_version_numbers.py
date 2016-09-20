class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A = map(int, A.split('.'))
        B = map(int, B.split('.'))
        n, m = len(A), len(B)
        for a,b in zip(A,B):
            if a < b:
                return -1
            elif a > b:
                return 1
        if n > m and sum(A[m:]) > 0:
            return 1
        if m > n and sum(B[n:]) > 0:
            return -1
        return 0