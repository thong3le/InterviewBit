class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        pos = 0
        for i in range(len(A)-1):
            if A[i] != A[i+1]:
                A[pos] = A[i]
                pos += 1
        A[pos] = A[len(A) - 1]
        return pos + 1