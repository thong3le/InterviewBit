class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = {}
        for i in range(len(A)):
            if B - A[i] in d:
                return [d[B-A[i]]+1, i+1]
            elif A[i] not in d:
                d[A[i]] = i
        return []