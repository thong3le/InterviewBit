class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        pos = 0
        for j in range(len(A)):
            if j < len(A) - 2 and A[j] == A[j+1] and A[j] == A[j+2]:
                continue
            else:
                A[pos] = A[j]
                pos += 1
        return pos