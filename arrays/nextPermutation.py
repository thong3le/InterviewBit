class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        for k in range(len(A) - 2, -1, -1):
            if A[k] < A[k+1]:
                break
        else:
            return reversed(A)
        
        for i in range(len(A) -1 , k, -1):
            if A[i] > A[k]:
                l = i
                break
            
        A[k], A[l] = A[l], A[k]
        A[k+1:] = A[k+1:][::-1]
    
        return A
            

