class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        nums = range(1, A*A + 1)
        res = [[0] * A for _ in range(A)]
        c = 0
        for i in range(A//2):
            for j in range(i, A-1-i):
                res[i][j] = nums[c]
                c += 1
            for j in range(i, A-1-i):
                res[j][A-1-i] = nums[c]
                c += 1
            for j in range(A-1-i, i, -1):
                res[A-1-i][j] = nums[c]
                c += 1
            for j in range(A-1-i, i, -1):
                res[j][i] = nums[c]
                c += 1
        if A % 2 == 1:
            res[A//2][A//2] = nums[c]
        
        return res