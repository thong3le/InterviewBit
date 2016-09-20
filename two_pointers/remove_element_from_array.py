class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        pos = 0
        for i in range(len(A)):
            if A[i] != B:
                A[pos] = A[i]
                pos += 1
        return pos