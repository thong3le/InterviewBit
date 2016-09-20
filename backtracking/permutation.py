class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        A.sort()
        result = []
        self.recursion(result, A, 0)
        return result
        
    def recursion(self, result, A, i):
        if i == len(A) - 1:
            result.append(list(A))
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            self.recursion(result, A, i+1)
            A[i], A[j] = A[j], A[i]