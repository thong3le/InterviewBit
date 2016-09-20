class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        fac = [1] * 256
        for i in range(1, 256):
            fac[i] = fac[i-1] * i % 1000003
        chars = [0] * 256
        for c in A:
            chars[ord(c)] += 1
        rank = 1
        for i in range(n):
            for j in range(ord(A[i])):
                if chars[j] > 0:
                    rank = (rank + fac[len(A)-1-i]) % 1000003
            chars[ord(A[i])] -= 1
        return rank