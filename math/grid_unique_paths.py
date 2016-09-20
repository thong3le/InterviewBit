class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A <= 1 or B <= 1:
            return 1
        count = [1] * B
        for i in range(1, A):
            for j in range(1, B):
                count[j] += count[j-1]
        return count[B-1]