class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        result = []
        self.recursion(result, A, 0)
        return result
    def recursion(self, result, A, i):
        if i == len(A) - 1:
            result.append(tuple(A))
        for j in range(i, len(A)):
            if j > i and A[j] == A[j-1]:
                continue
            A[i], A[j] = A[j], A[i]
            self.recursion(result, A, i+1)
            A[i], A[j] = A[j], A[i]

class Solution2:
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

A = [1,3,1]
S = Solution()
S2 = Solution2()
print(len(S.permute(A)))
print(len(set(S.permute(A))))
print(S.permute(A))
