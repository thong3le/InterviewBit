import sys
sys.setrecursionlimit(20000)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange(self, A, B):
        A.sort()
        count = [0] * (B+1)
        count[0] = 1
        for i in range(len(A)):
            for j in range(A[i], B+1):
                count[j] = (count[j] + count[j-A[i]]) % 1000007
        return count[B]
    
    def coinchange2(self, A, B):
        m = len(A)
        self.M = {}
        return self.rec(A, m-1, B) % 1000007
    
    def rec(self, A, i, B):
        if i >= -1 and B == 0:
            self.M[(i,B)] = 1
            return 1
        if i < 0 and B > 0:
            self.M[(i,B)] = 0
            return 0
        result = 0
        if (i-1, B) in self.M:
            result += self.M[(i-1,B)]
        else:
            result += self.rec(A, i-1, B)
        if A[i] <= B:
            result += self.M[(i, B-A[i])] if (i, B-A[i]) in self.M else self.rec(A, i, B-A[i])
        self.M[(i, B)] = result
        return result
            